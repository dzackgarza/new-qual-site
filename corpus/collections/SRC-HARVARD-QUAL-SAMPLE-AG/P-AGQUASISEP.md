---
schema: qual/card@1
id: P-AGQUASISEP
kind: problem
title: Quasi-separatedness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-separated Morphisms
  - Quasicompactness
  - Definitions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks for the meaning of quasi-separatedness.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Do you know what quasi-separated means?
:::

::: {.solution}
<1>1. A morphism
\[
f:X\longrightarrow Y
\]
is quasi-separated if its relative diagonal
\[
\Delta_{X/Y}:X\longrightarrow X\times_YX
\]
is quasicompact.
::: {.proof}
This is the definition.  Thus quasi-separatedness is obtained from separatedness by weakening the requirement
\[
\Delta_{X/Y}\text{ closed immersion}
\]
to the finiteness condition
\[
\Delta_{X/Y}\text{ quasicompact}.
\]
:::

<1>2. A scheme $X$ is quasi-separated if and only if the intersection of any two affine open subsets of $X$ is quasicompact.
::: {.proof}
Regard quasi-separatedness of $X$ as quasi-separatedness of the structure morphism
\[
X\longrightarrow\operatorname{Spec}\mathbb Z.
\]

For affine opens $U,V\subseteq X$, the inverse image of
\[
U\times V\subseteq X\times X
\]
under the diagonal is
\[
U\cap V.
\]
Since the products $U\times V$ form an affine open cover of $X\times X$, the diagonal is quasicompact exactly when each such inverse image $U\cap V$ is quasicompact.
:::

<1>3. Equivalently, $X$ is quasi-separated if the intersection of any two quasicompact open subsets is quasicompact.
::: {.proof}
The implication to affine opens is immediate because affine schemes are quasicompact.

Conversely, let $U,V$ be quasicompact opens.  Choose finite affine covers
\[
U=\bigcup_{i=1}^r U_i,
\qquad
V=\bigcup_{j=1}^s V_j.
\]
Then
\[
U\cap V
=\bigcup_{i,j}(U_i\cap V_j).
\]
If intersections of affine opens are quasicompact, this is a finite union of quasicompact opens and is therefore quasicompact.
:::

<1>4. Every separated morphism is quasi-separated.
::: {.proof}
If $f$ is separated, then
\[
\Delta_{X/Y}:X\to X\times_YX
\]
is a closed immersion.  Closed immersions are quasicompact, so the diagonal is quasicompact.  Hence $f$ is quasi-separated.
:::

<1>5. Every morphism with Noetherian source is quasi-separated; in particular every morphism between Noetherian schemes is quasi-separated.
::: {.proof}
If $X$ is Noetherian, every open subset of $X$ is quasicompact.  For the diagonal
\[
\Delta_{X/Y}:X\longrightarrow X\times_YX,
\]
the inverse image of every affine open of the target is an open subset of $X$, hence is quasicompact.  Thus the diagonal is a quasicompact morphism.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>1 is the definition, and steps <1>2--<1>5 give its standard working forms and immediate relation to separatedness.
:::
:::
