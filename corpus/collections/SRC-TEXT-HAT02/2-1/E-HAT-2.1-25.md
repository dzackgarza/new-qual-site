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
    Certificate scope recorded after <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean>. Now formalized, with no `sorryAx`
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
    $\pi$, in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean>: `pairCount_ofFn` (a list count over `List.ofFn g` is the
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
    question: <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> now proves, in the free abelian group on ordered chains of
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
    Hatcher's operator formula, as a theorem. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> proves
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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    The exercise's formula, closed for an arbitrary singular simplex. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> proves
    `hatcher_formula_arbitrary`: for every `n = M` and every `σ : Δⁿ → X` (a continuous map out of the
    standard-simplex subtype), `lift (c ↦ ι (chainSigma σ c)) (subdiv univ) = Σ_π
    (−1)^{n(n+1)/2} sgn(π) • ι (barySigma σ π)` in degree `n` of `X.chainComplex (ModuleCat.of ℤ ℤ)`.
    The left side is the transported recursion — `subdiv` is `S λ = b_λ (S ∂λ)`, each chain is read as
    its affine map corestricted to the standard simplex (`chainAffineOn`, using `affineMap_mem`, with a
    fixed-vertex junk fallback so the map is total), composed with `σ` (`chainSigma`) and coprojected
    into the chain group (`singularChainIota`, the degree-`n` group being definitionally the coproduct
    of one copy of ℤ per singular `n`-simplex). The right side is the closed formula with the descending
    parametrisation: `chainAffineOn_chainOf_peel` proves the chain of `π` gives `Δ̄_π`
    (`barySimplexOn`), whose first vertex is the barycentre of the whole simplex (`descVertex_zero`), and
    `toSSetObjEquiv_barySigma` reads the summand back as `σ ∘ Δ̄_π`. Scope: `∂S = S∂` is **not** claimed
    (the exercise asks for the coefficient formula); nothing else is deferred. 58 printed theorems,
    exit 0 on the canonical baseline, no errors of any form, zero `sorryAx`, axioms only `propext`,
    `Classical.choice`, `Quot.sound`.
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Prior-art check on the certificate above, run through the formalization corpus API (OpenAPI
    1.1.0) under the formulations barycentric subdivision, singular_subdivision, simplicial_subdivision,
    `barycentric subBarycenter`, subdivision boundary chain, iterated subdivision, `file:Tor.lean`-style
    filters, then opened at pinned commits. What was checked and what it changes. (1) Mathlib at the
    pinned `db584cd6d46c92f209a44c0f1c829460d327499d` has no barycentric subdivision of singular
    chains and no `∂S = S∂`; the only subdivision there is the simplicial-**set** functor `SSet.sd` in
    `AlgebraicTopology/SimplicialSet/Subdivision.lean`. Verified by search of that tree, not inferred
    from a missing search hit. (2) The formula is already formalized in Lean 4 twice:
    `TauCeti/AlgebraicTopology/Singular/Subdivision/Basic.lean` at TauCeti commit 67e852853c
    (`sum_sign_boundary`, `singularSubdivisionChainMap`, `singularSubdivision`) with
    `…/Subdivision/Homotopy.lean` adding `∂P + P∂ = 1 − S`, and
    `DifferentialGeometry/External/CanonicalTopology/Topology/Homology/SingularSubdivisionBoundary.lean`
    at qinz1yang/differential-geometry commit fd2f07fba4 (`integralSingularSubdivision_boundary_simplex`,
    `integralSingularSubdivision_boundary`), both Apache-2.0. (3) Cross-prover: Isabelle
    `src/HOL/Homology/Simplices.thy` (`simplicial_subdivision`, `singular_subdivision`) and HOL Light
    `Multivariate/homology.ml` at commit 31fe213ce4 (`simplicial_subdivision` l.1716,
    `singular_subdivision` l.2031, `CHAIN_BOUNDARY_SIMPLICIAL_SUBDIVISION` l.1797,
    `CHAIN_BOUNDARY_SINGULAR_SUBDIVISION` l.2293, `CHAIN_HOMOTOPIC_SINGULAR_SUBDIVISION` l.2598), the
    last with hypotheses checked at the source: `singular_chain (p,s) c ⟹
    chain_boundary p (singular_subdivision p c) = singular_subdivision (p-1) (chain_boundary p c)`.
    Consequence recorded rather than silently absorbed: <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> is an
    independent re-derivation in an explicit coefficient model, not the first formalization of this
    formula, and the card's notes and proofs/README.md §7a now say so. The decision not to develop
    `∂S = S∂` locally is corroborated by this lookup — that identity is proved in Lean 4 in both
    projects above and in HOL Light and Isabelle — but no claim in this card rests on the upstream
    proofs: the certificate here is separate and its scope is unchanged. Not checked in this pass:
    the facebookresearch/atlas-lean `AlgebraicTopologyI` files, which the corpus lists and which were
    located but not opened.
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
which is the displayed factor. The pair counts, the inversion/noninversion partition and $\operatorname{sgn}(\pi)=(-1)^{\operatorname{inv}(\pi)}$ are proved in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySign.lean> (`card_pairSet`, `noninv_add_inv`, `sign_eq_neg_one_pow_inv`). Everything else in this step, and the formula itself, is machine-checked for every $n$ in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean>. There, $S\lambda=b_\lambda(S\partial\lambda)$ is modelled in the free abelian group on ordered chains of faces with **every** coefficient computed (`coeff_subdiv`); the deletion positions are exactly the recursion's signs (`stepSign`, `coeff_subdiv_chainOf`); they aggregate to a pair count (`stepExp_eq_pairCount`) which reindexes to the permutation-indexed sum `pairCount_peel_eq_delSum`, giving the coefficient $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$ at every $\pi$ (`coeff_subdiv_peel_sign`); and the support of the recursion is exhausted and nonduplicated (`chainCoeff_exists_chainOf`, `chainOf_injective`), so the recursion **equals** the signed sum with one summand per permutation and nothing else (`subdiv_univ_eq_sum_perm`). Geometrically, the chain of $\pi$ is the list of prefix faces (`chainOf_peel_eq_ofFn_descFace`), each face read as its barycentre gives the descending vertex list (`map_baryWeight_chainOf_peel`), and the affine simplex those vertices span is continuous and has exactly them as vertices (`affineMap_mem`, `affineMap_single`, `continuous_affineMap`), with the prepended apex entering through its own barycentric coordinate (`affineMap_cons_apply`). The resulting theorem is `hatcher_formula_arbitrary`: for an **arbitrary** singular simplex $\sigma:\Delta^n\to X$, the recursion — corestricted to the standard simplex (`chainAffineOn`), composed with $\sigma$ (`chainSigma`) and coprojected into degree $n$ of the singular chain complex — equals the displayed signed sum, each summand read back as $\sigma\circ\bar\Delta_\pi$ (`barySigma`, `toSSetObjEquiv_barySigma`). The only thing not claimed is that $S$ is a chain map, $\partial S=S\partial$: the exercise asks for the formula.

:::

:::

::: pf-step

Chain-level regression

::: pf-proof

The general argument is an induction on `n` whose bookkeeping is a stated combinatorial identity; that identity, and with it the formula, is proved for every `n` in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> as the previous step records, and the regression below is a bounded cross-check of the resulting chains. Write `S(lambda) = b_lambda(S partial lambda)` with `partial lambda = sum_k (-1)^k partial_k lambda`. By induction the closed form is known on each `(n-1)`-simplex `partial_k lambda`, with global sign `(-1)^{(n-1)n/2}`; coning with `b_lambda` prepends the apex and keeps the coefficient of the corresponding permutation, while the factor `(-1)^k` from the boundary and the fact that coning reverses the effective vertex order contribute exactly `(-1)^n` per summand, i.e. an extra `(-1)^n` overall. Since `(n-1)n/2 + n = n(n+1)/2`, the two global signs multiply to `(-1)^{n(n+1)/2}`, which is the stated factor. Equivalently, and this is the form proved outright: along the descending chain indexed by $\pi$, the sum of the deletion positions equals the number of noninversions of $\pi$, namely $n(n+1)/2-\operatorname{inv}(\pi)$, so the recursion's sign `(-1)^{\text{sum}}` equals $(-1)^{n(n+1)/2}\operatorname{sgn}(\pi)$ because $\operatorname{sgn}(\pi)=(-1)^{\operatorname{inv}(\pi)}$. That is `stepExp_eq_pairCount` together with `pairCount_peel_eq_delSum` and `pow_delSum_eq_global_mul_sign`, and it gives the coefficient of every summand (`coeff_subdiv_peel_sign`); the whole identity follows from the exhaustion and nonduplication of the support (`chainCoeff_exists_chainOf`, `chainOf_injective`, `subdiv_univ_eq_sum_perm`). The same induction shows the *ascending* formula cannot be right: coning prepends the apex, so the sub-simplices begin at `b_{Delta^n}` and their vertex lists descend.

`proofs/cards/bary_regression.py` is a **bounded regression**, not a proof of the identity: it computes for `n = 1, 2, 3` only, in the free abelian group on vertex tuples, both the recursive operator and the two closed formulas, and confirms the identity there as well as refuting the old ascending formula — in dimension `1`, `S[v_0,v_1] = [b,v_1] - [b,v_0]`, whose summands are `[b,v_1]` and `[b,v_0]`, whereas the ascending formula gives `[v_0,b] - [v_1,b]`, different generators of `C_1`. It says nothing about `n >= 4`; those are covered by the induction above, which the Lean development proves for all $n$.

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
