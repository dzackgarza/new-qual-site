---
schema: qual/card@1
id: P-AGSEPPROP
kind: problem
title: Equalizers of morphisms to separated and quasi-separated targets
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

::: pf

::: {.pf-step #equalizer-pullback-definition}
The scheme-theoretic equalizer of $g$ and $h$ is the pullback of the diagonal:
\[
\begin{array}{ccc}
E&\longrightarrow&X\\
\downarrow&&\downarrow{\scriptstyle\Delta_{X/Y}}\\
Z&\xrightarrow{(g,h)}&X\times_YX.
\end{array}
\]

::: pf-proof
By the universal property of the fibre product, a morphism $T\to Z$ factors through $E$ exactly when the two composites
\[
T\longrightarrow Z\overset{g,h}{\rightrightarrows}X
\]
are equal.  Thus $E$ represents the equalizer of $g$ and $h$.
:::

:::

::: {.pf-step #separated-gives-closed-equalizer}
If $f$ is separated, then $E\to Z$ is a closed immersion.

::: pf-proof
Separatedness means that
\[
\Delta_{X/Y}:X\longrightarrow X\times_YX
\]
is a closed immersion.  Closed immersions are preserved by base change, so the pullback $E\to Z$ in step [](#equalizer-pullback-definition){.pf-ref} is a closed immersion.
:::

:::

::: {.pf-step #dense-reduced-gives-equality}
Consequently, if $f$ is separated, $Z$ is reduced, and $g$ and $h$ agree on a dense open subset
\[
U\subseteq Z,
\]
then
\[
\boxed{g=h.}
\]

::: pf-proof
Since $g|_U=h|_U$, the inclusion
\[
U\hookrightarrow Z
\]
factors through the equalizer $E$.  Thus the underlying closed subset $|E|\subseteq|Z|$ contains the dense subset $U$.  By step [](#separated-gives-closed-equalizer){.pf-ref}, $|E|$ is closed, so
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
Therefore $E=Z$, and by the equalizer property in step [](#equalizer-pullback-definition){.pf-ref}, $g=h$.
:::

:::

::: {.pf-step #quasiseparated-gives-quasicompact-immersion}
If $f$ is only quasi-separated, the corresponding conclusion is that the equalizer
\[
E\longrightarrow Z
\]
is a quasicompact immersion.

::: pf-proof
For every morphism of schemes the diagonal is an immersion.  Quasi-separatedness of $f$ means, by definition, that
\[
\Delta_{X/Y}
\]
is quasicompact.  Both properties are preserved by base change, so the equalizer morphism in step [](#equalizer-pullback-definition){.pf-ref} is a quasicompact immersion.

Equivalently, the agreement locus is retrocompact in $Z$: its intersection with every quasicompact open subset of $Z$ is quasicompact.
:::

:::

::: {.pf-step #quasiseparated-counterexample}
Quasi-separatedness does not imply the uniqueness statement in step [](#dense-reduced-gives-equality){.pf-ref}.

::: pf-proof
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

Their equalizer is exactly $\mathbb G_m\hookrightarrow\mathbb A^1$, which is a quasicompact immersion, as step [](#quasiseparated-gives-quasicompact-immersion){.pf-ref} predicts, but not a closed immersion.
:::

:::

::: pf-step
Thus
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

::: pf-proof
This is exactly the combination of steps [](#dense-reduced-gives-equality){.pf-ref}, [](#quasiseparated-gives-quasicompact-immersion){.pf-ref} and [](#quasiseparated-counterexample){.pf-ref}.
:::

:::

::: pf-qed
Step [](#dense-reduced-gives-equality){.pf-ref} gives the dense-open uniqueness property of separated morphisms, and steps [](#quasiseparated-gives-quasicompact-immersion){.pf-ref} and [](#quasiseparated-counterexample){.pf-ref} give the quasi-separated analogue and a counterexample to uniqueness in that case.
:::

:::
:::
