---
schema: qual/card@1
id: P-TOPS25C
kind: problem
title: Homology of a torus with two discs attached
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $T$ be the standard torus, and let $e$ and $f$ be generators of $H_1(T; \mathbb{Z}) \cong \mathbb{Z}^2$.
Now let $X$ be the space obtained by gluing two discs onto $T$ along their boundary circles: the first attaches along a curve with homology class $e + 4f$, and the second along a curve with homology class $4e + f$.
Calculate the integral homology groups $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. With the standard CW structure on the torus, attaching the two new $2$-cells gives
$$C_2\cong\mathbb Z^3\xrightarrow{\partial_2}C_1\cong\mathbb Z^2,$$
where the original torus $2$-cell has zero boundary and the two new columns are $(1,4)^T$ and $(4,1)^T$.
::: {.proof}
The cellular boundary records the homology classes of the attaching loops in the $1$-skeleton after abelianization.
:::

<1>2. The matrix
$$A=\begin{pmatrix}1&4\\4&1\end{pmatrix}$$
has determinant $-15$, so it has rank $2$, cokernel $\mathbb Z/15$, and zero kernel.
::: {.proof}
Its Smith normal form is $\operatorname{diag}(1,15)$ because the gcd of its entries is $1$ and $|\det A|=15$.
:::

<1>3. Hence
$$\boxed{H_i(X;\mathbb Z)\cong\begin{cases}\mathbb Z,&i=0,2,\\\mathbb Z/15,&i=1,\\0,&i\ge3.\end{cases}}$$
::: {.proof}
The original torus $2$-cell spans the kernel of $\partial_2$, giving $H_2\cong\mathbb Z$; <1>2 gives $H_1$, and the complex has no cells above dimension $2$.
:::
:::
