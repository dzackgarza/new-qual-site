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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Certificate scope recorded after `proofs/cards/BarySubdiv.lean`. Now formalized, with no `sorryAx`
    and axioms only `propext`, `Classical.choice`, `Quot.sound`: (i) the recursion
    $S\lambda=b_\lambda(S\partial\lambda)$ itself, in the free abelian group on ordered chains of faces of
    $\Delta^n$, with **every** coefficient of it computed (`coeff_subdiv`) and the coefficient of the chain of
    a peeling order proved to be the recursion's own sign at that order (`coeff_subdiv_chainOf`,
    `coeff_subdiv_chainOf_eq_pow`); (ii) the deletion positions aggregated with no reference to the
    intermediate faces (`stepExp_eq_pairCount`), and the outermost deletion's factor identified with the
    peeled vertex's value (`deletionPos_univ`); (iii) the first vertex of the descending barycentric vertex
    list proved to be the barycentre of the whole simplex (`descVertex_zero`), the vertex the cone prepends.
    Not formalized, and not claimed: the reindexing of the peeling-order pair count against
    $\sum_j \#\{i\le j:\pi i<\pi j\}$, hence the coefficient $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$
    itself; the exhaustive nonduplicated indexing of the recursion's support by $S_{n+1}$; and the transport
    to singular chains of $\Delta^n$. This event records certificate scope only: the solution text was not
    re-proved here.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Supersedes the scope clause of the previous event, which said the reindexing and the coefficient
    $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$ were not formalized. They now are, for every $n$ and every
    $\pi$, in `proofs/cards/BarySubdiv.lean`: `pairCount_ofFn` (a list count over `List.ofFn g` is the
    `Fin`-indexed count of the pairs $i<j$ with $g j<g i$), `pairCount_peel_eq_delSum` (the peeling order
    $\pi(N-1),\dots,\pi 0$ has deletion-position count exactly $\sum_j\#\{i\le j:\pi i<\pi j\}$), the sign
    algebra restated there and applied, and `coeff_subdiv_peel_sign`: the recursion's coefficient of the
    descending chain of $\pi$ is $(-1)^{N(N-1)/2}\operatorname{sgn}(\pi)$. Elaborated on the canonical
    baseline, 26 printed theorems, no `sorryAx`, axioms only `propext`, `Classical.choice`, `Quot.sound`.
    Still **not** formalized, and not claimed: the assembly of the coefficient statements into the single
    chain-level identity (the exhaustive nonduplicated indexing of the recursion's support by $S_{n+1}$),
    and any identification with Hatcher's operator on singular chains of $\Delta^n$.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Whole-chain stage. Supersedes the "not formalized" clauses of both previous events for the support
    question: `proofs/cards/BarySubdiv.lean` now proves, in the free abelian group on ordered chains of
    faces of the standard simplex, `subdiv_univ_eq_sum_perm`, i.e.
    $S = \sum_{\pi\in S_N}(-1)^{N(N-1)/2}\operatorname{sgn}(\pi)\,[\text{chain of }\pi]$, with one
    summand per permutation and nothing else in the support — by `chainCoeff_exists_chainOf` (support
    exhaustion, by induction along the recursion's own coefficient function), `chainOf_injective`
    (nonduplication, by strong induction on the face), `exists_perm_peel`, `chainOf_peel_injective` and
    `ext_coeff` (comparison of all coefficients). Transport side, also proved: `chainOf_getElem?_take`
    (the $k$-th face of a chain is the face with the first $k$ peeled vertices removed),
    `descFace_antitone`, `descFace_last`, `descVertex_last`, so the descending barycentric vertex list
    runs from $b_{\Delta^{N-1}}$ down to the vertex $\pi 0$; `affineMap_mem`/`affineMap_single` give the
    affine simplex spanned by such a list. 36 printed theorems, no `sorryAx`, axioms only `propext`,
    `Classical.choice`, `Quot.sound`, on the canonical baseline. Still **not** formalized, and not
    claimed: the identification of the flags `descFace` with the faces of the chains, the geometric
    reading of the chains as the singular simplices $\sigma\circ\bar\Delta_\pi$, and therefore the
    displayed identity as a statement about $C_n(X)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Flags and transport, up to vertex lists. `chainOf_peel_eq_ofFn_descFace` proves that the
    recursion's chain for $\pi$ is the list of prefix faces $\pi''\mathrm{Iic}(\mathrm{rev}\,k)$, so
    the flags are exactly that summand's sub-simplices (pieces: `peel_take_toFinset`, `rev_image_Iio`,
    `sdiff_image_of_bijective`, `univ_sdiff_Ioi`, `peel_take_face`, `chainOf_length`).
    `map_baryWeight_chainOf_peel` reads them as barycentres and obtains the descending vertex list;
    `map_subdiv_univ_bary` is the linear extension of that reading over the free abelian group and
    carries the whole recursion to the signed sum of descending vertex lists with the same coefficients;
    `affineMap_cons_apply` states the coordinate form of Hatcher's prepend (the apex enters with its own
    barycentric coordinate $x_0$); `continuous_affineMap` with `affineMap_mem` and `affineMap_single`
    makes such a list a continuous affine map of the standard simplex with exactly those vertices. 45
    printed theorems, no `sorryAx`, axioms only `propext`, `Classical.choice`, `Quot.sound`. Still not
    formalized, and not claimed: identifying this free abelian group on continuous affine maps of
    $\mathrm{stdSimplex}$ with the degree-$n$ group of the maintained singular chain complex, and
    composing with a singular simplex $\sigma$ to reach Hatcher's operator on $C_n(X)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Hatcher's operator formula, as a theorem. `proofs/cards/BarySubdiv.lean` proves
    `hatcher_formula`: for every `M` and every continuous `sigma` out of the standard `M`-simplex,
    `map (c => sigma.comp (chainAffineMap c)) (subdiv univ) = sum_pi ((-1)^(M(M+1)/2) sgn pi) •
    of (sigma.comp (barySimplex pi))`, where `subdiv` is the proved recursion
    $S\lambda=b_\lambda(S\partial\lambda)$ on the free abelian group on chains of faces,
    `chainAffineMap` reads a chain of faces as the continuous map whose vertex $k$ is the barycentre
    of the $k$-th face, `barySimplex` is $\bar\Delta_\pi$ on the descending vertex list (first vertex
    = the barycentre of the whole simplex, `descVertex_zero`), and `chainAffineMap_chainOf_peel`
    proves the chain of $\pi$ is its $\bar\Delta_\pi$ (via the take/Ici identification
    `chainOf_peel_eq_ofFn_descFace`). So the displayed formula $S\sigma =
    (-1)^{n(n+1)/2}\sum_\pi\operatorname{sgn}(\pi)(\sigma\circ\bar\Delta_\pi)$ is proved for
    $n=M$, coefficients and vertex order included, and the prepend convention is the proved
    `affineMap_cons_apply`/`descVertex_zero`. Boundaries: the maps are self-maps of the ambient
    $\mathbb{R}^{n+1}$ landing in `stdSimplex` (`affineMap_mem`), `TopCat.toSSetObjEquiv` identifies
    such maps with singular $n$-simplices of the standard simplex, but the identification of their
    free abelian group with the degree-$n$ object of `singularChainComplexFunctor` is not written out,
    and the chain-map property $\partial S=S\partial$ is not claimed. 47 printed theorems, no
    `sorryAx`, axioms only `propext`, `Classical.choice`, `Quot.sound`.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Corrects the previous event's scope clause and closes the singular-chain target. Two corrections:
    (i) the published file carried a stale `#print axioms BarySubdiv.sdiff_image_of_injective` target —
    the declaration is `sdiff_image_of_bijective`; Lean reported it as
    `error(lean.unknownIdentifier)`, which a check written as `grep -c "error:"` missed, so the earlier
    "zero errors" claim for this file was wrong. The target is corrected and the whole file re-run,
    checked by exit status and by a grep for `error` in any form: exit 0, no errors, 53 axiom lines,
    zero `sorryAx`. (ii) The singular-chain target is now formalized: the degree-$n$ group of
    `X.chainComplex (ModuleCat.of ℤ ℤ)` is definitionally the coproduct of one copy of ℤ per singular
    $n$-simplex (checked by `rfl`), `singularChainIota` is the coprojection,
    `barySimplexOn`/`barySimplexSingular` package $\bar\Delta_\pi$ as an honest singular $n$-simplex via
    `TopCat.toSSetObjEquiv` (faithfully, `toSSetObjEquiv_barySimplexSingular`), `chainSingular_chainOf_peel`
    identifies the packaged chain of $\pi$ with $\bar\Delta_\pi$, and `singular_chain_formula` states the
    recursion pushed through the barycentric affine maps and the coprojections as the signed sum
    $\sum_\pi(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)\,\iota(\bar\Delta_\pi)$. Boundaries still: simplices
    are packaged into the ambient space $\mathbb{R}^{n+1}$, and $\partial S=S\partial$ is not claimed.
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

The coefficient $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$ gives each subdivided domain simplex the orientation induced from $\Delta^n$.

::: pf-proof

For the identity permutation, the ordered barycentric vertices
$$
b_{0\cdots n},\ b_{0\cdots n-1},\ \dots,\ b_0
$$
are the subdivision of $[e_0,\dots,e_n]$ traversed from the top face down, and the recurrence $S\lambda=b_\lambda(S\partial\lambda)$ gives them the sign $+1$ against the orientation of $[e_0,\dots,e_n]$ in dimension $n$ for $n\equiv0,3\pmod4$ and $-1$ for $n\equiv1,2\pmod4$ — that is the factor $(-1)^{n(n+1)/2}={{}\pm1}$ displayed. Permuting the domain vertices by $\pi$ permutes these barycentric vertices in the same way, contributing $\operatorname{sgn}(\pi)$.

The global factor is not a convention and not a guess: it is the parity of the sum of the deletion positions along the descending chain. Going from the face $F_j=\{\pi 0,\dots,\pi j\}$ down to $F_{j-1}$ deletes the vertex $\pi j$, and its position among the vertices of $F_j$ is
$$d_j=\#\{i\le j: \pi i<\pi j\},$$
so the recursion's sign for the $\pi$-summand is $(-1)^{d_0+\dots+d_{n-1}}$. The diagonal terms contribute nothing, so
$$d_0+\dots+d_{n-1}=\#\{(i,j): i<j,\ \pi i<\pi j\},$$
the number of *noninversions* of $\pi$; and inversions plus noninversions count all pairs, $n(n+1)/2$ of them. Hence
$$(-1)^{d_0+\dots+d_{n-1}}=(-1)^{n(n+1)/2}(-1)^{\operatorname{inv}(\pi)}=(-1)^{n(n+1)/2}\operatorname{sgn}(\pi),$$
which is the displayed factor. The pair counts, the inversion/noninversion partition and $\operatorname{sgn}(\pi)=(-1)^{\operatorname{inv}(\pi)}$ are proved in `proofs/cards/BarySign.lean` (`card_pairSet`, `noninv_add_inv`, `sign_eq_neg_one_pow_inv`); that $d_j$ really is the position of the deleted vertex, and that the recursion carries these positions as its signs, is proved in `proofs/cards/BarySubdiv.lean` (`coeff_subdiv`, `coeff_subdiv_chainOf`, `stepExp_eq_pairCount`), where $S\lambda=b_\lambda(S\partial\lambda)$ is modelled in the free abelian group on ordered chains of faces and **every** coefficient of it is computed rather than assumed. The reindexing of that pair count against the permutation-indexed sum $\sum_j\#\{i\le j:\pi i<\pi j\}$ is also formalized there (`pairCount_ofFn`, `pairCount_peel_eq_delSum`), and with the sign algebra (`pow_delSum_eq_global_mul_sign`) it gives the coefficient of the recursion's descending chain at every $\pi$, namely $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$ (`coeff_subdiv_peel_sign`). The exhaustive nonduplicated indexing of the recursion's support by $S_{n+1}$ is formalized there as well (`chainCoeff_exists_chainOf`, `chainOf_injective`, `subdiv_univ_eq_sum_perm`), so the displayed identity holds in the free abelian group on ordered chains of faces of the standard simplex, one summand per permutation and nothing else in the support. Not formalized: the *geometric reading* of those chains as the singular simplices $\sigma\circ\bar\Delta_\pi$ — no subdivision operator is available on singular chains — so the displayed identity is not yet a statement about $C_n(X)$; the $n=1,2,3$ regression below is a bounded check of the resulting chains.

:::

:::

::: pf-step

Chain-level regression

::: pf-proof

The general argument is an induction on `n` whose bookkeeping is a stated combinatorial identity, and it is the *only* proof of the formula for all `n`. Write `S(lambda) = b_lambda(S partial lambda)` with `partial lambda = sum_k (-1)^k partial_k lambda`. By induction the closed form is known on each `(n-1)`-simplex `partial_k lambda`, with global sign `(-1)^{(n-1)n/2}`; coning with `b_lambda` prepends the apex and keeps the coefficient of the corresponding permutation, while the factor `(-1)^k` from the boundary and the fact that coning reverses the effective vertex order contribute exactly `(-1)^n` per summand, i.e. an extra `(-1)^n` overall. Since `(n-1)n/2 + n = n(n+1)/2`, the two global signs multiply to `(-1)^{n(n+1)/2}`, which is the stated factor. Equivalently, and this is the form to prove outright: along the descending chain indexed by `\pi`, the sum of the deletion positions equals the number of noninversions of `\pi`, namely `n(n+1)/2 - \operatorname{inv}(\pi)`, so the recursion's sign `(-1)^{\text{sum}}` equals `(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)` because `\operatorname{sgn}(\pi) = (-1)^{\operatorname{inv}(\pi)}`. That identity is a statement about permutations and is what the all-`n` proof rests on. For the coefficient of a fixed summand this identity is now machine-checked: the sign algebra (`proofs/cards/BarySign.lean`, restated in `proofs/cards/BarySubdiv.lean`), the modelling of the recursion with all its coefficients, the aggregation of the deletion positions to a pair count (`stepExp_eq_pairCount`), and the reindexing of that pair count against the index $\pi$ (`pairCount_peel_eq_delSum`), so `coeff_subdiv_peel_sign` gives the coefficient $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$ of the chain of $\pi$ in the recursion. The assembly of the coefficient statements into the single identity displayed above is formalized too: in the free abelian group on ordered chains of faces, `subdiv_univ_eq_sum_perm` proves $S = \sum_\pi (-1)^{N(N-1)/2}\operatorname{sgn}(\pi)\,[\text{chain of }\pi]$ with nothing else in the support (`chainCoeff_exists_chainOf` for exhaustion, `chainOf_injective` for nonduplication). The transport side is partly formalized: `chainOf_getElem?_take` computes the faces of a chain from its peeling order, `descFace_antitone` shows the descending flags are nested, and `descVertex_zero`/`descVertex_last` pin the barycentric vertex list from the barycentre of the whole simplex down to the vertex $\pi 0$; `affineMap_mem` and `affineMap_single` give the affine simplex such a list spans. The identification of `descFace` with the chain's faces is formalized as well (`chainOf_peel_eq_ofFn_descFace`): the recursion's chain for $\pi$ is exactly the list of its prefix faces, so the flags *are* that summand's sub-simplices. Reading those faces as barycentres gives the descending vertex list (`map_baryWeight_chainOf_peel`), the linear extension of that reading over the chain group carries the whole recursion to the signed sum of those vertex lists (`map_subdiv_univ_bary`), the affine map of such a list has exactly those vertices (`affineMap_single`) and is continuous (`continuous_affineMap`), and `affineMap_cons_apply` is the coordinate form of the prepend in $S\lambda=b_\lambda(S\partial\lambda)$: the prepended apex enters with its own barycentric coordinate $x_0$. The composition with a singular simplex is formalized too, as Hatcher's operator formula: `chainAffineMap` reads a chain of faces as the continuous map whose vertex $k$ is the barycentre of the $k$-th face, `barySimplex` is $\bar\Delta_\pi$ on the descending vertex list, `chainAffineMap_chainOf_peel` proves that the chain of $\pi$ *is* its $\bar\Delta_\pi$, and `hatcher_formula` states, for an arbitrary continuous $\sigma$ out of the standard $n$-simplex, that the subdivision defined from $S\lambda=b_\lambda(S\partial\lambda)$ and read geometrically equals the displayed signed sum:
$$S\sigma=(-1)^{n(n+1)/2}\sum_{\pi\in S_{n+1}}\operatorname{sgn}(\pi)\,(\sigma\circ\bar\Delta_\pi).$$
The passage into the maintained chain complex is formalized as well: the degree-$n$ group of `X.chainComplex (ModuleCat.of ℤ ℤ)` is *definitionally* the coproduct of one copy of $\mathbb{Z}$ per singular $n$-simplex, so `singularChainIota` is the coprojection with no extra identification, `barySimplexOn`/`barySimplexSingular` package $\bar\Delta_\pi$ through `TopCat.toSSetObjEquiv` as an honest singular $n$-simplex, and `singular_chain_formula` states the recursion pushed through the barycentric affine maps and the coprojections: the lift of the chain of faces to `ι ∘ chainSingular` applied to `subdiv univ` is $\sum_\pi(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)\,\iota(\bar\Delta_\pi)$. Boundaries: the simplices are packaged into the ambient space $\mathbb{R}^{n+1}$ (which contains the standard simplex, where `affineMap_mem` puts their images), and the chain-map property $\partial S=S\partial$ is not claimed here (the exercise asks for the formula, not the chain map). The same induction shows the *ascending* formula cannot be right: coning prepends the apex, so the sub-simplices begin at `b_{Delta^n}` and their vertex lists descend.

`proofs/cards/bary_regression.py` is a **bounded regression**, not a proof of the identity: it computes for `n = 1, 2, 3` only, in the free abelian group on vertex tuples, both the recursive operator and the two closed formulas, and confirms the identity there as well as refuting the old ascending formula — in dimension `1`, `S[v_0,v_1] = [b,v_1] - [b,v_0]`, whose summands are `[b,v_1]` and `[b,v_0]`, whereas the ascending formula gives `[v_0,b] - [v_1,b]`, different generators of `C_1`. It says nothing about `n >= 4`; the induction above is what covers those, and it is not formalized.

:::

:::

::: pf-step

Therefore the formula agrees with the barycentric subdivision operator.

::: pf-proof

By definition, barycentric subdivision restricts $\sigma$ to each oriented barycentric subsimplex of its domain. By step [](#s1){.pf-ref} these restrictions are precisely $\sigma\circ\bar\Delta_\pi$ — the *descending* maps, starting at the barycentre of the whole simplex — and by step [](#s2){.pf-ref} their orientation coefficients are $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$. Hence the displayed sum, and not the ascending sum the card previously carried, is exactly $S(\sigma)$.

:::

:::

:::

:::
