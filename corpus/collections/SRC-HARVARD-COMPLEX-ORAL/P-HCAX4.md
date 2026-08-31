---
schema: qual/card@1
id: P-HCAX4
kind: problem
title: Normalized conformal map onto the slit plane
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
  - Univalent Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let
\[
\Omega=\mathbb C\setminus(-\infty,-1/4].
\]

a. Show that there is a conformal isomorphism $f:\mathbb D\to\Omega$ with $f(0)=0$.

b. Give a normalization which makes $f$ unique.

c. Write $f(z)=\sum_{j\geq 1}a_jz^j$.
Use another conformal map expressed in terms of $f$ and $-z$ to determine a ring containing all coefficients $a_j$.

d. Compute the coefficients $a_j$.
:::

::: {.solution}
**Part (a).**

<1>1. $\Omega = \CC \setminus (-\infty, -1/4]$ is simply connected.
::: {.proof}
the complement of a closed ray is simply connected (it is a slit plane).
:::

<1>2. $\Omega$ is a proper simply connected domain, so by the Riemann mapping theorem there is a conformal isomorphism $f: \DD \to \Omega$.
::: {.proof}
Riemann mapping theorem.
:::

<1>3. We may arrange $f(0) = 0$ by composing with an automorphism of $\Omega$ (or by the normalization in part (b)).
::: {.proof}
the Riemann map can be normalized to send $0$ to any prescribed point of $\Omega$.
:::

**Part (b).**

<1>1. The normalization $f(0) = 0$ and $f'(0) > 0$ makes $f$ unique.
::: {.proof}
the Riemann mapping theorem gives a unique conformal map with $f(0) = 0$ and $f'(0) > 0$ (positive real derivative).
:::

**Part (c).**

<1>1. The map $z \mapsto -z$ is an automorphism of $\DD$, so $f(-z)$ is another conformal map $\DD \to \Omega$ with $f(-0) = 0$.
::: {.proof}
$-z$ is a rotation of $\DD$.
:::

<1>2. $f(-z)$ has derivative $-f'(0) < 0$ at $0$, so it is the "other" normalized map (the one with negative real derivative).
::: {.proof}
$\frac{d}{dz} f(-z)\big|_{z=0} = -f'(0)$.
:::

<1>3. The explicit map is the Koebe function $f(z) = \frac{z}{(1-z)^2}$, whose Taylor coefficients are $a_j = j$.
::: {.proof}
$\frac{z}{(1-z)^2} = z\sum_{j=0}^{\infty}(j+1)z^j = \sum_{j=1}^{\infty} j z^j$.
:::

<1>4. Hence all coefficients $a_j = j$ lie in the ring $\ZZ$ (the integers).
::: {.proof}
<1>3.
:::

**Part (d).**

<1>1. $f(z) = \frac{z}{(1-z)^2}$.
::: {.proof}
the Koebe function maps $\DD$ biholomorphically onto $\CC \setminus (-\infty, -1/4]$, with $f(0) = 0$ and $f'(0) = 1 > 0$.
:::

<1>2. $f(z) = \frac{z}{(1-z)^2} = z(1-z)^{-2} = z\sum_{j=0}^{\infty}(j+1)z^j = \sum_{j=1}^{\infty} j z^j$.
::: {.proof}
binomial expansion $(1-z)^{-2} = \sum_{j=0}^{\infty}(j+1)z^j$.
:::

<1>3. Hence $a_j = j$ for all $j \ge 1$.
::: {.proof}
read off the coefficient of $z^j$.
:::

<1>4. Q.E.D.
::: {.proof}
$a_j = j$ (<1>3).
:::
:::
