---
schema: qual/card@1
id: P-AGSEPPROP
kind: problem
title: A good property of separated morphisms, and its quasi-separated analogue
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Quasi-separated Morphisms
  - Quasicompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; Ogus follows this question by asking about two morphisms agreeing on a dense open subset.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Name a good property of separated morphisms.

What would be the analogue for quasiseparated in place of separated?
:::

::: {.solution}
Let
\[
f:X\longrightarrow Y
\]
be a morphism, let $Z$ be a $Y$-scheme, and let
\[
g,h:Z\longrightarrow X
\]
be $Y$-morphisms.

<1>1. The scheme-theoretic equalizer of $g$ and $h$ is the pullback of the diagonal:
\[
\begin{array}{ccc}
E&\longrightarrow&X\\
\downarrow&&\downarrow{\scriptstyle\Delta_{X/Y}}\\
Z&\xrightarrow{(g,h)}&X\times_YX.
\end{array}
\]
::: {.proof}
By the universal property of the fibre product, a morphism $T\to Z$ factors through $E$ exactly when the two composites
\[
T\longrightarrow Z\overset{g,h}{\rightrightarrows}X
\]
are equal.  Thus $E$ represents the equalizer of $g$ and $h$.
:::

<1>2. If $f$ is separated, then $E\to Z$ is a closed immersion.
::: {.proof}
Separatedness means that
\[
\Delta_{X/Y}:X\longrightarrow X\times_YX
\]
is a closed immersion.  Closed immersions are preserved by base change, so the pullback $E\to Z$ in <1>1 is a closed immersion.
:::

<1>3. Consequently, if $f$ is separated, $Z$ is reduced, and $g$ and $h$ agree on a dense open subset
\[
U\subseteq Z,
\]
then
\[
\boxed{g=h.}
\]
::: {.proof}
Since $g|_U=h|_U$, the inclusion
\[
U\hookrightarrow Z
\]
factors through the equalizer $E$.  Thus the underlying closed subset $|E|\subseteq|Z|$ contains the dense subset $U$.  By <1>2, $|E|$ is closed, so
\[
|E|=|Z|.
\]

Let $\mathcal I\subseteq\mathcal O_Z$ be the ideal sheaf defining the closed immersion $E\hookrightarrow Z$.  The equality of underlying spaces says
\[
V(\mathcal I)=Z,
\]
so every local section of $\mathcal I$ is nilpotent.  Because $Z$ is reduced, its nilradical is zero, hence
\[
\mathcal I=0.
\]
Therefore $E=Z$, and by the equalizer property in <1>1, $g=h$.
:::

<1>4. If $f$ is only quasi-separated, the corresponding conclusion is that the equalizer
\[
E\longrightarrow Z
\]
is a quasicompact immersion.
::: {.proof}
For every morphism of schemes the diagonal is an immersion.  Quasi-separatedness of $f$ means, by definition, that
\[
\Delta_{X/Y}
\]
is quasicompact.  Both properties are preserved by base change, so the equalizer morphism in <1>1 is a quasicompact immersion.

Equivalently, the agreement locus is retrocompact in $Z$: its intersection with every quasicompact open subset of $Z$ is quasicompact.
:::

<1>5. Quasi-separatedness does not imply the uniqueness statement in <1>3.
::: {.proof}
Let $X$ be the affine line with doubled origin: glue two copies
\[
U_1\cong\mathbb A^1_k,
\qquad
U_2\cong\mathbb A^1_k
\]
along
\[
D(t)=\mathbb G_{m,k}
\]
by the identity.  The morphism
\[
X\longrightarrow\operatorname{Spec}k
\]
is quasi-separated, because the intersection of the two affine opens $U_1$ and $U_2$ is the affine, hence quasicompact, open $\mathbb G_m$.

Let
\[
Z=\mathbb A^1_k
\]
and let
\[
g:Z\xrightarrow{\sim}U_1\hookrightarrow X,
\qquad
h:Z\xrightarrow{\sim}U_2\hookrightarrow X
\]
be the two chart inclusions.  They agree on the dense open
\[
\mathbb G_m\subseteq\mathbb A^1,
\]
because that is precisely the open along which the two copies were glued, but they send $0$ to the two distinct origins.  Hence
\[
g\ne h.
\]

Their equalizer is exactly $\mathbb G_m\hookrightarrow\mathbb A^1$, which is quasicompact but not closed.  This is the quasi-separated analogue from <1>4 in its sharp form.
:::

<1>6. Thus a useful separatedness principle is:
\[
\boxed{
\begin{gathered}
f\text{ separated},\ Z\text{ reduced},\
g|_U=h|_U\text{ on a dense open }U
\\
\Longrightarrow g=h,
\end{gathered}
}
\]
whereas replacing separated by quasi-separated only makes the equalizer quasicompact; it does not force equality.
::: {.proof}
This is exactly the combination of <1>3--<1>5.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>3 gives the good property of separated morphisms, and steps <1>4--<1>5 give the quasi-separated analogue and its limitation.
:::
:::
