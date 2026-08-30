---
title: Morera and converses
order: 40
problems:
  topics:
  - Morera

---

# Morera and converses

Cauchy's theorem says a holomorphic function has vanishing closed integrals.
This page is the traffic in the other direction: vanishing integrals imply holomorphy, and that converse is what makes limits and series of holomorphic functions holomorphic.

## Morera's theorem

[[T-LHSMY]]

[[FT-B73T5]]

:::{.slogan}
Vanishing on every triangle implies holomorphic.
Equivalently, $f(z)\dz$ is a closed differential form exactly when $f$ is holomorphic.

:::

:::{.proof title="Sketch"}
Fix $z_0\in \Omega$ and define $F(z) \da \int_{z_0}^z f(\xi) \dxi$ along any path from $z_0$ to $z$.
This is well defined: two paths $\gamma, \mu$ satisfy $\int_\gamma f + \int_\mu f = \int_{\gamma \cdot \mu} f = 0$ by hypothesis, since the concatenation bounds a closed region.
Then show $F' = f$.

:::

:::{.remark title="What makes it powerful"}
Almost nothing is assumed about $f$: not smoothness, not differentiability, only continuity and the vanishing integrals.
That is why it can be applied to a limit, where differentiability of the limit is exactly what is unknown.
It is sometimes stated for rectangles with sides parallel to the axes, which is the form the Goursat argument below produces.

:::

## The converse that gets used

[[C-TODSQ]]

:::{.proof}
Commute the limit with the integral and apply Morera.

:::

:::{.remark}
This is the theorem behind every "the limit is holomorphic" step, and it applies to series $\sum_k f_k(z)$ through their partial sums.
Uniform convergence on compact subsets is what licenses the interchange; pointwise is not enough.

:::

## Goursat

The bisection argument that removes the continuity assumption from Cauchy's theorem, proved through Morera.

[[T-B3BDO]]

:::{.proof title="from Gamelin"}
Break the region into nested rectangles:

![](../../../../assets/assets/figures/2021-12-10_19-47-54.png)

Let $R$ be a closed rectangle in $D$, subdivided into four equal subrectangles.
The integral around $\partial R$ is the sum of the integrals around the four, so at least one, call it $R_1$, satisfies
\[
\left|\int_{\partial R_{1}} f(z) \dz \right| \geq \frac{1}{4}\left|\int_{\partial R} f(z) \dz \right|
.\]
Subdividing repeatedly yields nested $\ts{R_n}$ with
\[
\left|\int_{\partial R_{n}} f(z) \dz\right| \geq \frac{1}{4}\left|\int_{\partial R_{n-1}} f(z) \dz \right| \geq \cdots \geq \frac{1}{4^{n}}\left|\int_{\partial R} f(z) \dz\right|
.\]
The $R_n$ decrease with diameters tending to zero, so they converge to a point $z_0 \in D$.
Differentiability at $z_0$ gives
\[
\left|\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}-f^{\prime}\left(z_{0}\right)\right| \leq \varepsilon_{n}, \quad z \in R_{n}
,\]
with $\varepsilon_n \to 0$.
Writing $L$ for the length of $\partial R$, the length of $\partial R_n$ is $L/2^n$, and for $z \in R_n$,
\[
\left|f(z)-f\left(z_{0}\right)-f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)\right| \leq \varepsilon_{n}\left|z-z_{0}\right| \leq 2 \varepsilon_{n} L / 2^{n}
.\]
By the ML estimate and Cauchy's theorem,
\[
\left|\int_{\partial R_{n}} f(z) \dz\right| &=\left|\int_{\partial R_{n}}\left[f(z)-f\left(z_{0}\right)-f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)\right] \dz\right| \\
& \leq\left(2 \varepsilon_{n} L / 2^{n}\right) \cdot\left(L / 2^{n}\right)=2 L^{2} \varepsilon_{n} / 4^{n}
,\]
hence
\[
\left|\int_{\partial R} f(z) \dz\right| \leq 4^{n}\left|\int_{\partial R_{n}} f(z) \dz\right| \leq 2 L^{2} \varepsilon_{n}
.\]
Since $\varepsilon_n \to 0$, the integral over $\partial R$ vanishes, and Morera gives analyticity.

:::

## Exercises

[[E-WIANB]]
