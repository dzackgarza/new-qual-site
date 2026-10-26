---
schema: qual/card@1
id: P-KSRING17-065
kind: problem
title: The nilpotent elements of a commutative ring form an ideal
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 65 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity.
Show that if x and y are nilpotent elements of R then $x + y$ is nilpotent and the set of all nilpotent elements is an ideal in R.
:::

Let
$$
\mathcal N
\coloneqq
\{r\in R:r^k=0\text{ for some }k\ge1\}.
$$

::: pf

::: pf-step

If
$$
x^m=0
$$
and
$$
y^n=0,
$$
then
$$
(x+y)^{m+n-1}=0.
$$


::: pf-proof

By the binomial theorem,
$$
(x+y)^{m+n-1}
=
\sum_{k=0}^{m+n-1}
\binom{m+n-1}{k}
x^k y^{m+n-1-k}.
$$
Fix a summand.
If
$$
k\ge m,
$$
then
$$
x^k=0.
$$
If instead
$$
k<m,
$$
then
$$
k\le m-1,
$$
so
$$
m+n-1-k
\ge
n,
$$
and therefore
$$
y^{m+n-1-k}=0.
$$
Thus every summand is zero, and hence
$$
(x+y)^{m+n-1}=0.
$$

:::

:::

::: pf-step

The sum of two nilpotent elements is nilpotent.


::: pf-proof

If
$$
x,y\in\mathcal N,
$$
choose
$$
m,n\ge1
$$
with
$$
x^m=0,
\qquad
y^n=0.
$$
Step <1>1 then gives
$$
(x+y)^{m+n-1}=0.
$$
Thus
$$
x+y\in\mathcal N.
$$

:::

:::

::: pf-step

The additive inverse of a nilpotent element is nilpotent.


::: pf-proof

If
$$
x^m=0,
$$
then
$$
(-x)^m
=
(-1)^m x^m
=
0.
$$
Thus
$$
-x\in\mathcal N.
$$

:::

:::

::: pf-step

The set $\mathcal N$ is an additive subgroup of $R$.


::: pf-proof

The element
$$
0
$$
is nilpotent.
Step <1>2 gives closure under addition, and step <1>3 gives closure under additive inverses.

:::

:::

::: pf-step

If
$$
r\in R
$$
and
$$
x\in\mathcal N,
$$
then
$$
rx\in\mathcal N.
$$


::: pf-proof

Choose
$$
m\ge1
$$
such that
$$
x^m=0.
$$
Because $R$ is commutative,
$$
(rx)^m
=
r^m x^m
=
0.
$$
Hence
$$
rx
\in
\mathcal N.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
\mathcal N
\text{ is an ideal of }R.
}
$$


::: pf-proof

By step <1>4, $\mathcal N$ is an additive subgroup.
By step <1>5, it is closed under multiplication by arbitrary elements of $R$.
Thus it is an ideal.

:::

:::

::: pf-qed

Step <1>2 proves the first assertion, and step <1>6 proves the second.

:::

:::
