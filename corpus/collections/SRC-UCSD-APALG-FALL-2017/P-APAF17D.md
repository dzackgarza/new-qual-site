---
schema: qual/card@1
id: P-APAF17D
kind: problem
title: Reynolds average of a matrix under an irreducible $\mathrm{GL}_3(\mathbb{C})$ representation
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Invariant Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a finite group and let $X\colon G\to\mathrm{GL}_3(\mathbb{C})$ be an irreducible $3$-dimensional complex matrix representation of $G$.
Let $A$ be the matrix
\[
A=\begin{pmatrix}
1 & -12 & 4 \\
0 & 5 & 3 \\
-2 & 1 & 3
\end{pmatrix}
\]
and let
\[
B=\frac{1}{|G|}\sum_{g\in G}X(g)A X(g)^{-1}.
\]

(a) Determine the trace of the matrix $B$.

(b) Determine the matrix $B$.
:::

::: {.solution}
<1>1. The trace of $B$ is
\[
\boxed{9}.
\]
::: {.proof}
Trace is invariant under similarity, so for every $g\in G$,
\[
\operatorname{tr}(X(g)AX(g)^{-1})=\operatorname{tr}(A).
\]
Hence
\[
\operatorname{tr}(B)
=\frac1{|G|}\sum_{g\in G}\operatorname{tr}(A)
=\operatorname{tr}(A).
\]
Since
\[
\operatorname{tr}(A)=1+5+3=9,
\]
part (a) follows.
:::

<1>2. The matrix $B$ commutes with $X(h)$ for every $h\in G$.
::: {.proof}
For fixed $h\in G$,
\[
\begin{aligned}
X(h)BX(h)^{-1}
&=\frac1{|G|}\sum_{g\in G}X(hg)AX(hg)^{-1}.
\end{aligned}
\]
As $g$ runs through $G$, so does $hg$. Reindexing the sum therefore gives
\[
X(h)BX(h)^{-1}=B.
\]
Equivalently, $X(h)B=BX(h)$.
:::

<1>3. One has
\[
B=cI_3
\]
for some $c\in\mathbb C$.
::: {.proof}
The representation $X$ is irreducible over the algebraically closed field $\mathbb C$. By <1>2, $B$ is an intertwining endomorphism of this irreducible representation. Schur's lemma therefore gives
\[
B=cI_3.
\]
:::

<1>4. In fact,
\[
\boxed{B=3I_3}.
\]
::: {.proof}
By <1>1 and <1>3,
\[
9=\operatorname{tr}(B)=\operatorname{tr}(cI_3)=3c.
\]
Hence $c=3$ and $B=3I_3$. This proves part (b).
:::
:::
