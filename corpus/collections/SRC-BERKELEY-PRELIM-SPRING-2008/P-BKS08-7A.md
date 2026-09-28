---
schema: qual/card@1
id: P-BKS08-7A
kind: problem
title: Irreducible polynomials of degree at most $4$ over $\FF_2$
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
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the root tests in degrees two and three and the
    complete degree-four elimination of the unique irreducible quadratic
    factor against the vendored solution.
---

::: {.problem}
Find all irreducible polynomials of degree at most $4$ over $\mathbb F_2$.
:::

::: {.solution}
<1>1. The irreducible polynomials of degree $1$ are
$$
x,
\qquad
x+1.
$$

::: {.proof}
These are exactly the two monic linear polynomials over $\FF_2$, and
every nonconstant linear polynomial over a field is irreducible.
:::

<1>2. The unique irreducible polynomial of degree $2$ is
$$
x^2+x+1.
$$

::: {.proof}
A monic quadratic over a field is irreducible exactly when it has no
root in that field. An irreducible quadratic over $\FF_2$ must have
constant term $1$, so the only possibilities are
$$
x^2+1,
\qquad
x^2+x+1.
$$
The first has $1$ as a root, while the second takes the value $1$ at
both $0$ and $1$. Hence only $x^2+x+1$ is irreducible.
:::

<1>3. The irreducible polynomials of degree $3$ are
$$
x^3+x+1,
\qquad
x^3+x^2+1.
$$

::: {.proof}
A reducible cubic over a field has a linear factor, so a cubic over
$\FF_2$ is irreducible exactly when it has no root in $\FF_2$.
Any irreducible cubic must have constant term $1$, so write
$$
f(x)=x^3+ax^2+bx+1.
$$
The condition $f(0)\ne0$ already holds, while
$$
f(1)=a+b.
$$
Thus $f(1)\ne0$ exactly when $a+b=1$. The two possibilities are
$(a,b)=(0,1)$ and $(1,0)$, giving the displayed cubics.
:::

<1>4. A monic quartic over $\FF_2$ with no root in $\FF_2$ is one of
$$
\begin{aligned}
&x^4+x^3+1,\qquad x^4+x^2+1,\\
&x^4+x+1,\qquad x^4+x^3+x^2+x+1.
\end{aligned}
$$

::: {.proof}
An irreducible quartic must have constant term $1$, so write
$$
f(x)=x^4+ax^3+bx^2+cx+1.
$$
Again $f(0)=1$, and
$$
f(1)=a+b+c.
$$
Thus the absence of roots in $\FF_2$ is equivalent to
$a+b+c=1$. The four triples of odd parity give exactly the four
polynomials displayed above.
:::

<1>5. Among the four quartics in step <1>4, exactly
$$
x^4+x^2+1
$$
is reducible.

::: {.proof}
A reducible quartic with no linear factor must be a product of two
irreducible quadratics. By step <1>2, the only irreducible quadratic
over $\FF_2$ is $q(x)=x^2+x+1$. Hence the only such reducible quartic
is
$$
q(x)^2=(x^2+x+1)^2=x^4+x^2+1.
$$
Therefore the other three quartics in step <1>4 are irreducible.
:::

<1>6. The complete list is
$$
\boxed{
\begin{gathered}
x,\quad x+1,\\
x^2+x+1,\\
x^3+x+1,\quad x^3+x^2+1,\\
x^4+x+1,\quad x^4+x^3+1,\quad
x^4+x^3+x^2+x+1.
\end{gathered}
}
$$

::: {.proof}
Steps <1>1--<1>5 classify every degree from $1$ through $4$ and show
that no other polynomial in those degrees is irreducible.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested list.
:::
:::
