---
schema: qual/card@1
id: P-BERK98S-15
kind: problem
title: A quartic orthogonal to all lower-degree polynomials on $[-1,1]$
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
  date: 2026-09-23
---

::: {.problem}
For continuous real-valued functions on $[-1,1]$, define
\[
\langle f,g\rangle=\int_{-1}^1f(x)g(x)\,dx.
\]
Find the polynomial
\[
p(x)=a+bx^2-x^4
\]
that is orthogonal to every polynomial of lower degree.
:::

::: {.solution}
<1>1. It is enough to impose
$$
\langle p,1\rangle=0
\qquad\text{and}\qquad
\langle p,x^2\rangle=0.
$$

::: {.proof}
The polynomials of degree less than $4$ are spanned by
$$
1,\qquad x,\qquad x^2,\qquad x^3.
$$
The polynomial
$$
p(x)=a+bx^2-x^4
$$
is even. Hence $p(x)x$ and $p(x)x^3$ are odd, so their integrals over the
symmetric interval $[-1,1]$ vanish automatically. Thus only the two even
basis elements give conditions.
:::

<1>2. The condition $\langle p,1\rangle=0$ is
$$
a+\frac b3=\frac15.
$$

::: {.proof}
Using
$$
\int_{-1}^1x^{2k}\,dx=\frac{2}{2k+1},
$$
we obtain
$$
0
=
\int_{-1}^1(a+bx^2-x^4)\,dx
=
2a+\frac{2b}{3}-\frac25.
$$
Dividing by $2$ gives the displayed equation.
:::

<1>3. The condition $\langle p,x^2\rangle=0$ is
$$
\frac a3+\frac b5=\frac17.
$$

::: {.proof}
One has
$$
0
=
\int_{-1}^1(a+bx^2-x^4)x^2\,dx
=
\frac{2a}{3}+\frac{2b}{5}-\frac27.
$$
Dividing by $2$ gives the displayed equation.
:::

<1>4. The unique solution of the two equations in steps <1>2 and <1>3 is
$$
a=-\frac3{35},
\qquad
b=\frac67.
$$

::: {.proof}
From step <1>2,
$$
a=\frac15-\frac b3.
$$
Substitution into step <1>3 gives
$$
\frac1{15}
-\frac b9
+\frac b5
=
\frac17.
$$
Hence
$$
\frac{4b}{45}
=
\frac17-\frac1{15}
=
\frac8{105},
$$
so $b=6/7$, and then
$$
a
=
\frac15-\frac27
=
-\frac3{35}.
$$
:::

<1>5. Therefore the required polynomial is
$$
\boxed{
p(x)
=
-\frac3{35}
+\frac67x^2
-x^4
}.
$$

::: {.proof}
Steps <1>2--<1>4 make $p$ orthogonal to $1$ and $x^2$, and step <1>1 then
makes it orthogonal to every polynomial of degree less than $4$.
Uniqueness follows because the two independent linear equations in steps
<1>2 and <1>3 have the unique solution found in step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required polynomial.
:::
:::
