---
schema: qual/card@1
id: E-SMI-8000E-GG5
kind: problem
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
A monic quadratic over $\FF_3$ is irreducible if and only if it has no root in $\FF_3$. Evaluating the $9$ monic quadratics at $0, 1, 2$ leaves exactly these three.
:::
<2>2. None of these divides $f$.
::: {.proof}
Division in $\FF_3[X]$ gives remainders $-1$, $X - 1$, and $X - 1$ respectively, all nonzero.
:::

<1>3. $f$ is irreducible over $\FF_3$.
::: {.proof}
A reducible polynomial of degree $5$ has an irreducible factor of degree $1$ or $2$. Step <1>1 excludes a linear factor, and step <1>2 excludes an irreducible quadratic factor.
:::

<1>4. $f$ is separable over $\FF_3$.
<2>1. $f'(X) = 5X^4 - 1 = 2X^4 - 1$ in $\FF_3[X]$.
::: {.proof}
$5 \equiv 2 \pmod 3$.
:::
<2>2. $\gcd(f, f') = 1$.
::: {.proof}
$f$ is irreducible by step <1>3, and $f'$ is nonzero of degree $4 < 5$, so $f \nmid f'$. A common factor of $f$ and $f'$ of positive degree would be an associate of $f$, so the gcd is $1$.
:::
<2>3. Q.E.D.
::: {.proof}
A polynomial $f$ has no repeated roots in any extension if and only if $\gcd(f, f') = 1$, which is step <2>2.
:::

<1>5. Q.E.D.
::: {.proof}
Steps <1>3 and <1>4.
:::
:::
