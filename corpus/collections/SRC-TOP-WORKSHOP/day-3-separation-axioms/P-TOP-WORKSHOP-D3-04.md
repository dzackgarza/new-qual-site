---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-04
kind: problem
title: A separable metric space is second countable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The family of balls is a step with the
    count of its members, the basis property is proved for an arbitrary point of an arbitrary open
    set with the radius chosen so that the containment is strict, and the triangle-inequality chain
    is carried out rather than asserted. The card states where separability enters: in meeting the
    ball of radius eps/3 around x. Not checked: the workshop sheet itself, which the collection
    retains as a problem file only (assets/attachments/Day_3_-_Separation_Problems.pdf); the
    statement is as transcribed on the card. No retained solution set covers the exercise, so the
    argument is the card's own. No statement repair.
---

::: {.problem}
Show that if the metric space $(X,d)$ is separable, then the metric topology on $X$ is second countable.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the problem sheets alone, so the argument is the card's own. Let $(X,d)$ be a metric space with a countable dense subset $D=\{p_1,p_2,\dots\}$, and let $\mathcal B$ be the family of all balls $B(p,q)$ with $p\in D$ and $q\in\QQ_{>0}$.

::: pf

::: {.pf-step #countable}
$\mathcal B$ is countable.

::: pf-proof
$\mathcal B$ is the union over $p\in D$ of the sets $\{B(p,q):q\in\QQ_{>0}\}$, and $q\mapsto B(p,q)$ is injective, so each of these is in bijection with the countable set $\QQ_{>0}$. A countable union of countable sets is countable, and $D$ is countable, so $\mathcal B$ is countable.
:::

:::

::: {.pf-step #basis}
For every open $U$ and every $x\in U$ there is $B\in\mathcal B$ with $x\in B\subseteq U$.

::: pf-proof
Since $U$ is open and $x\in U$ there is $\varepsilon>0$ with $B(x,\varepsilon)\subseteq U$. The set $D$ is dense, so the ball $B(x,\varepsilon/3)$ meets $D$; choose $p\in D$ with $d(x,p)<\varepsilon/3$. Choose a rational $q$ with $d(x,p)<q<\varepsilon/3$, which is possible by density of $\QQ$; then $q>0$ so $B(p,q)\in\mathcal B$, and $x\in B(p,q)$ because $d(x,p)<q$. If $y\in B(p,q)$ then
$$
d(x,y)\le d(x,p)+d(p,y)<\frac{\varepsilon}{3}+q<\frac{2\varepsilon}{3}<\varepsilon
$$
by the triangle inequality, so $y\in B(x,\varepsilon)\subseteq U$; hence $B(p,q)\subseteq U$.
:::

:::

::: {.pf-step #second}
The metric topology on $X$ is second countable.

::: pf-proof
A family $\mathcal B$ of open sets is a basis for a topology when every point of every open set lies in a member of $\mathcal B$ contained in that open set. Step [](#basis){.pf-ref} verifies exactly this for the metric topology, and every member of $\mathcal B$ is open there because a ball is open. With step [](#countable){.pf-ref} that gives a countable basis, which is the definition of second countability. So a separable metric space is second countable; the only property of separability used is that $D$ meets every nonempty open set.
:::

:::

:::

:::
