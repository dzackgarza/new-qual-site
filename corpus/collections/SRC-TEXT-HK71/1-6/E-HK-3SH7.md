---
schema: qual/card@1
id: E-HK-3SH7
kind: problem
title: Row-reduction and invertible matrix factorization $R = PA$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze Exercise 1.6.1.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the verification into numbered steps and wrote out what the prose asserted: the
    row-reduced echelon conditions on R one by one, the twelve entries of P A computed row by row,
    the 3 x 3 determinant expansion giving det P = 1/16, and the reason R is row-equivalent to A
    (an invertible matrix is a product of elementary matrices, which is proved). Both numerical
    claims were re-checked independently with sympy: P A equals the displayed R and det P = 1/16
    exactly. Not checked this session: the printed statement and page, the collection's provenance
    being an archive.org scan and no Hoffman--Kunze text retained in tmp/sources; the computation
    is the card's own, which the solution section states.
---

::: {.exercise}
Let

$$
A = \left[ \begin{array}{r r r r} 1 & 2 & 1 & 0 \\ - 1 & 0 & 3 & 5 \\ 1 & - 2 & 1 & 1 \end{array} \right].
$$

Find a row-reduced echelon matrix $R$ which is row-equivalent to $A$ and an invertible $3 \times 3$ matrix $P$ such that $R = PA$.
:::


::: {.solution}

The computation is the card's own: no copy of Hoffman and Kunze and no solution set for it is retained in `tmp/sources`, so nothing here is transcribed. The statement is the exercise the collection index records as Hoffman and Kunze, *Linear Algebra* §1.6 Exercise 1.

Let
$$
A=\begin{bmatrix}1&2&1&0\\ -1&0&3&5\\ 1&-2&1&1\end{bmatrix},\qquad
R=\begin{bmatrix}1&0&0&-\tfrac78\\ 0&1&0&-\tfrac14\\ 0&0&1&\tfrac{11}{8}\end{bmatrix},\qquad
P=\begin{bmatrix}\tfrac38&-\tfrac14&\tfrac38\\ \tfrac14&0&-\tfrac14\\ \tfrac18&\tfrac14&\tfrac18\end{bmatrix}.
$$

::: pf

