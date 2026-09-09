---
schema: qual/card@1
id: E-GEVBZ
kind: problem
title: Rank-nullity theorem via Jordan canonical form
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Jordan Canonical Form
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Let $T:V\to W$ be a linear map of vector spaces over a field, with $V$ finite-dimensional. Prove using Jordan canonical form that
\[
\dim V=\dim\ker T+\dim\operatorname{im}T.
\]
:::

::: {.solution}
Set $U=\operatorname{im}T$, which is finite-dimensional because $V$ is finite-dimensional.

<1>1. Define an endomorphism $S$ of the finite-dimensional space $V\oplus U$ by
\[
S(v,u)=(0,Tv).
\]
Then $S^2=0$.
::: {.proof}
For $(v,u)\in V\oplus U$,
\[
S^2(v,u)=S(0,Tv)=(0,T0)=(0,0).
\]
Thus the minimal polynomial of $S$ divides $x^2$. In particular it splits over the base field, so $S$ has Jordan canonical form consisting only of nilpotent Jordan blocks of sizes $1$ and $2$.
:::

<1>2. For every Jordan block of $S$, its rank plus its nullity equals its size.
::: {.proof}
A size-$1$ block is $J_1(0)=[0]$, which has rank $0$ and nullity $1$. A size-$2$ block is
\[
J_2(0)=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\]
which has rank $1$ and nullity $1$. Thus each block contributes its full dimension to rank plus nullity. Since rank and nullity add across block-diagonal direct sums,
\[
\operatorname{rank}S+\operatorname{nullity}S=\dim(V\oplus U).
\]
:::

<1>3. The image and kernel of $S$ are
\[
\operatorname{im}S=\{0\}\oplus U,
\qquad
\ker S=\ker T\oplus U.
\]
::: {.proof}
By definition,
\[
\operatorname{im}S=\{(0,Tv):v\in V\}=\{0\}\oplus\operatorname{im}T=\{0\}\oplus U.
\]
Also $S(v,u)=0$ exactly when $Tv=0$, with no restriction on $u\in U$. Hence
\[
\ker S=\ker T\oplus U.
\]
:::

<1>4. Therefore
\[
\dim V=\dim\ker T+\dim\operatorname{im}T.
\]
::: {.proof}
By <1>3,
\[
\operatorname{rank}S=\dim U,
\qquad
\operatorname{nullity}S=\dim\ker T+\dim U.
\]
Substituting these into <1>2 gives
\[
\dim V+\dim U
=\dim U+\dim\ker T+\dim U.
\]
Cancelling $\dim U$ from both sides gives
\[
\dim V=\dim\ker T+\dim U
=\dim\ker T+\dim\operatorname{im}T.
\]
:::
:::
