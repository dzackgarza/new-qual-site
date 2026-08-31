---
schema: qual/card@1
id: E-SMI-8000E-GG5
kind: exercise
title: X^5 - X - 1 is irreducible and separable mod 3
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Show that $X^5 - X - 1$ is irreducible and separable mod 3.
:::

::: {.solution}
Let $f(X) = X^5 - X - 1 \in \FF_3[X]$.

<1>1. $f$ has no root in $\FF_3$.
::: {.proof}
$f(0) = -1 = 2$, $f(1) = 1 - 1 - 1 = -1 = 2$, $f(2) = 32 - 2 - 1 = 29 = 2$ in $\FF_3$; none is $0$.
:::

<1>2. $f$ has no irreducible quadratic factor over $\FF_3$.
<2>1. The monic irreducible quadratics over $\FF_3$ are $X^2 + 1$, $X^2 + X + 2$, and $X^2 + 2X + 2$.
::: {.proof}
a monic quadratic is irreducible iff it has no root in $\FF_3$; checking the $9$ monic quadratics leaves exactly these three.
:::
<2>2. None of these divides $f$.
::: {.proof}
division in $\FF_3[X]$ gives remainders $-1$, $X - 1$, and $X - 1$ respectively, all nonzero.
:::

<1>3. Hence $f$ is irreducible over $\FF_3$.
::: {.proof}
$f$ has degree $5$; if reducible it would have a factor of degree $1$ or $2$. <1>1 rules out a linear factor, <1>2 rules out a quadratic factor.
:::

<1>4. $f$ is separable over $\FF_3$.
<2>1. $f'(X) = 5X^4 - 1 = 2X^4 - 1$ in $\FF_3[X]$.
::: {.proof}
$5 \equiv 2 \pmod 3$.
:::
<2>2. $\gcd(f, f') = 1$.
::: {.proof}
$f$ is irreducible (<1>3) and $f'$ has degree $4 < 5$, so $f \nmid f'$; hence the gcd is $1$.
:::
<2>3. Therefore $f$ has no repeated roots in any extension.
::: {.proof}
a polynomial is separable iff $\gcd(f, f') = 1$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>3 and <1>4.
:::
:::
