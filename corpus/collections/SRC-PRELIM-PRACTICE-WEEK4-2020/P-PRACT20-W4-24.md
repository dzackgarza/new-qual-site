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
<1>1. The polynomials
$$
1,
\qquad
x^2+x+1,
\qquad
x^2-x+1
$$
are linearly independent.
::: {.proof}
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

<1>2. Any representation
$$
1+xy+x^2y^2=a(x)b(y)+c(x)d(y)
$$
would put all three polynomials from step <1>1 in the span of $a$ and $c$.
::: {.proof}
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

<1>3. No such polynomials $a,b,c,d$ exist.
::: {.proof}
Step <1>1 gives three linearly independent polynomials, while step <1>2 would place them in a space of dimension at most $2$. This is impossible.
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 proves the required nonexistence.
:::
:::
