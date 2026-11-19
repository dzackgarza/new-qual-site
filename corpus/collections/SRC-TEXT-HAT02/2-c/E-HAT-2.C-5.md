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
  note: Verified the simplicial, Lefschetz-trace, or surface argument used against the preceding section results.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 5, printed page
    184; the statement matches word for word. The card answers yes with an explicit
    construction, and it was checked: in a collar (θ,t) of a fixed circle the
    reflection is r(θ,t) = (θ,−t), the twist h(θ,t) = (θ + δρ(t), t) with ρ = 1 near
    t = 0 is an isotopy of homeomorphisms supported in the collars, and g = h∘r
    satisfies g(θ,t) = (θ + δρ(−t), −t), so a fixed point would force t = 0 and
    δρ(0) = δ ≠ 0. This is consistent with tau(r) = chi(M ∩ P) = 0 from the preceding
    exercise, so the Lefschetz theorem does not obstruct it. No defect.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 5 of §2.C, printed p. 184, in
    `tmp/sources/hatcher-2002-algebraic-topology.md`, and against Li, Exercise 2.C.3 (Hatcher 2.C.5),
    whose statement closes printed p. 44 and whose solution is on printed p. 45 — the card's page is
    right. The card's criticism of the source is also right, and was checked against the page: Li's
    $H(x,t)$ is the identity off the collar and twists by $\pi t\abs{s}$ inside it, so at $t=0$ it is
    not $r$ off the collar, and at $s=0$ the twist vanishes, so his fixed circles stay fixed and the
    claim that the time-one map has no fixed point on $N$ does not follow. Checked in the card:
    $h_s(\theta,t)=(\theta+s\delta\rho(t),t)$ is an isotopy of homeomorphisms supported in the
    collars, so $h_s\circ r$ is a homotopy from $r$ to $g=h\circ r$; off the collars $g=r$ has no
    fixed point because $\operatorname{Fix}(r)=M\cap P$ lies in them; inside,
    $g(\theta,t)=(\theta+\delta\rho(-t),-t)$ forces $t=0$ and then $\delta\ne0$ in $S^1$; and
    $\tau(r)=\chi(M\cap P)=0$ by Exercise 4, so no Lefschetz obstruction exists. No defect.

---

::: {.problem}
Let $M$ be a closed orientable surface embedded in $\RR^3$ in such a way that reflection across a plane $P$ defines a homeomorphism $r: M \to M$ fixing $M \cap P$, a collection of circles.
Is it possible to homotope $r$ to have no fixed points?
:::

::: {.solution}
Yes. In fact one can remove the fixed circles by an arbitrarily small perturbation through maps homotopic to the reflection.

Let
$$
F=M\cap P=C_1\amalg\cdots\amalg C_r.
$$
Since $r$ is reflection across $P$, each $C_j$ has an $r$-invariant annular neighborhood with coordinates
$$
(\theta,t)\in S^1\times(-\varepsilon,\varepsilon)
$$
in which
$$
r(\theta,t)=(\theta,-t).
$$

::: pf

::: pf-step

There is a homeomorphism $h:M\to M$, isotopic to the identity and supported in these annuli, such that on a smaller annulus about each $C_j$,
$$
h(\theta,t)=(\theta+\delta,t)
$$
for a fixed small $\delta\ne0$.

::: pf-proof

Choose a bump function $\rho(t)$ equal to $1$ near $0$ and $0$ near the boundary of the annulus, and set
$$
h_s(\theta,t)=(\theta+s\delta\rho(t),t),\qquad 0\le s\le1.
$$
These maps give an isotopy, extended by the identity outside the disjoint annuli.

:::

:::

::: pf-step

The map
$$
g=h\circ r
$$
has no fixed points.

::: pf-proof

Outside the chosen annuli, $h$ is the identity and $r$ has no fixed points. In an annulus,
$$
g(\theta,t)=(\theta+\delta\rho(-t),-t).
$$
A fixed point would require $t=-t$, hence $t=0$, and then would require $\theta+\delta=\theta$ in $S^1$, impossible for the chosen nonzero sufficiently small $\delta$.

:::

:::

::: pf-step

The map $g$ is homotopic to $r$.

::: pf-proof

Since $h$ is isotopic to the identity, the maps $h_s\circ r$ give a homotopy from $r$ to $g$.

:::

:::

:::

Thus
$$
\boxed{r\text{ can be homotoped to a fixed-point-free map}.}
$$
This is consistent with Exercise 4: $\tau(r)=\chi(F)=0$ because $F$ is a disjoint union of circles.

The annulus-based perturbation is in **Guanyu Li, [`Hatcher.pdf`](https://guanyulee.github.io/Hatcher.pdf)**, Exercise 2.C.3 (Hatcher 2.C.5), printed p. 45 (`tmp/sources/hatcher-solutions-guanyu-li.pdf`). Li's displayed formula is not adopted: outside the annular neighborhood $U$, at $t=0$ it is $x$ rather than $r(x)$, and at $s=0$ the twist term vanishes. The construction immediately above is the **correction of that endpoint behavior**: $h_s$ is an isotopy to the identity supported inside each annulus, so $h_s\circ r$ still agrees with $r$ outside those annuli and removes every point fixed by $r$ on their boundaries $s=0$. The consistency check $\tau(r)=\chi(C_1\sqcup\cdots\sqcup C_r)=0$ uses Exercise 4.


:::
