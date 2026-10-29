---
schema: qual/card@1
id: P-UCLAB07S-02
kind: problem
title: Invertibility of factors from an invertible composition
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $V,W,Z$ be $n$-dimensional vector spaces and let $T\colon V\to W$ and $U\colon W\to Z$ be linear.
Prove, without using determinants, that if $UT\colon V\to Z$ is invertible, then both $T$ and $U$ are invertible.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The map
$$
T:V\to W
$$
is injective.


::: pf-proof

Suppose
$$
Tv=0.
$$
Then
$$
(UT)v
=
U(Tv)
=
U(0)
=0.
$$
Since
$$
UT
$$
is invertible, it is injective.
Therefore
$$
v=0.
$$
Thus
$$
\ker T=\{0\},
$$
so $T$ is injective.

:::

:::

::: {.pf-step #s1-2}

Since
$$
\dim V=\dim W=n,
$$
the injective map $T$ is surjective.


::: pf-proof

By rank-nullity,
$$
\dim V
=
\dim\ker T
+
\dim\operatorname{im}T.
$$
Step [](#s1-1){.pf-ref} gives
$$
\dim\ker T=0.
$$
Therefore
$$
\dim\operatorname{im}T
=
n.
$$
But
$$
\operatorname{im}T
\subseteq W
$$
and
$$
\dim W=n.
$$
Hence
$$
\operatorname{im}T=W.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore $T$ is invertible.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} show that $T$ is both injective and surjective.
A linear bijection between vector spaces has a linear inverse.
Thus
$$
\boxed{T\text{ is invertible}.}
$$

:::

:::

::: {.pf-step #s1-4}

The map
$$
U:W\to Z
$$
is surjective.


::: pf-proof

Let
$$
z\in Z.
$$
Since
$$
UT:V\to Z
$$
is invertible, it is surjective.
Therefore there exists
$$
v\in V
$$
such that
$$
UTv=z.
$$
Set
$$
w=Tv\in W.
$$
Then
$$
Uw=z.
$$
Thus every $z\in Z$ lies in the image of $U$.

:::

:::

::: {.pf-step #s1-5}

Since
$$
\dim W=\dim Z=n,
$$
the surjective map $U$ is injective.


::: pf-proof

Rank-nullity gives
$$
\dim W
=
\dim\ker U
+
\dim\operatorname{im}U.
$$
By step [](#s1-4){.pf-ref},
$$
\operatorname{im}U=Z,
$$
so
$$
\dim\operatorname{im}U=n.
$$
Hence
$$
n
=
\dim\ker U+n,
$$
which forces
$$
\dim\ker U=0.
$$
Thus $U$ is injective.

:::

:::

::: {.pf-step #s1-6}

Therefore $U$ is invertible.


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} show that $U$ is bijective.
Thus
$$
\boxed{U\text{ is invertible}.}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves that $T$ is invertible, and step [](#s1-6){.pf-ref} proves that $U$ is invertible, without using determinants.

:::

:::

:::
