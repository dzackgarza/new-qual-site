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

::: {.problem}
Compute the first, second and third homotopy groups of $X = \mathbb{RP}^2 \times S^1 \times S^1$.
:::

::: {.solution}

::: pf

::: pf-step
The fundamental group is
$$
\pi_1(X)\cong\mathbb Z/2\oplus\mathbb Z\oplus\mathbb Z.
$$

::: pf-proof
Fundamental groups commute with finite products, and
$$
\pi_1(\mathbb{RP}^2)=\mathbb Z/2,
\qquad
\pi_1(S^1)=\mathbb Z.
$$
:::

:::

::: {.pf-step #pi-n-x-equals-pi-n-rp2}
For every $n\ge2$,
$$
\pi_n(X)\cong\pi_n(\mathbb{RP}^2).
$$

::: pf-proof
Higher homotopy groups commute with products, while $\pi_n(S^1)=0$ for $n\ge2$.
:::

:::

::: {.pf-step #universal-cover-iso-degree2}
The universal cover $S^2\to\mathbb{RP}^2$ induces isomorphisms on homotopy groups in degrees at least $2$.

::: pf-proof
Every covering map induces isomorphisms on $\pi_n$ for $n\ge2$.
:::

:::

::: pf-step
Therefore
$$
\boxed{
\pi_1(X)=\mathbb Z/2\oplus\mathbb Z^2,
\qquad
\pi_2(X)=\mathbb Z,
\qquad
\pi_3(X)=\mathbb Z.}
$$

::: pf-proof
Use steps [](#pi-n-x-equals-pi-n-rp2){.pf-ref} and [](#universal-cover-iso-degree2){.pf-ref} together with
$$
\pi_2(S^2)\cong\mathbb Z,
\qquad
\pi_3(S^2)\cong\mathbb Z.
$$
:::

:::

:::

:::
