---
schema: qual/card@1
id: P-DFB3Y
kind: problem
title: Homology of the mapping cone of a degree-$k$ map $S^n\to S^n$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Degree
relations: []
review: draft
---

::: problem
For topological spaces $X, Y$, the **mapping cone** $C(f)$ of a continuous map $f: X \to Y$ is the quotient space
$$
C(f) = (X \times [0, 1]) \amalg Y / \sim,
$$
where $(x, 0) \sim (x', 0)$ for all $x, x' \in X$ (collapsing the cone base to an apex), and $(x, 1) \sim f(x)$ for all $x \in X$ (gluing the base along $f$).

Let $\phi_k: S^n \to S^n$ ($n \ge 1$) be a continuous map of degree $k \in \mathbb{Z}$.
Find the integral homology groups $H_i(C(\phi_k); \mathbb{Z})$ for all $i \ge 0$.
:::

::: solution
**Goal:** Compute the homology groups $H_i(C(\phi_k); \mathbb{Z})$ using the long exact sequence of the pair $(C(\phi_k), S^n)$ and cellular homology.

<1>1. Cellular / topological structure of the mapping cone:
::: {.proof}
    <2>1. The mapping cone $C(\phi_k)$ is homeomorphic to the space obtained by attaching an $(n+1)$-cell $D^{n+1}$ to $S^n$ along the boundary attaching map $\phi_k: \partial D^{n+1} = S^n \to S^n$:
    $$C(\phi_k) \cong S^n \cup_{\phi_k} D^{n+1}.$$
    <2>2. The subcomplex $Y = S^n \subset C(\phi_k)$ is a deformation retract of a neighborhood in $C(\phi_k)$, so $(C(\phi_k), S^n)$ is a good pair.
    <2>3. The quotient space is the suspension of $S^n$:
    $$C(\phi_k) / S^n \cong D^{n+1} / \partial D^{n+1} \cong S^{n+1}.$$

:::

<1>2. Long exact sequence of the pair $(C(\phi_k), S^n)$:
::: {.proof}
    <2>1. The reduced homology exact sequence of the pair $(C(\phi_k), S^n)$ is:
    $$\cdots \to \tilde{H}_{i+1}(S^n) \to \tilde{H}_{i+1}(C(\phi_k)) \to \tilde{H}_{i+1}(S^{n+1}) \xrightarrow{\partial_*} \tilde{H}_i(S^n) \to \tilde{H}_i(C(\phi_k)) \to \tilde{H}_i(S^{n+1}) \to \cdots$$
    <2>2. The connecting homomorphism $\partial_*: \tilde{H}_{n+1}(S^{n+1}) \to \tilde{H}_n(S^n)$ is the induced map of the attaching map $\phi_k$ on top homology:
    $$\partial_*: \mathbb{Z} \to \mathbb{Z}, \quad \partial_*(1) = \deg(\phi_k) = k.$$
    <2>3. For degrees $i \notin \{0, n, n+1\}$:
    $$\tilde{H}_i(S^n) = 0 \quad \text{and} \quad \tilde{H}_i(S^{n+1}) = 0 \implies \tilde{H}_i(C(\phi_k)) = 0.$$

:::

<1>3. Computation in critical dimensions:
::: {.proof}
    <2>1. Degrees $n$ and $n+1$:
        - The relevant segment of the exact sequence is:
        $$0 \to \tilde{H}_{n+1}(C(\phi_k)) \xrightarrow{j_*} \tilde{H}_{n+1}(S^{n+1}) \xrightarrow{\partial_*} \tilde{H}_n(S^n) \xrightarrow{i_*} \tilde{H}_n(C(\phi_k)) \to 0.$$
        - Substituting $\tilde{H}_{n+1}(S^{n+1}) \cong \mathbb{Z}$ and $\tilde{H}_n(S^n) \cong \mathbb{Z}$ with $\partial_*(x) = k x$:
        $$0 \to \tilde{H}_{n+1}(C(\phi_k)) \xrightarrow{j_*} \mathbb{Z} \xrightarrow{\cdot k} \mathbb{Z} \xrightarrow{i_*} \tilde{H}_n(C(\phi_k)) \to 0.$$
    <2>2. Case $k \ne 0$:
        - The multiplication map $\cdot k: \mathbb{Z} \to \mathbb{Z}$ is injective ($\ker(\cdot k) = 0$).
        - Thus $\tilde{H}_{n+1}(C(\phi_k)) \cong \ker(\cdot k) = 0$.
        - The image is $k \mathbb{Z}$, so $\tilde{H}_n(C(\phi_k)) \cong \operatorname{coker}(\cdot k) = \mathbb{Z} / k \mathbb{Z} \cong \mathbb{Z}/|k|\mathbb{Z}$.
    <2>3. Case $k = 0$:
        - The multiplication map $\cdot 0: \mathbb{Z} \to \mathbb{Z}$ is the zero map.
        - Thus $\tilde{H}_{n+1}(C(\phi_0)) \cong \ker(0) = \mathbb{Z}$.
        - Thus $\tilde{H}_n(C(\phi_0)) \cong \operatorname{coker}(0) = \mathbb{Z}$.
    <2>4. Degree $i = 0$:
        - Since $C(\phi_k)$ is path-connected ($n \ge 1$), $H_0(C(\phi_k)) \cong \mathbb{Z}$.

:::

<1>4. Conclusion:
::: {.proof}
    - If $k \ne 0$:
    $$H_i(C(\phi_k); \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & i = 0, \\ \mathbb{Z}/|k|\mathbb{Z} & i = n, \\ 0 & \text{otherwise}. \end{cases}$$
    - If $k = 0$:
    $$H_i(C(\phi_0); \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & i \in \{0, n, n+1\}, \\ 0 & \text{otherwise}. \end{cases}$$
:::
:::
