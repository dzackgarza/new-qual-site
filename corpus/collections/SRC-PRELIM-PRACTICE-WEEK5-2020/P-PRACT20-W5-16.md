---
schema: qual/card@1
id: P-PRACT20-W5-16
kind: problem
title: Singular $2\times2$ matrices of trace $1$ over $\mathbb F_p$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement with clean inline math and corrected the source typo 'or order p' to 'of order p', checked against Week5_solns.pdf page 5 (Problem 16).
---

::: {.problem}
Let $F$ be a finite field of order $p$. How many non-invertible $2 \times 2$ matrices with entries in $F$ have trace $1$?
:::

::: {.solution}
Write a matrix of trace $1$ as
\[
A=
\begin{pmatrix}
a&b\\
c&1-a
\end{pmatrix},
\qquad
a,b,c\in F.
\]

<1>1. The matrix $A$ is non-invertible exactly when
\[
bc=a(1-a).
\]

::: {.proof}
One has
\[
\det A
=a(1-a)-bc.
\]
A $2\times2$ matrix over a field is non-invertible exactly when its
determinant is zero.
:::

<1>2. If $a=0$ or $a=1$, there are
\[
2p-1
\]
choices for the pair $(b,c)$ satisfying step <1>1.

::: {.proof}
For either value of $a$,
\[
a(1-a)=0,
\]
so the condition is $bc=0$. Since $F$ is a field, this means $b=0$ or
$c=0$. There are $p$ pairs with $b=0$ and $p$ pairs with $c=0$, with
$(0,0)$ counted twice. Hence the number is
\[
p+p-1=2p-1.
\]
:::

<1>3. If $a\notin\{0,1\}$, there are
\[
p-1
\]
choices for $(b,c)$ satisfying step <1>1.

::: {.proof}
Now
\[
\lambda=a(1-a)\ne0.
\]
The equation $bc=\lambda$ forces $b\ne0$. For each of the $p-1$ choices
$b\in F^\times$, there is exactly one choice
\[
c=\lambda b^{-1}.
\]
:::

<1>4. The total number of non-invertible matrices of trace $1$ is
\[
\boxed{p^2+p}.
\]

::: {.proof}
There are two values $a=0,1$, contributing
\[
2(2p-1),
\]
and $p-2$ remaining values of $a$, each contributing $p-1$. Thus
\[
\begin{aligned}
N
&=2(2p-1)+(p-2)(p-1)\\
&=4p-2+p^2-3p+2\\
&=p^2+p.
\end{aligned}
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested count.
:::
:::
