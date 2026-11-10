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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 11, printed p. 128, with its
    bracketed hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 20.11, printed p. 231.
    The answer is his. The subadditivity of t/(1+t), which replaces the book's mean-value-
    theorem hint and yields the same estimate, is proved by clearing denominators, and the
    identity d'(x,y) < u iff d(x,y) < u/(1-u) for u < 1 shows that the balls of the two
    metrics agree. (tmp/sources/munkres-solutions-whitman.pdf).
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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 20.11, printed p. 231** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer is his. The subadditivity used below replaces the book's mean-value-theorem hint and gives the same estimate.

Let $d$ be a metric for $X$ and $d'(x,y)=d(x,y)/(1+d(x,y))$; then $0\le d'<1$, so $d'$ is bounded.

*$d'$ is a metric.* It is nonnegative, vanishes exactly when $d(x,y)=0$, and is symmetric. Let $f(t)=t/(1+t)$ for $t\ge0$, so that $d'=f\circ d$. For $s,t\ge0$,
$$
f(s+t)=\frac{s+t}{1+s+t}\le\frac{s}{1+s}+\frac{t}{1+t}=f(s)+f(t),
$$
because after multiplying by $(1+s)(1+t)(1+s+t)>0$ the inequality becomes $(s+t)(1+s)(1+t)\le s(1+t)(1+s+t)+t(1+s)(1+s+t)$, that is $s^{2}t+st^{2}\ge0$. Hence, with $a=d(x,z)$, $b=d(z,y)$, $c=d(x,y)\le a+b$ and $f$ increasing on $[0,\infty)$,
$$
d'(x,y)=f(c)\le f(a+b)\le f(a)+f(b)=d'(x,z)+d'(z,y).
$$

*$d'$ induces the topology of $d$.* For $u\in[0,1)$ one has $d'(x,y)<u\iff d(x,y)<u/(1-u)$, since $t\mapsto t/(1+t)$ is strictly increasing with inverse $u\mapsto u/(1-u)$. Hence for every $x$ and every $u\in(0,1)$,
$$
B_{d'}(x,u)=B_{d}\big(x,u/(1-u)\big),
$$
and every $d$-ball of radius $r>0$ contains the $d'$-ball of radius $u=r/(1+r)\in(0,1)$ around the same point. So each topology is finer than the other: they coincide.
:::
