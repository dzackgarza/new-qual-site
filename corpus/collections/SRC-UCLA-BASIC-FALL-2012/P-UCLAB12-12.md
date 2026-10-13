---
schema: qual/card@1
id: P-UCLAB12-12
kind: problem
title: Row rank equals column rank
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let M be an n by m matrix.
Prove that the row rank of M equals the column rank of M. Also, however you prove it, interpret this result as an equality of the dimensions of two vector spaces naturally attached to the map defined by M.
:::

::: {.solution}
Let
\[
T:\mathbb F^m\to\mathbb F^n
\]
be the linear map whose matrix in the standard bases is $M$, where $\mathbb F$ is the underlying field.

<1>1. The column rank of $M$ equals
\[
\dim\operatorname{image}T.
\]

::: {.proof}
If
\[
e_1,\ldots,e_m
\]
is the standard basis of $\mathbb F^m$, then
\[
T(e_j)
\]
is the $j$th column of $M$.
Hence the span of the columns is exactly $\operatorname{image}T$.
:::

<1>2. Let
\[
T^*:(\mathbb F^n)^*\to(\mathbb F^m)^*
\]
be the dual map
\[
T^*(\varphi)=\varphi\circ T.
\]
Then the row rank of $M$ equals
\[
\dim\operatorname{image}T^*.
\]

::: {.proof}
In the standard dual bases, the matrix of $T^*$ is the transpose
\[
M^t.
\]
Its columns are exactly the rows of $M$, regarded as coordinate vectors in $(\mathbb F^m)^*$.
Thus the row space of $M$ is naturally identified with $\operatorname{image}T^*$.
:::

<1>3. One has
\[
\ker T^*
=
(\operatorname{image}T)^0,
\]
the annihilator of $\operatorname{image}T$ in $(\mathbb F^n)^*$.

::: {.proof}
Let
\[
\varphi\in(\mathbb F^n)^*.
\]
Then
\[
\varphi\in\ker T^*
\]
if and only if
\[
T^*(\varphi)=\varphi\circ T=0.
\]
This means
\[
\varphi(Tv)=0
\]
for every $v\in\mathbb F^m$, equivalently $\varphi$ vanishes on every vector in $\operatorname{image}T$.
That is precisely the condition
\[
\varphi\in(\operatorname{image}T)^0.
\]
:::

<1>4. For every subspace
\[
U\subseteq\mathbb F^n,
\]
one has
\[
\dim U^0=n-\dim U.
\]

::: {.proof}
Let
\[
u_1,\ldots,u_r
\]
be a basis of $U$, and extend it to a basis
\[
u_1,\ldots,u_r,v_{r+1},\ldots,v_n
\]
of $\mathbb F^n$.
In the corresponding dual basis, the annihilator $U^0$ is spanned by
\[
v_{r+1}^*,\ldots,v_n^*.
\]
Hence
\[
\dim U^0=n-r=n-\dim U.
\]
:::

<1>5. The dual map has the same rank as the original map:
\[
\dim\operatorname{image}T^*
=
\dim\operatorname{image}T.
\]

::: {.proof}
By rank-nullity for
\[
T^*:(\mathbb F^n)^*\to(\mathbb F^m)^*,
\]
steps <1>3--<1>4 give
\[
\begin{aligned}
\dim\operatorname{image}T^*
&=
n-\dim\ker T^*\\
&=
n-\dim(\operatorname{image}T)^0\\
&=
n-\bigl(n-\dim\operatorname{image}T\bigr)\\
&=
\dim\operatorname{image}T.
\end{aligned}
\]
:::

<1>6. Therefore the row rank of $M$ equals the column rank of $M$.

::: {.proof}
By step <1>1, the column rank is
\[
\dim\operatorname{image}T.
\]
By step <1>2, the row rank is
\[
\dim\operatorname{image}T^*.
\]
These dimensions are equal by step <1>5.
:::

<1>7. The equality has the natural vector-space interpretation
\[
\boxed{
\dim\operatorname{image}T
=
\dim\operatorname{image}T^*
}.
\]

::: {.proof}
The column space is naturally the image of the map $T$ defined by $M$, while the row space is naturally the image of its dual map $T^*$.
Thus row rank equals column rank precisely because these two naturally attached image spaces have equal dimension.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>6 proves equality of row and column rank, and step <1>7 gives the requested interpretation.
:::
:::
