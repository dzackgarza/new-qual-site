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
Let $f(t)=t/(1+t)=1-1/(1+t)$ for $t\ge0$, so that $d'=f\circ d$; $f$ is increasing, $f(0)=0$, and $0\le f<1$.

<1>1. $f(a+b)\le f(a)+f(b)$ for $a,b\ge0$.

::: {.proof}
$$
f(a+b)=\frac a{1+a+b}+\frac b{1+a+b}\le\frac a{1+a}+\frac b{1+b}.
$$
:::

<1>2. $d'$ is a metric bounded by $1$.

::: {.proof}
$d'\ge0$, with $d'(x,y)=0$ if and only if $d(x,y)=0$, that is, $x=y$; $d'$ is symmetric because $d$ is; and $d'<1$ because $f<1$.
Since $f$ is increasing, step <1>1 gives
$$
d'(x,z)=f(d(x,z))\le f(d(x,y)+d(y,z))\le d'(x,y)+d'(y,z).
$$
:::

<1>3. For $0<r\le\frac12$ and every $x$, $B_d(x,r)\subseteq B_{d'}(x,r)$ and $B_{d'}(x,r)\subseteq B_d(x,2r)$.

::: {.proof}
$d'\le d$ gives the first inclusion.
If $d'(x,y)<r\le\frac12$, then $d(x,y)=d'(x,y)/(1-d'(x,y))<r/(1-r)\le2r$.
:::

<1>4. Q.E.D.

::: {.proof}
By step <1>3, every ball of either metric about a point contains a ball of the other metric about that point, so $d$ and $d'$ have the same open sets; step <1>2 shows that $d'$ is a bounded metric.
:::
:::
