---
title: Building the algebraic geometry wiki
order: 99
topics:
- Algebraic Geometry
---

# Building the algebraic geometry wiki

Algebraic geometry is a qualifying subject at Berkeley and Harvard, and this tree is being written for it.
The source material is a 2022 oral-exam vault — 120 markdown files of reading notes, worked Hartshorne problems, study guides and an examiner-attributed question bank — but the tree is not an import of it.
Cards here are written the way the rest of the wiki is written: around the question an examiner actually asks, with the source used as evidence for what gets asked and as a supply of worked mathematics.

## What the exam asks, and what that implies

The question bank is the strongest evidence available about the exam, because every entry carries the examiner who asked it: Ogus, Poonen, Hartshorne, Wodzicki, Coleman, Frenkel, Sturmfels.
Reading it, the questions fall into shapes, and the shapes — not Hartshorne's chapter order — are what the tree is organised around.

| Shape | Examples from the bank | Card kind |
| --- | --- | --- |
| Produce an example or a counterexample | a projective curve that is not rational; a non-separated morphism; a variety with $\Pic = \ZZ/3$ | example-driven strategy card |
| Decide a property from a presentation | is this scheme affine; is this curve nonsingular; where are the singularities of $X^3+Y^3+Z^3=3CXYZ$ | decision-procedure card |
| Compute an invariant | $H^0(\PP^1, \Omega^1)$; arithmetic genus of $y^3 = x^2z$; $\Pic(k[t^2,t^3])$ | computation card, worked |
| State and apply a theorem | Riemann–Hurwitz; Serre's criterion; Abel's theorem | theorem card with its use |
| Define, then probe the definition | define differentials, separated, geometric genus; then "can you weaken Noetherian?" | definition card whose second half is the probe |

The last shape is the one a naive import gets wrong.
An oral examiner asks for a definition in order to ask the follow-up, so a definition card that stops at the definition has done none of the work.
`Definitions.md` is 179 KB of raw definitions; it is a quarry, not a card.

## The tree

Ordering is pedagogical: each topic depends only on the ones above it, and the varieties material comes first because the scheme material is unreadable without a geometric picture to attach it to.

```
wiki/algebraic-geometry/
  index.md                      what the exam covers, how to use this tree
  varieties/                    affine and projective varieties, the Nullstellensatz,
                                dimension, the classical dictionary
  sheaves/                      presheaves, sheafification, stalks, the sheaf condition
                                as the thing that fails
  schemes/                      Spec, gluing, fibre products, properties of schemes
  morphisms/                    separated, proper, finite, flat, smooth; the valuative
                                criteria and what they are for
  sheaves-of-modules/           quasicoherent and coherent sheaves, twisting, Serre's
                                theorems, line bundles
  divisors/                     Weil and Cartier, class groups, linear systems, the
                                Picard group as a computation
  cohomology/                   Cech, higher direct images, Serre duality, Riemann-Roch
  curves-and-surfaces/          genus, Riemann-Hurwitz, embeddings, classification
  toric/                        fans, orbit correspondence, as a worked example generator
  resources/                    references, past questions, where to read more
```

This mirrors the source's own numbering (020 varieties, 022 sheaves, 030 schemes, 031 modules, 032 morphisms, 040 divisors, 050 cohomology, 060 toric, 070 curves) because that numbering was itself derived from the syllabus.
What changes is the content of each node.

## How source material converts

**Reading notes (43 files, Hartshorne I–IV and Fulton).** These are sectioned by chapter and are the least reusable as prose: they are notes from a reading, not exposition.
They are the source for *what belongs* in each topic, and occasional passages survive verbatim.
Expect one topic card to draw on three or four reading notes and to be written fresh.

**Worked problems (42 Hartshorne + 11 extra, including Gathmann).** These become `corpus/problems/` cards with provenance in the title and classification — "Hartshorne II.3.5", "Gathmann 2020-09-18" — and are transcluded into the topic card they illustrate.
A worked solution that demonstrates a general method gets promoted: the method becomes the card, the problem becomes its example.

**The question bank (`001 Practice Questions.md`).** Every entry becomes a problem card carrying its examiner.
This is the highest-value material in the vault and the only part of it that cannot be reconstructed from a textbook.

