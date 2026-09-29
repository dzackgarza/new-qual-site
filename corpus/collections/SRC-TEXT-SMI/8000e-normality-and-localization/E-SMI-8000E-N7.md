---
schema: qual/card@1
id: E-SMI-8000E-N7
kind: problem
title: Normality localizes
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Integral Closure
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the localization-normality statement with the local 8000e PDF and extraction, localization exercise 7."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Cleared a common denominator in a monic equation over R_P to show that a suitable denominator multiple of the integral element is integral over R, then divided by that denominator in the localization."
---

::: {.exercise}
If $R$ is normal and $P$ prime, prove that $R_P$ is also normal.
:::

::: {.solution}
Let $K$ be the fraction field of $R$. Since
$$
R\subseteq R_P\subseteq K,
$$
the fraction field of $R_P$ is also $K$.

Let
$$
z\in K
$$
be integral over $R_P$. We prove that $z\in R_P$.

::: pf

::: {.pf-step #s1}

Choose one common denominator for the coefficients of an integral equation.

::: pf-proof

There is a monic equation
$$
z^n+c_1z^{n-1}+\cdots+c_n=0
$$
with
$$
c_i\in R_P.
$$
Write
$$
c_i=\frac{a_i}{s_i},
\qquad
s_i\notin P.
$$
Set
$$
s=s_1s_2\cdots s_n.
$$
Since $P$ is prime and each $s_i\notin P$,
$$
s\notin P.
$$
Writing
$$
c_i=\frac{b_i}{s}
$$
with
$$
b_i=a_i(s/s_i)\in R,
$$
we have
$$
z^n+\frac{b_1}{s}z^{n-1}+\cdots+\frac{b_n}{s}=0.
$$

:::

:::

::: pf-step

The element $sz$ is integral over $R$.

::: pf-proof

Put
$$
y=sz.
$$
Multiply the equation from step [](#s1){.pf-ref} by $s^n$ and substitute
$z=y/s$. The $i$th lower-degree term becomes
$$
s^n\frac{b_i}{s}z^{n-i}
=b_i s^{i-1}y^{n-i}.
$$
Thus $y$ satisfies the monic equation
$$
y^n+b_1y^{n-1}+b_2s\,y^{n-2}+\cdots+b_ns^{n-1}=0
$$
with all coefficients in $R$. Hence $y=sz$ is integral over $R$.

:::

:::

::: pf-step

Use normality of $R$.

::: pf-proof

Because $R$ is normal and $y=sz\in K$ is integral over $R$, one has
$$
y=sz\in R.
$$
Since $s\notin P$,
$$
z=\frac ys
$$
belongs to $R_P$. Thus every element of the fraction field integral over
$R_P$ lies in $R_P$.

Therefore
$$
\boxed{R_P\text{ is normal}.}
$$

:::

:::

:::

:::
