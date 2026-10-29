---
schema: qual/card@1
id: P-OOVED
kind: problem
title: Holomorphic functions of modulus one on the circle are finite Blaschke products
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'Removed the source note "Also cf. Stein et al, 1.4.7, 3.8.17" from the statement.'
---

::: {.problem}
Suppose $f$ is analytic in an open set containing the unit disc $\DD$ and $\abs{f(z)} =1$ when $\abs{z}=1$. Show that either $f(z) = e^{i \theta}$ for some $\theta \in \RR$ or there are
finite number of $z_k \in \DD$, $k \leq n$ and
$\theta \in \RR$ such that
$$
f(z) = e^{i\theta} \prod_{k=1}^n \frac{z-z_k}{1 - \bar{z}_k z }.
$$
:::

::: {.solution}
Since $\overline\DD$ is compact, the open set on which $f$ is analytic contains a disk $\Omega=\theset{\abs{z}<\rho}$ with $\rho>1$.

::: pf

::: {.pf-step #finite-zeros}
$f$ has finitely many zeros in $\DD$, say $z_1,\ldots,z_n$ listed with multiplicity, and none on $\abs{z}=1$.

::: pf-proof
$\abs{f}=1$ on the circle, so $f\not\equiv0$ and $f$ has no zero there. The zeros of $f$ are then isolated in $\Omega$, so only finitely many lie in the compact set $\overline\DD$.
:::

:::

::: {.pf-step #blaschke}
$B(z)\definedas\prod_{k=1}^n\frac{z-z_k}{1-\bar z_kz}$ is holomorphic on a neighbourhood of $\overline\DD$, has $\abs{B}=1$ on $\abs{z}=1$, and has exactly the zeros $z_1,\ldots,z_n$ in $\overline\DD$, with multiplicity.

::: pf-proof
The pole of the $k$th factor is $1/\bar z_k$, outside $\overline\DD$. For $\abs{z}=1$, $\abs{1-\bar z_kz}=\abs{\bar z-\bar z_k}=\abs{z-z_k}$, so each factor has modulus $1$.
:::

:::

::: {.pf-step #quotient}
$g\definedas f/B$ extends to a holomorphic function on a neighbourhood of $\overline\DD$ with no zero in $\overline\DD$ and $\abs{g}=1$ on $\abs{z}=1$.

::: pf-proof
By steps [](#finite-zeros){.pf-ref} and [](#blaschke){.pf-ref}, $f$ and $B$ vanish to the same order at each $z_k$, so the singularities of $g$ at the $z_k$ are removable and the extended $g$ is nonzero there. On the circle $\abs{g}=\abs{f}/\abs{B}=1$.
:::

:::

::: {.pf-step #g-constant}
$g\equiv e^{i\theta}$ for some $\theta\in\RR$.

::: pf-proof
By step [](#quotient){.pf-ref} and the maximum modulus principle applied to $g$ and to $1/g$, both holomorphic near $\overline\DD$, we get $\abs{g}\le1$ and $\abs{1/g}\le1$ on $\DD$. So $\abs{g}\equiv1$ on $\DD$; then $g(\DD)$ lies in the unit circle and is not open, so by the open mapping theorem $g$ is constant on $\DD$, and its constant has modulus $1$.
:::

:::

::: pf-step
$f(z)=e^{i\theta}\prod_{k=1}^n\frac{z-z_k}{1-\bar z_kz}$, which is the constant $e^{i\theta}$ when $n=0$.

::: pf-proof
By step [](#g-constant){.pf-ref}, $f=gB=e^{i\theta}B$ on $\DD$.
:::

:::

:::
:::
