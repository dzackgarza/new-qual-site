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
For an oriented simplex
\[
\sigma=[v_0,\dots,v_n],
\]
and a nonempty subset $I\subseteq\{0,\dots,n\}$, write $b_I$ for the barycenter of the face spanned by the vertices $v_i$ with $i\in I$.

For a permutation $\pi=(i_0,\dots,i_n)\in S_{n+1}$, let
\[
\Delta_\pi=
[b_{\{i_0\}},b_{\{i_0,i_1\}},\dots,b_{\{i_0,\dots,i_n\}}].
\]
This is one of the $n$-simplices in the barycentric subdivision of $\sigma$.

Then the explicit formula is
\[
\boxed{
S([v_0,\dots,v_n])
=
\sum_{\pi\in S_{n+1}}
\operatorname{sgn}(\pi)\,
[b_{\{i_0\}},b_{\{i_0,i_1\}},\dots,b_{\{i_0,\dots,i_n\}}].
}
\]
Extend this linearly to $C_n(X)$.

<1>1. The summands are exactly the $n$-simplices of the barycentric subdivision.
::: {.proof}
An $n$-simplex of the barycentric subdivision corresponds to a maximal strict chain of nonempty faces
\[
F_0<F_1<\cdots<F_n=\sigma.
\]
Such a chain is uniquely obtained by choosing an ordering $i_0,\dots,i_n$ of the original vertices and setting
\[
F_k=[v_{i_0},\dots,v_{i_k}].
\]
Thus maximal chains are in bijection with permutations of the vertices, and the associated barycentric vertices are exactly those displayed in $\Delta_\pi$.
:::

<1>2. The coefficient $\operatorname{sgn}(\pi)$ gives each subdivided simplex the orientation induced from $\sigma$.
::: {.proof}
For the identity permutation, the ordered barycentric vertices
\[
v_0,\ b_{01},\ b_{012},\dots,b_{0\cdots n}
\]
have the orientation of $[v_0,\dots,v_n]$. Permuting the original vertices by $\pi$ changes orientation by $\operatorname{sgn}(\pi)$, and the corresponding maximal face chain changes in exactly the same way. Hence the displayed coefficient is the induced orientation sign.
:::

<1>3. Therefore the formula agrees with the barycentric subdivision operator.
::: {.proof}
By definition, barycentric subdivision replaces an oriented simplex by the sum of all its oriented barycentric subsimplices. By <1>1 these are precisely the $\Delta_\pi$, and by <1>2 their orientation coefficients are $\operatorname{sgn}(\pi)$. Hence the displayed sum is exactly $S(\sigma)$.
:::
:::
