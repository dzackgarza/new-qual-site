---
schema: qual/card@1
id: P-BKS04-3A
kind: problem
title: Rational interpolation with prescribed pole-order bounds
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained solution: clear the allowed
    poles by Q(z)=prod_i (z-a_i)^{r_i}, interpolate c_j Q(b_j), and use
    deg G <= sum_i r_i for holomorphy at infinity.
---

::: {.problem}
Let $a_1,\ldots,a_n,b_1,\ldots,b_m$ be distinct complex numbers, let $r_1,\ldots,r_n$ be nonnegative integers, and let $c_1,\ldots,c_m$ be complex numbers.
Prove that if
\[
m\le r_1+\cdots+r_n+1,
\]
then there exists a rational function $F(z)\in\mathbb C(z)$ satisfying all of the following:

1. $F(z)$ is holomorphic at $\infty$ and everywhere in $\mathbb C$ except possibly at $a_1,\ldots,a_n$.

2. $\operatorname{ord}_{z=a_i}F(z)\ge -r_i$.

3. $F(b_j)=c_j$ for $j=1,\ldots,m$.
:::

::: {.solution}
Set
$$
R\coloneqq r_1+\cdots+r_n
$$
and
$$
Q(z)\coloneqq\prod_{i=1}^n(z-a_i)^{r_i}.
$$

::: pf

::: {.pf-step #s1}

There is a polynomial $G\in\CC[z]$ with
$$
\deg G\leq m-1\leq R
$$
such that
$$
G(b_j)=c_jQ(b_j)
$$
for every $j=1,\ldots,m$.

::: pf-proof

The points $b_1,\ldots,b_m$ are pairwise distinct, so Lagrange
interpolation gives a polynomial of degree at most $m-1$ taking the
prescribed values
$$
c_jQ(b_j).
$$
The hypothesis
$$
m\leq R+1
$$
gives $m-1\leq R$.

:::

:::

::: {.pf-step #s2}

Define
$$
F(z)\coloneqq\frac{G(z)}{Q(z)}.
$$
Then $F$ is holomorphic on
$$
\CC\setminus\{a_1,\ldots,a_n\}
$$
and at $\infty$.

::: pf-proof

The only zeros of $Q$ are among $a_1,\ldots,a_n$, so the quotient is
holomorphic away from those points.

Moreover,
$$
\deg G\leq R=\deg Q.
$$
Hence the rational function $G/Q$ has no pole at infinity. Equivalently,
after writing $w=1/z$, the function
$$
F(1/w)
$$
extends holomorphically to $w=0$ because multiplying numerator and
denominator by $w^R$ produces a quotient of polynomials in $w$ whose
denominator is nonzero at $w=0$.

:::

:::

::: {.pf-step #s3}

For every $i=1,\ldots,n$,
$$
\operatorname{ord}_{z=a_i}F(z)\geq-r_i.
$$

::: pf-proof

Because the $a_i$ are distinct, write
$$
Q(z)=(z-a_i)^{r_i}Q_i(z),
$$
where $Q_i(a_i)\neq0$. Then
$$
(z-a_i)^{r_i}F(z)
=
\frac{G(z)}{Q_i(z)}
$$
is holomorphic at $a_i$. This is exactly the assertion that
$\operatorname{ord}_{z=a_i}F\geq-r_i$.

:::

:::

::: {.pf-step #s4}

For every $j=1,\ldots,m$,
$$
F(b_j)=c_j.
$$

::: pf-proof

All of the $a_i$ and $b_j$ are distinct, so $Q(b_j)\neq0$. By step
[](#s1){.pf-ref},
$$
F(b_j)
=
\frac{G(b_j)}{Q(b_j)}
=
\frac{c_jQ(b_j)}{Q(b_j)}
=
c_j.
$$

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} verify the three required properties of the
rational function $F$.

:::

:::

:::
