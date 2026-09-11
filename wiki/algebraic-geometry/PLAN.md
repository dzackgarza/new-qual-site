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

- `\operatorname{Spec}`, `\operatorname{Proj}`, `\Pic`, `\Div`, `\Frac`, `\QCoh`, `\Coh` do **not** exist in `vocabularies/macros.json` and must be added before the first card is written, not invented per-card.

- `\left(...\right)` is removed rather than translated; the site's other subjects do not use it and it renders badly at small sizes.

Adding the AG macros to the shared vocabulary is the first task, because every card written before it exists will have to be rewritten.

## Order of work

1. Extend `vocabularies/macros.json` with the algebraic-geometry vocabulary.

2. `index.md` for the tree, and the topic `index.md` pages, from the study guides.
   This fixes the skeleton before any card is written into it.

3. The question bank into problem cards, examiner attribution preserved.
   This is pure transcription of irreplaceable material and can proceed immediately.

4. Topic cards, in tree order, each one written against the questions it is supposed to answer — varieties first, toric last.

5. Worked problems, attached to the topic cards as they are written, so that each problem lands next to the method it illustrates.
