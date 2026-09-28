---
schema: qual/card@1
id: P-AGXVARAFFINECONES
kind: problem
title: Whether isomorphic varieties have isomorphic affine cones
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Cones
  - Projective Varieties
  - Isomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the problem in the recorded Zaidenberg problem-list PDF. The source
    explicitly asks for isomorphic projective varieties with non-isomorphic
    affine cones and hints to use a Veronese embedding.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the standard and quadratic-Veronese embeddings of P1, computed
    their affine cones, and separated the cones by regularity at the vertex.
---

::: {.problem}
Do isomorphic varieties have isomorphic affine cones?
:::

::: {.solution}
<1>1. For the standard embedding
$$
\PP^1\subseteq\PP^1,
$$
the affine cone is
$$
\widehat{\PP^1}=\AA^2.
$$

::: {.proof}
The homogeneous ideal of $\PP^1$ in its own homogeneous coordinate ring
$$
\CC[s,t]
$$
is zero. By definition, the affine cone is the zero locus of the same
homogeneous ideal in $\AA^2$, hence all of $\AA^2$.
:::

<1>2. Under the quadratic Veronese embedding
$$
\nu_2:\PP^1\longrightarrow\PP^2,
\qquad
[s:t]\longmapsto[s^2:st:t^2],
$$
the image is the conic
$$
C=V(XZ-Y^2).
$$

::: {.proof}
Every image point satisfies
$$
XZ-Y^2=s^2t^2-(st)^2=0.
$$
Conversely, $\nu_2$ is the quadratic Veronese closed immersion, so it is
an isomorphism of $\PP^1$ onto its image. Since the image is an
irreducible projective curve contained in the irreducible conic
$V(XZ-Y^2)$, the two coincide.
:::

<1>3. The affine cone over the Veronese image is
$$
\widehat C
=
V(XZ-Y^2)
\subseteq
\AA^3.
$$

::: {.proof}
The conic $C\subseteq\PP^2$ is defined by the homogeneous ideal
$$
(XZ-Y^2).
$$
The affine cone is the zero locus of that same homogeneous ideal in
$\AA^3$.
:::

<1>4. The cone $\widehat C$ is singular at the origin.

::: {.proof}
Its coordinate ring is
$$
A=\CC[X,Y,Z]/(XZ-Y^2).
$$
At the origin let
$$
\mfm=(X,Y,Z)\normal A.
$$
The defining relation has degree $2$, so it gives no linear relation in
$$
\mfm/\mfm^2.
$$
Hence
$$
\dim_\CC\mfm/\mfm^2=3.
$$
On the other hand, $A$ is a hypersurface domain of dimension
$$
3-1=2.
$$
Thus the local ring $A_\mfm$ has embedding dimension $3$ and Krull
dimension $2$, so it is not regular. Therefore the vertex is singular.
:::

<1>5. The two affine cones are not isomorphic.

::: {.proof}
The affine plane $\AA^2$ is smooth, hence all of its local rings are
regular. By step <1>4, $\widehat C$ has a nonregular local ring at its
vertex. An isomorphism of varieties induces isomorphisms of local rings
and therefore preserves regularity. Consequently
$$
\AA^2\not\cong\widehat C.
$$

But both projective varieties are abstractly $\PP^1$: one is the standard
copy of $\PP^1$ and the other is its Veronese image. Hence isomorphic
projective varieties can have non-isomorphic affine cones.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 construct the affine cones of two embeddings of $\PP^1$,
and steps <1>4--<1>5 show that they are not isomorphic. The answer is
$\boxed{\text{no}}$: the affine cone depends on the projective embedding.
:::
:::
