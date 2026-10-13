---
schema: qual/card@1
id: PR-SHFPUSHEX
kind: proposition
title: Exactness of pushforward, and pullback to a point
slogan: 'Pushforward is left exact, closed-embedding pushforward is exact, and pulling a sheaf back to a point gives its stalk.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Direct Image Functor
  - Inverse Image Functor
  - Exact Sequences
relations:
- kind: uses
  target: PR-C9ZEK
review: draft
prompts:
- Show that pushforward is left exact, and exact along a closed embedding.
- For $i \colon \{x\} \hookrightarrow X$, show that $i^{-1} \mathcal{F} \cong \mathcal{F}_x$.
---

::: {.proposition}
Let $f \colon X \to Y$ be continuous and $0 \to \mcf' \to \mcf \to \mcf''$ an exact sequence of sheaves of abelian groups on $X$.

1. $0 \to f_* \mcf' \to f_* \mcf \to f_* \mcf''$ is exact.

2. If $f$ is a homeomorphism onto a closed subset of $Y$, then $f_*$ is exact.

3. For $i \colon \{x\} \hookrightarrow X$ the inclusion of a point, the sheaf $i^{-1}\mcf$ on the one-point space $\{x\}$ corresponds to the abelian group $\mcf_x$.
:::

::: {.proof}
For every open $V\subseteq Y$,
$$
(f_*\mcf)(V)=\mcf(f^{-1}V).
$$
The section functor on any open set is left exact, so
$$
0\to(f_*\mcf')(V)\to(f_*\mcf)(V)\to(f_*\mcf'')(V)
$$
is exact. This proves part 1.

For part 2, identify $X$ with a closed subspace of $Y$. Exactness of sheaves may be checked on stalks. If $y\in X$, then
$$
(f_*\mcf)_y\cong\mcf_y;
$$
if $y\notin X$, the open complement $Y\sm X$ contains $y$, so $(f_*\mcf)_y=0$. Thus applying $f_*$ to a short exact sequence is exact on every stalk.

For part 3, the unique stalk of $i^{-1}\mcf$ is
$$
\colim_{U\ni x}\mcf(U)=\mcf_x,
$$
which is the definition of the stalk.
:::

::: {.remark}
The closed-image hypothesis in part 2 is essential. For the open immersion $j\colon\CC^\times\hookrightarrow\CC$, the exponential sequence
$$
0\to2\pi i\ZZ\to\OO\xrightarrow{\exp}\OO^\times\to0
$$
on $\CC^\times$ is exact, but
$$
j_*\OO\longrightarrow j_*\OO^\times
$$
is not surjective on the stalk at $0$: the invertible function $z$ on a punctured disc has no holomorphic logarithm there.
:::
