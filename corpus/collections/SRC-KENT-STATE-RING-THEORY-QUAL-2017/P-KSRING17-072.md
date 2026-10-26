---
schema: qual/card@1
id: P-KSRING17-072
kind: problem
title: Non-units form an ideal when $a$ or $1-a$ is always invertible
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 72 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity.
Suppose that for every $a \in R$ , either a or $1 - a$ is invertible.
Prove that $N = \{ a \in R \mid$ a is not invertible} is an ideal of R.
:::

Let
$$
N
\coloneqq
\{a\in R:a\text{ is not a unit}\}.
$$

::: pf

::: pf-step

The element
$$
0
$$
lies in $N$.


::: pf-proof

The zero element is not invertible in a nonzero ring with identity.
Hence
$$
0\in N.
$$

:::

:::

::: pf-step

If
$$
a\in N,
$$
then
$$
-a\in N.
$$


::: pf-proof

Suppose
$$
-a
$$
were a unit.
Then
$$
a=(-1)(-a)
$$
would be a product of units, hence a unit, contradicting
$$
a\in N.
$$
Thus
$$
-a
$$
is not invertible.

:::

:::

::: pf-step

If
$$
a\in N
$$
and
$$
r\in R,
$$
then
$$
ra\in N.
$$


::: pf-proof

Suppose
$$
ra
$$
were a unit.
Then there exists
$$
u\in R
$$
such that
$$
(ra)u=1.
$$
Because $R$ is commutative,
$$
a(ru)=1.
$$
Thus $a$ would be invertible, contradicting
$$
a\in N.
$$
Therefore
$$
ra\in N.
$$

:::

:::

::: pf-step

Suppose
$$
a,b\in N.
$$
Then
$$
a+b
$$
is not invertible.


::: pf-proof

Suppose, for contradiction, that
$$
u
\coloneqq
a+b
$$
is a unit.
Define
$$
c
\coloneqq
au^{-1}.
$$
Then
$$
1-c
=
1-au^{-1}
=
(a+b)u^{-1}-au^{-1}
=
bu^{-1}.
$$

The element
$$
c=au^{-1}
$$
is not a unit: if it were, then
$$
a=cu
$$
would be a product of units and therefore a unit, contradicting
$$
a\in N.
$$

Similarly,
$$
1-c=bu^{-1}
$$
is not a unit, because otherwise
$$
b=(1-c)u
$$
would be a unit.

Thus neither
$$
c
$$
nor
$$
1-c
$$
is invertible.
This contradicts the hypothesis that for every element of $R$, either that element or its complement to $1$ is invertible.

Therefore
$$
a+b
$$
cannot be a unit.

:::

:::

::: pf-step

The set $N$ is an additive subgroup of $R$.


::: pf-proof

Step <1>1 gives
$$
0\in N.
$$
Step <1>2 gives closure under additive inverses, and step <1>4 gives closure under addition.
Hence $N$ is an additive subgroup.

:::

:::

::: pf-step

Therefore
$$
\boxed{
N
\text{ is an ideal of }R.
}
$$


::: pf-proof

By step <1>5, $N$ is an additive subgroup of $R$.
By step <1>3, it is closed under multiplication by arbitrary elements of $R$.
Thus
$$
N\trianglelefteq R.
$$

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
