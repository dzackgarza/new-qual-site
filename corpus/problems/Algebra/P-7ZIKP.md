---
schema: qual/card@1
id: P-7ZIKP
kind: problem
title: Maximal ideals in a countable product of copies of a commutative ring
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Give examples of maximal ideals in $K = R \times R \times R \times \cdots$, the product of countably many copies of R. What about for a product of countably many copies of an arbitrary commutative ring $R$?
:::


::: {.solution}
Assume throughout that $R$ is a nonzero commutative ring with identity, and put
\[
K=\prod_{i\in\NN}R.
\]

<1>1. Every maximal ideal $\mathfrak m\subset R$ and every coordinate $j\in\NN$ give a maximal ideal
\[
M_{j,\mathfrak m}=\{(a_i)\in K:a_j\in\mathfrak m\}.
\]
::: {.proof}
Let
\[
\pi_j:K\to R\to R/\mathfrak m
\]
be projection to the $j$th coordinate followed by the quotient map. This is a surjective ring homomorphism and
\[
\ker \pi_j=M_{j,\mathfrak m}.
\]
Since $R/\mathfrak m$ is a field, the first isomorphism theorem gives
\[
K/M_{j,\mathfrak m}\cong R/\mathfrak m,
\]
so $M_{j,\mathfrak m}$ is maximal.
:::

<1>2. More generally, let $\mathcal U$ be an ultrafilter on $\NN$ and let $\mathfrak m$ be a maximal ideal of $R$. Then
\[
M_{\mathcal U,\mathfrak m}
=
\left\{(a_i)\in K:\{i:a_i\in\mathfrak m\}\in\mathcal U\right\}
\]
is a maximal ideal of $K$.
::: {.proof}
Let $k=R/\mathfrak m$, a field. Coordinatewise reduction modulo $\mathfrak m$ gives a surjective homomorphism
\[
K\longrightarrow k^{\NN}.
\]
Compose this with the quotient map to the ultraproduct
\[
k^{\NN}\longrightarrow k^{\NN}/\mathcal U.
\]
The ultraproduct of fields is again a field: if the class of $(x_i)$ is nonzero, then
\[
S=\{i:x_i\ne0\}\in\mathcal U,
\]
and defining $y_i=x_i^{-1}$ on $S$ and arbitrarily off $S$ gives $(x_i)(y_i)=1$ modulo $\mathcal U$.

The kernel of the composite consists exactly of those $(a_i)$ for which
\[
\{i:a_i\bmod\mathfrak m=0\}
=
\{i:a_i\in\mathfrak m\}
\]
belongs to $\mathcal U$. Hence its kernel is $M_{\mathcal U,\mathfrak m}$, and the quotient is a field. Therefore $M_{\mathcal U,\mathfrak m}$ is maximal.
:::

<1>3. The coordinate examples are the principal-ultrafilter cases, while nonprincipal ultrafilters give genuinely non-coordinate maximal ideals.
::: {.proof}
If $\mathcal U$ is the principal ultrafilter at $j$, then
\[
S\in\mathcal U\iff j\in S,
\]
so
\[
M_{\mathcal U,\mathfrak m}=M_{j,\mathfrak m}.
\]
If $\mathcal U$ is nonprincipal, then no singleton belongs to $\mathcal U$, so membership in $M_{\mathcal U,\mathfrak m}$ cannot be determined by a single coordinate. Thus infinite direct products have maximal ideals beyond the obvious coordinate kernels.
:::

Hence, for an arbitrary commutative ring $R$, every maximal ideal of $R$ and every ultrafilter on the index set produce a maximal ideal in the countable product. These give the standard coordinate examples and, when nonprincipal ultrafilters are available, non-coordinate examples as well.
:::
