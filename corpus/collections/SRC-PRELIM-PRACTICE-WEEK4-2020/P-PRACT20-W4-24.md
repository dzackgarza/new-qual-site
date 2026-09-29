---
schema: qual/card@1
id: P-PRACT20-W4-24
kind: problem
title: $1+xy+x^2y^2$ is not a sum of two products of one-variable polynomials
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Polynomials
  - Rank and Nullity
relations: []
review: draft
---

::: {.problem}
Show that there are no polynomials $a , b , c , d : \mathbb { R } \to \mathbb { R }$ such that

$$
1 + x y + x ^ { 2 } y ^ { 2 } = a ( x ) b ( y ) + c ( x ) d ( y )
$$

for all $x , y \in \mathbb { R }$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The polynomials
$$
1,
\qquad
x^2+x+1,
\qquad
x^2-x+1
$$
are linearly independent.

::: pf-proof

Suppose
$$
\alpha+\beta(x^2+x+1)+\gamma(x^2-x+1)=0.
$$
Comparing the coefficients of $1$, $x$, and $x^2$ gives
$$
\alpha+\beta+\gamma=0,
\qquad
\beta-\gamma=0,
\qquad
\beta+\gamma=0.
$$
The last two equations imply $\beta=\gamma=0$, and then the first gives $\alpha=0$.

:::

:::

::: {.pf-step #s2}

Any representation
$$
1+xy+x^2y^2=a(x)b(y)+c(x)d(y)
$$
would put all three polynomials from step [](#s1){.pf-ref} in the span of $a$ and $c$.

::: pf-proof

Evaluate the identity at $y=0,1,-1$. We obtain
$$
1=a(x)b(0)+c(x)d(0),
$$
$$
x^2+x+1=a(x)b(1)+c(x)d(1),
$$
and
$$
x^2-x+1=a(x)b(-1)+c(x)d(-1).
$$
Thus each of these three polynomials lies in
$$
\operatorname{span}_{\mathbb R}\{a(x),c(x)\},
$$
whose dimension is at most $2$.

:::

:::

::: {.pf-step #s3}

No such polynomials $a,b,c,d$ exist.

::: pf-proof

Step [](#s1){.pf-ref} gives three linearly independent polynomials, while step [](#s2){.pf-ref} would place them in a space of dimension at most $2$. This is impossible.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the required nonexistence.

:::

:::

:::
