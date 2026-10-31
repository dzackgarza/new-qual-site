---
schema: qual/card@1
id: E-HAT-2.1-25
kind: problem
title: Explicit noninductive formula for barycentric subdivision operator
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
  - Barycentric Subdivision
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 25; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed against the relevant chain, relative-homology, local-homology, or covering-space calculation.
---

::: {.problem}
Find an explicit, noninductive formula for the barycentric subdivision operator $S: C_n(X) \to C_n(X)$.
:::

::: {.solution}
Let $\sigma:\Delta^n\to X$ be a singular simplex, with standard domain vertices $e_0,\dots,e_n$. For each nonempty subset $I\subseteq\{0,\dots,n\}$, let $b_I\in\Delta^n$ be the barycenter of the domain face spanned by the $e_i$ with $i\in I$.

For a permutation $\pi=(i_0,\dots,i_n)\in S_{n+1}$, let
$$
\Delta_\pi:\Delta^n\to\Delta^n
$$
be the affine map taking the ordered vertices of its domain to
$$
b_{\{i_0\}},b_{\{i_0,i_1\}},\dots,b_{\{i_0,\dots,i_n\}}.
$$
Its image is one of the $n$-simplices in the barycentric subdivision of the standard domain simplex.

Then the explicit formula is
$$
\boxed{
S(\sigma)
=
\sum_{\pi\in S_{n+1}}
\operatorname{sgn}(\pi)\,(\sigma\circ\Delta_\pi).
}
$$
Extend this linearly to $C_n(X)$.

::: pf

::: {.pf-step #s1}

The summands are exactly the $n$-simplices of the barycentric subdivision.

::: pf-proof

An $n$-simplex of the subdivided domain corresponds to a maximal strict chain of nonempty faces
$$
F_0<F_1<\cdots<F_n=\Delta^n.
$$
Such a chain is uniquely obtained by choosing an ordering $i_0,\dots,i_n$ of the domain vertices and setting
$$
F_k=[e_{i_0},\dots,e_{i_k}].
$$
Thus maximal chains are in bijection with permutations of the vertices, and the associated affine maps are exactly the $\Delta_\pi$.

:::

:::

::: {.pf-step #s2}

The coefficient $\operatorname{sgn}(\pi)$ gives each subdivided domain simplex the orientation induced from $\Delta^n$.

::: pf-proof

For the identity permutation, the ordered barycentric vertices
$$
e_0,\ b_{01},\ b_{012},\dots,b_{0\cdots n}
$$
have the orientation of $[e_0,\dots,e_n]$. Permuting the domain vertices by $\pi$ changes orientation by $\operatorname{sgn}(\pi)$, and the corresponding maximal face chain changes in exactly the same way. Hence the displayed coefficient is the induced orientation sign.

:::

:::

::: pf-step

Therefore the formula agrees with the barycentric subdivision operator.

::: pf-proof

By definition, barycentric subdivision restricts $\sigma$ to each oriented barycentric subsimplex of its domain. By step [](#s1){.pf-ref} these restrictions are precisely $\sigma\circ\Delta_\pi$, and by step [](#s2){.pf-ref} their orientation coefficients are $\operatorname{sgn}(\pi)$. Hence the displayed sum is exactly $S(\sigma)$.

:::

:::

:::

:::
