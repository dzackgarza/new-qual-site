---
schema: qual/card@1
id: P-PRACT20-W4-17
kind: problem
title: Dimension of cubic polynomials vanishing at $-1$, $0$, $1$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Polynomials
  - Dimension
relations: []
review: draft
---

::: {.problem}
What is the dimension of the space of all polynomials p of degree at most 3 such that $p ( - 1 ) = p ( 0 ) = p ( 1 ) = 0 ?$
:::

::: {.solution}
<1>1. Every polynomial in the space is a scalar multiple of $x(x-1)(x+1)$.
::: {.proof}
If $p(-1)=p(0)=p(1)=0$, then the three distinct linear factors
$$
x+1,\qquad x,\qquad x-1
$$
all divide $p$. Hence
$$
x(x-1)(x+1)\mid p.
$$
Since $\deg p\le3$, the quotient is constant. Thus
$$
p(x)=\alpha x(x-1)(x+1)
$$
for some $\alpha\in\mathbb R$.
:::

<1>2. The dimension is $\boxed{1}$.
::: {.proof}
Step <1>1 identifies the space with
$$
\operatorname{span}_{\mathbb R}\{x(x-1)(x+1)\}.
$$
The spanning polynomial is nonzero, so this span is one-dimensional.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 gives the requested dimension.
:::
:::