**Study guides (15 files).** These map onto topic `index.md` pages, which is close to what they already are.

**Not carried over:** the exam-logistics files, `progress.md`, `Tasks.md`, `IW-Queues`, `900_Changelog.md`. They are the record of one person's revision schedule in 2022.

**Figures and attachments.** Most are worth keeping — the pictures of blowups, fans, and curve degenerations are the parts hardest to rewrite.
They move into `assets/` under the topic that uses them, and a figure is kept only if a card references it.

## Macros

The source predates the macro vocabulary this site uses, and this is the most mechanical-looking part of the work that is not mechanical.
`Definitions.md` alone contains 811 `\mathscr`, 336 `\operatorname`, and 429 `\left`/`\right` pairs: raw LaTeX where the site has a curated vocabulary of 316 macros.

Conversion is an uplift, not a substitution:

- `\mathscr{O}_X` becomes `\OO_X`; `\mathbb{P}^n` becomes `\PP^n`. Both targets already exist.

- `\left(...\right)` is removed rather than translated; the site's other subjects do not use it and it renders badly at small sizes.

`vocabularies/macros.json` is **generated** by `tools/sync_macros.py` from `/home/dzack/Dropbox/pandoc/custom/preamble.tex`, narrowed to the macros the corpus and wiki actually use.
It is never hand-edited: writing a card that uses a macro the preamble defines, then running `just macros`, is the whole procedure.

The preamble tree defines **1318** macros, so the vocabulary is far larger than the generated `macros.json` shows: that file holds only the macros the corpus and wiki have used so far.
Reading `macros.json` to decide whether a macro exists gives the wrong answer.
Read the preamble instead, `\input`s expanded, the way `sync_macros.py` reads it.

Everything the algebraic geometry material needs is already central: `\Spec`, `\Proj`, `\Pic`, `\Div`, `\Cl`, `\CaCl`, `\Jac`, `\codim`, `\krulldim`, `\trdeg`, `\Der`, `\length`, `\Ext`, `\inp`, `\GG`, `\fiberproduct`, the `\mc` family, and the usual `\OO`, `\PP`, `\AA`, `\da`, `\ts`, `\st`, `\sm`, `\union`, `\intersect`, `\ro`, `\dual`, `\gens`, `\mfm`, `\mfp`, `\injects`, `\tensor`, `\abs`, `\Frac`, `\Hom`.

Two paradigm changes the vault predates, and both are renames, not rewrites:

- script letters are **lowercase**: the vault's `\mcI`, `\mcF` become `\mci`, `\mcf`, matching `\mca`–`\mcz`;

- the fibre product takes its base as an argument: `\fiberprod{Y}` becomes `\fiberproduct{Y}`.

`\CaCl` was the one name genuinely absent, and it was added to `latexmacs.tex` beside `\Cl` rather than spelled out per-card, because the vocabulary is the place a name is defined once.

The remaining hazard is that nothing reports an undefined macro: `just check` passes and the page ships with the macro unexpanded, as red source.
See [issue #87](https://github.com/dzackgarza/new-qual-site/issues/87).

## Order of work

1. **Done.** `index.md` for the tree, and the nine topic `index.md` pages, from the study guides.

2. **Done.** The question bank into problem cards under `SRC-HARVARD-QUAL-SAMPLE-AG`, examiner attribution preserved.
   Sixty-two bullets of the MGSA compilation became forty cards; the collection is `completion: complete`.

3. **Done.** Topic pages and statement cards, in tree order, each written against the questions it answers.
   Statement cards live in `corpus/theory/Algebraic_Geometry`.

4. Solutions on the problem cards, one at a time, per the repository's solution workflow.
   Two are known to need a construction rather than a statement: the torsion Picard group, and the twisted cubic as a scheme-theoretic intersection.

5. Worked problems from the vault — 42 Hartshorne, 11 extra including Gathmann — as corpus problems with their original provenance, attached to the topic page each illustrates.

6. Figures and attachments from the vault re-homed under `assets/`, kept only where a page references them.

Authored data is written one card at a time, read and verified before the next.
`AGENTS.md` forbids scripts, loops and templates for this, and the rule is load-bearing: the cards are curation decisions, not records.
