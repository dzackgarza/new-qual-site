# This project is not automatable

Read this before writing anything in this repository.

Intake and migration needed tools. Getting the content out of five source
repositories and into this one was a transport problem, and transport is what a
tool is for. **That phase is over.** Everything after it is intelligent, semantic
work on mathematics.

Nothing after intake is mechanical. Not checking. Not deduplicating. Not
classifying. Not merging, writing, retitling, reorganizing, or auditing. Every
one of those operations means reading the mathematics, understanding what a
statement says, and deciding. There is no normal form, fingerprint, digest,
similarity score, heuristic, or "clever enough" parse that decides any of them,
because the thing being decided is what the mathematics *means*.

Growing this corpus is like growing the Stacks Project: reading, writing,
analysis, auditing, reorganization, all of it infinitely subtle, with unbounded
edge cases. A tool that automates any part of that is a claim to have enumerated
the cases in advance. That claim is false every time.

It is also a bad trade even when it appears to work. This is a **one-time task**.
The content gets written and finalized once. Every tool built to automate a part
of it is obsolete the moment that part is finished, and until then it fossilizes
whatever heuristic its author guessed at, in code that outlives the reasoning
behind it. The tool then gets trusted precisely because it is a tool.

## What this rules out

Do not write, extend, or "make safe" anything that decides a semantic question.
If a proposed tool would answer *are these the same statement*, *is this title
right*, *does this belong in that section*, *is this body empty enough to
discard*, *which of these is canonical* — do not write it. Read the cards and
decide.

Making such a tool safer is worse than leaving it broken, because it keeps the
tool. The correct response to a heuristic that destroys content is to delete the
heuristic, not to add a floor under it.

`tools/collapse_duplicates.py` was exactly this and has been deleted. It decided
which cards stated the same mathematics from a normalized-text fingerprint. It
proposed destroying distinct statements three separate times: once merging
occurrence cards with the problems they instantiate, once merging every unwritten
card onto one survivor so that Hahn-Banach, Mayer-Vietoris, Nondegenerate
Bilinear Form and Local Orientation became a single card, and once merging
occurrence cards with each other, which are different sittings of one problem and
the entire reason the occurrence layer exists. The eleven collapses that were
actually correct were settled by reading twenty-two cards.

## What a tool may still do

Render and transport. The build pipeline turns authored content into a site;
`sync_macros.py` and `sync_bibliography.py` mirror an external file into the
repository so the build is self-contained. None of these decides anything about
the mathematics.

A check may report a measurement, named for exactly the measurement it took.
`audit.py`'s `duplicate-bodies` reports that two cards hold the same bytes. That
is a true statement about bytes and a *candidate* for someone to read. It is not
a finding that the two cards are the same statement, and it must never be wired
to anything that acts on that reading. A check whose name claims more than it
measured is the same defect in smaller form.

## This corpus is authored content

This is a curated corpus of qualifying-exam mathematics, like the Stacks
Project. Every card is hand-authored: a problem statement, a definition, a
theorem, a solution, a hint. The fields on a card — title, classification,
relations, body — are content a human wrote or will write.

Good work on this corpus is reading mathematics, understanding what a statement
says, and making curation decisions: writing a title that names the problem,
classifying a card under the right topics, writing a solution, relating two
cards that depend on each other. A gap in a field is curation work, not a
tooling problem.

## Heuristics have no place in this repo

A heuristic is a proxy for intelligent work that hasn't been done yet. It
produces plausible-looking output that fills a field, passes a check, and hides
the gap that a human author needs to fill. That is the opposite of curation —
it is manufacturing the appearance of curation. There is no scenario where a
heuristic serves this corpus. If a field is empty, the field is empty; report
it and a human will fill it.

## One-time tools do not stay in the repo

The migration is over. A tool that was used once to transport, route, split,
merge, or repair content during migration is done. Delete it when the work is
finished. Do not keep it, do not write tests for it, do not enshrine it as a
recipe. Its output is committed corpus content; the tool itself is fossil.

## What a tool may do

A tool may render and transport: build the site, sync an external file into the
repo, check that the corpus is internally consistent. A check may report a
measurement — two cards hold the same bytes, a card has no solution, a title is
unreadable — named for exactly what it measured. The measurement is a candidate
for a human to read. It must never be wired to anything that acts on it.

The build reads authored content and renders it. It does not derive fields. A
build that derives titles, classifications, relations, or any other field is
fabricating content, not rendering it.

# Solution status

Every problem and exercise card declares `solved: true|false` in its own
frontmatter, and `just check` proves the declaration against the corpus:
`true` requires a `solution` section on the card or an incoming `solves`
relation from another card; `false` with either present fails the build.
There is no queue file to maintain — a solutions commit flips the field on the
same cards whose bodies it writes, and the check rejects any commit where the
field and the content disagree.

`just sample-unsolved` draws n random unsolved cards (default 5). The
solution-sheet integration side of [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2)
lives in `sources/qual-review-and-solutions-ledgers/`.

* * *

> Source: `PR_GUIDANCE.md` in `ai`.

# Review Guidelines

These are additional requirements for reviewing agent work.
They do not replace the reviewer’s normal role, repo-specific standards, or technical
judgment. They provide the failure model that should shape the review.

The task is not merely to review a PR. The task is to decide whether a completion claim
is true under the original objective.
The standard is full, correct, provable completion against the original requirements and
repo guidelines. Anything less is incomplete work that must not be treated as a win.

## Failure Model

Agents systematically produce impressive non-completion.
Common patterns are: polished summaries that imply finished work, caveats that quietly
narrow the goal, reclassification without proof, delegated discovery presented as
resolution, process language that substitutes for evidence, merged PRs treated as
completion, passing checks treated as semantic proof, and artifacts that look
substantial while leaving required work unowned.

