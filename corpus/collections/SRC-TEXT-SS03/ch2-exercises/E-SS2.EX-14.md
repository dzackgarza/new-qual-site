---
schema: qual/card@1
id: E-SS2.EX-14
kind: problem
title: A pole on the circle of convergence and its coefficient growth
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Each step re-read: the principal part exists because the only
    singularity on the closed disc is a pole; subtracting it leaves a function holomorphic past the
    unit circle, whose Taylor coefficients decay geometrically by Cauchy's estimates; the negative
    powers expand by the binomial series since |z/z_0| < 1 inside the disc; the coefficients are
    therefore z_0^{-n} P(n) plus a geometrically decaying error, with deg P = m-1 and nonzero
    leading coefficient; hence a_n is eventually nonzero and the ratio tends to z_0 because
    P(n)/P(n+1) tends to 1. The remark that some versions first ask for eventual nonvanishing of a_n
    is kept, and that step is now proved rather than assumed. Not claimed: any statement about the
    rate of convergence.
---

::: {.exercise}
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a pole at $z_0$ on the unit circle. Show that if
$$
\sum_{n=0}^{\infty} a_n z^n
$$
denotes the power series expansion of $f$ in the open unit disc, then
$$
\lim_{n \to \infty} \frac{a_n}{a_{n+1}} = z_0.
$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 2 Exercise 14.

::: pf

::: {.pf-step #principalpart}
The pole at $z_{0}$ has some order $m\ge1$, and $f$ has a principal part $\sum_{k=1}^{m}c_{-k}(z-z_{0})^{-k}$ at $z_{0}$ with $c_{-m}\ne0$.

::: pf-proof
$f$ is holomorphic on an open set containing the closed disc except at $z_{0}$, so $z_{0}$ is an isolated singularity of $f$ and it is a pole because $f$ is meromorphic there; its order is the least $m\ge1$ with $(z-z_{0})^{m}f$ holomorphic at $z_{0}$, and the principal part is the negative-degree part of the Laurent expansion, whose leading coefficient $c_{-m}$ is nonzero by definition of the order.
:::

:::

::: {.pf-step #holomorphic}
$h(z)=f(z)-\sum_{k=1}^{m}c_{-k}(z-z_{0})^{-k}$ is holomorphic on a neighbourhood of the closed disc, so $h(z)=\sum b_{n}z^{n}$ on $\abs{z}<\rho$ for some $\rho>1$ and $b_{n}=O(\rho^{-n})$.

::: pf-proof
Subtracting the principal part removes the singularity at $z_{0}$ and changes nothing elsewhere on the open set, so $h$ is holomorphic on a neighbourhood of the closed disc; that neighbourhood contains $\abs{z}<\rho$ for some $\rho>1$. Cauchy's estimates on the circle of radius $r$ with $1<r<\rho$ give $\abs{b_{n}}\le Mr^{-n}$ for a constant $M$, hence $b_{n}=O(\rho'^{-n})$ for any $1<\rho'<\rho$.
:::

:::

::: {.pf-step #expansion}
For $\abs{z}<1$ and $k\ge1$, $(z-z_{0})^{-k}=(-1)^{k}z_{0}^{-k}\sum_{n\ge0}\binom{n+k-1}{k-1}z^{n}z_{0}^{-n}$.

::: pf-proof
Since $\abs{z_{0}}=1$ and $\abs{z}<1$, $\abs{z/z_{0}}<1$, so $1/(1-z/z_{0})=\sum_{n\ge0}(z/z_{0})^{n}$ and its $(k-1)$-fold derivative gives $(1-z/z_{0})^{-k}=\sum_{n\ge0}\binom{n+k-1}{k-1}(z/z_{0})^{n}$. Now $(z-z_{0})^{-k}=(-1)^{k}z_{0}^{-k}(1-z/z_{0})^{-k}$.
:::

:::

::: {.pf-step #coefficients}
$a_{n}=z_{0}^{-n}P(n)+b_{n}$, where $P(n)=\sum_{k=1}^{m}(-1)^{k}c_{-k}z_{0}^{-k}\binom{n+k-1}{k-1}$ is a polynomial in $n$ of degree $m-1$ with nonzero leading coefficient.

::: pf-proof
Multiply the expansion of step [](#expansion){.pf-ref} by $c_{-k}$ and sum over $k$: the coefficient of $z^{n}$ is $z_{0}^{-n}\sum_{k}(-1)^{k}c_{-k}z_{0}^{-k}\binom{n+k-1}{k-1}$, which is the displayed $P(n)$. Each $\binom{n+k-1}{k-1}$ is a polynomial in $n$ of degree $k-1$, so the sum is a polynomial of degree at most $m-1$, and the degree $m-1$ term comes only from $k=m$, with coefficient $(-1)^{m}c_{-m}z_{0}^{-m}\cdot\frac{1}{(m-1)!}\ne0$. Adding the coefficients $b_{n}$ of $h$ gives $a_{n}$.
:::

:::

::: {.pf-step #nonzero}
$a_{n}\ne0$ for all sufficiently large $n$.

::: pf-proof
$\abs{z_{0}^{-n}P(n)}=\abs{P(n)}\to\infty$ because $P$ has positive degree with nonzero leading coefficient, while $\abs{b_{n}}\le M\rho^{-n}\to0$ by step [](#holomorphic){.pf-ref}. So for large $n$ the first term dominates and $a_{n}\ne0$; in particular the quotient $a_{n}/a_{n+1}$ is defined eventually.
:::

:::

::: {.pf-step #ratio}
$\dfrac{a_{n}}{a_{n+1}}=z_{0}\,\dfrac{P(n)+z_{0}^{n}b_{n}}{P(n+1)+z_{0}^{n+1}b_{n+1}}$ and the second factor tends to $1$.

::: pf-proof
Using step [](#coefficients){.pf-ref}, $a_{n}=z_{0}^{-n}\bigl(P(n)+z_{0}^{n}b_{n}\bigr)$ and $a_{n+1}=z_{0}^{-(n+1)}\bigl(P(n+1)+z_{0}^{n+1}b_{n+1}\bigr)$, so the quotient is $z_{0}$ times the displayed fraction. Since $\abs{z_{0}}=1$, the terms $z_{0}^{n}b_{n}$ and $z_{0}^{n+1}b_{n+1}$ are $O(\rho^{-n})=o(1)$ while $P(n),P(n+1)\to\infty$; and $P(n)/P(n+1)\to1$ because $P(n+1)/P(n)\to1$ for a polynomial of positive degree with nonzero leading coefficient.
:::

:::

::: {.pf-step}
$\displaystyle\lim_{n\to\infty}\frac{a_{n}}{a_{n+1}}=z_{0}$.

::: pf-proof
By steps [](#ratio){.pf-ref} and [](#nonzero){.pf-ref},
$$
\boxed{\lim_{n\to\infty}\frac{a_{n}}{a_{n+1}}=z_{0}.}
$$
The pole order $m$ enters only through the degree $m-1$ of $P$, which cancels in the limit; a pole of any order on the unit circle produces the same asymptotic ratio.
:::

:::

:::
:::

::: {.remark title="Variations"}
Some versions first ask to show that $a_n\neq0$ for all sufficiently large $n$, so that the quotient $a_n/a_{n+1}$ is defined.
:::
