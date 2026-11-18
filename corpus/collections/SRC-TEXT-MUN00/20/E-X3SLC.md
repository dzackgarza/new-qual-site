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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that d' = d/(1+d) is bounded, symmetric and
    vanishes only on the diagonal, that f(t)=t/(1+t) is strictly increasing and subadditive
    (the difference st(2+s+t) >= 0 after clearing denominators; the earlier prose recorded s^2 t + s t^2, which is not what remains), the triangle inequality
    through increasingness and subadditivity, and the identity B_{d'}(x,u) = B_d(x, u/(1-u))
    for 0 < u < 1, which gives the same topology. Whitman, Exercise 20.11, printed p. 231.
    The printed statement needed no repair.
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
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 20.11, printed p. 231** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer is his. The subadditivity proved below replaces the book's mean-value-theorem hint and gives the same estimate.

Let $d$ be a metric for $X$ and $d'(x,y)=d(x,y)/\big(1+d(x,y)\big)$.

::: pf

::: {.pf-step #bounded}
$0\le d'(x,y)<1$ for all $x,y$, so $d'$ is bounded.

::: pf-proof
$d(x,y)\ge0$ gives $d'\ge0$, and $d(x,y)<1+d(x,y)$ gives $d'<1$.
:::

:::

::: {.pf-step #symmetric}
$d'(x,y)=d'(y,x)$, and $d'(x,y)=0$ exactly when $x=y$.

::: pf-proof
$d(y,x)=d(x,y)$, so the two quotients are equal. Also $d'(x,y)=0$ exactly when the numerator $d(x,y)$ is $0$, that is exactly when $x=y$.
:::

:::

::: {.pf-step #subadditive}
With $f(t)=t/(1+t)$ for $t\ge0$ one has $f(s+t)\le f(s)+f(t)$ for $s,t\ge0$, and $f$ is strictly increasing.

::: pf-proof
For $s,t\ge0$ the inequality $f(s+t)\le f(s)+f(t)$ holds: multiplying it by the positive number $(1+s)(1+t)(1+s+t)$ turns it into
$$
(s+t)(1+s)(1+t)\le s(1+t)(1+s+t)+t(1+s)(1+s+t),
$$
whose right-hand side minus the left-hand side is $st(2+s+t)\ge0$; so the inequality holds. If $0\le s<t$ then $f(t)-f(s)=\big(t(1+s)-s(1+t)\big)/\big((1+t)(1+s)\big)=(t-s)/\big((1+t)(1+s)\big)>0$, so $f$ is strictly increasing.
:::

:::

::: {.pf-step #triangle}
$d'(x,y)\le d'(x,z)+d'(z,y)$.

::: pf-proof
Write $a=d(x,z)$, $b=d(z,y)$ and $c=d(x,y)$, so $c\le a+b$ by the triangle inequality for $d$ and $d'=f\circ d$. By steps [](#subadditive){.pf-ref} and [](#bounded){.pf-ref},
$$
d'(x,y)=f(c)\le f(a+b)\le f(a)+f(b)=d'(x,z)+d'(z,y).
$$
:::

:::

::: {.pf-step #metric}
$d'$ is a metric on $X$.

::: pf-proof
Steps [](#bounded){.pf-ref}, [](#symmetric){.pf-ref} and [](#triangle){.pf-ref} give nonnegativity, the vanishing on the diagonal and symmetry, and the triangle inequality.
:::

:::

::: {.pf-step #same-topology}
$d'$ induces the topology of $d$.

::: pf-proof
The map $t\mapsto t/(1+t)$ is strictly increasing by step [](#subadditive){.pf-ref} with inverse $u\mapsto u/(1-u)$ defined for $0\le u<1$. Hence for $x\in X$ and $0<u<1$ one has $d'(x,y)<u$ exactly when $d(x,y)<u/(1-u)$, that is
$$
B_{d'}(x,u)=B_{d}\big(x,u/(1-u)\big).
$$
So every $d'$-ball is a $d$-ball, and every $d$-ball $B_{d}(x,r)$ with $r>0$ is the $d'$-ball $B_{d'}\big(x,r/(1+r)\big)$ with $r/(1+r)\in(0,1)$. A set is open for a metric exactly when each of its points has a ball around it inside the set, so the two topologies have the same open sets.
:::

:::

::: {.pf-step}
$d'$ is a bounded metric giving the topology of $X$.

::: pf-proof
Steps [](#metric){.pf-ref} and [](#same-topology){.pf-ref} are the two assertions, the boundedness being step [](#bounded){.pf-ref}.
:::

:::

:::
:::
