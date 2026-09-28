---
schema: qual/card@1
id: P-BERK86S-10
kind: problem
title: Surjective ring homomorphisms from $\mathbb C^n$ to $\mathbb C$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the coordinate idempotents of C^n to force exactly one surviving
    coordinate. The restriction to that coordinate is a surjective field
    endomorphism of C, hence an automorphism; conversely every such
    automorphism composed with a coordinate projection works.
---

::: {.problem}
Give $\mathbb C^n$ coordinatewise addition and multiplication. Determine all surjective ring homomorphisms
\[
\mathbb C^n\longrightarrow\mathbb C.
\]
:::

::: {.solution}
For $1\leq j\leq n$, let
$$
e_j=(0,\ldots,0,1,0,\ldots,0)\in\CC^n
$$
be the $j$th coordinate idempotent.

<1>1. Any surjective ring homomorphism
$$
\phi:\CC^n\to\CC
$$
satisfies
$$
\phi(1,\ldots,1)=1.
$$

::: {.proof}
Surjectivity gives $x\in\CC^n$ with $\phi(x)=1$. Then
$$
\phi(1,\ldots,1)
=
\phi(1,\ldots,1)\phi(x)
=
\phi(x)
=1.
$$
Thus the conclusion holds even under a convention in which a ring
homomorphism is not assumed a priori to preserve the identity.
:::

<1>2. There is a unique index $j$ such that
$$
\phi(e_j)=1,
$$
while
$$
\phi(e_k)=0
$$
for every $k\neq j$.

::: {.proof}
Each $e_k$ is idempotent, so $\phi(e_k)$ is an idempotent of the field
$\CC$. Hence
$$
\phi(e_k)\in\{0,1\}.
$$
Moreover,
$$
e_1+\cdots+e_n=(1,\ldots,1),
$$
so step <1>1 gives
$$
\phi(e_1)+\cdots+\phi(e_n)=1.
$$
Thus at least one image equals $1$. If $j\neq k$, then
$$
e_je_k=0,
$$
so
$$
\phi(e_j)\phi(e_k)=0.
$$
Hence two distinct coordinate idempotents cannot both map to $1$.
Therefore the index is unique.
:::

<1>3. Fix the index $j$ from step <1>2 and define
$$
\iota_j:\CC\to\CC^n,
\qquad
\iota_j(z)=(0,\ldots,0,z,0,\ldots,0),
$$
and
$$
\sigma\coloneqq\phi\circ\iota_j.
$$
Then for every $(z_1,\ldots,z_n)\in\CC^n$,
$$
\phi(z_1,\ldots,z_n)=\sigma(z_j).
$$

::: {.proof}
Write
$$
(z_1,\ldots,z_n)
=
\sum_{k=1}^n\iota_k(z_k).
$$
If $k\neq j$, then
$$
\iota_k(z_k)=e_k\iota_k(z_k),
$$
so step <1>2 gives
$$
\phi(\iota_k(z_k))
=
\phi(e_k)\phi(\iota_k(z_k))
=0.
$$
Therefore only the $j$th summand survives:
$$
\phi(z_1,\ldots,z_n)
=
\phi(\iota_j(z_j))
=
\sigma(z_j).
$$
:::

<1>4. The map $\sigma:\CC\to\CC$ from step <1>3 is a field
automorphism.

::: {.proof}
The coordinate inclusion $\iota_j$ preserves addition and multiplication,
so its composite with $\phi$ does as well. Also
$$
\sigma(1)
=
\phi(e_j)
=1
$$
by step <1>2. Thus $\sigma$ is a unital ring homomorphism from the field
$\CC$ to itself. Its kernel is therefore zero, so it is injective.

By step <1>3, the image of $\phi$ equals the image of $\sigma$. Since
$\phi$ is surjective, $\sigma$ is surjective as well. Thus $\sigma$ is a
bijection preserving addition and multiplication, hence a field
automorphism of $\CC$.
:::

<1>5. Conversely, for every index $j$ and every
$\sigma\in\Aut(\CC)$, the map
$$
\phi_{\sigma,j}(z_1,\ldots,z_n)
\coloneqq
\sigma(z_j)
$$
is a surjective ring homomorphism $\CC^n\to\CC$.

::: {.proof}
The coordinate projection
$$
\pi_j:\CC^n\to\CC
$$
is a surjective ring homomorphism, and $\sigma$ is a bijective ring
homomorphism. Therefore
$$
\phi_{\sigma,j}
=
\sigma\circ\pi_j
$$
is a surjective ring homomorphism.
:::

<1>6. Hence all surjective ring homomorphisms are exactly
$$
\boxed{
(z_1,\ldots,z_n)\longmapsto\sigma(z_j),
\qquad
1\leq j\leq n,\quad
\sigma\in\Aut(\CC)
}.
$$

::: {.proof}
Steps <1>2--<1>4 show that every surjective ring homomorphism has the
displayed form, and step <1>5 shows that every map of that form works.
Such a map is $\CC$-linear exactly when $\sigma=\operatorname{id}_{\CC}$,
so the $\CC$-linear ones are the coordinate projections.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the complete classification.
:::
:::
