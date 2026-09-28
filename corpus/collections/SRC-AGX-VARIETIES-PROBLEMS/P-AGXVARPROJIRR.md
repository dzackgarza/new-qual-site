---
schema: qual/card@1
id: P-AGXVARPROJIRR
kind: problem
title: Irreducibility of projective varieties
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Irreducibility
  - Homogeneous Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 7.4 and 7.9 together with Remark 7.5 in the
    recorded source. Definition 7.9 calls a projective variety a projective
    algebraic set defined by a homogeneous prime ideal; Remark 7.5 identifies
    the same ideal with the affine cone.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the defining homogeneous prime ideal and the conventional nonempty
    variety hypothesis explicit, so the standalone card asks for the
    topological irreducibility consequence of the source definition.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Passed to the affine cone V(P), used primality to make the cone
    irreducible, removed the vertex, and projected continuously and
    surjectively to X. Continuous images of irreducible spaces are
    irreducible.
---

::: {.problem}
Let $k$ be the algebraically closed ground field of the source, and let
$$
X=V_+(P)\subseteq\PP^n_k
$$
be a nonempty projective variety, where
$$
P\subseteq k[x_0,\ldots,x_n]
$$
is a homogeneous prime ideal. Show that $X$ is irreducible.
:::

::: {.solution}
Let
$$
\widehat X=V(P)\subseteq\AA^{n+1}_k
$$
be the affine cone over $X$.

<1>1. The affine cone $\widehat X$ is irreducible.

::: {.proof}
Its coordinate ring is
$$
k[\widehat X]
\cong
k[x_0,\ldots,x_n]/P.
$$
Since $P$ is prime, this quotient is an integral domain. An affine algebraic
set has integral-domain coordinate ring exactly when it is irreducible.
Therefore $\widehat X$ is irreducible.
:::

<1>2. The punctured cone
$$
\widehat X^\times
\coloneqq
\widehat X\sm\{0\}
$$
is a nonempty irreducible topological space.

::: {.proof}
The origin is closed in affine space, so $\widehat X^\times$ is open in
$\widehat X$. A nonempty open subset of an irreducible topological space is
irreducible.

It is nonempty because $X$ is nonempty: any projective point of $X$ has a
nonzero affine representative lying in $\widehat X$.
:::

<1>3. The projectivization map
$$
q:\widehat X^\times\longrightarrow X,
\qquad
(a_0,\ldots,a_n)
\longmapsto
[a_0:\ldots:a_n]
$$
is continuous and surjective.

::: {.proof}
Every point of $X$ has a nonzero homogeneous representative in the affine
cone, so $q$ is surjective.

To check continuity, let
$$
Y=V_+(J)\subseteq X
$$
be projectively closed, with $J$ homogeneous. Then
$$
q^{-1}(Y)
=
V(J)\intersect\widehat X^\times,
$$
which is closed in the subspace $\widehat X^\times$. Thus inverse images of
closed subsets are closed, so $q$ is continuous.
:::

<1>4. The projective variety $X$ is irreducible.

::: {.proof}
By step <1>2, $\widehat X^\times$ is irreducible. By step <1>3,
$$
X=q(\widehat X^\times)
$$
is its continuous image. A continuous image of an irreducible space is
irreducible. Hence
$$
\boxed{X\text{ is irreducible}.}
$$
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 show that $V_+(P)$ is irreducible for every homogeneous
prime $P$ with $V_+(P)\neq\varnothing$.
:::
:::
