---
schema: qual/card@1
id: P-KBHAC
kind: problem
title: Compact surfaces of Euler characteristic $-1$
classification:
  areas:
  - topology
  topics:
  - Classification
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Spring 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Solved both Euler-characteristic Diophantine equations and used the compact-surface classification invariants to check completeness and nonduplication.
---

::: problem
Give a list without repetitions of all compact surfaces (orientable or non-orientable and with or without boundary) that have Euler characteristic negative one.

Explain why there are no repetitions on your list.
:::

::: {.solution}
Use the standard convention that a surface is connected.
Write $\Sigma_{g,b}$ for the compact orientable surface of genus $g$ with $b$ boundary components, and $N_{k,b}$ for the compact nonorientable surface of nonorientable genus $k$ with $b$ boundary components.

<1>1. The orientable surfaces with Euler characteristic $-1$ are exactly
\[
\boxed{\Sigma_{0,3},\qquad \Sigma_{1,1}}.
\]
Thus they are a pair of pants and a torus with one open disk removed.
::: {.proof}
The classification theorem for compact connected orientable surfaces gives
\[
\chi(\Sigma_{g,b})=2-2g-b,
\qquad g,b\ge0.
\]
The equation $\chi=-1$ is therefore
\[
2g+b=3.
\]
Its only solutions in nonnegative integers are
\[
(g,b)=(0,3),\ (1,1).
\]
:::

<1>2. The nonorientable surfaces with Euler characteristic $-1$ are exactly
\[
\boxed{N_{1,2},\qquad N_{2,1},\qquad N_{3,0}}.
\]
Equivalently, these are a projective plane with two open disks removed, a Klein bottle with one open disk removed, and the closed connected sum of three projective planes.
::: {.proof}
The classification theorem for compact connected nonorientable surfaces gives
\[
\chi(N_{k,b})=2-k-b,
\qquad k\ge1,\ b\ge0.
\]
Thus $\chi=-1$ is equivalent to
\[
k+b=3.
\]
The only solutions are
\[
(k,b)=(1,2),\ (2,1),\ (3,0).
\]
Since $N_{2,0}$ is the Klein bottle, $N_{2,1}$ is a Klein bottle with one open disk removed.
:::

<1>3. The five surfaces in <1>1 and <1>2 form the complete list without repetitions.
::: {.proof}
Every compact connected surface is either orientable or nonorientable, and the classification theorem places it in exactly one of the forms $\Sigma_{g,b}$ or $N_{k,b}$ used above.
Steps <1>1 and <1>2 exhaust every integer solution of $\chi=-1$ in the two cases.

There can be no repetition between the two lists because orientability is a homeomorphism invariant.
Within either list, the ordered data consisting of genus and number of boundary components are classification invariants, and the displayed parameter pairs are distinct.
Hence no two listed surfaces are homeomorphic.
:::
:::
