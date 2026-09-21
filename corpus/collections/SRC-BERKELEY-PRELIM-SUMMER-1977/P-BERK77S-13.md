---
schema: qual/card@1
id: P-BERK77S-13
kind: problem
title: Radius of convergence after re-expanding $1+2z+3z^2+\cdots$ about $-2$
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
    Summed the original series to 1/(1-z)^2, re-expanded this function at
    z=-2 as (3-(z+2))^-2, and obtained a_n=(n+1)/3^(n+2). The resulting
    coefficient series has radius three by the ratio test.
---

::: {.problem}
Let $f$ be analytic and suppose
\[
f(z)=1+2z+3z^2+\cdots
\qquad(|z|<1).
\]
Define real numbers $a_0,a_1,a_2,\dots$ by
\[
f(z)=\sum_{n=0}^\infty a_n(z+2)^n.
\]
What is the radius of convergence of
\[
\sum_{n=0}^\infty a_nz^n?
\]
:::

::: {.solution}
<1>1. For $\abs{z}<1$,
$$
f(z)=\frac1{(1-z)^2}.
$$

::: {.proof}
The geometric series gives
$$
\frac1{1-z}
=
\sum_{n=0}^{\infty}z^n
$$
for $\abs{z}<1$. Differentiating term by term,
$$
\frac1{(1-z)^2}
=
\sum_{n=1}^{\infty}nz^{n-1}
=
\sum_{n=0}^{\infty}(n+1)z^n.
$$
This is exactly the series
$$
1+2z+3z^2+\cdots.
$$
:::

<1>2. Writing
$$
w=z+2,
$$
one has
$$
f(z)
=
\frac1{(3-w)^2}.
$$

::: {.proof}
Since $z=w-2$,
$$
1-z
=
1-(w-2)
=
3-w.
$$
Substitute this into the expression from step <1>1. By uniqueness of
analytic continuation, this rational expression is the analytic function
whose Taylor expansion at $z=-2$ defines the coefficients $a_n$.
:::

<1>3. For $\abs{w}<3$,
$$
\frac1{(3-w)^2}
=
\sum_{n=0}^{\infty}
\frac{n+1}{3^{n+2}}w^n.
$$

::: {.proof}
Factor
$$
\frac1{(3-w)^2}
=
\frac1{9}
\frac1{(1-w/3)^2}.
$$
Using the differentiated geometric-series identity from step <1>1 with
$w/3$ in place of $z$ gives
$$
\frac1{(1-w/3)^2}
=
\sum_{n=0}^{\infty}(n+1)\left(\frac w3\right)^n
$$
for $\abs{w}<3$. Multiplying by $1/9$ gives the displayed expansion.
:::

<1>4. The coefficients in the expansion about $-2$ are
$$
a_n=\frac{n+1}{3^{n+2}}.
$$

::: {.proof}
By the definition of the $a_n$,
$$
f(z)
=
\sum_{n=0}^{\infty}a_n(z+2)^n
=
\sum_{n=0}^{\infty}a_nw^n.
$$
Uniqueness of power-series coefficients and step <1>3 give the formula.
:::

<1>5. The series
$$
\sum_{n=0}^{\infty}a_nz^n
$$
has radius of convergence
$$
\boxed{3}.
$$

::: {.proof}
For $a_n=(n+1)/3^{n+2}$,
$$
\abs{\frac{a_{n+1}}{a_n}}
=
\frac{n+2}{3(n+1)}
\longrightarrow
\frac13.
$$
The ratio test therefore gives radius of convergence
$$
R=\frac1{1/3}=3.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested radius.
:::
:::
