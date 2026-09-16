---
schema: qual/card@1
id: E-HK-1EVA
kind: problem
title: Row-reduced $2 \times 2$ complex matrices with trace zero
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the statement with Hoffman--Kunze 1.3.6 and used the book's Section 1.3 definition of row-reduced, which does not impose echelon ordering."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Exhausted the zero-row and two-nonzero-row cases under the book's pivot-column conditions and checked all three surviving matrices directly."
---

::: {.exercise}
Let

$$
A = \left[ \begin{array}{c c} a & b \\ c & d \end{array} \right]
$$

be a $2 \times 2$ matrix with complex entries.
Suppose that $A$ is row-reduced and also that $a + b + c + d = 0$ . Prove that there are exactly three such matrices.
:::

::: {.solution}
The three matrices are
$$
\boxed{
\begin{pmatrix}0&0\\0&0\end{pmatrix},\qquad
\begin{pmatrix}1&-1\\0&0\end{pmatrix},\qquad
\begin{pmatrix}0&0\\1&-1\end{pmatrix}.}
$$

Recall that in this section a matrix is row-reduced when the first nonzero
entry of each nonzero row is $1$, and every column containing such a leading
$1$ has all its other entries equal to $0$ [@HK71]. No condition orders the
nonzero rows; that stronger requirement belongs to row-reduced echelon form.

<1>1. If exactly one row is nonzero, there are exactly two possibilities.
::: {.proof}
Suppose first that the first row is nonzero and the second row is zero. Then
$c=d=0$. If $a\ne0$, row-reducedness forces the leading entry $a$ to equal
$1$, and the sum condition gives $1+b=0$, so
$$
A=\begin{pmatrix}1&-1\\0&0\end{pmatrix}.
$$
If instead $a=0$, then the nonzero row begins with $b$, so $b=1$; the sum of
the entries is then $1$, impossible.

Now suppose the first row is zero and the second row is nonzero. The same
argument gives either $c=1$ and then $d=-1$, or else $c=0,d=1$, the latter
again contradicting the zero-sum condition. Thus the only possibility in this
case is
$$
A=\begin{pmatrix}0&0\\1&-1\end{pmatrix}.
$$
:::

<1>2. If both rows are nonzero, no matrix satisfies the sum condition.
::: {.proof}
Each nonzero row has a leading $1$. The two leading $1$'s cannot occur in the
same column, because a pivot column must have all other entries zero.

If the first row leads in column $1$, then $a=1$ and the pivot-column condition
forces $c=0$. Since the second row is nonzero, it must then lead in column $2$,
so $d=1$; the pivot condition in column $2$ forces $b=0$. Hence
$A=I_2$, whose entries sum to $2$.

If instead the second row leads in column $1$, then $c=1$ and $a=0$. The first
row must therefore lead in column $2$, so $b=1$, and the pivot condition in
column $2$ forces $d=0$. Hence
$$
A=\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$
whose entries also sum to $2$. Therefore no matrix with two nonzero rows works.
:::

<1>3. The zero matrix supplies the third example, and all three displayed matrices are row-reduced.
::: {.proof}
The zero matrix is row-reduced vacuously and has entry sum zero. In each of the
two rank-one matrices displayed above, the only nonzero row has leading entry
$1$, and its leading column has zero in the other row; their entry sums are
$1-1=0$. Thus all three satisfy the hypotheses. Steps <1>1 and <1>2 show that
there are no others.
:::
:::
