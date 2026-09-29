---
schema: qual/card@1
id: P-BKF08-4B
kind: problem
title: Nonreal zeros of $z^{11}-3z^3+1$ in the annulus $1\le\lvert z\rvert\le2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both Rouché counts, absence of boundary zeros, monotonicity on
    the two real annular intervals, and simplicity of the two real zeros.
---

::: {.problem}
How many nonreal complex zeros does
$$
z^{11}-3z^3+1
$$
have in the region $1\le\abs{z}\le2$?
:::

::: {.solution}
Put
$$
P(z)\coloneqq z^{11}-3z^3+1.
$$

::: pf

::: {.pf-step #s1}

The polynomial $P$ has exactly $11$ zeros in
$\abs{z}<2$, counted with multiplicity, and no zero on $\abs{z}=2$.

::: pf-proof

On $\abs{z}=2$,
$$
\abs{-3z^3+1}
\le3\abs{z}^3+1
=25
<2048
=\abs{z^{11}}.
$$
By Rouché's theorem, $P(z)=z^{11}+(-3z^3+1)$ and $z^{11}$ have the
same number of zeros in $\abs{z}<2$, namely $11$. The strict inequality
also implies $P(z)\ne0$ on the boundary circle.

:::

:::

::: {.pf-step #s2}

The polynomial $P$ has exactly $3$ zeros in
$\abs{z}<1$, counted with multiplicity, and no zero on $\abs{z}=1$.

::: pf-proof

On $\abs{z}=1$,
$$
\abs{z^{11}+1}
\le\abs{z}^{11}+1
=2
<3
=\abs{-3z^3}.
$$
Rouché's theorem therefore shows that
$P(z)=-3z^3+(z^{11}+1)$ and $-3z^3$ have the same number of zeros in
$\abs{z}<1$, namely $3$. Again the strict inequality excludes zeros on
the boundary circle.

:::

:::

::: {.pf-step #s3}

The annulus
$$
1\le\abs{z}\le2
$$
contains exactly $8$ zeros of $P$, counted with multiplicity.

::: pf-proof

By step [](#s1){.pf-ref} there are $11$ zeros inside the circle of radius $2$, and
by step [](#s2){.pf-ref} exactly $3$ of them lie inside the unit circle. Neither
boundary circle contains a zero. Hence the annulus contains
$$
11-3=8
$$
zeros counted with multiplicity.

:::

:::

::: {.pf-step #s4}

Exactly two of the zeros in the annulus are real, one in
$(1,2)$ and one in $(-2,-1)$, and both are simple.

::: pf-proof

For real $x$,
$$
P'(x)=11x^{10}-9x^2=x^2(11x^8-9).
$$
If $1\le\abs{x}\le2$, then $11x^8-9\ge2>0$, so $P'(x)>0$.
Thus $P$ is strictly increasing on each of $[-2,-1]$ and $[1,2]$.
Moreover,
$$
P(-2)=-2023<0<P(-1)=3
$$
and
$$
P(1)=-1<0<P(2)=2025.
$$
The intermediate value theorem and strict monotonicity give exactly one
real zero in each interval. Since $P'$ is positive there, both zeros are
simple.

:::

:::

::: {.pf-step #s5}

The number of nonreal zeros in the annulus is
$$
\boxed{6}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives $8$ annular zeros counted with multiplicity. Step [](#s4){.pf-ref}
shows that exactly two of those zeros are real and each has multiplicity
$1$. Therefore the remaining $8-2=6$ zeros are nonreal.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the requested number.

:::

:::

:::
