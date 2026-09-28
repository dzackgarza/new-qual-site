---
schema: qual/card@1
id: P-BERK79S-13
kind: problem
title: Cardinality of $V$ and orders of $GL_n(F)$ and $SL_n(F)$ over a finite field
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    A basis identifies V with F^n, giving q^n vectors. An invertible matrix
    is an ordered basis of F^n: the jth column can be chosen in
    q^n-q^{j-1} ways after the previous columns. Finally determinant maps
    GL_n(F) surjectively onto F^× with kernel SL_n(F), so
    |SL_n(F)|=|GL_n(F)|/(q-1).
---

::: {.problem}
Let $F$ be a finite field with $q$ elements and let $V$ be an $n$-dimensional vector space over $F$.

1. Determine $|V|$.

2. Determine the order of $GL_n(F)$.

3. Determine the order of $SL_n(F)$.
:::

::: {.solution}
<1>1. The vector space $V$ has
$$
\boxed{
\abs{V}=q^n.
}
$$

::: {.proof}
Choose a basis
$$
v_1,\ldots,v_n
$$
of $V$. Every vector has a unique expression
$$
a_1v_1+\cdots+a_nv_n
$$
with
$$
a_i\in F.
$$
There are $q$ choices for each of the $n$ coefficients, independently.
Hence there are $q^n$ vectors.
:::

<1>2. An $n\times n$ matrix over $F$ is invertible if and only if its
columns form an ordered basis of $F^n$.

::: {.proof}
The columns of a matrix are the images of the standard basis under the
associated linear map
$$
F^n\longrightarrow F^n.
$$
The matrix is invertible exactly when this map is an isomorphism, which is
equivalent to its images of the standard basis forming a basis.
:::

<1>3. After choosing $j-1$ linearly independent columns, their span has
exactly
$$
q^{j-1}
$$
elements.

::: {.proof}
The span of $j-1$ linearly independent vectors is a
$(j-1)$-dimensional vector space over $F$. Step <1>1 applied in dimension
$j-1$ gives $q^{j-1}$ elements.
:::

<1>4. The order of the general linear group is
$$
\boxed{
\abs{GL_n(F)}
=
\prod_{j=0}^{n-1}(q^n-q^j).
}
$$

::: {.proof}
The first column can be any nonzero vector, giving $q^n-1$ choices.
After $j-1$ independent columns have been chosen, step <1>3 says their
span has $q^{j-1}$ elements, so the $j$th column has
$$
q^n-q^{j-1}
$$
available choices. Multiplying the numbers of choices for
$j=1,\ldots,n$ gives
$$
(q^n-1)(q^n-q)\cdots(q^n-q^{n-1}),
$$
which is the displayed product.
:::

<1>5. The determinant map
$$
\det:GL_n(F)\longrightarrow F^\times
$$
is a surjective group homomorphism with kernel $SL_n(F)$.

::: {.proof}
Multiplicativity of determinant makes it a group homomorphism, and by
definition its kernel is $SL_n(F)$. For any $a\in F^\times$, the diagonal
matrix
$$
\operatorname{diag}(a,1,\ldots,1)
$$
has determinant $a$, so the map is surjective.
:::

<1>6. The multiplicative group $F^\times$ has order
$$
q-1.
$$

::: {.proof}
The field $F$ has $q$ elements, exactly one of which is zero.
:::

<1>7. The order of the special linear group is
$$
\boxed{
\abs{SL_n(F)}
=
\frac1{q-1}
\prod_{j=0}^{n-1}(q^n-q^j).
}
$$

::: {.proof}
By step <1>5 and the first isomorphism theorem,
$$
GL_n(F)/SL_n(F)\cong F^\times.
$$
Hence
$$
\frac{\abs{GL_n(F)}}{\abs{SL_n(F)}}
=
\abs{F^\times}
=
q-1
$$
by step <1>6. Substitute the formula from step <1>4 and solve for
$\abs{SL_n(F)}$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>1 answers part (1), step <1>4 answers part (2), and step <1>7
answers part (3).
:::
:::
