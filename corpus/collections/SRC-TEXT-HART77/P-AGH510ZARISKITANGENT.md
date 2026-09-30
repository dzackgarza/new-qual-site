---
schema: qual/card@1
id: P-AGH510ZARISKITANGENT
kind: problem
title: The Zariski tangent space $T_P(X) = \dualof{(\mfm/\mfm^2)}$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Tangent Spaces
  - Local Rings
  - Nonsingular Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with the retained Hartshorne I.5.10 transcription. The proof identifies tangent-space dimension with local embedding dimension, constructs functoriality by dualizing the induced map on maximal-ideal cotangent spaces, and computes the parabola projection from x mapping to y^2.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
For a point $P$ on a variety $X$, let $\mfm$ be the maximal ideal of the local ring $\mco_P$.
Define the *Zariski tangent space* $T_P(X)$ of $X$ at $P$ to be the dual $k\definedas$vector space of $\mfm/\mfm^2$.

1. For any point $P \in X$, show that $\dim T_P(X) \geq \dim X$, with equality if and only if $P$ is nonsingular.

2. For any morphism $\varphi: X \to Y$, show that there is a natural induced $k\definedas$linear map $T_P(\varphi): T_P(X) \to T_{\varphi(P)}(Y)$.

3. If $\varphi$ is the vertical projection of the parabola $x = y^2$ onto the $x\definedas$axis, show that the induced map $T_0(\varphi)$ of tangent spaces at the origin is the zero map.
:::

::: {.solution}
Let
$$
A=\OO_{X,P},\qquad \mathfrak m=\mathfrak m_P.
$$
Since $X$ is a variety over the algebraically closed field $k$, the residue field at the closed point $P$ is $k$.

::: pf

::: {.pf-step #s1}

The tangent-space dimension is the embedding dimension of the local ring:
$$
\dim_kT_P(X)=\dim_k\mathfrak m/\mathfrak m^2.
$$

::: pf-proof

This is immediate from the definition
$$
T_P(X)=(\mathfrak m/\mathfrak m^2)^\vee.
$$
The vector space $\mathfrak m/\mathfrak m^2$ is finite-dimensional because the local ring is noetherian and its maximal ideal is finitely generated.
Its dimension is the minimum number of generators of $\mathfrak m$, by Nakayama's lemma, and is called the embedding dimension of $A$.
Dual finite-dimensional vector spaces have the same dimension.

:::

:::

::: {.pf-step #s2}

For every point $P$ of the variety,
$$
\boxed{\dim T_P(X)\ge\dim X,}
$$
with equality exactly when $P$ is nonsingular.

::: pf-proof

The noetherian local ring $A$ satisfies
$$
\dim A\le\dim_k\mathfrak m/\mathfrak m^2
$$
[@Har10a, Chapter I, §5].
One way to see the inequality is to choose a minimal set of $e=\dim_k\mathfrak m/\mathfrak m^2$ generators of $\mathfrak m$.
Krull's height theorem gives
$$
\dim A=\operatorname{height}\mathfrak m\le e.
$$
For a closed point of a variety, $\dim A=\dim X$ [@Har10a, Exercise I.3.12].
Step [](#s1){.pf-ref} therefore gives the displayed inequality.

By definition, a noetherian local ring is regular precisely when
$$
\dim A=\dim_k\mathfrak m/\mathfrak m^2.
$$
For varieties, the local ring $\OO_{X,P}$ is regular exactly when $P$ is nonsingular [@Har10a, Theorem I.5.1].
Thus equality in the tangent-space inequality is equivalent to nonsingularity, proving part (1).

:::

:::

::: {.pf-step #s3}

A morphism $\varphi:X\to Y$ naturally induces a linear tangent map
$$
\boxed{T_P(\varphi):T_P(X)\longrightarrow T_{\varphi(P)}(Y).}
$$

::: pf-proof

Put $Q=\varphi(P)$ and let
$$
\mathfrak n\subseteq\OO_{Y,Q}
$$
be the maximal ideal.
The morphism induces the local homomorphism
$$
\varphi_P^*:\OO_{Y,Q}\longrightarrow\OO_{X,P}.
$$
Because it is a local homomorphism,
$$
\varphi_P^*(\mathfrak n)\subseteq\mathfrak m.
$$
Multiplicativity then gives
$$
\varphi_P^*(\mathfrak n^2)\subseteq\mathfrak m^2.
$$
Hence there is a well-defined $k$-linear map of cotangent spaces
$$
d_P^*\varphi:\mathfrak n/\mathfrak n^2
\longrightarrow
\mathfrak m/\mathfrak m^2,
\qquad
[a]\longmapsto[\varphi_P^*(a)].
$$
Dualizing reverses its direction and gives
$$
T_P(\varphi)
=(d_P^*\varphi)^\vee:
(\mathfrak m/\mathfrak m^2)^\vee
\longrightarrow
(\mathfrak n/\mathfrak n^2)^\vee.
$$
These are exactly $T_P(X)$ and $T_Q(Y)$.
The construction uses only the induced local-ring map, so it is natural and respects identities and composition.
This proves part (2).

:::

:::

::: {.pf-step #s4}

For vertical projection of the parabola $X=V(x-y^2)$ to the $x$-axis,
$$
\boxed{T_0(\varphi)=0.}
$$

::: pf-proof

The parabola has coordinate ring
$$
k[x,y]/(x-y^2)\cong k[y],
$$
and vertical projection corresponds contravariantly to
$$
k[x]\longrightarrow k[y],
\qquad
x\longmapsto y^2.
$$
At the origins, the induced map on cotangent spaces is
$$
(x)/(x^2)
\longrightarrow
(y)/(y^2).
$$
The class of its generator $x$ maps to the class of $y^2$, which is zero modulo $(y^2)$.
Thus the cotangent map is zero.
Its dual is therefore the zero map
$$
T_0(X)\longrightarrow T_0(\AA_x^1),
$$
as required.
Geometrically, the parabola has vertical tangent at the origin, so its differential under vertical projection collapses that tangent direction.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (1), step [](#s3){.pf-ref} proves part (2), and step [](#s4){.pf-ref} proves part (3).

:::

:::

:::
