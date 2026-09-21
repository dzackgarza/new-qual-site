---
schema: qual/card@1
id: P-PRELIM82S-12
kind: problem
title: Irreducibility over $\mathbb Q$ of four quadratic and cubic polynomials
classification:
  areas:
  - prelim
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
    A quadratic or cubic over Q is reducible exactly when it has a
    rational root. The first polynomial has no real root; the second
    factors as (x-13)(x+13); the third factors as (x+1)(x^2+1); and
    the fourth has no rational root, since a reduced rational root must
    be an integer divisor of 4 and none of ±1, ±2, ±4 is a root.
---

::: {.problem}
Determine, with proof, which of the following polynomials are irreducible over $\mathbb Q$:

1. $x^2+3$;

2. $x^2-169$;

3. $x^3+x^2+x+1$;

4. $x^3+2x^2+3x+4$.
:::

::: {.solution}
<1>1. A polynomial in $\QQ[x]$ of degree $2$ or $3$ is reducible over
$\QQ$ if and only if it has a root in $\QQ$.

::: {.proof}
If such a polynomial has a root $r\in\QQ$, then the factor theorem
gives a nontrivial factor $x-r$, so the polynomial is reducible.
Conversely, suppose a polynomial of degree $2$ or $3$ factors
nontrivially over $\QQ$. The positive degrees of its two factors add to
$2$ or $3$, so at least one factor has degree $1$. A linear factor over
$\QQ$ has a root in $\QQ$, which is also a root of the original
polynomial.
:::

<1>2. Item 1,
$$
x^2+3,
$$
is irreducible over $\QQ$.

::: {.proof}
For every $r\in\QQ\subset\RR$,
$$
r^2+3>0.
$$
Thus the polynomial has no rational root. Step <1>1 implies that it is
irreducible.
:::

<1>3. Item 2,
$$
x^2-169,
$$
is reducible over $\QQ$.

::: {.proof}
One has
$$
x^2-169
=
(x-13)(x+13),
$$
a nontrivial factorization in $\QQ[x]$.
:::

<1>4. Item 3,
$$
x^3+x^2+x+1,
$$
is reducible over $\QQ$.

::: {.proof}
Grouping terms gives
$$
\begin{aligned}
x^3+x^2+x+1
&=
x^2(x+1)+(x+1)\\
&=
(x+1)(x^2+1).
\end{aligned}
$$
Both factors have positive degree.
:::

<1>5. If
$$
P(x)=x^3+2x^2+3x+4
$$
has a rational root, then that root belongs to
$$
\{-4,-2,-1,1,2,4\}.
$$

::: {.proof}
Suppose $a/b\in\QQ$ is a root, where $a,b\in\ZZ$, $b>0$, and
$\gcd(a,b)=1$. Multiplying
$$
\left(\frac ab\right)^3
+2\left(\frac ab\right)^2
+3\left(\frac ab\right)
+4
=0
$$
by $b^3$ gives
$$
a^3+2a^2b+3ab^2+4b^3=0.
$$
Hence $b\mid a^3$. Since $\gcd(a,b)=1$, this forces $b=1$, so the root
is an integer $a$. The equation
$$
a(a^2+2a+3)=-4
$$
then shows that $a$ divides $4$. Therefore
$$
a\in\{-4,-2,-1,1,2,4\}.
$$
:::

<1>6. Item 4,
$$
x^3+2x^2+3x+4,
$$
is irreducible over $\QQ$.

::: {.proof}
For the six possible rational roots from step <1>5,
$$
\begin{aligned}
P(-4)&=-40,&
P(-2)&=-2,&
P(-1)&=2,\\
P(1)&=10,&
P(2)&=26,&
P(4)&=112.
\end{aligned}
$$
None is zero. Thus the polynomial has no rational root, and step <1>1
implies that it is irreducible.
:::

<1>7. Therefore the irreducible polynomials are exactly
$$
\boxed{x^2+3}
\qquad\text{and}\qquad
\boxed{x^3+2x^2+3x+4}.
$$

::: {.proof}
Step <1>2 proves item 1 irreducible, step <1>3 proves item 2 reducible,
step <1>4 proves item 3 reducible, and step <1>6 proves item 4
irreducible.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 gives the requested classification.
:::
:::
