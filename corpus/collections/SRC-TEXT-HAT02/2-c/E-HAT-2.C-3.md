---
schema: qual/card@1
id: E-HAT-2.C-3
kind: problem
title: Conjugate-linear map on $\mathbb{C}^{2k}$ induces fixed-point-free map on $\mathbb{CP}^{2k-1}$
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Projective Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
---

Verify that the formula $f(z_1, \cdots, z_{2k}) = (\bar{z}_2, -\bar{z}_1, \bar{z}_4, -\bar{z}_3, \cdots, \bar{z}_{2k}, -\bar{z}_{2k-1})$ defines a map $f: \mathbb{C}^{2k} \to \mathbb{C}^{2k}$ inducing a quotient map $\mathbb{CP}^{2k-1} \to \mathbb{CP}^{2k-1}$ without fixed points.

::: {.solution}
Define
\[
F(z_1,\ldots,z_{2k})=(\bar z_2,-\bar z_1,\ldots,\bar z_{2k},-\bar z_{2k-1}).
\]

<1>1. The map $F$ is conjugate-linear and satisfies
\[
F(\lambda z)=\bar\lambda F(z),
\qquad
F^2=-\operatorname{id}.
\]
::: {.proof}
Both identities follow by direct calculation on each coordinate pair $(z_{2j-1},z_{2j})$:
\[
(z_{2j-1},z_{2j})\mapsto(\bar z_{2j},-\bar z_{2j-1})
\mapsto(-z_{2j-1},-z_{2j}).
\]
:::

<1>2. Hence $F$ induces a well-defined map
\[
f:\mathbb{CP}^{2k-1}\to\mathbb{CP}^{2k-1},
\qquad
f([z])=[F(z)].
\]
::: {.proof}
If $[z]=[\lambda z]$ with $\lambda\ne0$, then
\[
F(\lambda z)=\bar\lambda F(z),
\]
so $F(\lambda z)$ and $F(z)$ determine the same complex line. Also $F(z)\ne0$ for $z\ne0$ because $F^2=-\operatorname{id}$.
:::

<1>3. The map $f$ has no fixed point.
::: {.proof}
If $[z]$ were fixed, then for some $\lambda\in\mathbb C^*$ we would have
\[
F(z)=\lambda z.
\]
Applying $F$ and using conjugate-linearity gives
\[
-z=F^2(z)=F(\lambda z)=\bar\lambda F(z)=|\lambda|^2z.
\]
Since $z\ne0$, this would imply $|\lambda|^2=-1$, impossible.
:::

Thus the displayed conjugate-linear map induces a fixed-point-free self-map of $\mathbb{CP}^{2k-1}$.
:::
