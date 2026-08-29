---
schema: qual/card@1
id: P-TOPF24B
kind: problem
title: Examples separating $\pi_2$ and $H_2$
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Give an explicit example:
(a) of a topological space $X$ with $\pi_2(X) = 0$ and $H_2(X) \neq 0$, and
(b) of a topological space $Y$ with $\pi_2(Y) \neq 0$ and $H_2(Y) = 0$.
:::

::: solution
**Goal:** Construct spaces separating the second homotopy group $\pi_2$ and second homology group $H_2$.

<1>1. Part (a): Space $X$ with $\pi_2(X) = 0$ and $H_2(X) \ne 0$:
    *Proof:*
    <2>1. **Example:** The 2-torus $X = T^2 = S^1 \times S^1$.
    <2>2. **Computation of $\pi_2(T^2)$:**
        - The universal covering space of the torus is the Euclidean plane:
          $$p: \mathbb{R}^2 \longrightarrow T^2 = \mathbb{R}^2 / \mathbb{Z}^2.$$
        - Since $\mathbb{R}^2$ is contractible ($\pi_k(\mathbb{R}^2) = 0$ for all $k \ge 1$), the long exact sequence of homotopy groups for a covering space gives an isomorphism:
          $$\pi_k(T^2) \cong \pi_k(\mathbb{R}^2) = 0 \quad \text{for all } k \ge 2.$$
        - In particular, $\pi_2(T^2) = 0$.
    <2>3. **Computation of $H_2(T^2)$:**
        - $T^2$ is a closed orientable 2-manifold, so its top homology is:
          $$H_2(T^2; \mathbb{Z}) \cong \mathbb{Z} \ne 0.$$
    <2>4. Thus $X = T^2$ satisfies $\pi_2(X) = 0$ and $H_2(X) \cong \mathbb{Z} \ne 0$.
        *(Other valid examples: any closed orientable surface $\Sigma_g$ of genus $g \ge 1$, or the real projective plane $\mathbb{RP}^2$ for $H_2(-; \mathbb{Z}/2\mathbb{Z})$).*

<1>2. Part (b): Space $Y$ with $\pi_2(Y) \ne 0$ and $H_2(Y) = 0$:
    *Proof:*
    <2>1. **Example:** The real projective plane $Y = \mathbb{RP}^2$.
    <2>2. **Computation of $\pi_2(\mathbb{RP}^2)$:**
        - The 2-sphere $S^2$ is the universal 2-sheeted covering space:
          $$p: S^2 \longrightarrow \mathbb{RP}^2.$$
        - For $k \ge 2$, covering projections induce isomorphisms on homotopy groups:
          $$\pi_2(\mathbb{RP}^2) \cong \pi_2(S^2) \cong \mathbb{Z} \ne 0.$$
    <2>3. **Computation of $H_2(\mathbb{RP}^2; \mathbb{Z})$:**
        - The integer homology groups of $\mathbb{RP}^2$ are $H_0 \cong \mathbb{Z}$, $H_1 \cong \mathbb{Z}/2\mathbb{Z}$, and:
          $$H_2(\mathbb{RP}^2; \mathbb{Z}) = 0.$$
    <2>4. Thus $Y = \mathbb{RP}^2$ satisfies $\pi_2(Y) \cong \mathbb{Z} \ne 0$ and $H_2(Y; \mathbb{Z}) = 0$.
        *(Alternative Example: $Y = S^2 \times S^3 / \sim$ attached to kill $H_2$, or the universal cover of a Moore space with fundamental group).*

<1>3. Conclusion:
    (a) $X = T^2$ has $\pi_2(T^2) = 0$ and $H_2(T^2) \cong \mathbb{Z}$;
    (b) $Y = \mathbb{RP}^2$ has $\pi_2(\mathbb{RP}^2) \cong \mathbb{Z}$ and $H_2(\mathbb{RP}^2) = 0$. Q.E.D.
:::
