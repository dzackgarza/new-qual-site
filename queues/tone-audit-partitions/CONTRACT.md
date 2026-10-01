# Tone-audit worker contract

Repo / cwd: `/home/dzack/gitclones/new-qual-site`

## Mandatory reading before any edit

1. Read `queues/tone-audit.md` (scope and method).
2. Read these policies in full — the files themselves, not this contract’s summary:
   - `CONTRIBUTING.md`, `## Contributing to this document` and `## Writing house conventions`
   - [authorial stance](https://github.com/dzackgarza/ai/blob/main/opencode/skills/mathematics/writing/policy/references/authorial-stance.md) (`STANCE-*`)
   - [prose](https://github.com/dzackgarza/ai/blob/main/opencode/skills/mathematics/writing/policy/references/prose.md) (`PROSE-*`)
   - [resource descriptions](https://github.com/dzackgarza/ai/blob/main/opencode/skills/mathematics/writing/policy/references/resource-descriptions.md) (`RESOURCE-*`, `PROVENANCE-*`)
3. Your assigned partition list: `queues/tone-audit-partitions/<name>.txt`

Do not treat this contract as a substitute for those policies. Do not reduce the work to synonym cleanup, “friendlier tone,” or phrase search. A phrase search cannot close a coverage entry.

## What you are auditing for

The relationship the prose establishes (writer as judge, supervisor, certifier of scholars, spokesperson for faculty, arbiter of worthwhile study) and the professional severity of that stance under the site owner’s name. Correction is substantive mathematical or bibliographic service that restores reader autonomy — not softer commands that keep the same hierarchy. See especially `STANCE-01`, `STANCE-11`–`STANCE-16`, and `STANCE-21`.

## Execution

1. For each path in your partition file: full-page read; revise site-authored copy that violates the policies above; preserve original mathematical problem instructions and external source wording.
2. Mark the matching coverage row checked in the owning queue (`tone-audit-wiki.md`, `tone-audit-wiki-analysis-topology.md`, `tone-audit-theory-problems.md`, or `tone-audit-collections.md`), with a brief note when prose changed.
3. Commit only your intended paths with `git -c core.hooksPath=/dev/null commit`. Do not push. One checkout, `main` (`QUAL-07` / `QUAL-09`).
4. Do not edit paths outside your partition except the owning queue file.
5. Neutral wording without the displaced content is unfinished (`STANCE-11`, `STANCE-16`).

## Dirty baseline

`wiki/algebra/**` may have uncommitted stance edits already marked `[x]` in `tone-audit-wiki.md`. The `wiki-ag-misc` worker commits those first if still dirty, then continues with open paths only.

## Acceptance

Every path in your partition is checked in the owning queue; your edits are committed; report commit hashes and remaining open count in your partition (must be 0 unless blocked, with exact remaining paths).
