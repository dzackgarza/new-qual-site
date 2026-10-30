---
schema: qual/card@1
id: P-KSRING17-016
kind: problem
title: Ideals of the matrix ring $M_n(R)$ are $M_n(I)$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 16 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be any ring with identity, and $n$ any positive integer. If $M_{n}(R)$ denotes the ring of $n \times n$ matrices with entries in $R$, prove that $M_{n}(I)$ is an ideal of $M_{n}(R)$ whenever $I$ is an ideal of $R$, and that every ideal of $M_{n}(R)$ has this form.
:::

::: {.solution}

Let
$$
E_{ij}
$$
denote the standard matrix unit with $1_R$ in position $(i,j)$ and $0$ elsewhere.

::: pf

::: {.pf-step #s1-1}

If
$$
I\trianglelefteq R,
$$
then
$$
M_n(I)
$$
is a two-sided ideal of
$$
M_n(R).
$$


::: pf-proof

The set $M_n(I)$ is closed under subtraction entrywise because $I$ is an additive subgroup of $R$.

Let
$$
A=(a_{ij})\in M_n(I),
\qquad
B=(b_{ij})\in M_n(R).
$$
The $(i,j)$ entry of $BA$ is
$$
\sum_{k=1}^n b_{ik}a_{kj}.
$$
Since every $a_{kj}\in I$ and $I$ is a left ideal,
$$
b_{ik}a_{kj}\in I.
$$
Hence every entry of $BA$ lies in $I$, so
$$
BA\in M_n(I).
$$

Similarly, the $(i,j)$ entry of $AB$ is
$$
\sum_{k=1}^n a_{ik}b_{kj},
$$
and every summand lies in $I$ because $I$ is a right ideal. Therefore
$$
AB\in M_n(I).
$$
Thus $M_n(I)$ is a two-sided ideal.

:::

:::

::: {.pf-step #s1-2}

Let
$$
J\trianglelefteq M_n(R).
$$
Define
$$
I
\coloneqq
\{r\in R:rE_{11}\in J\}.
$$
Then $I$ is a two-sided ideal of $R$.


::: pf-proof

Since
$$
0\cdot E_{11}=0\in J,
$$
one has $0\in I$.

If
$$
r,s\in I,
$$
then
$$
rE_{11},sE_{11}\in J,
$$
so
$$
(r-s)E_{11}
=
rE_{11}-sE_{11}
\in J.
$$
Hence
$$
r-s\in I.
$$

Let
$$
t\in R
$$
and
$$
r\in I.
$$
Then
$$
(tE_{11})(rE_{11})
=
(tr)E_{11}
\in J
$$
and
$$
(rE_{11})(tE_{11})
=
(rt)E_{11}
\in J,
$$
because $J$ is a two-sided ideal of $M_n(R)$. Therefore
$$
tr,rt\in I.
$$
Thus $I\trianglelefteq R$.

:::

:::

::: {.pf-step #s1-3}

If
$$
A=(a_{ij})\in J,
$$
then every entry
$$
a_{ij}
$$
lies in $I$.


::: pf-proof

For any indices
$$
i,j,
$$
the ideal property gives
$$
E_{1i}AE_{j1}
\in J.
$$
A direct matrix-unit computation gives
$$
E_{1i}AE_{j1}
=
a_{ij}E_{11}.
$$
Hence
$$
a_{ij}E_{11}\in J,
$$
so by definition
$$
a_{ij}\in I.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
J\subseteq M_n(I).
$$


::: pf-proof

Let
$$
A=(a_{ij})\in J.
$$
By step [](#s1-3){.pf-ref}, every entry $a_{ij}$ lies in $I$. Therefore
$$
A\in M_n(I).
$$

:::

:::

::: {.pf-step #s1-5}

If
$$
r\in I,
$$
then for every pair of indices $k,\ell$,
$$
rE_{k\ell}\in J.
$$


::: pf-proof

By definition of $I$,
$$
rE_{11}\in J.
$$
Since $J$ is a two-sided ideal,
$$
E_{k1}(rE_{11})E_{1\ell}
\in J.
$$
The product equals
$$
rE_{k\ell}.
$$
Hence
$$
rE_{k\ell}\in J.
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
M_n(I)\subseteq J.
$$


::: pf-proof

Let
$$
A=(a_{k\ell})\in M_n(I).
$$
Then
$$
A
=
\sum_{k,\ell=1}^n
a_{k\ell}E_{k\ell}.
$$
Each
$$
a_{k\ell}\in I,
$$
so step [](#s1-5){.pf-ref} gives
$$
a_{k\ell}E_{k\ell}\in J.
$$
Because $J$ is closed under finite sums,
$$
A\in J.
$$
Therefore
$$
M_n(I)\subseteq J.
$$

:::

:::

::: {.pf-step #s1-7}

Hence every ideal of $M_n(R)$ is of the form $M_n(I)$ for a unique ideal $I$ of $R$:
$$
\boxed{
J=M_n(I).
}
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref} prove the two inclusions.

Uniqueness follows because if
$$
M_n(I)=M_n(I'),
$$
then
$$
r\in I
\iff
rE_{11}\in M_n(I)
\iff
rE_{11}\in M_n(I')
\iff
r\in I'.
$$
Thus
$$
I=I'.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the first assertion, and steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} prove the classification of all ideals of $M_n(R)$.

:::

:::

:::
