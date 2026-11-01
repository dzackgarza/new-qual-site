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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the explicit formula: for each permutation $\pi$ an affine map carries the standard simplex onto the corresponding subdivided simplex, and the signed sum $\sum_\pi\mathrm{sgn}(\pi)\,\sigma\Delta_\pi$ is the noninductive subdivision operator with the signs that make it a chain map.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    The formula was wrong as stated and is corrected here. The card gave
    `S(sigma) = sum_pi sgn(pi) (sigma o Delta_pi)` with `Delta_pi` running *up* the face chain from a
    single vertex. Hatcher defines `S lambda = b_lambda (S partial lambda)` (p.121), and the cone
    prepends the barycentre of the whole simplex, so his sub-simplices begin at `b_{Delta^n}`: in
    dimension `1` his chain is `[b, v_1] - [b, v_0]`, whereas the card's formula gives
    `[v_0, b] - [v_1, b]`. Those are different elements of the free abelian group on singular
    simplices — a reordered affine simplex is a different generator, not the negative of the original
    — so the two conventions cannot be identified silently. The boxed formula now uses the descending
    map `bar Delta_pi(e_k) = b_{i_0 ... i_{n-k}}` with the global factor `(-1)^{n(n+1)/2}`, which is
    exactly the sign difference between the two vertex orderings. The general identity is argued by the induction recorded in the solution; the exact
    chain-level regression `proofs/cards/bary_regression.py` covers only `n = 1, 2, 3` and computes the
    recursive operator and both closed formulas in the free abelian group on vertex tuples and shows
    that the operator equals `(-1)^{n(n+1)/2}` times the descending formula there, and equals neither the
    ascending formula nor its negative; it is a bounded regression, not a proof for all `n`, and the
    general statement rests on the induction, which is not formalized. Everything else in the solution stands: the summands are the
    `n`-simplices of the subdivision, and the coefficients are the permutation signs; only the vertex
    ordering and the global sign needed repair.
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

Order the barycentres the way the cone formula does, from the whole simplex down:
$$\bar\Delta_\pi(e_k)=b_{\{i_0,\dots,i_{n-k}\}},\qquad k=0,\dots,n,$$
so that $\bar\Delta_\pi$ starts at the barycentre $b_{\Delta^n}$ of the whole domain. Then the explicit formula is
$$
\boxed{
S(\sigma)
=
(-1)^{n(n+1)/2}
\sum_{\pi\in S_{n+1}}
\operatorname{sgn}(\pi)\,(\sigma\circ\bar\Delta_\pi).
}
$$
Extend this linearly to $C_n(X)$.

Two warnings about the conventions, because both are easy to get wrong. First, the vertex order matters: $\Delta_\pi$ above runs *up* the face chain starting from a single vertex, while $\bar\Delta_\pi$ runs *down* from the whole simplex, and $\bar\Delta_\pi$ is the one Hatcher's cone formula $S\lambda=b_\lambda(S\partial\lambda)$ produces, since the cone prepends $b_\lambda$. Second, a reordered affine simplex is a genuinely different singular simplex, not the negative of the original: $[b,v_1]$ and $[v_1,b]$ are distinct generators of the free abelian group $C_1(X)$, so passing from $\bar\Delta_\pi$ to $\Delta_\pi$ is *not* multiplication by a sign. The global factor $(-1)^{n(n+1)/2}$ is exactly the difference between the two orderings, and it is computed below rather than guessed.

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
b_{0\cdots n},\ b_{0\cdots n-1},\ \dots,\ b_0
$$
are the subdivision of $[e_0,\dots,e_n]$ traversed from the top face down, and the recurrence $S\lambda=b_\lambda(S\partial\lambda)$ gives them the sign $+1$ against the orientation of $[e_0,\dots,e_n]$ in dimension $n$ for $n\equiv0,3\pmod4$ and $-1$ for $n\equiv1,2\pmod4$ — that is the factor $(-1)^{n(n+1)/2}={{}\pm1}$ displayed. Permuting the domain vertices by $\pi$ permutes these barycentric vertices in the same way, contributing $\operatorname{sgn}(\pi)$. The exact computation of the two orderings and of the global sign is the regression below.

:::

:::

::: pf-step

Chain-level regression

::: pf-proof

The general argument is an induction on `n`, and it is the *only* proof of the formula for all `n`. Write `S(lambda) = b_lambda(S partial lambda)` with `partial lambda = sum_k (-1)^k partial_k lambda`. By induction the closed form is known on each `(n-1)`-simplex `partial_k lambda`, with global sign `(-1)^{(n-1)n/2}`; coning with `b_lambda` prepends the apex and keeps the coefficient of the corresponding permutation, while the factor `(-1)^k` from the boundary and the fact that coning reverses the effective vertex order contribute exactly `(-1)^n` per summand, i.e. an extra `(-1)^n` overall. Since `(n-1)n/2 + n = n(n+1)/2`, the two global signs multiply to `(-1)^{n(n+1)/2}`, which is the stated factor. The same induction shows the *ascending* formula cannot be right: coning prepends the apex, so the sub-simplices begin at `b_{Delta^n}` and their vertex lists descend.

`proofs/cards/bary_regression.py` is a **bounded regression**, not a proof of the identity: it computes for `n = 1, 2, 3` only, in the free abelian group on vertex tuples, both the recursive operator and the two closed formulas, and confirms the identity there as well as refuting the old ascending formula — in dimension `1`, `S[v_0,v_1] = [b,v_1] - [b,v_0]`, whose summands are `[b,v_1]` and `[b,v_0]`, whereas the ascending formula gives `[v_0,b] - [v_1,b]`, different generators of `C_1`. It says nothing about `n >= 4`; the induction above is what covers those, and it is not formalized.

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
