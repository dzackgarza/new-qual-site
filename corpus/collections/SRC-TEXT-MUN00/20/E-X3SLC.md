---
schema: qual/card@1
id: E-X3SLC
kind: problem
title: A bounded metric giving the same topology
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $d$ is a metric for $X$, then

$$
d'(x, y) = d(x, y) / (1 + d(x, y))
$$

is a bounded metric that gives the topology of $X$.
[Hint: If $f(x) = x/(1+x)$ for $x > 0$, use the mean-value theorem to show that $f(a+b) - f(b) \leq f(a)$.]
:::

::: {.solution}
<1>1. $d'$ is a metric.
<2>1. $d'(x,y) \ge 0$ and $d'(x,y) = 0$ iff $x = y$.
::: {.proof}
$d(x,y) \ge 0$ and $d(x,y) = 0$ iff $x = y$, and $d/(1+d) = 0$ iff $d = 0$.
:::
<2>2. $d'(x,y) = d'(y,x)$.
::: {.proof}
$d$ is symmetric.
:::
<2>3. Triangle inequality: $d'(x,z) \le d'(x,y) + d'(y,z)$.
::: {.proof}
let $f(t) = t/(1+t)$; $f$ is increasing and concave, and $f(a+b) \le f(a) + f(b)$ for $a, b \ge 0$ (by the hint, $f(a+b) - f(b) \le f(a)$). Hence $d'(x,z) = f(d(x,z)) \le f(d(x,y) + d(y,z)) \le f(d(x,y)) + f(d(y,z)) = d'(x,y) + d'(y,z)$.
:::

<1>2. $d'$ is bounded.
::: {.proof}
$d'(x,y) = \frac{d(x,y)}{1+d(x,y)} < 1$ for all $x, y$.
:::

<1>3. $d'$ gives the same topology as $d$.
<2>1. $d'(x,y) \le d(x,y)$.
::: {.proof}
$\frac{d}{1+d} \le d$ since $1 + d \ge 1$.
:::
<2>2. For $d(x,y) < 1$, $d(x,y) \le 2d'(x,y)$.
::: {.proof}
$d' = \frac{d}{1+d} \ge \frac{d}{2}$ when $d < 1$ (since $1 + d < 2$).
:::
<2>3. Hence the $d$-balls and $d'$-balls are mutually cofinal, so the topologies coincide.
::: {.proof}
<2>1 and <2>2 show that every $d'$-ball contains a $d$-ball and every small $d$-ball contains a $d'$-ball.
:::

<1>4. Q.E.D.
::: {.proof}
<1>1, <1>2, and <1>3.
:::
:::
