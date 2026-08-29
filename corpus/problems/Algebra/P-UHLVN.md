---
schema: qual/card@1
id: P-UHLVN
kind: problem
title: Galois groups of cubics
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What are the possible Galois groups for a cubic polynomial $f(x) \in K[x]$ over a field $K$ (of characteristic $\ne 2, 3$)?
Classify them completely using the discriminant and irreducibility.
:::

::: solution
**Goal:** Classify all possible Galois groups of cubic polynomials over a field $K$.

<1>1. General Setting and Embedding into $S_3$:
    *Proof:*
    <2>1. Let $f(x) = x^3 + a x^2 + b x + c \in K[x]$ be a cubic polynomial with roots $\alpha_1, \alpha_2, \alpha_3$ in an algebraic closure $\bar{K}$.
    <2>2. Let $L = K(\alpha_1, \alpha_2, \alpha_3)$ be the splitting field of $f(x)$ over $K$.
    <2>3. The Galois group $G = \operatorname{Gal}(L/K)$ acts faithfully by permutations on the set of 3 roots $\{\alpha_1, \alpha_2, \alpha_3\}$.
    <2>4. Thus $G$ embeds as a subgroup of the symmetric group $S_3$:
        $$G \le S_3.$$
    <2>5. The subgroups of $S_3$ are: the trivial group $\{e\}$, $\mathbb{Z}_2$ (order 2), $A_3 \cong \mathbb{Z}_3$ (order 3), and $S_3$ (order 6).

<1>2. Reducible Cubics (at least one root in $K$):
    *Proof:*
    <2>1. **Three roots in $K$:** If $f(x) = (x - \alpha_1)(x - \alpha_2)(x - \alpha_3)$ splits completely in $K$, then $L = K$, so:
        $$G \cong \{e\}.$$
    <2>2. **One root in $K$, irreducible quadratic factor:** If $f(x) = (x - \alpha_1) q(x)$ where $q(x)$ is an irreducible quadratic over $K$:
        - The splitting field is $L = K(\sqrt{\Delta})$ where $\Delta$ is the discriminant of $q(x)$.
        - $[L : K] = 2$, so:
            $$G \cong \mathbb{Z}_2.$$

<1>3. Irreducible Cubics (Transitive Subgroups of $S_3$):
    *Proof:*
    <2>1. If $f(x)$ is irreducible over $K$, then the Galois group $G$ must act transitively on the 3 roots.
    <2>2. By the Orbit-Stabilizer Theorem, $3 = [\deg(f)]$ divides $|G|$.
    <2>3. The only transitive subgroups of $S_3$ are $A_3 \cong \mathbb{Z}_3$ and $S_3$.
    <2>4. **Role of the Discriminant $\Delta(f)$:**
        - Let $\delta = (\alpha_1 - \alpha_2)(\alpha_1 - \alpha_3)(\alpha_2 - \alpha_3)$, so $\Delta(f) = \delta^2 \in K$.
        - An element $\sigma \in G$ is an even permutation (i.e. $\sigma \in A_3$) if and only if $\sigma(\delta) = \delta$.
        - Therefore, $G \subseteq A_3 \iff \delta \in K \iff \Delta(f) \text{ is a square in } K$.
    <2>5. **Case 1: $\Delta(f) \in (K^\times)^2$ (Square Discriminant):**
        $$G \cong A_3 \cong \mathbb{Z}_3.$$
        - $[L : K] = 3$; adjoining one root yields the full splitting field ($K(\alpha_1) = L$).
        - *Example:* $f(x) = x^3 - 3x + 1$ over $\mathbb{Q}$ has $\Delta = 81 = 9^2$, so $\operatorname{Gal}(f/\mathbb{Q}) \cong \mathbb{Z}_3$.
    <2>6. **Case 2: $\Delta(f) \notin (K^\times)^2$ (Non-Square Discriminant):**
        $$G \cong S_3.$$
        - $[L : K] = 6$; $L = K(\alpha_1, \sqrt{\Delta})$.
        - *Example:* $f(x) = x^3 - 2$ over $\mathbb{Q}$ has $\Delta = -108 < 0$, so $\operatorname{Gal}(f/\mathbb{Q}) \cong S_3$.

<1>4. Summary Table of Galois Groups of Cubics:
    $$\begin{array}{|c|c|c|}
    \hline
    \text{Reducibility of } f & \text{Discriminant } \Delta(f) & \operatorname{Gal}(f/K) \\
    \hline
    \text{Splits completely in } K & \text{Square} & \{e\} \\
    \text{Linear } \times \text{ Irreducible quadratic} & \text{Non-square} & \mathbb{Z}_2 \\
    \text{Irreducible} & \text{Square in } K & A_3 \cong \mathbb{Z}_3 \\
    \text{Irreducible} & \text{Not a square in } K & S_3 \\
    \hline
    \end{array}$$

<1>5. Conclusion:
    An irreducible cubic has Galois group $S_3$ if $\Delta$ is not a square in $K$, and $A_3 \cong \mathbb{Z}_3$ if $\Delta$ is a square in $K$. Q.E.D.
:::
