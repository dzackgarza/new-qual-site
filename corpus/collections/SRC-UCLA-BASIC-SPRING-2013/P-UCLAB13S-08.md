---
schema: qual/card@1
id: P-UCLAB13S-08
kind: problem
title: Adjoints and equality of row rank and column rank
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
Let $T$ be a linear transformation from a finite-dimensional inner-product space $V$ to a finite-dimensional inner-product space $W$.

(a) Define the adjoint $T^*:W\to V$.

(b) Show that, relative to orthonormal bases of $V$ and $W$, the matrix of $T^*$ is the transpose of the matrix of $T$.

(c) Show that the kernel of $T^*$ is the orthogonal complement of the range of $T$.

(d) Use (b) and (c) to show that the row rank of a matrix equals its column rank.
:::

::: {.solution}
<1>1. The adjoint of
\[
T:V\to W
\]
is the unique linear map
\[
\boxed{T^*:W\to V}
\]
such that
\[
\boxed{
\langle Tv,w\rangle_W
=
\langle v,T^*w\rangle_V
}
\]
for every
\[
v\in V,
\qquad
w\in W.
\]

::: {.proof}
This is the definition of the adjoint.
In finite-dimensional inner-product spaces, existence and uniqueness follow from the Riesz representation theorem.
:::

<1>2. Let
\[
e_1,\ldots,e_n
\]
be an orthonormal basis of $V$ and
\[
f_1,\ldots,f_m
\]
an orthonormal basis of $W$.
If
\[
[T]=(a_{ij}),
\]
then
\[
a_{ij}
=
\langle Te_j,f_i\rangle_W.
\]

::: {.proof}
The $j$th column of $[T]$ consists of the coordinates of $Te_j$ in the basis $(f_i)$.
Because the basis is orthonormal, the $i$th coordinate is
\[
\langle Te_j,f_i\rangle_W.
\]
:::

<1>3. The matrix of $T^*$ in the corresponding orthonormal bases is
\[
\boxed{[T^*]=[T]^T}.
\]

::: {.proof}
The $(j,i)$ entry of $[T^*]$ is
\[
\langle T^*f_i,e_j\rangle_V.
\]
By the adjoint identity,
\[
\langle T^*f_i,e_j\rangle_V
=
\langle f_i,Te_j\rangle_W
=
\langle Te_j,f_i\rangle_W
=
a_{ij},
\]
because the spaces are real inner-product spaces.
Thus the $(j,i)$ entry of $[T^*]$ equals the $(i,j)$ entry of $[T]$.
Hence
\[
[T^*]=[T]^T.
\]
This proves part (b).
:::

<1>4. One has
\[
\ker T^*
\subseteq
(\operatorname{im}T)^\perp.
\]

::: {.proof}
Let
\[
w\in\ker T^*.
\]
Then
\[
T^*w=0.
\]
For every
\[
v\in V,
\]
\[
\langle Tv,w\rangle_W
=
\langle v,T^*w\rangle_V
=0.
\]
Thus $w$ is orthogonal to every vector in $\operatorname{im}T$.
:::

<1>5. One also has
\[
(\operatorname{im}T)^\perp
\subseteq
\ker T^*.
\]

::: {.proof}
Let
\[
w\in(\operatorname{im}T)^\perp.
\]
Then for every
\[
v\in V,
\]
\[
0
=
\langle Tv,w\rangle_W
=
\langle v,T^*w\rangle_V.
\]
Taking
\[
v=T^*w
\]
gives
\[
\|T^*w\|^2=0.
\]
Hence
\[
T^*w=0.
\]
:::

<1>6. Therefore
\[
\boxed{
\ker T^*
=
(\operatorname{im}T)^\perp.
}
\]

::: {.proof}
Combine steps <1>4 and <1>5.
This proves part (c).
:::

<1>7. The rank of $T^*$ equals the rank of $T$.

::: {.proof}
By rank-nullity for
\[
T^*:W\to V,
\]
\[
\operatorname{rank}T^*
=
\dim W-\dim\ker T^*.
\]
By step <1>6,
\[
\dim\ker T^*
=
\dim(\operatorname{im}T)^\perp
=
\dim W-\dim\operatorname{im}T.
\]
Thus
\[
\operatorname{rank}T^*
=
\dim\operatorname{im}T
=
\operatorname{rank}T.
\]
:::

<1>8. Let $A$ be the matrix of $T$ in orthonormal bases.
Then the column rank of $A$ equals
\[
\operatorname{rank}T,
\]
while the row rank of $A$ equals
\[
\operatorname{rank}T^*.
\]

::: {.proof}
The columns of $A$ are the coordinate vectors of
\[
Te_1,\ldots,Te_n.
\]
Their span is therefore the coordinate image of $\operatorname{im}T$, so the column rank is $\operatorname{rank}T$.

By step <1>3,
\[
[T^*]=A^T.
\]
The columns of $A^T$ are the rows of $A$.
Hence the row rank of $A$ is the column rank of $A^T$, which equals
\[
\operatorname{rank}T^*.
\]
:::

<1>9. Therefore
\[
\boxed{
\operatorname{rowrank}A
=
\operatorname{colrank}A.
}
\]

::: {.proof}
By step <1>8, these ranks are
\[
\operatorname{rank}T^*
\quad\text{and}\quad
\operatorname{rank}T.
\]
Step <1>7 shows they are equal.
This proves part (d).
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>1 answers part (a), step <1>3 proves part (b), step <1>6 proves part (c), and step <1>9 proves part (d).
:::
:::
