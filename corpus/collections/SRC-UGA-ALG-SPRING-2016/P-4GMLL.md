---
schema: qual/card@1
id: P-4GMLL
kind: problem
title: Jordan form of $\begin{pmatrix}-3&3&-2\\-7&6&-3\\1&-1&2\end{pmatrix}$ and a
  conjugating matrix
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and verified every computation
    exactly (rational arithmetic): trace 5, det 4 and sum of principal 2x2 minors 8 give
    chi = x^3 - 5x^2 + 8x - 4 = (x-1)(x-2)^2; rank(A - 2I) = 2 by the nonzero 3x2 minor with
    a nontrivial kernel, so the geometric multiplicity of 2 is 1 and the block is 2x2;
    Av_1 = v_1, (A-2I)v_2 = 0, (A-2I)v_3 = v_2; det P = 1/4; and AP = PJ column by column.
    The prose asserted that the eigenspace for 2 is one-dimensional without computing a rank,
    and quoted det P and the Jordan-basis relations without deriving them; both are now steps.
    The statement is true as printed. The collection's provenance is the examination paper
    only, so no retained solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
Let
$$
A=\left(\begin{array}{ccc}
-3 & 3 & -2 \\
-7 & 6 & -3 \\
1 & -1 & 2
\end{array}\right) \in M_{3}(\mathrm{C})
.$$

a.
Find the Jordan canonical form $J$ of $A$.

b.
Find an invertible matrix $P$ such that $\inverseof{P} A P = J$.
You do not need to compute $\inverseof{P}$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Write $A$ for the given matrix, $v_1\coloneqq(1,2,1)$, $v_2\coloneqq\frac12(1,1,-1)$, $v_3\coloneqq\frac12(1,2,0)$ and $P$ with columns $v_1,v_2,v_3$.

::: pf

::: {.pf-step #charpoly}
$\chi_A(x)=\det(xI-A)=x^3-5x^2+8x-4=(x-1)(x-2)^2$.

::: pf-proof
The coefficients are the elementary symmetric functions of the eigenvalues: $\operatorname{tr}A=-3+6+2=5$, the sum of the three principal $2\times2$ minors is $(-3\cdot6-3\cdot(-7))+(-3\cdot2-(-2)\cdot1)+(6\cdot2-(-3)(-1))=3+(-4)+9=8$, and $\det A=4$. Hence $\chi_A=x^3-(\operatorname{tr}A)x^2+8x-\det A$, and $x^3-5x^2+8x-4=(x-1)(x-2)^2$ by expansion.
:::

:::

::: {.pf-step #eigenspace}
$\dim\ker(A-2I)=1$.

::: pf-proof
$A-2I=\begin{pmatrix}-5&3&-2\\-7&4&-3\\1&-1&0\end{pmatrix}$, whose minor on rows $2,3$ and columns $1,2$ is $(-7)(-1)-4\cdot1=3\ne0$, so the rank is at least $2$; it is not $3$ because $(A-2I)v_2=0$ with $v_2\ne0$. Hence the rank is $2$ and the nullity is $3-2=1$, so the eigenvalue $2$ has geometric multiplicity $1$ although its algebraic multiplicity is $2$.
:::

:::

::: {.pf-step}
(a) The Jordan form of $A$ is
$$
J=\begin{pmatrix}1&0&0\\0&2&1\\0&0&2\end{pmatrix}.
$$

::: pf-proof
Step [](#charpoly){.pf-ref} shows the eigenvalues are $1$ and $2$, with $1$ simple and $2$ of algebraic multiplicity $2$; step [](#eigenspace){.pf-ref} shows the geometric multiplicity of $2$ is $1$, so the eigenvalue $2$ carries a single Jordan block, of size $2$. Assembling these blocks gives $J$ as displayed.
:::

:::

::: {.pf-step #jordan-basis}
$Av_1=v_1$, $(A-2I)v_2=0$ and $(A-2I)v_3=v_2$.

::: pf-proof
Direct computation: $A(1,2,1)^t=(-3+6-2,\,-7+12-3,\,1-2+2)^t=(1,2,1)^t$; $A(1,1,-1)^t=(-3+3+2,\,-7+6+3,\,1-1-2)^t=(2,2,-2)^t=2(1,1,-1)^t$, so that vector and hence $v_2$ are fixed by $A-2I$; and $A(1,2,0)^t=(-3+6,\,-7+12,\,1-2)^t=(3,5,-1)^t$, so $(A-2I)v_3=\frac12(3,5,-1)^t-\frac12\cdot2(1,2,0)^t=\frac12(1,1,-1)^t=v_2$.
:::

:::

::: {.pf-step #invertible}
$\det P=\frac14$, so $P$ is invertible.

::: pf-proof
Expanding, $\det P=\frac14\det\begin{pmatrix}2&1&1\\4&1&2\\2&-1&0\end{pmatrix}=\frac14\left(2(1\cdot0-2\cdot(-1))-1(4\cdot0-2\cdot2)+1(4\cdot(-1)-1\cdot2)\right)=\frac14(4+4-6)=\frac14$.
:::

:::

::: {.pf-step}
(b) $P^{-1}AP=J$ for the displayed $P$; no inverse of $P$ need be computed.

::: pf-proof
Steps [](#jordan-basis){.pf-ref} read column by column as $AP=PJ$: the first column of $AP$ is $Av_1=v_1$, which is the first column of $PJ$; the second is $Av_2=2v_2$, which is the second column of $PJ$; and the third is $Av_3=2v_3+v_2$, which is the third column of $PJ$. Since $P$ is invertible by step [](#invertible){.pf-ref}, multiplying $AP=PJ$ on the left by $P^{-1}$ gives $P^{-1}AP=J$.
:::

:::

:::
:::
