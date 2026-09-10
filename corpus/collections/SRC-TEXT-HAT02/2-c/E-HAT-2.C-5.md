---
schema: qual/card@1
id: E-HAT-2.C-5
kind: problem
title: Fixed-point-free homotopies of reflected surfaces
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
---

Let $M$ be a closed orientable surface embedded in $\mathbb{R}^3$ in such a way that reflection across a plane $P$ defines a homeomorphism $r: M \to M$ fixing $M \cap P$, a collection of circles.
Is it possible to homotope $r$ to have no fixed points?

::: {.solution}
Yes. In fact one can remove the fixed circles by an arbitrarily small perturbation through maps homotopic to the reflection.

Let
\[
F=M\cap P=C_1\amalg\cdots\amalg C_r.
\]
Since $r$ is reflection across $P$, each $C_j$ has an $r$-invariant annular neighborhood with coordinates
\[
(\theta,t)\in S^1\times(-\varepsilon,\varepsilon)
\]
in which
\[
r(\theta,t)=(\theta,-t).
\]

<1>1. There is a homeomorphism $h:M\to M$, isotopic to the identity and supported in these annuli, such that on a smaller annulus about each $C_j$,
\[
h(\theta,t)=(\theta+\delta,t)
\]
for a fixed small $\delta\ne0$.
::: {.proof}
Choose a bump function $\rho(t)$ equal to $1$ near $0$ and $0$ near the boundary of the annulus, and set
\[
h_s(\theta,t)=(\theta+s\delta\rho(t),t),\qquad 0\le s\le1.
\]
These maps give an isotopy, extended by the identity outside the disjoint annuli.
:::

<1>2. The map
\[
g=h\circ r
\]
has no fixed points.
::: {.proof}
Outside the chosen annuli, $h$ is the identity and $r$ has no fixed points. In an annulus,
\[
g(\theta,t)=(\theta+\delta\rho(-t),-t).
\]
A fixed point would require $t=-t$, hence $t=0$, and then would require $\theta+\delta=\theta$ in $S^1$, impossible for the chosen nonzero sufficiently small $\delta$.
:::

<1>3. The map $g$ is homotopic to $r$.
::: {.proof}
Since $h$ is isotopic to the identity, the maps $h_s\circ r$ give a homotopy from $r$ to $g$.
:::

Thus
\[
\boxed{r\text{ can be homotoped to a fixed-point-free map}.}
\]
This is consistent with Exercise 4: $\tau(r)=\chi(F)=0$ because $F$ is a disjoint union of circles.
:::