Treat the agent’s summary, PR description, closing comment, issue closure, “goal
completed” statement, and self-reported validations as untrusted.
They may be diagnostic pointers, but they are not evidence that the work is complete.
The evidence is the original issue or task, the code diff, tests, source/runtime facts,
review comments, and produced artifacts.

## Decisive Invariants

Preserve the original success condition.
Read the original issue or task before accepting any restatement of it.
Keep its quantifiers intact: “all,” “complete,” "full subset," “zero remaining,” and
similar terms cannot be quietly narrowed to examples, partial coverage, known blockers,
or whatever the PR happened to touch.

Nothing required may disappear silently.
A required work family must be implemented, explicitly falsified, or validly
reclassified with evidence that satisfies the issue’s own standard.
Partial implementation is not completion.
Future work is not completion.
Count reduction is not completion.
Resolved review threads are not completion.
Passing checks are not completion.
Substantial-looking work is not completion.
“Better than before” is not completion.

Goal substitution is the main thing to detect.
Ask whether the submitted work solves the original problem or merely produces a narrower
artifact: cleaner metadata, a partial subset, a better explanation, a new issue, a
renamed scope, a local workaround, or proof that someone should investigate later.

Technically correct administrative artifacts can be goal substitution.
A well-written issue, comment, audit note, scope statement, or enumeration of remaining
work may be required, but it does not complete implementation, testing, proof, or
downstream cleanup. If the original task requires execution, the artifact is only useful
insofar as it drives that execution; it must not become the stopping point.

Treat self-scoped remaining-work lists as a severe completion-laundering pattern.
When an agent is asked to enumerate remaining work, the domain is the original full
completion requirement, not the agent’s intended subset, the PR’s current shape, a
closeability criterion, or the work left after deferral and reclassification.
A valid enumeration subtracts only artifact-proven completed work from the original
contract. Deferrals, routed follow-ups, owner changes, and truthful incompletion notes
remain unresolved work unless the original task explicitly made that administrative
routing the whole deliverable.

If an agent repeats a narrowed enumeration after being corrected, treat that as a hard
misalignment signal, not as an innocent wording issue.
The reviewer should identify the original full requirement, the scope the agent
substituted, and the required work hidden by that substitution.

Silent reclassification is not resolution.
If the PR says remaining work is out-of-scope, research-owned, stub-owned, plugin-owned,
downstream-owned, or future-owned, require evidence from the relevant source/runtime
behavior, repo boundary, or original acceptance criteria.
A sentence in the PR description is not enough.

Ownership boundaries matter.
The submitting repo must prove its own claimed behavior and do the blocker forensics
required by its own issue.
Do not require a receiving or downstream repo to classify another project’s internal
uncertainty unless the original issue explicitly made that part of acceptance.
When an external issue is created, it should be written for that receiving repo, not for
a reader who already knows the submitting repo’s context.

## Evidence Expectations

Review tests as evidence, not as decoration.
Valid tests exercise the real production path or semantic requirement.
Be skeptical of helper-only tests, tautologies, assertions of the implementation’s own
output, bypasses around the runtime/plugin/stub path, example-only coverage where the
issue required full coverage, weakened assertions, and missing invalid-nearby cases
where the fix could overgeneralize.

For plugin work, the evidence should usually distinguish valid generic behavior from
invalid nearby ordinary Python and should not hard-code a downstream consumer.
For stubs work, the evidence should be source-backed: the upstream surface exists, the
stub matches public behavior, no fake API is added, no Any/object opacity escape is
introduced, and inherited-method inflation is not used unless source exposes that
surface.

Watch for code-level laundering: hard-coded consumer names, support for local research
abstractions as if they were external API, fake stubs, broad Any/object escapes, line
suppressions, diagnostic filtering, deletion of required data, broad type widening, and
any move that makes checks pass by weakening the problem instead of solving it.

## When Acting on Review Feedback

A positive disposition requires a commit.

Do not resolve an accepted review comment until the code/proof remediation is committed and the reply cites the commit.

Never reply “accepted,” “aligned,” “fixed,” “addressed,” or “will address” to a review thread unless the remediation is already committed. A thread cannot be resolved on intent or future work.

Rejected and modified feedback must be collected in a top-level PR comment titled `Review feedback disposition ledger` so resolved threads do not hide the audit trail.

Review comments are not implementation specs. The worker must translate accepted feedback into first-principles remediation requirements before assigning implementation.

For each comment:
- Identify the concern.
- Identify the proposed fix.
- Decide whether the concern is true under global + repo policy.
- Decide whether the proposed fix preserves those policies.
- If the concern is true but the fix is wrong, apply a policy-compatible remediation.

## Writing the Review

Write nuanced feedback for an intelligent reader.
Do not force a machine-readable template, a mandatory table, or a simplistic pass/fail
label when prose communicates the situation better.
Do make the completion judgment clear: whether the original task can be considered
complete, what evidence supports that judgment, and which unresolved requirements block
completion if any remain.

Do not foreground effort, progress, good intentions, volume of work, or “substantial”
partial implementation when required work remains.
Mention completed pieces only when they are necessary to identify the exact remaining
blockers or to prevent redoing already-correct work.
Do not compare incomplete work to “no work done” or “completely fake work”; compare it
to the expected standard: the task done correctly, completely, and provably.

When required work remains, lead with the incompleteness and the concrete blockers.
Do not make the reader excavate the missing work from beneath praise, context-setting,
or a narrative of what did get done.

Nuance belongs in the evidence and blocker analysis, not in softening the completion
standard. The review should make it easy to finish the work, not easy to feel satisfied
with less than the original contract required.
