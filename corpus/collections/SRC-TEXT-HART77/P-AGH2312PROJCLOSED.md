---
schema: qual/card@1
id: P-AGH2312PROJCLOSED
kind: problem
title: Closed subschemes of Proj from surjections of graded rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proj
  - Closed Subschemes
  - Graded Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.12 statement and the Proj morphism construction of II.2.14.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
a. Let $\phi: S \to T$ be a surjective homomorphism of graded rings, preserving degrees.
Show that the open set $U$ of Hartshorne II.2.14 is equal to $\Proj T$, and that the morphism $f: \Proj T \to \Proj S$ is a closed immersion.

b. If $I \subseteq S$ is a homogeneous ideal, take $T = S/I$ and let $Y$ be the closed subscheme of $X = \Proj S$ defined as the image of the closed immersion $\Proj S/I \to X$.
Show that different homogeneous ideals can give rise to the same closed subscheme.
For example, let $d_0$ be an integer and let $I' = \bigoplus_{d \geq d_0} I_d$.
Show that $I$ and $I'$ determine the same closed subscheme.
:::

::: {.remark}
Hartshorne II.5.16 shows that every closed subscheme of $X$ comes from a homogeneous ideal $I$ of $S$, at least when $S$ is a polynomial ring over $S_0$.
:::

::: {.solution}
<1>1. If
\[
\phi:S\twoheadrightarrow T
\]
is a surjective degree-preserving homomorphism, then
\[
\phi(S_+)=T_+.
\]
::: {.proof}
For every $d>0$, surjectivity as a graded homomorphism means
\[
\phi(S_d)=T_d.
\]
Taking the direct sum over positive degrees gives
\[
\phi(S_+)=\bigoplus_{d>0}T_d=T_+.
\]
:::

<1>2. The open set
\[
U=\{\mathfrak p\in\Proj T:\mathfrak p\not\supseteq\phi(S_+)\}
\]
from Hartshorne II.2.14 is all of $\Proj T$.
::: {.proof}
By <1>1,
\[
\phi(S_+)=T_+.
\]
By definition, a point of $\Proj T$ is a homogeneous prime ideal which does not contain $T_+$.  Hence every point belongs to $U$.
:::

<1>3. For every homogeneous $s\in S_+$, the induced ring map
\[
S_{(s)}\longrightarrow T_{(\phi(s))}
\]
is surjective.
::: {.proof}
Localizing the surjection $S\twoheadrightarrow T$ at the powers of $s$ gives a surjection of graded rings
\[
S_s\twoheadrightarrow T_{\phi(s)}.
\]
If a degree-zero element of the target is represented by
\[
\frac{t}{\phi(s)^n},
\qquad
\deg t=n\deg s,
\]
choose a homogeneous lift $u\in S_{n\deg s}$ of $t$.  Then
\[
\frac{u}{s^n}\in S_{(s)}
\]
maps to the given element.  Thus the degree-zero map is surjective.
:::

<1>4. On the standard affine chart $D_+(s)\subseteq\Proj S$, the morphism
\[
f:\Proj T\longrightarrow\Proj S
\]
restricts to the closed immersion
\[
D_+(\phi(s))
=
\Spec T_{(\phi(s))}
\longrightarrow
\Spec S_{(s)}
=
D_+(s).
\]
::: {.proof}
Hartshorne II.2.14 constructs the restriction from the homomorphism
\[
S_{(s)}\longrightarrow T_{(\phi(s))}.
\]
This homomorphism is surjective by <1>3.  A surjective ring homomorphism induces a closed immersion of affine spectra.
:::

<1>5. The morphism
\[
\boxed{f:\Proj T\longrightarrow\Proj S}
\]
is a closed immersion.
::: {.proof}
The standard opens $D_+(s)$ for homogeneous $s\in S_+$ cover $\Proj S$.  By <1>4, the inverse image over every such member is a closed subscheme and the restricted morphism is a closed immersion.

Being a closed immersion is local on the target.  Hence $f$ is a closed immersion globally.
:::

<1>6. Now let $I\subseteq S$ be homogeneous and put
\[
I'=\bigoplus_{d\ge d_0}I_d.
\]
Then $I'\subseteq I$ is a homogeneous ideal, and the quotient map induces a graded surjection
\[
S/I'\twoheadrightarrow S/I.
\]
::: {.proof}
Because the grading is nonnegative, multiplying an element of $I_d$ with $d\ge d_0$ by a homogeneous element of nonnegative degree stays in a component of degree at least $d_0$.  Thus $I'$ is an ideal, and it is homogeneous by construction.

The inclusion $I'\subseteq I$ gives the displayed quotient homomorphism.
:::

<1>7. For every $d\ge d_0$, the degree-$d$ component map
\[
(S/I')_d\longrightarrow(S/I)_d
\]
is an isomorphism.
::: {.proof}
For $d\ge d_0$,
\[
I'_d=I_d.
\]
Therefore
\[
(S/I')_d=S_d/I'_d=S_d/I_d=(S/I)_d.
\]
:::

<1>8. The morphism
\[
\Proj(S/I)\longrightarrow\Proj(S/I')
\]
induced by <1>6 is an isomorphism.
::: {.proof}
By <1>7, the graded homomorphism
\[
S/I'\longrightarrow S/I
\]
is an isomorphism in every sufficiently large degree.  Hartshorne II.2.14(c) states that such a graded map induces an isomorphism on $\Proj$.
:::

<1>9. The homogeneous ideals $I$ and $I'$ define the same closed subscheme of
\[
X=\Proj S.
\]
::: {.proof}
The maps to $X$ fit into
\[
\Proj(S/I)
\longrightarrow
\Proj(S/I')
\longrightarrow
\Proj S,
\]
and the first arrow is an isomorphism by <1>8.  Both composites are induced by the same quotient map from $S$, so this isomorphism identifies the two closed immersions over $X$.  Therefore their scheme-theoretic images in $X$ are the same closed subscheme.
:::

<1>10. Thus homogeneous ideals are not determined by the closed subschemes they define on $\Proj S$.
::: {.proof}
Whenever $I$ has a nonzero component in some degree below $d_0$, one has
\[
I'\ne I,
\]
while <1>9 shows that the associated closed subschemes are identical.
:::

<1>11. Q.E.D.
::: {.proof}
Steps <1>1--<1>5 prove part (a), and steps <1>6--<1>10 prove part (b).
:::
:::
