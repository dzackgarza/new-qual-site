---
schema: qual/card@1
id: P-PC6ZW
kind: problem
title: A finite free module remains free of the same rank after reducing modulo an
  ideal
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Bases
  - Tensor Products
relations: []
review: draft
---

::: {.problem}
Let $R$ be a commutative ring with 1.
Suppose that $M$ is a free $R\dash$module with a finite basis $X$.

a.
Let $I \normal R$ be a proper ideal.
Prove that $M/IM$ is a free $R/I\dash$module with basis $X'$, where $X'$ is the image of $X$ under the canonical map $M\to M/IM$.

b.
Prove that any two bases of $M$ have the same number of elements.
You may assume that the result is true when $R$ is a field.

:::


::: {.solution}

<1>1. The images of the elements of $X$ form an $R/I$-basis of $M/IM$.

::: {.proof}
Write $X=\{e_1,\ldots,e_n\}$. The chosen basis yields an isomorphism $R^n\to M$ carrying $I^n$ onto $IM$. Passing to quotients gives an $R/I$-linear isomorphism $(R/I)^n\to M/IM$ carrying the standard basis onto the images of $X$. This also proves part (a) directly.
:::

<1>2. If $R$ is nonzero, any two finite bases of $M$ have the same cardinality.

::: {.proof}
Choose a maximal ideal $\mathfrak m$ of $R$, which exists by Zorn's lemma. If $X$ and $Y$ have cardinalities $n$ and $m$, respectively, step <1>1 gives bases of cardinalities $n$ and $m$ for the vector space $M/\mathfrak mM$ over the field $R/\mathfrak m$. By uniqueness of finite vector-space dimension, $n=m$.
:::

<1>3. Without the nonzero-ring hypothesis, part (b) is false.

::: {.proof}
Over the zero ring, the zero module is isomorphic to $R^n$ for every $n\geq0$. It therefore admits finite bases of different cardinalities. Thus part (b) requires $1\neq0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 establishes part (a); steps <1>2 and <1>3 determine exactly when the assertion in part (b) is valid.
:::


:::
