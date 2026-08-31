---
schema: qual/card@1
id: P-IFN65
kind: problem
title: Freely homotopic loops on a closed genus-$2$ surface that are not homotopic
  rel basepoint
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Surfaces
relations: []
review: draft
---

::: problem
Let $M = \Sigma_2$ be a compact orientable surface of genus $2$ without boundary.

Give an example of a pair of based loops $\gamma_0, \gamma_1: S^1 \to M$ with $\gamma_0(1) = \gamma_1(1) = x_0$ such that there is a continuous free homotopy $\Gamma: [0, 1] \times S^1 \to M$ with
$$
\Gamma(0, t) = \gamma_0(t), \quad \Gamma(1, t) = \gamma_1(t) \quad \text{for all } t \in S^1,
$$
but there is no based homotopy between $\gamma_0$ and $\gamma_1$ (that is, no continuous map $\Gamma$ satisfying the additional condition $\Gamma(s, 1) = x_0$ for all $s \in [0, 1]$).
:::

::: solution
**Goal:** Provide an explicit example of loops on $\Sigma_2$ that are freely homotopic (conjugate in $\pi_1$) but not based homotopic (distinct in $\pi_1$), and prove both properties.

<1>1. General characterization of free vs based homotopy:
::: {.proof}
    <2>1. For any path-connected space $X$ with basepoint $x_0$, the set of free homotopy classes of unbased loops $[S^1, X]$ is in natural bijection with the conjugacy classes of the fundamental group:
    $$[S^1, X] \longleftrightarrow \operatorname{Conj}(\pi_1(X, x_0)) = \pi_1(X, x_0) / \sim_{\text{conjugacy}}.$$
    <2>2. Two based loops $\gamma_0, \gamma_1$ with $[\gamma_0] = g_0$ and $[\gamma_1] = g_1$ in $\pi_1(X, x_0)$ are:
        - *Freely homotopic* if and only if $g_1 = h g_0 h^{-1}$ for some $h \in \pi_1(X, x_0)$.
        - *Based homotopic* if and only if $g_1 = g_0$ in $\pi_1(X, x_0)$.
    <2>3. Thus $\gamma_0$ and $\gamma_1$ are freely homotopic but not based homotopic if and only if $g_1 = h g_0 h^{-1}$ with $g_1 \ne g_0$ (meaning $g_0$ and $h$ do not commute in $\pi_1(X, x_0)$).

:::

<1>2. Fundamental group of the genus 2 surface $\Sigma_2$:
::: {.proof}
    <2>1. Choose a basepoint $x_0 \in \Sigma_2$.
    <2>2. The fundamental group of the closed genus 2 surface has the standard presentation:
    $$\pi_1(\Sigma_2, x_0) = \langle a_1, b_1, a_2, b_2 \mid [a_1, b_1][a_2, b_2] = 1 \rangle.$$
    <2>3. Here $a_1$ and $b_1$ represent the canonical meridian and longitude loops around the first handle passing through $x_0$.

:::

<1>3. Explicit construction of the pair of loops:
::: {.proof}
    <2>1. Let $\gamma_0: S^1 \to \Sigma_2$ be the meridian loop around the first handle representing $a_1 \in \pi_1(\Sigma_2, x_0)$.
    <2>2. Let $\beta: S^1 \to \Sigma_2$ be the longitudinal loop around the first handle representing $b_1 \in \pi_1(\Sigma_2, x_0)$.
    <2>3. Define $\gamma_1$ to be the conjugated loop $\gamma_1 = \beta * \gamma_0 * \bar{\beta}$ representing
    $$[\gamma_1] = b_1 a_1 b_1^{-1} \in \pi_1(\Sigma_2, x_0).$$

:::

<1>4. Proof of free homotopy:
::: {.proof}
    <2>1. By <1>1, since $[\gamma_1] = b_1 [\gamma_0] b_1^{-1}$ is conjugate to $[\gamma_0]$ in $\pi_1(\Sigma_2, x_0)$, $\gamma_0$ and $\gamma_1$ are freely homotopic.
    <2>2. Geometrically, the homotopy $\Gamma(s, t)$ is obtained by dragging the loop $\gamma_0$ along the longitudinal path $\beta(s)$ from $s = 0$ to $s = 1$.

:::

<1>5. Proof of non-based homotopy:
::: {.proof}
    <2>1. Suppose for contradiction that $\gamma_0$ and $\gamma_1$ are based homotopic.
    <2>2. Then $[\gamma_0] = [\gamma_1]$ in $\pi_1(\Sigma_2, x_0)$, which requires
    $$a_1 = b_1 a_1 b_1^{-1} \implies [a_1, b_1] = a_1 b_1 a_1^{-1} b_1^{-1} = 1.$$
    <2>3. Consider the retraction homomorphism $\rho: \pi_1(\Sigma_2, x_0) \to F(a_1, b_1)$ to the free group on two generators obtained by sending $a_2 \mapsto 1, b_2 \mapsto 1$.
    <2>4. The defining relation $[a_1, b_1][a_2, b_2] = 1$ is sent to $[a_1, b_1] = 1$.
    <2>5. But in $\pi_1(\Sigma_2, x_0)$, the elements $a_1$ and $b_1$ generate a subgroup that is non-abelian (for instance, the surface $\Sigma_2$ has a hyperbolic metric whose universal cover is $\mathbb{H}^2$, where $a_1$ and $b_1$ act as non-commuting hyperbolic translations with disjoint axes).
    <2>6. Thus $a_1 \ne b_1 a_1 b_1^{-1}$ in $\pi_1(\Sigma_2, x_0)$.
    <2>7. Therefore $\gamma_0$ and $\gamma_1$ are not homotopic relative to $x_0$.

:::

<1>6. Conclusion:
::: {.proof}
    $\gamma_0 = a_1$ and $\gamma_1 = b_1 * a_1 * \bar{b}_1$ are freely homotopic but not based homotopic on $\Sigma_2$.
:::
:::
