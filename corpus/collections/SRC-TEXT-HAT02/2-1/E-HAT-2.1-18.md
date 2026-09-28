---
schema: qual/card@1
id: E-HAT-2.1-18
kind: problem
title: $H_1(\mathbb{R}, \mathbb{Q})$ is free abelian
classification:
  areas:
  - topology
  topics:
  - Homology
  - Relative Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 18; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified H_1(R,Q) with the augmentation kernel of the free abelian group on Q and exhibited the standard difference basis.
---

::: {.problem}
Show that for the subspace $\mathbb{Q} \subset \mathbb{R}$, the relative homology group $H_1(\mathbb{R}, \mathbb{Q})$ is free abelian and find a basis.
:::

::: {.solution}
Since $\mathbb R$ is contractible,
\[
H_1(\mathbb R)=0,
\qquad
H_0(\mathbb R)\cong\mathbb Z.
\]
The subspace $\mathbb Q$ is totally disconnected, so each rational number is a path-component and
\[
H_0(\mathbb Q)\cong\bigoplus_{q\in\mathbb Q}\mathbb Z[q].
\]

<1>1. The long exact sequence gives
\[
H_1(\mathbb R,\mathbb Q)
\cong
\ker\left(H_0(\mathbb Q)\to H_0(\mathbb R)\right).
\]
::: {.proof}
The relevant segment is
\[
0=H_1(\mathbb R)\to H_1(\mathbb R,\mathbb Q)
\to H_0(\mathbb Q)\to H_0(\mathbb R).
\]
Exactness gives the claimed identification.
:::

<1>2. Under the component bases, the map
\[
H_0(\mathbb Q)\to H_0(\mathbb R)\cong\mathbb Z
\]
is the augmentation
\[
\sum_q n_q[q]\longmapsto\sum_q n_q.
\]
::: {.proof}
All points of $\mathbb Q$ lie in the single path-component of $\mathbb R$, so every generator $[q]$ maps to the same generator $1$ of $H_0(\mathbb R)$.
:::

<1>3. Fix $0\in\mathbb Q$. Then
\[
\mathcal B=\{[q]-[0]:q\in\mathbb Q,\ q\ne0\}
\]
is a basis of the augmentation kernel.
::: {.proof}
Each element lies in the kernel. Any finite sum
\[
\sum_q n_q[q]
\]
with total coefficient zero equals
\[
\sum_{q\ne0}n_q([q]-[0]),
\]
so $\mathcal B$ spans. If a finite linear combination of elements of $\mathcal B$ vanishes, comparison of the coefficient of each $[q]$ with $q\ne0$ shows every coefficient is zero, so the set is independent.
:::

<1>4. Therefore
\[
\boxed{H_1(\mathbb R,\mathbb Q)
\cong\bigoplus_{q\in\mathbb Q\setminus\{0\}}\mathbb Z,}
\]
with basis represented by the classes $[q]-[0]$.
::: {.proof}
Combine <1>1--<1>3.
:::
:::