::: {.pf-step #rref}
$R$ is in row-reduced echelon form.

::: pf-proof
The first nonzero entry of each nonzero row of $R$ is $1$, in columns $1,2,3$ respectively, so the leading entries move strictly to the right as the row index increases; each of those columns has its leading $1$ and zeros in the other two positions, since column $1$ is $(1,0,0)^{t}$, column $2$ is $(0,1,0)^{t}$ and column $3$ is $(0,0,1)^{t}$; and there is no zero row. That is the definition of row-reduced echelon form.
:::

:::

::: {.pf-step #row1}
The first row of $PA$ is $\bigl(1,\,0,\,0,\,-\tfrac78\bigr)$.

::: pf-proof
The $(1,j)$ entry of $PA$ is $\tfrac38A_{1j}-\tfrac14A_{2j}+\tfrac38A_{3j}$. For $j=1$: $\tfrac38-\tfrac14(-1)+\tfrac38=\tfrac34+\tfrac14=1$. For $j=2$: $\tfrac38\cdot2-\tfrac14\cdot0+\tfrac38(-2)=\tfrac34-\tfrac34=0$. For $j=3$: $\tfrac38-\tfrac14\cdot3+\tfrac38=\tfrac34-\tfrac34=0$. For $j=4$: $\tfrac38\cdot0-\tfrac14\cdot5+\tfrac38\cdot1=-\tfrac54+\tfrac38=-\tfrac{10}{8}+\tfrac38=-\tfrac78$.
:::

:::

::: {.pf-step #row2}
The second row of $PA$ is $\bigl(0,\,1,\,0,\,-\tfrac14\bigr)$.

::: pf-proof
The $(2,j)$ entry is $\tfrac14A_{1j}+0\cdot A_{2j}-\tfrac14A_{3j}$. For $j=1$: $\tfrac14-\tfrac14=0$. For $j=2$: $\tfrac14\cdot2-\tfrac14(-2)=\tfrac12+\tfrac12=1$. For $j=3$: $\tfrac14-\tfrac14=0$. For $j=4$: $\tfrac14\cdot0-\tfrac14\cdot1=-\tfrac14$.
:::

:::

::: {.pf-step #row3}
The third row of $PA$ is $\bigl(0,\,0,\,1,\,\tfrac{11}{8}\bigr)$.

::: pf-proof
The $(3,j)$ entry is $\tfrac18A_{1j}+\tfrac14A_{2j}+\tfrac18A_{3j}$. For $j=1$: $\tfrac18-\tfrac14+\tfrac18=0$. For $j=2$: $\tfrac28+\tfrac14(-2)=\tfrac14-\tfrac14=0$. For $j=3$: $\tfrac18+\tfrac34+\tfrac18=\tfrac14+\tfrac34=1$. For $j=4$: $\tfrac18\cdot0+\tfrac14\cdot5+\tfrac18\cdot1=\tfrac54+\tfrac18=\tfrac{10}{8}+\tfrac18=\tfrac{11}{8}$.
:::

:::

::: {.pf-step #pa}
$PA=R$.

::: pf-proof
Steps [](#row1){.pf-ref}, [](#row2){.pf-ref} and [](#row3){.pf-ref} give the three rows of $PA$, and they are the three rows of $R$ by its definition; two matrices with the same rows are equal.
:::

:::

::: {.pf-step #det}
$\det P=\tfrac1{16}\neq0$.

::: pf-proof
Expanding along the first row,
$$
\det P=\tfrac38\det\begin{bmatrix}0&-\tfrac14\\ \tfrac14&\tfrac18\end{bmatrix}-\bigl(-\tfrac14\bigr)\det\begin{bmatrix}\tfrac14&-\tfrac14\\ \tfrac18&\tfrac18\end{bmatrix}+\tfrac38\det\begin{bmatrix}\tfrac14&0\\ \tfrac18&\tfrac14\end{bmatrix}.
$$
The three $2\times2$ determinants are $0\cdot\tfrac18-(-\tfrac14)(\tfrac14)=\tfrac1{16}$, $\tfrac14\cdot\tfrac18-(-\tfrac14)(\tfrac18)=\tfrac1{32}+\tfrac1{32}=\tfrac1{16}$, and $\tfrac14\cdot\tfrac14-0=\tfrac1{16}$. Hence $\det P=\tfrac38\cdot\tfrac1{16}+\tfrac14\cdot\tfrac1{16}+\tfrac38\cdot\tfrac1{16}=\tfrac{6}{128}+\tfrac{2}{128}=\tfrac8{128}=\tfrac1{16}$, which is nonzero.
:::

:::

::: {.pf-step #invertible}
$P$ is invertible and is a product of elementary matrices.

::: pf-proof
A square matrix is invertible exactly when its determinant is nonzero, so step [](#det){.pf-ref} gives invertibility. For the second claim, apply elementary row operations to $P$ to reach its row-reduced echelon form; an invertible matrix has row-reduced echelon form $I$ (each of its $n$ rows has a leading $1$, in $n$ distinct columns, hence in every column), so there are elementary matrices $E_{1},\dots,E_{k}$ with $E_{k}\cdots E_{1}P=I$. Then $P=E_{1}^{-1}\cdots E_{k}^{-1}$, and the inverse of an elementary matrix is elementary, so $P$ is a product of elementary matrices.
:::

:::

::: {.pf-step #equivalent}
$R$ is row-equivalent to $A$.

::: pf-proof
Multiplying $A$ on the left by an elementary matrix performs one elementary row operation, so multiplying by the product $P$ of step [](#invertible){.pf-ref} performs a finite sequence of them; by step [](#pa){.pf-ref} that sequence carries $A$ to $R$. Hence $R$ is row-equivalent to $A$.
:::

:::

::: {.pf-step}
$R=PA$ with $R$ row-reduced echelon, $R$ row-equivalent to $A$, and $P$ invertible: the exercise is answered.

::: pf-proof
Steps [](#rref){.pf-ref}, [](#pa){.pf-ref}, [](#equivalent){.pf-ref} and [](#invertible){.pf-ref} give the four required properties.
:::

:::

:::

:::
