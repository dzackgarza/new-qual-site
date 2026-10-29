---
schema: qual/card@1
id: P-SMK7Q
kind: problem
title: An analytic self-map of the disk with $|f|=1$ on the circle is a finite Blaschke
  product
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Zeros
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.problem}
Suppose $f:\DD\to\DD$ is analytic and admits a continuous extension $\tilde f: \bar \DD \to \bar \DD$ such that $\abs{z} = 1 \implies \abs{f(z)} = 1$.

(a) Prove that $f$ is a rational function.

(b) Suppose that $z=0$ is the unique zero of $f$.
Show that
$$
\exists n\in \NN, \lambda \in S^1 \text{ such that } f(z) = \lambda z^n
.$$

(c) Suppose that $a_1, \cdots, a_n \in \DD$ are the zeros of $f$ and prove that
$$
\exists \lambda \in S^1 \text{ such that } f(z) = \lambda \prod_{j=1}^n {z - a_j \over 1 - \bar{a_j} z}
.$$
:::

::: {.solution}
For $a\in\DD$ write $B_a(z)\coloneqq\dfrac{z-a}{1-\overline az}$; it is holomorphic on a neighborhood of $\overline\DD$, vanishes only at $a$ (simply), and satisfies $\abs{B_a}=1$ on $\abs z=1$.

::: pf

::: {.pf-step #finite}

$f$ has finitely many zeros in $\DD$, counted with multiplicity; list them as $a_1,\ldots,a_n$.

::: pf-proof

Since $\abs{\tilde f}=1$ on $\partial\DD$ and $\tilde f$ is continuous on the compact set $\overline\DD$, there is $\rho<1$ with $\tilde f\ne0$ on $\rho\le\abs z\le1$. The zeros of the nonzero holomorphic function $f$ are isolated, so only finitely many lie in the compact disk $\abs z\le\rho$.

:::

:::

::: {.pf-step #quotient}

$g\coloneqq f/\prod_{j=1}^nB_{a_j}$ is holomorphic and zero-free on $\DD$, extends continuously to $\overline\DD$, and has $\abs g=1$ on $\partial\DD$.

::: pf-proof

By step [](#finite){.pf-ref}, the zeros of the denominator, with multiplicity, are exactly those of $f$, so the singularities of $g$ are removable and $g$ has no zeros. The denominator is continuous and nonvanishing near $\partial\DD$ with modulus $1$ there.

:::

:::

::: {.pf-step #blaschke}

$f(z)=\boxed{\lambda\prod_{j=1}^n\dfrac{z-a_j}{1-\overline{a_j}z}}$ for some $\lambda\in S^1$.

::: pf-proof

By step [](#quotient){.pf-ref} and the maximum modulus principle applied to $g$ and to $1/g$, we get $\abs g\le1$ and $\abs{1/g}\le1$ on $\DD$. So $\abs g\equiv1$, and by the open mapping theorem $g$ is a constant $\lambda\in S^1$.

:::

:::

::: pf-step

(a) $f$ is rational.

::: pf-proof

By step [](#blaschke){.pf-ref}, $f$ is a constant times a finite product of the rational functions $B_{a_j}$.

:::

:::

::: pf-step

(b) If $0$ is the only zero of $f$, then $f(z)=\boxed{\lambda z^n}$ for some $n\in\NN$ and $\lambda\in S^1$.

::: pf-proof

Every $a_j$ equals $0$ and $B_0(z)=z$, so step [](#blaschke){.pf-ref} gives $f(z)=\lambda z^n$, where $n$ is the multiplicity of the zero at $0$.

:::

:::

::: pf-step

(c) If $a_1,\ldots,a_n$ are the zeros of $f$, then $f(z)=\lambda\prod_{j=1}^n\dfrac{z-a_j}{1-\overline{a_j}z}$ for some $\lambda\in S^1$.

::: pf-proof

This is step [](#blaschke){.pf-ref}.

:::

:::

:::

:::
