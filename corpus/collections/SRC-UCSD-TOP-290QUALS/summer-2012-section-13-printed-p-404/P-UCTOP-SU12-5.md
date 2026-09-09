---
schema: qual/card@1
id: P-UCTOP-SU12-5
kind: problem
title: Homotopy groups of RP^2 × S^1 × S^1
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

Compute the first, second and third homotopy groups of $X = \mathbb{RP}^2 \times S^1 \times S^1$.

::: {.solution}
<1>1. The fundamental group is
$$
\pi_1(X)\cong\mathbb Z/2\oplus\mathbb Z\oplus\mathbb Z.
$$
::: {.proof}
Fundamental groups commute with finite products, and
$$
\pi_1(\mathbb{RP}^2)=\mathbb Z/2,
\qquad
\pi_1(S^1)=\mathbb Z.
$$
:::

<1>2. For every $n\ge2$,
$$
\pi_n(X)\cong\pi_n(\mathbb{RP}^2).
$$
::: {.proof}
Higher homotopy groups commute with products, while $\pi_n(S^1)=0$ for $n\ge2$.
:::

<1>3. The universal cover $S^2\to\mathbb{RP}^2$ induces isomorphisms on homotopy groups in degrees at least $2$.
::: {.proof}
Every covering map induces isomorphisms on $\pi_n$ for $n\ge2$.
:::

<1>4. Therefore
$$
\boxed{
\pi_1(X)=\mathbb Z/2\oplus\mathbb Z^2,
\qquad
\pi_2(X)=\mathbb Z,
\qquad
\pi_3(X)=\mathbb Z.}
$$
::: {.proof}
Use <1>2--<1>3 together with
$$
\pi_2(S^2)\cong\mathbb Z,
\qquad
\pi_3(S^2)\cong\mathbb Z.
$$
:::
:::
