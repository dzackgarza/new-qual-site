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

::: pf

::: {.pf-step #phi-splus-equals-tplus}
If
\[
\phi:S\twoheadrightarrow T
\]
is a surjective degree-preserving homomorphism, then
\[
\phi(S_+)=T_+.
\]

::: pf-proof
For every $d>0$, surjectivity as a graded homomorphism means
\[
\phi(S_d)=T_d.
\]
Taking the direct sum over positive degrees gives
\[
\phi(S_+)=\bigoplus_{d>0}T_d=T_+.
\]
:::

:::

::: {.pf-step #u-equals-projt}
The open set
\[
U=\{\mathfrak p\in\Proj T:\mathfrak p\not\supseteq\phi(S_+)\}
\]
from Hartshorne II.2.14 is all of $\Proj T$.

::: pf-proof
By step [](#phi-splus-equals-tplus){.pf-ref},
\[
\phi(S_+)=T_+.
\]
By definition, a point of $\Proj T$ is a homogeneous prime ideal which does not contain $T_+$.  Hence every point belongs to $U$.
:::

:::

::: {.pf-step #local-map-surjective}
For every homogeneous $s\in S_+$, the induced ring map
\[
S_{(s)}\longrightarrow T_{(\phi(s))}
\]
is surjective.

::: pf-proof
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

:::

::: {.pf-step #restriction-is-closed-immersion}
On the standard affine chart $D_+(s)\subseteq\Proj S$, the morphism
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

::: pf-proof
Hartshorne II.2.14 constructs the restriction from the homomorphism
\[
S_{(s)}\longrightarrow T_{(\phi(s))}.
\]
This homomorphism is surjective by step [](#local-map-surjective){.pf-ref}.  A surjective ring homomorphism induces a closed immersion of affine spectra.
:::

:::

::: {.pf-step #f-is-closed-immersion}
The morphism
\[
\boxed{f:\Proj T\longrightarrow\Proj S}
\]
is a closed immersion.

::: pf-proof
The standard opens $D_+(s)$ for homogeneous $s\in S_+$ cover $\Proj S$.  By step [](#restriction-is-closed-immersion){.pf-ref}, the inverse image over every such member is a closed subscheme and the restricted morphism is a closed immersion.

Being a closed immersion is local on the target.  Hence $f$ is a closed immersion globally.
:::

:::

::: {.pf-step #iprime-subset-i-quotient-surjection}
Now let $I\subseteq S$ be homogeneous and put
\[
I'=\bigoplus_{d\ge d_0}I_d.
\]
Then $I'\subseteq I$ is a homogeneous ideal, and the quotient map induces a graded surjection
\[
S/I'\twoheadrightarrow S/I.
\]

::: pf-proof
Because the grading is nonnegative, multiplying an element of $I_d$ with $d\ge d_0$ by a homogeneous element of nonnegative degree stays in a component of degree at least $d_0$.  Thus $I'$ is an ideal, and it is homogeneous by construction.

The inclusion $I'\subseteq I$ gives the displayed quotient homomorphism.
:::

:::

::: {.pf-step #degree-d-iso-for-d-geq-d0}
For every $d\ge d_0$, the degree-$d$ component map
\[
(S/I')_d\longrightarrow(S/I)_d
\]
is an isomorphism.

::: pf-proof
For $d\ge d_0$,
\[
I'_d=I_d.
\]
Therefore
\[
(S/I')_d=S_d/I'_d=S_d/I_d=(S/I)_d.
\]
:::

:::

::: {.pf-step #proj-si-iso-proj-siprime}
The morphism
\[
\Proj(S/I)\longrightarrow\Proj(S/I')
\]
induced by step [](#iprime-subset-i-quotient-surjection){.pf-ref} is an isomorphism.

::: pf-proof
By step [](#degree-d-iso-for-d-geq-d0){.pf-ref}, the graded homomorphism
\[
S/I'\longrightarrow S/I
\]
is an isomorphism in every sufficiently large degree.  Hartshorne II.2.14(c) states that such a graded map induces an isomorphism on $\Proj$.
:::

:::

::: {.pf-step #i-and-iprime-same-subscheme}
The homogeneous ideals $I$ and $I'$ define the same closed subscheme of
\[
X=\Proj S.
\]

::: pf-proof
The maps to $X$ fit into
\[
\Proj(S/I)
\longrightarrow
\Proj(S/I')
\longrightarrow
\Proj S,
\]
and the first arrow is an isomorphism by step [](#proj-si-iso-proj-siprime){.pf-ref}.  Both composites are induced by the same quotient map from $S$, so this isomorphism identifies the two closed immersions over $X$.  Therefore their scheme-theoretic images in $X$ are the same closed subscheme.
:::

:::

::: {.pf-step #ideals-not-determined-by-subscheme}
Thus homogeneous ideals are not determined by the closed subschemes they define on $\Proj S$.

::: pf-proof
Whenever $I$ has a nonzero component in some degree below $d_0$, one has
\[
I'\ne I,
\]
while step [](#i-and-iprime-same-subscheme){.pf-ref} shows that the associated closed subschemes are identical.
:::

:::

::: pf-qed
Steps [](#phi-splus-equals-tplus){.pf-ref}, [](#u-equals-projt){.pf-ref}, [](#local-map-surjective){.pf-ref}, [](#restriction-is-closed-immersion){.pf-ref} and [](#f-is-closed-immersion){.pf-ref} prove part (a), and steps [](#iprime-subset-i-quotient-surjection){.pf-ref}, [](#degree-d-iso-for-d-geq-d0){.pf-ref}, [](#proj-si-iso-proj-siprime){.pf-ref}, [](#i-and-iprime-same-subscheme){.pf-ref} and [](#ideals-not-determined-by-subscheme){.pf-ref} prove part (b).
:::

:::

:::
