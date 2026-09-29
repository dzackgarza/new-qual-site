---
schema: qual/card@1
id: P-AGH48CARDINALITY
kind: problem
title: A variety of positive dimension has the cardinality of $k$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Birational Geometry
  - Zariski Topology
relations:
- kind: uses
  target: T-MORFIBDIM
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts and the projection hint with Hartshorne I.4.8. To preserve source order without depending on the still-unsolved I.4.9, the proof uses the equivalent affine Noether-normalization theorem already recorded in T-MORFIBDIM; published solutions also use this route.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked both cardinal inequalities and the cofinite-topology argument against independent solutions. The lower bound uses surjectivity of the finite dominant Noether-normalization morphism; the upper bound uses a quasi-projective embedding.'
---

::: {.problem}
(a) Show that any variety of positive dimension over $k$ has the same cardinality as $k$.

(b) Deduce that any two curves over $k$ are homeomorphic.
:::

::: {.hint}
Treat $\AA^n$ and $\PP^n$ first.
Then for any $X$, use induction on the dimension $n$: make $X$ birational to a hypersurface $H \subseteq \PP^{n+1}$, and show that the projection of $H$ to $\PP^n$ from a point not on $H$ is finite-to-one and surjective.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every integer $n\ge1$,
$$
\abs{\AA^n}=\abs{\PP^n}=\abs{k}.
$$

::: pf-proof

The algebraically closed field $k$ is infinite.
For every finite $n\ge1$, finite Cartesian powers of an infinite set have the same cardinality as the set itself, so
$$
\abs{\AA^n}=\abs{k^n}=\abs{k}.
$$

Projective space is the finite disjoint union of its standard affine strata
$$
\PP^n
=
\AA^n\sqcup\AA^{n-1}\sqcup\cdots\sqcup\AA^0.
$$
Thus
$$
\abs{\PP^n}=\abs{k}
$$
as well.

:::

:::

::: {.pf-step #s2}

Let $X$ be a variety of dimension $d\ge1$. Then
$$
\abs{X}\le\abs{k}.
$$

::: pf-proof

By definition, $X$ is quasi-projective, so it is a locally closed subset of some projective space $\PP^N$.
Hence
$$
\abs{X}\le\abs{\PP^N}=\abs{k}
$$
by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

The same variety satisfies
$$
\abs{X}\ge\abs{k}.
$$

::: pf-proof

Choose a nonempty affine open subset $U\subseteq X$.
Because $X$ is irreducible, every nonempty open subset has the same function field and hence the same dimension, so
$$
\dim U=d.
$$

By the affine Noether-normalization theorem in [[T-MORFIBDIM]], there is a finite morphism
$$
\pi:U\to\AA^d
$$
induced by an inclusion
$$
k[t_1,\ldots,t_d]\hookrightarrow A(U).
$$
The inclusion makes $\pi$ dominant.
A finite morphism is closed, so its image is both dense and closed in $\AA^d$; hence
$$
\pi(U)=\AA^d.
$$
Thus there is a surjection of underlying sets
$$
U\twoheadrightarrow\AA^d.
$$
Therefore
$$
\abs{X}\ge\abs{U}\ge\abs{\AA^d}=\abs{k}.
$$

:::

:::

::: {.pf-step #s4}

Every positive-dimensional variety has cardinality
$$
\boxed{\abs{X}=\abs{k}}.
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.
This proves (a).

:::

:::

::: {.pf-step #s5}

Every curve over $k$ has the cofinite topology on its set of closed points.

::: pf-proof

Let $C$ be a curve and let $Z\subsetneq C$ be closed.
Write $Z$ as the finite union of its irreducible components; this is possible because varieties are Noetherian.
Every irreducible component of $Z$ is a proper irreducible closed subset of the one-dimensional irreducible variety $C$, so it has dimension zero.
An irreducible zero-dimensional variety is a single point.
Thus every proper closed subset of $C$ is finite.

Conversely, every point is closed over the algebraically closed field $k$, so every finite subset is closed.
Hence the closed subsets of $C$ are exactly $C$ and the finite subsets.

:::

:::

::: {.pf-step #s6}

Any two curves over $k$ are homeomorphic.

::: pf-proof

Let $C$ and $D$ be curves.
By part (a),
$$
\abs{C}=\abs{k}=\abs{D},
$$
so choose a bijection
$$
b:C\to D.
$$
By step [](#s5){.pf-ref}, both spaces carry the cofinite topology.
A bijection carries finite sets to finite sets, so both $b$ and $b^{-1}$ preserve closed sets.
Therefore $b$ is a homeomorphism.
This proves (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (a), and steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove (b).

:::

:::

:::
