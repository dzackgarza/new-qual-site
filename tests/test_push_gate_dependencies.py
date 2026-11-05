"""The push gate's dependency closure holds no site build and no queue regeneration.

Issue #100: `test-push` depended on `crawl`, which depends on `build`, so every push
ran a whole-corpus `qualc build` -- up to eight Pandoc servers over the whole corpus
-- and `_unsolved-push` committed a regenerated queue and refused the push when it
moved, so a normal push ran that build a second time. The load average reached 29 on
12 cores and a 256-document batch could outlive its request deadline and refuse the
push outright.

The build and the queue regeneration now run in CI (`323a586823`), and the fan-out
reads the machine's load (`266a881e08`). That leaves the defect as a property of the
gate's dependency graph, and a property nothing was checking: the graph can grow a
`build` edge back at any commit. This test reads the `justfile` as text -- `just` is
not a test dependency -- and holds the property still.

It measures two facts about that graph, with exact answers:

* no gate recipe reaches a recipe that builds or renders the site, and
* no gate recipe reaches a recipe that regenerates `queues/C-unsolved-cards.md`.

Both are facts about the `justfile`; neither says anything about the mathematics.

It prints each gate's closure, so the claim is read off a run rather than taken from
this docstring: `pytest -q -s tests/test_push_gate_dependencies.py`.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JUSTFILE = ROOT / "justfile"

#: Recipes that compile the corpus or render the site. `query` shells into the built
#: catalog, so it is a build consumer like the rest.
BUILD_RECIPES = frozenset({"build", "site", "crawl", "preview", "query"})

#: A recipe whose body writes the unsolved queue. `_no-bare-disposition` names
#: `^queues/` in a grep pattern and commits nothing, so only these two spellings
#: count: running the queue generator, and committing the queue file.
QUEUE_WRITE_PATTERNS = ("unsolved_queue.py", "-- queues/C-unsolved-cards.md")

#: The recipes a push runs. `test-push` calls the two `*-push` recipes by name in its
#: body rather than as declared dependencies, so all three are roots here.
GATE_ROOTS = ("test-commit", "test-push", "_extraction-detector-push", "_macros-push")

_HEADER = re.compile(r"^(?P<name>[A-Za-z_][A-Za-z0-9_-]*)(?P<params>[^:]*):(?P<deps>[^:]*)$")


def read_justfile(path: Path = JUSTFILE) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Return the recipe dependency graph and each recipe's body lines."""
    dependencies: dict[str, list[str]] = {}
    bodies: dict[str, list[str]] = {}
    current: str | None = None
    for line in path.read_text().splitlines():
        if line[:1] in {" ", "\t"}:
            if current is not None and line.strip():
                bodies[current].append(line.strip())
            continue
        current = None
        if not line or line.startswith("#") or line.startswith("["):
            continue
        if ":=" in line:
            continue
        match = _HEADER.match(line)
        if match is None:
            continue
        current = match["name"]
        dependencies[current] = match["deps"].split()
        bodies[current] = []
    return dependencies, bodies


def closure(dependencies: dict[str, list[str]], root: str) -> list[str]:
    """Every recipe `root` needs, in discovery order, `root` first."""
    order: list[str] = []
    pending = [root]
    while pending:
        name = pending.pop(0)
        if name in order:
            continue
        assert name in dependencies, f"{root} depends on {name!r}, which the justfile does not define"
        order.append(name)
        pending.extend(dependencies[name])
    return order


def test_every_gate_recipe_is_a_known_root() -> None:
    dependencies, _ = read_justfile()
    missing = [root for root in GATE_ROOTS if root not in dependencies]
    assert not missing, f"the push gate changed shape: {missing} are not recipes in the justfile; update GATE_ROOTS rather than letting this test stop measuring"


def test_no_gate_recipe_reaches_a_site_build() -> None:
    dependencies, _ = read_justfile()
    reachable: dict[str, list[str]] = {}
    for root in GATE_ROOTS:
        names = closure(dependencies, root)
        reachable[root] = names
        built = sorted(BUILD_RECIPES.intersection(names))
        assert not built, (
            f"issue #100: the push gate reaches a site build again. {root} -> {' -> '.join(names)} "
            f"includes {built}; a push must build only what it changes or reuse a build of the same tree, "
            f"and the whole-corpus build belongs to CI (see the `test-ci` recipe and .github/workflows/development.yml)."
        )
    for root, names in reachable.items():
        print(f"{root}: {' -> '.join(names)}")


def test_no_gate_recipe_regenerates_the_unsolved_queue() -> None:
    dependencies, bodies = read_justfile()
    for root in GATE_ROOTS:
        for name in closure(dependencies, root):
            writes = [
                line
                for line in bodies[name]
                if any(pattern in line for pattern in QUEUE_WRITE_PATTERNS)
            ]
            assert not writes, (
                f"issue #100: {name}, reached from the push gate recipe {root}, regenerates "
                f"queues/C-unsolved-cards.md: {writes}. A push that writes the queue refuses itself and the retry "
                f"repeats the push's work; the queue is regenerated in CI by `_reports-ci`."
            )


def test_the_ci_report_recipe_is_not_part_of_a_push() -> None:
    dependencies, _ = read_justfile()
    for root in GATE_ROOTS:
        assert "_reports-ci" not in closure(dependencies, root), (
            f"issue #100: {root} reaches the CI report recipe; corpus measurements are generated in the "
            f"`corpus-reports` job, not on the push path"
        )
