# Queue H: Mathematical defects recorded in COMPLAINTS.md

**Read this before taking an item.** These entries are the headings of `COMPLAINTS.md`,
promoted here so they can be selected. They have **not** been checked for whether they are
still outstanding — a sample of five found four whose own text describes the repair having
been made. Assume nothing in this list is open until you have looked.

The underlying defect is that `COMPLAINTS.md` carries no status field, so a resolved complaint
and an open one are indistinguishable without reading the whole entry and then the card. That
is the first item below, and it comes before any individual repair: until it is fixed this
queue cannot be trusted and neither can the complaints file.

For every other item, the first action is to read the full entry in `COMPLAINTS.md` and then
the card itself. If the defect is already repaired, close the item by recording the resolution
in the complaint entry under the new status convention — that is a real unit of work, because
it converts an unreadable file into a readable one. If it is still open, repair it against the
source in a commit that also updates the entry.

## Open items

- [ ] **H.0 — give `COMPLAINTS.md` a status convention.** Every entry gains an explicit
      status and, where resolved, the commit that resolved it. Decide the convention, apply it
      to all existing entries by reading each one, and record it in `CONTRIBUTING.md` so new
      complaints carry it from the start. Nothing else in this queue is trustworthy until this
      is done.

## Count

- Recorded defects: 53

## Recorded entries

- [ ] Berkeley Fall 1981 harmonic-function problem is not harmonic as printed and its correction is underspecified

- [ ] UCSD Spring 2011 Algebra solutions were stored with literal newline escapes

- [ ] `parse_cards` cannot be used from a stdin Python script under the forkserver start method

- [ ] Smith 8000e Noetherian-rings problem 7 must start from a proper ideal

- [ ] Smith 8000e finitely-generated-modules problem 1 uses the wrong variable in both primary-subspace definitions

- [ ] `P-EXTME` — locally reverses the underdetermined homogeneous-system corollary

- [ ] `P-SH5P6` — drops the splitting-field context and the coefficient $v_0$

- [ ] The authoring CLI name for collection-scoped unsolved traversal is easy to misremember

- [ ] Stale Git sequencer metadata can block unrelated prose commits

- [ ] Direct `.venv` authoring commands can see an unsupported host Pandoc

- [ ] The repository virtual environment does not include SymPy

- [ ] Stale Git sequencer metadata can block unrelated card commits

- [ ] The strip-bound proof states an open-disk inclusion that its argument does not give

- [ ] Spring 2001 JHU Gauss--Lucas statement omits nonconstancy

- [ ] Spring 2002 JHU disk-map inequality omits the normalization at zero

- [ ] P-VVXKF omits the proper-subgroup qualification

- [ ] The 2003–2009 algebra packet has mixed subject metadata

- [ ] P-4IKKY is internally inconsistent as transcribed

- [ ] P-MMAQ-WV7QEYSPXM omits the infinite-cyclic injectivity hypothesis

- [ ] A narrow patch also removed an unrelated trailing blank line

- [ ] Continuation tool responses were not available for verification

- [ ] Unmatched shell globs and guessed extraction paths interrupt source discovery

- [ ] The configured PDF extraction command is missing and service requests failed

- [ ] Single-card validation accepts duplicate YAML mapping keys

- [ ] Supposedly disjoint collection streams collided on consecutive cards

- [ ] A read-only connector command was rejected before execution

- [ ] The required Zotero bibliography service is not listening

- [ ] Primary local repository connector can silently become unavailable

- [ ] Commit history carries Claude session-provenance trailers

- [ ] Concurrent branch consolidation reset a live worker's tree and lost authored work

- [ ] `apply_patch` is unavailable in the repository shell

- [ ] `P-MFVEZ` — omits the orientation of the square boundary

- [ ] `just unsolved-in` can hang indefinitely while scanning the corpus

- [ ] Direct-to-`main` streams can globally block unrelated card commits with Git sequencer state

- [ ] The worktree-per-stream instruction filled the host volume

- [ ] `P-VHLIU` — reverses the Jordan similarity formula

- [ ] `P-ZLNVG` — labels both parts as “a.”

- [ ] `P-RXKJR` — forgets to exclude the zero vector

- [ ] `P-3UTDH` — is false for the squarefree positive integer `n=1`

- [ ] `P-SDO43` — drops “Let” at the start of the problem

- [ ] `P-OK5P3` — has the wrong arc endpoint and resulting title

- [ ] `P-MMAQ-F2ZJO265HN` — had a truncated non-mathematical title

- [ ] `P-IH6FO` — had a truncated source-stem title

- [ ] `P-PLFQZ` — reversed the representation-dimension bound

- [ ] `P-APAF21A` — omits idempotence in the orthogonal-projection criterion

- [ ] `P-APAF21I` — does not specify the Cayley-graph connection set

- [ ] `P-APAS04F` — has two incompatible symmetric-group labels in the source

- [ ] `P-APAS06B` — falsely claims uniqueness of the isometric polar factor for rank-deficient matrices

- [ ] `P-APASP07I` — mistranscribed the first Gröbner-basis generator

- [ ] `P-APASP07J` — dropped an eigenvalue from the diagonal action

- [ ] `P-APASP08K` — does not specify whether composition coordinates may vanish

- [ ] `P-APAS11A` — omits irreducibility in the central-element scalar claim

- [x] Harvard Math 21b Practice Final 6 Problem 8 has an incorrect supplied eigensolution
