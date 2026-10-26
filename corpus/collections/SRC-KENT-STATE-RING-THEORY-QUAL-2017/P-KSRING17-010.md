---
schema: qual/card@1
id: P-KSRING17-010
kind: problem
title: Ideals of a product of commutative rings are products of ideals
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 10 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R _ { 1 }$ and $R _ { 2 }$ be commutative rings with identities and let $R = R _ { 1 } \times R _ { 2 }$ . Show that every ideal I of R is of the form $I = I _ { 1 } \times I _ { 2 }$ with $I _ { i }$ an ideal of $R _ { i }$ for $i = 1 , 2$
:::

Let
$$
I\trianglelefteq R_1\times R_2.
$$
Define
$$
I_1
\coloneqq
\{a\in R_1:(a,0)\in I\},
\qquad
I_2
\coloneqq
\{b\in R_2:(0,b)\in I\}.
$$

::: pf

::: pf-step

The subset $I_1$ is an ideal of $R_1$.


::: pf-proof

Since
$$
(0,0)\in I,
$$
one has
$$
0\in I_1.
$$
If
$$
a,a'\in I_1,
$$
then
$$
(a,0),(a',0)\in I,
$$
so
$$
(a-a',0)\in I
$$
because $I$ is an additive subgroup. Hence
$$
a-a'\in I_1.
$$

If
$$
r\in R_1
$$
and
$$
a\in I_1,
$$
then
$$
(r,0)(a,0)
=
(ra,0)
\in I.
$$
Thus
$$
ra\in I_1.
$$
Therefore $I_1$ is an ideal of $R_1$.

:::

:::

::: pf-step

The subset $I_2$ is an ideal of $R_2$.


::: pf-proof

The proof is identical to step <1>1, using pairs of the form
$$
(0,b)
$$
and multiplication by
$$
(0,s),
\qquad
s\in R_2.
$$

:::

:::

::: pf-step

Every element of $I$ lies in
$$
I_1\times I_2.
$$


::: pf-proof

Let
$$
(a,b)\in I.
$$
Since
$$
(1,0),(0,1)\in R_1\times R_2,
$$
the ideal property gives
$$
(1,0)(a,b)
=
(a,0)
\in I
$$
and
$$
(0,1)(a,b)
=
(0,b)
\in I.
$$
Hence
$$
a\in I_1,
\qquad
b\in I_2,
$$
so
$$
(a,b)\in I_1\times I_2.
$$
Therefore
$$
I\subseteq I_1\times I_2.
$$

:::

:::

::: pf-step

Every element of
$$
I_1\times I_2
$$
lies in $I$.


::: pf-proof

Let
$$
(a,b)\in I_1\times I_2.
$$
By definition,
$$
(a,0)\in I,
\qquad
(0,b)\in I.
$$
Since $I$ is closed under addition,
$$
(a,b)
=
(a,0)+(0,b)
\in I.
$$
Thus
$$
I_1\times I_2\subseteq I.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
I
=
I_1\times I_2,
}
$$
with
$$
I_i\trianglelefteq R_i
$$
for
$$
i=1,2.
$$


::: pf-proof

Steps <1>1--<1>2 show that $I_1$ and $I_2$ are ideals, while steps <1>3--<1>4 prove the two inclusions.

:::

:::

::: pf-qed

Step <1>5 is the required decomposition.

:::

:::
