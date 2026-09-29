---
schema: qual/card@1
id: P-BKF99-1
kind: problem
title: Dimension lower bound for the inverse image of a subspace
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Applied rank-nullity to the restricted map from the inverse image of X
    onto X intersect im T, then used the dimension formula for two subspaces
    of W.
---

::: {.problem}
Let $V,W$ be finite-dimensional vector spaces, let $X\subseteq W$ be a subspace, and let $T:V\to W$ be linear. Prove that
\[
\dim T^{-1}(X)\ge \dim V-\dim W+\dim X.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #restricted-map-image-kernel}
The restriction of $T$ to $T^{-1}(X)$ has image
$X\cap\operatorname{im}T$ and kernel $\ker T$.

::: pf-proof
If $v\in T^{-1}(X)$, then $T(v)\in X$ and, by definition, $T(v)$ lies in
$\operatorname{im}T$. Thus the image of the restriction is contained in
$X\cap\operatorname{im}T$. Conversely, if
$w\in X\cap\operatorname{im}T$, then $w=T(v)$ for some $v\in V$, and
$w\in X$ implies $v\in T^{-1}(X)$. Hence $w$ lies in the image of the
restriction. Its kernel consists exactly of those $v$ with $T(v)=0$, namely
$\ker T$.
:::

:::

::: {.pf-step #rank-nullity-identity}
$$
\dim T^{-1}(X)
=
\dim\ker T+\dim(X\cap\operatorname{im}T).
$$

::: pf-proof
Apply the rank-nullity theorem to the restricted map described in step [](#restricted-map-image-kernel){.pf-ref}.
:::

:::

::: {.pf-step #dimension-formula-inequality}
$$
\dim(X\cap\operatorname{im}T)
\geq
\dim X+\dim\operatorname{im}T-\dim W.
$$

::: pf-proof
The dimension formula for the subspaces $X$ and $\operatorname{im}T$ gives
$$
\dim(X\cap\operatorname{im}T)
=
\dim X+\dim\operatorname{im}T
-\dim(X+\operatorname{im}T).
$$
Since $X+\operatorname{im}T\subseteq W$,
$$
\dim(X+\operatorname{im}T)\leq\dim W,
$$
which yields the claimed inequality.
:::

:::

::: {.pf-step #dimension-lower-bound}
$$
\dim T^{-1}(X)
\geq
\dim V-\dim W+\dim X.
$$

::: pf-proof
Combining steps [](#rank-nullity-identity){.pf-ref} and [](#dimension-formula-inequality){.pf-ref} gives
$$
\dim T^{-1}(X)
\geq
\dim\ker T+\dim X+\dim\operatorname{im}T-\dim W.
$$
By rank-nullity for $T:V\to W$,
$$
\dim\ker T+\dim\operatorname{im}T=\dim V.
$$
Substitution proves the desired inequality.
:::

:::

::: pf-qed
Step [](#dimension-lower-bound){.pf-ref} is the required conclusion.
:::

:::

:::
