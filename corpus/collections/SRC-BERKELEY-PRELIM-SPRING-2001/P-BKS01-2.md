---
schema: qual/card@1
id: P-BKS01-2
kind: problem
title: A continuous period-one function agrees with every translate somewhere
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    For g(x)=f(x+c)-f(x), periodicity makes the integral of g over one
    period zero. If g had no zero, continuity on [0,1] would force one
    strict sign and hence a nonzero integral.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and periodic with period $1$.
Prove that for every $c\in\mathbb R$ there exists $x_0\in\mathbb R$ such that
\[
f(x_0+c)=f(x_0).
\]
:::

::: {.solution}
Fix $c\in\RR$ and define
$$
g(x)=f(x+c)-f(x).
$$

<1>1. The function $g$ is continuous and satisfies
$$
\int_0^1 g(x)\,dx=0.
$$

::: {.proof}
Continuity is immediate from continuity of $f$. Also
$$
\int_0^1 f(x+c)\,dx
=
\int_c^{c+1}f(u)\,du.
$$
Because $f$ has period $1$, its integral over every interval of length
$1$ is the same. Hence
$$
\int_c^{c+1}f(u)\,du
=
\int_0^1f(u)\,du.
$$
Subtracting gives the claim.
:::

<1>2. There exists $x_0\in[0,1]$ such that
$$
g(x_0)=0.
$$

::: {.proof}
Suppose $g$ had no zero on $[0,1]$. Since $[0,1]$ is connected and
$g$ is continuous, $g$ would be either strictly positive everywhere or
strictly negative everywhere. Its integral over $[0,1]$ would then be
strictly positive or strictly negative, contradicting step <1>1.
:::

<1>3. The point $x_0$ from step <1>2 satisfies
$$
f(x_0+c)=f(x_0).
$$

::: {.proof}
This is exactly the identity $g(x_0)=0$ under the definition of $g$.
:::

<1>4. Q.E.D.

::: {.proof}
The number $c\in\RR$ was arbitrary, so step <1>3 proves the claim for
every real $c$.
:::
:::
