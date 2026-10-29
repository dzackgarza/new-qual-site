---
schema: qual/card@1
id: P-PRECALC2-18
kind: problem
title: Convergence and divergence of infinite products
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked Problem 18 on page 6 of Week2_solns.pdf and added an erratum remark that the first two factors of product (c) are undefined or negative.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source indexed product (c) from n=1, where the n=1 factor is undefined and the n=2 factor is negative; product (c) now starts at n=3, where every factor lies in (0,1).
---

::: {.problem}
Let $(a_n)$ be a sequence of positive numbers.
The infinite product
$$
\prod_{n=1}^{\infty}a_n=a_1a_2a_3\cdots
$$
is said to converge if there is $L\in(0,\infty)$ such that
$$
\lim_{N\to\infty}\prod_{n=1}^{N}a_n=L.
$$
Otherwise the product is said to diverge to zero or diverge to $+\infty$ if the limit is zero or $+\infty$, respectively.
Consider the infinite products
$$
\text{(a) }\prod_{n=1}^{\infty}\left(1+\frac1{n^2}\right),\qquad
\text{(b) }\prod_{n=1}^{\infty}\left(1+\frac1n\right),\qquad
\text{(c) }\prod_{n=3}^{\infty}\left(1-\frac1{\log n}\right).
$$
Show that (a) converges, (b) diverges to $+\infty$, and (c) diverges to $0$.
:::

::: {.solution}

## Product (a)

Let
$$
P_N
=
\prod_{n=1}^{N}
\left(1+\frac1{n^2}\right).
$$

::: pf

::: {.pf-step #s1-1}

For every $x\ge0$,
$$
\boxed{\log(1+x)\le x}.
$$


::: pf-proof

Define
$$
h(x)=x-\log(1+x).
$$
Then
$$
h(0)=0
$$
and
$$
h'(x)
=
1-\frac1{1+x}
=
\frac{x}{1+x}
\ge0.
$$
Hence $h(x)\ge0$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
0<
\log\left(1+\frac1{n^2}\right)
\le
\frac1{n^2}.
$$


::: pf-proof

Positivity follows because
$$
1+\frac1{n^2}>1.
$$
Apply step [](#s1-1){.pf-ref} with $x=1/n^2$.

:::

:::

::: {.pf-step #s1-3}

The series
$$
\sum_{n=1}^{\infty}
\log\left(1+\frac1{n^2}\right)
$$
converges.


::: pf-proof

By step [](#s1-2){.pf-ref} it is a nonnegative series dominated termwise by the convergent
$p$-series
$$
\sum_{n=1}^{\infty}\frac1{n^2}.
$$

:::

:::

::: pf-step

Hence there is a finite real number $S$ such that
$$
\log P_N
=
\sum_{n=1}^{N}
\log\left(1+\frac1{n^2}\right)
\longrightarrow
S.
$$


::: pf-proof

The logarithm of a finite product of positive factors is the sum of the
logarithms. Apply step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
P_N\longrightarrow e^S\in(0,\infty)}.
$$


::: pf-proof

Exponentiation is continuous and
$$
P_N=e^{\log P_N}.
$$
Since $S\in\RR$, one has
$$
e^S>0.
$$

:::

:::

::: {.pf-step #s1-6}

Thus
$$
\boxed{
\prod_{n=1}^{\infty}
\left(1+\frac1{n^2}\right)
\text{ converges}}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives a positive finite limit of the partial products.

:::

:::

::: {.pf-step #s1-7}

Let $Q_N=\prod_{n=1}^{N}\left(1+\frac1n\right)$. Each factor satisfies
$$
\boxed{
1+\frac1n
=
\frac{n+1}{n}}.
$$


::: pf-proof

This is direct algebra.

:::

:::

::: pf-step

Therefore
$$
Q_N
=
\frac21
\frac32
\frac43
\cdots
\frac{N+1}{N}.
$$


::: pf-proof

Substitute step [](#s1-7){.pf-ref} into the finite product.

:::

:::

::: {.pf-step #s1-9}

The product telescopes:
$$
\boxed{Q_N=N+1}.
$$


::: pf-proof

Every intermediate numerator cancels with the same denominator:
$$
\frac21
\frac32
\cdots
\frac{N+1}{N}
=
N+1.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\prod_{n=1}^{\infty}
\left(1+\frac1n\right)
\text{ diverges to }+\infty}.
$$


::: pf-proof

By step [](#s1-9){.pf-ref},
$$
Q_N=N+1\to+\infty.
$$

:::

:::

::: {.pf-step #s1-11}

Let $R_N=\prod_{n=3}^{N}\left(1-\frac1{\log n}\right)$. For every $n\ge3$,
$$
\boxed{
0<
1-\frac1{\log n}
<
1}.
$$


::: pf-proof

Since
$$
\log n>1
\qquad(n\ge3),
$$
one has
$$
0<\frac1{\log n}<1.
$$
Subtract from $1$.

:::

:::

::: {.pf-step #s1-12}

For $0<x<1$,
$$
\boxed{\log(1-x)\le -x}.
$$


::: pf-proof

Define
$$
k(x)=-x-\log(1-x).
$$
Then
$$
k(0)=0
$$
and
$$
k'(x)
=
-1+\frac1{1-x}
=
\frac{x}{1-x}
>0.
$$
Hence $k(x)>0$ for $x>0$.

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\log R_N
\le
-\sum_{n=3}^{N}
\frac1{\log n}.
$$


::: pf-proof

By step [](#s1-11){.pf-ref} all factors are positive, so logarithms are defined. Then
$$
\log R_N
=
\sum_{n=3}^{N}
\log\left(1-\frac1{\log n}\right).
$$
Apply step [](#s1-12){.pf-ref} termwise with
$$
x=\frac1{\log n}.
$$

:::

:::

::: {.pf-step #s1-14}

For every $n\ge3$,
$$
\boxed{
\frac1{\log n}
>
\frac1n}.
$$


::: pf-proof

For $n>1$,
$$
\log n<n.
$$
Both quantities are positive, so taking reciprocals reverses the inequality.

:::

:::

::: {.pf-step #s1-15}

Hence
$$
\sum_{n=3}^{\infty}
\frac1{\log n}
$$
diverges.


::: pf-proof

By step [](#s1-14){.pf-ref} it dominates the divergent harmonic tail
$$
\sum_{n=3}^{\infty}\frac1n.
$$

:::

:::

::: {.pf-step #s1-16}

Consequently,
$$
\boxed{\log R_N\to-\infty}.
$$


::: pf-proof

Step [](#s1-13){.pf-ref} gives
$$
\log R_N
\le
-\sum_{n=3}^{N}\frac1{\log n},
$$
and the right-hand side tends to $-\infty$ by step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

Therefore
$$
\boxed{R_N\to0}.
$$


::: pf-proof

Since
$$
R_N=e^{\log R_N}
$$
and the exponential tends to $0$ as its argument tends to $-\infty$,
step [](#s1-16){.pf-ref} gives the result.

:::

:::

::: {.pf-step #s1-18}

Thus
$$
\boxed{
\prod_{n=3}^{\infty}
\left(1-\frac1{\log n}\right)
=0}
$$
in the sense that its partial products diverge to zero.


::: pf-proof

This is step [](#s1-17){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves (a), step [](#s1-10){.pf-ref} proves (b), and step [](#s1-18){.pf-ref} proves (c).

:::

:::

:::
