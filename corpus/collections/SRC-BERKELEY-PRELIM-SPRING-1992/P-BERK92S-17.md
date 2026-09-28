---
schema: qual/card@1
id: P-BERK92S-17
kind: problem
title: Positive solutions of $\log_a x=x^b$
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
For which positive numbers $a,b$, with $a>1$, does the equation
\[
\log_a x=x^b
\]
have a positive solution $x$?
:::

::: {.solution}
Since $a>1$, we have $\log a>0$.

<1>1. Any solution must satisfy $x>1$, and the equation is equivalent
to
$$
\frac{\log x}{x^b}=\log a.
$$

::: {.proof}
The right-hand side $x^b$ is positive, so
$\log_a x>0$. Because $a>1$, this implies $x>1$. Using
$$
\log_a x=\frac{\log x}{\log a}
$$
and multiplying by the positive number $\log a/x^b$ gives the stated
equation.
:::

<1>2. For
$$
h(x)\coloneqq\frac{\log x}{x^b}
\qquad(x>1),
$$
the maximum value is
$$
\max_{x>1}h(x)=\frac1{be}.
$$

::: {.proof}
Differentiate:
$$
h'(x)
=x^{-b-1}(1-b\log x).
$$
Thus $h$ increases on
$1<x<e^{1/b}$ and decreases on $x>e^{1/b}$. Moreover,
$$
\lim_{x\downarrow1}h(x)=0,
\qquad
\lim_{x\to\infty}h(x)=0.
$$
Hence the unique maximum occurs at $x=e^{1/b}$, where
$$
h(e^{1/b})
=\frac{1/b}{e}
=\frac1{be}.
$$
:::

<1>3. The equation has a positive solution exactly when
$$
\boxed{b\log a\le\frac1e}.
$$

::: {.proof}
By step <1>1, solutions are exactly the points $x>1$ for which
$h(x)=\log a$. Since $\log a>0$, step <1>2 and continuity of $h$ show
that such a point exists if and only if
$$
\log a\le\frac1{be},
$$
which is equivalent to the displayed condition.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the complete parameter range.
:::
:::
