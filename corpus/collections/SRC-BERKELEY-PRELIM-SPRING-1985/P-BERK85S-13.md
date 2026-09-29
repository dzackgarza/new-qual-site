---
schema: qual/card@1
id: P-BERK85S-13
kind: problem
title: $1+z+az^n$ always has a root in $|z|\le2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Independently checked the later Berkeley Fall 2006 solution of the same
    problem: the small-|b| case follows from the product of the roots, and the
    large-|b| Rouché estimate follows from |1+z| >= ||z|-1| on |z|=2.
---

::: {.problem}
Let $a\in\mathbb C$ and let $n\ge2$ be an integer. Prove that
\[
1+z+az^n=0
\]
has at least one root in the closed disk
\[
|z|\le2.
\]
:::

::: {.solution}
::: pf

::: {.pf-step #zero-a-case}
If $a=0$, the equation has the root $z=-1$.

::: pf-proof
For $a=0$, the equation is $1+z=0$, and
$$
\abs{-1}=1\leq2.
$$
:::

:::

::: {.pf-step #p-same-roots}
Suppose $a\neq0$, set $b\coloneqq a^{-1}$, and define
$$
p(z)\coloneqq z^n+bz+b.
$$
Then $p$ has exactly the same roots as $1+z+az^n$.

::: pf-proof
Multiplying the original polynomial by the nonzero scalar $b$ gives
$$
b(1+z+az^n)=b+bz+z^n=p(z).
$$
Multiplication by a nonzero scalar does not change the zero set.
:::

:::

::: {.pf-step #small-b-case}
If $\abs b\leq2^n$, then $p$ has a root $z_0$ with
$\abs{z_0}\leq2$.

::: pf-proof
Let $z_1,\ldots,z_n$ be the roots of the monic polynomial $p$, counted with
multiplicity. By Vieta's formula,
$$
\abs{z_1\cdots z_n}=\abs b.
$$
If every root satisfied $\abs{z_j}>2$, then
$$
\abs{z_1\cdots z_n}>2^n,
$$
contradicting $\abs b\leq2^n$.
:::

:::

::: {.pf-step #large-b-case}
If $\abs b>2^n$, then $p$ has a root $z_0$ with
$\abs{z_0}<2$.

::: pf-proof
On the circle $\abs z=2$, let
$$
g(z)\coloneqq b(1+z).
$$
The reverse triangle inequality gives
$$
\abs{1+z}\geq\bigl|\abs z-1\bigr|=1.
$$
Hence
$$
\abs{p(z)-g(z)}
=\abs{z^n}
=2^n
<\abs b
\leq\abs{b(1+z)}
=\abs{g(z)}.
$$
By Rouché's theorem, $p$ and $g$ have the same number of zeros in
$\abs z<2$, counted with multiplicity. The function $g$ has exactly one
zero there, namely $z=-1$. Thus $p$ has a zero in $\abs z<2$.
:::

:::

::: {.pf-step #conclusion-boxed}
For every $a\in\CC$ and every integer $n\geq2$,
$$
\boxed{\text{there exists }z_0\in\CC\text{ such that }
1+z_0+az_0^n=0\text{ and }\abs{z_0}\leq2}.
$$

::: pf-proof
Step [](#zero-a-case){.pf-ref} handles $a=0$. For $a\neq0$, either
$\abs b\leq2^n$ or $\abs b>2^n$; steps [](#small-b-case){.pf-ref} and [](#large-b-case){.pf-ref} respectively give
the required root, and step [](#p-same-roots){.pf-ref} transfers that root to the original
polynomial.
:::

:::

::: pf-qed
Step [](#conclusion-boxed){.pf-ref} is exactly the required conclusion.
:::

:::
:::
