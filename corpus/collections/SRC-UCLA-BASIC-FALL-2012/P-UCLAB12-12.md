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
Let $M$ be an $n$ by $m$ matrix.
Prove that the row rank of $M$ equals the column rank of $M$. Also, however you prove it, interpret this result as an equality of the dimensions of two vector spaces naturally attached to the map defined by $M$.
:::

::: {.solution}

Let
$$
T:\FF^m\to\FF^n
$$
be the linear map whose matrix in the standard bases is $M$, where $\FF$ is the underlying field.

::: pf

::: {.pf-step #s1-1}

The column rank of $M$ equals
$$
\dim\operatorname{image}T.
$$


::: pf-proof

If
$$
e_1,\ldots,e_m
$$
is the standard basis of $\FF^m$, then
$$
T(e_j)
$$
is the $j$th column of $M$.
Hence the span of the columns is exactly $\operatorname{image}T$.

:::

:::

::: {.pf-step #s1-2}

Let
$$
T^*:(\FF^n)^*\to(\FF^m)^*
$$
be the dual map
$$
T^*(\varphi)=\varphi\circ T.
$$
Then the row rank of $M$ equals
$$
\dim\operatorname{image}T^*.
$$


::: pf-proof

In the standard dual bases, the matrix of $T^*$ is the transpose
$$
M^t.
$$
Its columns are exactly the rows of $M$, regarded as coordinate vectors in $(\FF^m)^*$.
Thus the row space of $M$ is naturally identified with $\operatorname{image}T^*$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\ker T^*
=
(\operatorname{image}T)^0,
$$
the annihilator of $\operatorname{image}T$ in $(\FF^n)^*$.


::: pf-proof

Let
$$
\varphi\in(\FF^n)^*.
$$
Then
$$
\varphi\in\ker T^*
$$
if and only if
$$
T^*(\varphi)=\varphi\circ T=0.
$$
This means
$$
\varphi(Tv)=0
$$
for every $v\in\FF^m$, equivalently $\varphi$ vanishes on every vector in $\operatorname{image}T$.
That is precisely the condition
$$
\varphi\in(\operatorname{image}T)^0.
$$

:::

:::

::: {.pf-step #s1-4}

For every subspace
$$
U\subseteq\FF^n,
$$
one has
$$
\dim U^0=n-\dim U.
$$


::: pf-proof

Let
$$
u_1,\ldots,u_r
$$
be a basis of $U$, and extend it to a basis
$$
u_1,\ldots,u_r,v_{r+1},\ldots,v_n
$$
of $\FF^n$.
In the corresponding dual basis, the annihilator $U^0$ is spanned by
$$
v_{r+1}^*,\ldots,v_n^*.
$$
Hence
$$
\dim U^0=n-r=n-\dim U.
$$

:::

:::

::: {.pf-step #s1-5}

The dual map has the same rank as the original map:
$$
\dim\operatorname{image}T^*
=
\dim\operatorname{image}T.
$$


::: pf-proof

By rank-nullity for
$$
T^*:(\FF^n)^*\to(\FF^m)^*,
$$
steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} give
$$
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
$$

:::

:::

::: {.pf-step #s1-6}

Therefore the row rank of $M$ equals the column rank of $M$.


::: pf-proof

By step [](#s1-1){.pf-ref}, the column rank is
$$
\dim\operatorname{image}T.
$$
By step [](#s1-2){.pf-ref}, the row rank is
$$
\dim\operatorname{image}T^*.
$$
These dimensions are equal by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The equality has the natural vector-space interpretation
$$
\boxed{
\dim\operatorname{image}T
=
\dim\operatorname{image}T^*
}.
$$


::: pf-proof

The column space is naturally the image of the map $T$ defined by $M$, while the row space is naturally the image of its dual map $T^*$.
Thus row rank equals column rank precisely because these two naturally attached image spaces have equal dimension.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves equality of row and column rank, and step [](#s1-7){.pf-ref} gives the requested interpretation.

:::

:::

:::
