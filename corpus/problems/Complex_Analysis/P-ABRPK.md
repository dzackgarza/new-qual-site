---
schema: qual/card@1
id: P-ABRPK
kind: problem
title: Self-maps of $\DD$ unimodular on the circle are finite Blaschke products
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Reflection
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
---

::: {.problem}
Suppose $f:\DD\to\DD$ is analytic and admits a continuous extension $\tilde f: \bar \DD \to \bar \DD$ such that $\abs{z} = 1 \implies \abs{f(z)} = 1$.

(a) Prove that $f$ is a rational function.

(b) Suppose that $z=0$ is the unique zero of $f$.
Show that
$$
\exists n\in \NN, \lambda \in S^1 \qtext{ such that }f(z) = \lambda z^n.
$$

(c) Suppose that $a_1, \cdots, a_n \in \DD$ are the zeros of $f$ and prove that
$$
\exists \lambda \in S^1 \qtext{such that} f(z) = \lambda \prod_{j=1}^n \frac{z - a_j}{1 - \bar{a_j} z}.
$$
:::

::: {.solution}
Write $f$ also for the extension $\tilde f$.
Zeros are counted with multiplicity.

::: pf

::: {.pf-step #finite-zeros}
$f$ has finitely many zeros in $\DD$, and there is $r<1$ with $\abs{f}\ge\frac12$ on $r\le\abs z\le1$.

::: pf-proof
$\abs f=1$ on the compact set $\abs z=1$ and $f$ is uniformly continuous on $\overline\DD$, which gives $r$.
The zeros therefore lie in the compact disk $\abs z\le r$, and they are isolated since $f\not\equiv0$, so there are finitely many.
:::

:::

::: {.pf-step #reflection}
(a) $f$ is a rational function.

::: pf-proof
Define $F$ on the Riemann sphere by $F(z)=f(z)$ for $\abs z\le1$ and $F(z)=1/\overline{f(1/\bar z)}$ for $\abs z\ge1$, with $F(\infty)=1/\overline{f(0)}$ (equal to $\infty$ if $f(0)=0$).
The two formulas agree on $\abs z=1$ because $\abs{f(z)}=1$ there.
By step [](#finite-zeros){.pf-ref}, $F$ is meromorphic on $\abs z>1$ with finitely many poles, none on $1\le\abs z<1/r$.
So $F$ is continuous on the annulus $r<\abs z<1/r$ and holomorphic off the circle $\abs z=1$; by Morera's theorem it is holomorphic across the circle.
Thus $F$ is meromorphic on the Riemann sphere, hence rational, and $f=F|_{\DD}$.
:::

:::

::: {.pf-step #unimodular-quotient}
If $B$ is holomorphic on a neighbourhood of $\overline\DD$, $\abs B=1$ on $\abs z=1$, and $B$ has the same zeros in $\DD$ as $f$, then $f=\lambda B$ for some $\lambda\in S^1$.

::: pf-proof
$g\coloneqq f/B$ has removable singularities at the common zeros, so it is holomorphic and zero-free on $\DD$, and continuous on $\overline\DD$ with $\abs g=1$ on $\abs z=1$.
The maximum modulus principle applied to $g$ and to $1/g$ gives $\abs g\le1$ and $\abs{1/g}\le1$ on $\DD$, so $\abs g\equiv1$.
A holomorphic function of constant modulus on $\DD$ is constant, so $g\equiv\lambda$ with $\abs\lambda=1$.
:::

:::

::: pf-step
(b) $f(z)=\lambda z^n$ with $n\ge1$ the order of the zero of $f$ at $0$ and $\lambda\in S^1$.

::: pf-proof
Apply step [](#unimodular-quotient){.pf-ref} with $B(z)=z^n$.
:::

:::

::: pf-step
(c) $f(z)=\lambda\prod_{j=1}^n\frac{z-a_j}{1-\bar a_jz}$ for some $\lambda\in S^1$.

::: pf-proof
Each factor $\frac{z-a_j}{1-\bar a_jz}$ is holomorphic on a neighbourhood of $\overline\DD$ because $\abs{a_j}<1$, has modulus $1$ on $\abs z=1$, and vanishes only at $a_j$.
Apply step [](#unimodular-quotient){.pf-ref} with $B$ their product.
:::

:::

:::

:::
