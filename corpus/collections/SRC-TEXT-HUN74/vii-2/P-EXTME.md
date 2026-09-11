---
schema: qual/card@1
id: P-EXTME
kind: problem
title: Rank criteria for consistency and uniqueness of linear systems
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Rank and Nullity
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Read the complete retained exercise. Corrected the locally false final corollary and made the uniqueness assertion explicitly conditional on consistency; the available source context did not determine whether the reversal was printed or introduced during extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved row-operation invariance using elementary matrices, consistency using the augmented-column rank criterion, uniqueness by rank-nullity, and the homogeneous criterion by nullity."
---

::: problem
Let $A=(a_{ij})$ be an $n\times m$ matrix over a field, let
$$
X=(x_1,\ldots,x_m)^t,
\qquad
B=(b_1,\ldots,b_n)^t,
$$
and consider the system
$$
\begin{aligned}
a_{11}x_1+\cdots+a_{1m}x_m&=b_1,\\
&\vdots\\
a_{n1}x_1+\cdots+a_{nm}x_m&=b_n.
\end{aligned}
$$

1. Show that the system has a simultaneous solution if and only if the matrix
   equation $AX=B$ has a solution.

2. If $A_1,B_1$ are obtained from $A,B$ by performing the same sequence of
   elementary row operations, show that $X$ solves $AX=B$ if and only if it
   solves $A_1X=B_1$.

3. Let
$$
C=[A\mid B]
$$
be the $n\times(m+1)$ augmented matrix. Show that $AX=B$ has a solution if
and only if
$$
\operatorname{rank}A=\operatorname{rank}C.
$$
When a solution exists, show that it is unique if and only if
$$
\operatorname{rank}A=m.
$$

4. If $B=0$, show that the homogeneous system has a nontrivial solution if
and only if
$$
\operatorname{rank}A<m.
$$
In particular, show that if $n<m$, then the homogeneous system has a
nontrivial solution.
:::

::: solution
<1>1. The displayed scalar system is exactly the coordinate form of $AX=B$.
::: proof
The $i$th entry of the product $AX$ is
$$
(AX)_i=\sum_{j=1}^m a_{ij}x_j.
$$
Therefore
$$
AX=B
$$
holds exactly when, for every $1\le i\le n$,
$$
\sum_{j=1}^m a_{ij}x_j=b_i.
$$
These are precisely the $n$ displayed equations. Hence a vector $X$ is a
simultaneous solution of the scalar system if and only if it solves the matrix
equation.
:::

<1>2. Simultaneous elementary row operations do not change the solution set.
::: proof
A sequence of elementary row operations is left multiplication by an
invertible matrix $E$, a product of elementary matrices. Thus
$$
A_1=EA,
\qquad
B_1=EB.
$$
If $AX=B$, then multiplying by $E$ gives
$$
A_1X=EAX=EB=B_1.
$$
Conversely, if $A_1X=B_1$, then
$$
EAX=EB.
$$
Multiplying by $E^{-1}$ yields $AX=B$. Therefore the two systems have exactly
the same solutions.
:::

<1>3. Consistency is equivalent to equality of the two ranks.
::: proof
The equation
$$
AX=B
$$
has a solution exactly when the column $B$ belongs to the column space of
$A$. Appending a column already in the column space does not increase its
dimension, while appending a column outside it increases that dimension by
one. Hence
$$
B\in\operatorname{Col}(A)
\iff
\operatorname{rank}[A\mid B]=\operatorname{rank}A.
$$
Since $C=[A\mid B]$, this is exactly
$$
\boxed{AX=B\text{ is solvable}\iff\operatorname{rank}A=\operatorname{rank}C.}
$$
:::

<1>4. A consistent system has a unique solution exactly when $\operatorname{rank}A=m$.
::: proof
Assume $AX=B$ is consistent and choose one solution $X_0$. Then $X$ is any
other solution if and only if
$$
A(X-X_0)=0.
$$
Thus the full solution set is the affine space
$$
X_0+\ker A.
$$
It consists of exactly one point if and only if
$$
\ker A=0.
$$
By rank-nullity for the linear map
$$
A:F^m\longrightarrow F^n,
$$
one has
$$
m=\dim\ker A+\operatorname{rank}A.
$$
Hence $\ker A=0$ if and only if $\operatorname{rank}A=m$. Therefore, for a
consistent system,
$$
\boxed{\text{the solution is unique}\iff\operatorname{rank}A=m.}
$$
:::

<1>5. The homogeneous system has a nontrivial solution exactly when $\operatorname{rank}A<m$.
::: proof
For $B=0$, the solution set is precisely $\ker A$. It contains a nonzero
vector if and only if
$$
\dim\ker A>0.
$$
Rank-nullity gives
$$
\dim\ker A=m-\operatorname{rank}A,
$$
so
$$
\ker A\ne0
\iff
\operatorname{rank}A<m.
$$
:::

<1>6. More unknowns than equations force a nontrivial homogeneous solution.
::: proof
Since $A$ has $n$ rows,
$$
\operatorname{rank}A\le n.
$$
If $n<m$, then
$$
\operatorname{rank}A\le n<m,
$$
so step <1>5 gives a nontrivial solution of $AX=0$.
:::
:::
