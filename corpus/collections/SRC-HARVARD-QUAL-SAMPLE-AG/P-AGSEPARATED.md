---
schema: qual/card@1
id: P-AGSEPARATED
kind: problem
title: Two morphisms agreeing on a dense open, under separatedness and reducedness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Reduced Schemes
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's follow-up on dense-open uniqueness under separatedness and reducedness, including counterexamples when either hypothesis is dropped.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What can you say about separated schemes?

Let $g, h : Z \to X$ be morphisms of schemes over $Y$, via $f : X \to Y$, and suppose $g$ and $h$ agree on a dense open subset of $Z$.
What can be said if $f$ is separated?
If $Z$ is reduced?

Give examples with $Z$ nonreduced, or $f$ not separated, where $g \neq h$.
:::

::: {.solution}
<1>1. If a scheme $X$ is separated over an affine base $S$, then the intersection of any two affine open subschemes $U,V\subseteq X$ is affine.
::: {.proof}
The intersection is the inverse image of the diagonal:
\[
U\cap V
\cong
(U\times_SV)\times_{X\times_SX}X.
\]
Since $X\to S$ is separated, the diagonal
\[
\Delta_{X/S}:X\longrightarrow X\times_SX
\]
is a closed immersion.  Hence
\[
U\cap V\longrightarrow U\times_SV
\]
is a closed immersion by base change.  The scheme $U\times_SV$ is affine because $U,V,S$ are affine, and a closed subscheme of an affine scheme is affine.  Therefore $U\cap V$ is affine.

In particular every affine scheme is separated: for $X=\operatorname{Spec}A$ over $S=\operatorname{Spec}R$, the diagonal corresponds to the surjective multiplication map
\[
A\otimes_RA\longrightarrow A,
\qquad
a\otimes b\longmapsto ab,
\]
so it is a closed immersion.
:::

<1>2. Let $f:X\to Y$ be separated and let
\[
g,h:Z\longrightarrow X
\]
be $Y$-morphisms.  Their scheme-theoretic equalizer
\[
E\longrightarrow Z
\]
is a closed immersion.
::: {.proof}
The pair $(g,h)$ defines
\[
(g,h):Z\longrightarrow X\times_YX.
\]
The equalizer is the pullback
\[
E
=Z\times_{X\times_YX,\,(g,h)}X,
\]
where $X\to X\times_YX$ is the diagonal.  Separatedness makes that diagonal a closed immersion, and closed immersions are stable under base change.
:::

<1>3. If $g$ and $h$ agree on a dense open subset $U\subseteq Z$, then the underlying closed subset $|E|$ is all of $|Z|$.
::: {.proof}
The equality
\[
g|_U=h|_U
\]
means precisely that $U\to Z$ factors through the equalizer $E$.  Thus
\[
U\subseteq |E|.
\]
By <1>2, $|E|$ is closed in $|Z|$.  Since $U$ is dense,
\[
|E|=|Z|.
\]
:::

<1>4. If, in addition, $Z$ is reduced, then
\[
\boxed{g=h.}
\]
::: {.proof}
Let $\mathcal I\subseteq\mathcal O_Z$ be the ideal sheaf defining the closed immersion $E\hookrightarrow Z$.  By <1>3,
\[
V(\mathcal I)=Z,
\]
so every local section of $\mathcal I$ lies in the nilradical of $\mathcal O_Z$.  Since $Z$ is reduced, that nilradical is zero.  Hence
\[
\mathcal I=0,
\qquad
E=Z.
\]
The universal property of the equalizer now gives $g=h$.
:::

<1>5. Reducedness of $Z$ is necessary, even when the target is affine and hence separated.
::: {.proof}
Let
\[
A=k[x,\varepsilon]/(\varepsilon^2,x\varepsilon),
\qquad
Z=\operatorname{Spec}A,
\qquad
X=\mathbb A^1_k=\operatorname{Spec}k[t].
\]
The scheme $Z$ is nonreduced because $\varepsilon\ne0$ but $\varepsilon^2=0$.

Define two morphisms
\[
g,h:Z\longrightarrow X
\]
by the ring maps
\[
g^\sharp(t)=0,
\qquad
h^\sharp(t)=\varepsilon.
\]
They are distinct because $\varepsilon\ne0$ in $A$.

On the dense open
\[
D(x)\subseteq Z,
\]
the element $x$ is invertible.  The relation $x\varepsilon=0$ therefore implies
\[
\varepsilon=0\quad\text{in }A_x.
\]
Thus
\[
g|_{D(x)}=h|_{D(x)}.
\]
The open $D(x)$ is dense because the underlying topological space of $Z$ is the same as that of
\[
\operatorname{Spec}(A/(\varepsilon))\cong\mathbb A^1_k,
\]
and $D(x)$ is the complement of the single closed point $x=0$ there.

Hence two maps to the separated scheme $\mathbb A^1$ can agree on a dense open and still differ when the source is nonreduced.
:::

<1>6. Separatedness of $f$ is also necessary, even when $Z$ is reduced.
::: {.proof}
Let $X$ be the affine line with doubled origin, obtained by gluing
\[
U_1\cong\mathbb A^1_k,
\qquad
U_2\cong\mathbb A^1_k
\]
along their common open
\[
\mathbb G_m=D(t)
\]
by the identity.  Then
\[
f:X\longrightarrow\operatorname{Spec}k
\]
is not separated.

Take the reduced scheme
\[
Z=\mathbb A^1_k
\]
and let
\[
g:Z\xrightarrow{\sim}U_1\hookrightarrow X,
\qquad
h:Z\xrightarrow{\sim}U_2\hookrightarrow X
\]
be the two chart inclusions.  They agree on the dense open $\mathbb G_m$, because that is the locus on which the two copies are identified, but
\[
g(0)\ne h(0)
\]
are the two distinct origins.  Therefore $g\ne h$.
:::

<1>7. The dense-open uniqueness principle is therefore
\[
\boxed{
f\text{ separated and }Z\text{ reduced}
\quad\Longrightarrow\quad
g|_U=h|_U\text{ on dense open }U
\Longrightarrow g=h,
}
\]
and both hypotheses are essential.
::: {.proof}
The implication is <1>2--<1>4.  Step <1>5 shows failure without reducedness, and <1>6 shows failure without separatedness.
:::

<1>8. Q.E.D.
::: {.proof}
Steps <1>1--<1>7 answer each part of the question.
:::
:::
