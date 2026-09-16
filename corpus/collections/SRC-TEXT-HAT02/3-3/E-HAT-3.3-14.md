---
schema: qual/card@1
id: E-HAT-3.3-14
kind: problem
title: "Shrinking wedge of circles"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the finite commutator-length obstruction from Exercise 12 after retracting onto finitely many circles.
---

::: {.problem}
Let $X$ be the shrinking wedge of circles in Example 1.25, the subspace of $\mathbb{R}^2$ consisting of the circles of radius $1/n$ and center $(1/n, 0)$ for $n = 1, 2, \ldots$.

(a) If $f_n: I \to X$ is the loop based at the origin winding once around the $n$th circle, show that the infinite product of commutators $[f_1, f_2][f_3, f_4] \cdots$ defines a loop in $X$ that is nontrivial in $H_1(X)$.

(b) If we view $X$ as the wedge sum of the subspaces $A$ and $B$ consisting of the odd-numbered and even-numbered circles, respectively, use the same loop to show that the map $H_1(X) \to H_1(A) \oplus H_1(B)$ induced by the retractions of $X$ onto $A$ and $B$ is not an isomorphism.
:::

::: {.solution}
Let
\[
\gamma=[f_1,f_2][f_3,f_4]\cdots
\]
be the infinite concatenation, parametrized so that the $j$th commutator is traversed on a subinterval whose lengths tend to $0$. Since the diameters of the circles tend to $0$, this defines a continuous based loop in $X$.

For $N\ge1$, let
\[
r_N:X\longrightarrow \bigvee_{i=1}^N S_i^1
\]
be the retraction that is the identity on the first $N$ circles and collapses all later circles to the wedge point.

<1>1. The class of $\gamma$ is nonzero in $H_1(X;\mathbb Z)$.
::: {.proof}
Suppose instead that $[\gamma]=0$ in $H_1(X;\mathbb Z)$. By the Hurewicz theorem in degree $1$,
\[
H_1(X;\mathbb Z)\cong \pi_1(X)_{\mathrm{ab}},
\]
so the element represented by $\gamma$ lies in the commutator subgroup of $\pi_1(X)$. By definition of the commutator subgroup, it is therefore a finite product of commutators:
\[
[\gamma]_{\pi_1}=[u_1,v_1]\cdots [u_k,v_k]
\]
for some $u_i,v_i\in\pi_1(X)$.

Apply $(r_{2k+2})_*$. If $x_i$ denotes the standard free generator of
\[
\pi_1\!\left(\bigvee_{i=1}^{2k+2}S_i^1\right)\cong F(x_1,\dots,x_{2k+2}),
\]
then every commutator in the tail of $\gamma$ uses circles numbered $>2k+2$ and is collapsed. Hence
\[
(r_{2k+2})_*([\gamma]_{\pi_1})
=[x_1,x_2][x_3,x_4]\cdots[x_{2k+1},x_{2k+2}].
\]
On the other hand, the image of the right-hand side above is a product of at most $k$ commutators in this free group. This contradicts Exercise 12, which says that the displayed product of $k+1$ basis commutators cannot be expressed as a product of fewer than $k+1$ commutators. Therefore $[\gamma]\ne0$ in $H_1(X;\mathbb Z)$.
:::

<1>2. The map
\[
H_1(X)\longrightarrow H_1(A)\oplus H_1(B)
\]
induced by the retractions onto the odd and even circles is not an isomorphism.
::: {.proof}
Let $r_A:X\to A$ and $r_B:X\to B$ be the two retractions. Each factor
\[
[f_{2j-1},f_{2j}]
\]
contains one loop in $A$ and one loop in $B$. Under $r_A$, the even loop is collapsed, so the commutator becomes trivial; under $r_B$, the odd loop is collapsed, so it again becomes trivial. Thus both $(r_A)_*([\gamma])$ and $(r_B)_*([\gamma])$ vanish in first homology.

By part 1, however, $[\gamma]\ne0$ in $H_1(X)$. Hence the displayed map has nonzero kernel and therefore is not an isomorphism.
:::
:::
