---
schema: qual/card@1
id: P-UCTOP-SU14-8
kind: problem
title: π_2 of CW complex with 2-cells attached to S^1
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $X$ be the CW complex formed by attaching $k$ two-cells $e_1^2, \ldots, e_k^2$ to the circle $S^1$ via attaching maps with degrees $n_1, n_2, \ldots, n_k$.
Compute $\pi_2(X)$ in terms of $n_1, \ldots, n_k$.
:::

::: {.solution}

::: pf

::: pf-step
Compute the fundamental group $\pi_1(X)$:

::: pf-proof

::: pf-step
$X$ has a cell presentation with one 0-cell, one 1-cell $a$, and $k$ 2-cells attached with degrees $n_1, \dots, n_k$.

::: pf-proof
definition of $X$.
:::

:::

::: pf-step
By the Seifert–van Kampen theorem / cellular presentation of fundamental groups:
\[
\pi_1(X) \cong \langle a \mid a^{n_1} = 1, \dots, a^{n_k} = 1 \rangle \cong \mathbb{Z}/d\mathbb{Z},
\]
where $d = \gcd(n_1, \dots, n_k)$ (with the convention $\gcd(0, \dots, 0) = 0$).

::: pf-proof
the ideal $\sum n_i \mathbb{Z} = d\mathbb{Z}$ in $\mathbb{Z}$.
:::

:::

:::

:::

::: {.pf-step #s2}
Relate $\pi_2(X)$ to the universal cover $\widetilde{X}$:

::: pf-proof

::: pf-step
Let $p: \widetilde{X} \to X$ be the universal covering space.

::: pf-proof
$X$ is a connected CW complex, hence semilocally simply connected.
:::

:::

::: pf-step
The universal cover $\widetilde{X}$ is simply connected: $\pi_1(\widetilde{X}) = 0$.

::: pf-proof
definition of universal cover.
:::

:::

::: pf-step
By the Hurewicz Theorem applied to $\widetilde{X}$:
\[
\pi_2(X) \cong \pi_2(\widetilde{X}) \cong H_2(\widetilde{X}; \mathbb{Z}).
\]

::: pf-proof
covering projection induces isomorphism on higher homotopy groups $\pi_n(X) \cong \pi_n(\widetilde{X})$ for $n \ge 2$, and Hurewicz isomorphism theorem for simply connected spaces.
:::

:::

:::

:::

::: {.pf-step #s3}
**Case 1: $d = 0$ (all $n_i = 0$).**

::: pf-proof

::: pf-step
If $n_1 = \cdots = n_k = 0$, then $X \cong S^1 \vee \bigvee_{j=1}^k S^2$.

::: pf-proof
degree 0 attaching maps contract the boundary of each $D^2$ to the basepoint.
:::

:::

::: pf-step
The universal cover $\widetilde{X}$ is the real line $\mathbb{R}$ with $k$ 2-spheres wedged at each integer point $m \in \mathbb{Z}$: $\widetilde{X} \simeq \bigvee_{m \in \mathbb{Z}} \bigvee_{j=1}^k S^2$.

::: pf-proof
universal cover of $S^1 \vee \bigvee S^2$ unwraps $S^1$ to $\mathbb{R}$.
:::

:::

::: pf-step
Thus $\pi_2(X) \cong H_2(\widetilde{X}; \mathbb{Z}) \cong \bigoplus_{m \in \mathbb{Z}} \mathbb{Z}^k \cong \mathbb{Z}[\mathbb{Z}]^k$.

::: pf-proof
homology of a bouquet of 2-spheres indexed by $\mathbb{Z} \times \{1, \dots, k\}$.
:::

:::

:::

:::

::: {.pf-step #s4}
**Case 2: $d > 0$ (at least one $n_i \neq 0$).**

::: pf-proof

::: pf-step
$\pi_1(X) \cong \mathbb{Z}/d\mathbb{Z}$ is finite of order $d$, so $\widetilde{X}$ is a $d$-sheeted covering space.

::: pf-proof
index $[\pi_1(X) : 1] = d$.
:::

:::

::: pf-step
The 1-skeleton of $\widetilde{X}$ is the unique connected $d$-fold cover of $S^1$, which is a single circle $\widetilde{S}^1$ composed of $d$ 1-cells.

::: pf-proof
covering space classification of $S^1$.
:::

:::

::: pf-step
Above each 2-cell $e_j^2$ of $X$, there are $d$ distinct 2-cells in $\widetilde{X}$, each attached to $\widetilde{S}^1$ by a map of degree $n_j / d$.

::: pf-proof
covering homotopy property for the attaching map $S^1 \xrightarrow{n_j} S^1$ lifted to the $d$-fold cover $\widetilde{S}^1 \xrightarrow{d} S^1$.
:::

:::

::: pf-step
Thus $\widetilde{X}$ has $kd$ 2-cells, and the cellular boundary map $d_2: C_2(\widetilde{X}) \to H_1(\widetilde{S}^1) \cong \mathbb{Z}$ sends each lifted cell of the $j$-th family to $n_j / d \in \mathbb{Z}$.

::: pf-proof
cellular boundary formula for attaching maps into a circle.
:::

:::

::: pf-step
Since $\gcd\left(\frac{n_1}{d}, \dots, \frac{n_k}{d}\right) = 1$, the image of $d_2$ is $\mathbb{Z}$, so $d_2: \mathbb{Z}^{kd} \to \mathbb{Z}$ is surjective.

::: pf-proof
Bézout's identity on coprime integers.
:::

:::

::: {.pf-step #s4-6}
Since $C_3(\widetilde{X}) = 0$, $H_2(\widetilde{X}; \mathbb{Z}) = \ker(d_2) \cong \mathbb{Z}^{kd - 1}$.

::: pf-proof
kernel of a surjective homomorphism from $\mathbb{Z}^{kd}$ to $\mathbb{Z}$ is a free abelian group of rank $kd - 1$.
:::

:::

::: pf-step
Thus $\pi_2(X) \cong \mathbb{Z}^{kd - 1}$.

::: pf-proof
step [](#s2){.pf-ref} and step [](#s4-6){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion:
\[
\pi_2(X) \cong \begin{cases}
\bigoplus_{m \in \mathbb{Z}} \mathbb{Z}^k & \text{if } \gcd(n_1, \dots, n_k) = 0, \\
\mathbb{Z}^{k \gcd(n_1, \dots, n_k) - 1} & \text{if } \gcd(n_1, \dots, n_k) > 0.
\end{cases}
\]

::: pf-proof
step [](#s3){.pf-ref} and step [](#s4){.pf-ref}.
:::

:::

:::
:::
