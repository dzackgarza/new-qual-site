---
schema: qual/card@1
id: P-APASP08H
kind: problem
title: "Representation-theoretic interpretation of a symmetric function identity"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Give a representation-theoretic interpretation of the identity
$$
\frac{\partial}{\partial p_1}p_1^n = n p_1^{n-1}.
$$
:::

::: {.solution}

**Goal:** Provide the representation-theoretic interpretation of the symmetric function identity $\frac{\partial}{\partial p_1} p_1^n = n p_1^{n-1}$ via the Frobenius characteristic map and representation restriction from $S_n$ to $S_{n-1}$.

::: pf

::: pf-step
The Frobenius characteristic map and the regular representation:

::: pf-proof
*Proof:*

::: pf-step
Let $R(S_n)$ denote the character ring of the symmetric group $S_n$, and let $\Lambda = \bigoplus_{n \ge 0} \Lambda^n$ be the graded ring of symmetric functions.
:::

::: pf-step
The Frobenius characteristic map $\operatorname{ch}: \bigoplus_{n \ge 0} R(S_n) \to \Lambda$ is an isometric isomorphism mapping the irreducible character $\chi^\lambda$ to the Schur function $s_\lambda$.
:::

::: pf-step
The regular representation $\mathbb{C}[S_n]$ has character $\chi_{\text{reg}}(w) = |S_n| \mathbf{1}_{\{w = e\}}$.
:::

::: pf-step
Under the Frobenius characteristic map, the regular representation corresponds to the power-sum monomial
$$\operatorname{ch}(\mathbb{C}[S_n]) = \sum_{\lambda \vdash n} \dim(V^\lambda) s_\lambda = p_1^n = h_1^n.$$
:::

:::

:::

::: {.pf-step #restriction-is-adjoint-of-p1-multiplication}
Adjointness of induction and restriction (Frobenius Reciprocity):

::: pf-proof
*Proof:*

::: pf-step
Induction of representations $\operatorname{Ind}_{S_{n-1}}^{S_n}: R(S_{n-1}) \to R(S_n)$ corresponds under $\operatorname{ch}$ to multiplication by $p_1 = s_{(1)}$:
$$\operatorname{ch}\left( \operatorname{Ind}_{S_{n-1}}^{S_n} W \right) = p_1 \cdot \operatorname{ch}(W).$$
:::

::: pf-step
The Hall inner product on $\Lambda$ makes the Frobenius characteristic map an isometry: $\langle \operatorname{ch}(\chi), \operatorname{ch}(\psi) \rangle = \langle \chi, \psi \rangle_{S_n}$.
:::

::: pf-step
By Frobenius Reciprocity, restriction $\operatorname{Res}_{S_{n-1}}^{S_n}: R(S_n) \to R(S_{n-1})$ is the adjoint of induction:
$$\langle \operatorname{Res}_{S_{n-1}}^{S_n} V, W \rangle_{S_{n-1}} = \langle V, \operatorname{Ind}_{S_{n-1}}^{S_n} W \rangle_{S_n}.$$
:::

::: pf-step
In $\Lambda$, the adjoint of multiplication by $p_1$ with respect to the Hall inner product is the partial derivative operator $\frac{\partial}{\partial p_1}$ (the skewing operator $s_{(1)}^\perp$):
$$\left\langle \frac{\partial f}{\partial p_1}, g \right\rangle = \langle f, p_1 g \rangle.$$
:::

::: pf-step
Therefore the differential operator $\frac{\partial}{\partial p_1}$ is the image of the restriction functor under $\operatorname{ch}$:
$$\operatorname{ch}\left( \operatorname{Res}_{S_{n-1}}^{S_n} V \right) = \frac{\partial}{\partial p_1} \operatorname{ch}(V).$$
:::

:::

:::

::: {.pf-step #restriction-of-regular-rep}
Restriction of the regular representation:

::: pf-proof
*Proof:*

::: pf-step
Viewing $S_{n-1} \le S_n$ as the subgroup fixing the element $n$, the index is $[S_n : S_{n-1}] = n$.
:::

::: pf-step
Decomposing $S_n$ into $n$ left cosets $S_n = \bigsqcup_{i=1}^n \sigma_i S_{n-1}$, the group algebra $\mathbb{C}[S_n]$ as an $S_{n-1}$-module is the direct sum of $n$ copies of $\mathbb{C}[S_{n-1}]$:
$$\operatorname{Res}_{S_{n-1}}^{S_n} \mathbb{C}[S_n] \cong (\mathbb{C}[S_{n-1}])^{\oplus n}.$$
:::

::: pf-step
Applying the Frobenius characteristic map:
$$\operatorname{ch}\left( \operatorname{Res}_{S_{n-1}}^{S_n} \mathbb{C}[S_n] \right) = n \cdot \operatorname{ch}(\mathbb{C}[S_{n-1}]) = n p_1^{n-1}.$$
:::

:::

:::

::: pf-step
Synthesis and interpretation of the identity:

::: pf-proof
*Proof:*

::: pf-step
Equating the differential characterization from step [](#restriction-is-adjoint-of-p1-multiplication){.pf-ref} with the geometric module decomposition from step [](#restriction-of-regular-rep){.pf-ref}:
$$\frac{\partial}{\partial p_1} p_1^n = \frac{\partial}{\partial p_1} \operatorname{ch}(\mathbb{C}[S_n]) = \operatorname{ch}\left( \operatorname{Res}_{S_{n-1}}^{S_n} \mathbb{C}[S_n] \right) = n p_1^{n-1}.$$
:::

::: pf-step
Interpretation: The operator $\frac{\partial}{\partial p_1}$ represents restriction of representations from $S_n$ to $S_{n-1}$, $p_1^n$ represents the regular representation of $S_n$, and the factor $n$ represents the index $[S_n : S_{n-1}] = n$, which is the number of copies of the regular representation of $S_{n-1}$ obtained upon restriction.
:::

:::

:::

:::

:::
