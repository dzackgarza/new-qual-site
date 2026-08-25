---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-W3
kind: problem
title: A nonzero derivative gives local injectivity
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Continuity
relations: []
review: draft
---

::: {.problem}
([KRD10, Exercise 6.2.B]) If $f:(a,b)\to\mathbb R$ is continuously differentiable and $f'(x_0)\ne0$ for some $x_0\in(a,b)$, then $f$ is injective on some interval $(c,d)$ containing $x_0$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $f'$ keeps the sign of $f'(x_0)$ in a neighborhood.
Proof: assume $f'(x_0) > 0$ (the case $< 0$ is symmetric).
Since $f'$ is continuous at $x_0$, there is $\delta > 0$ with $f'(x) > f'(x_0)/2 > 0$ for all $x \in (c, d) := (x_0 - \delta, x_0 + \delta) \subseteq (a,b)$.
<1>2. $f$ is strictly increasing on $(c,d)$.
Proof: for $c < u < v < d$, by MVT there is $\xi \in (u,v)$ with $f(v) - f(u) = f'(\xi)(v - u) > 0$ (as $f'(\xi) > 0$ and $v - u > 0$). Hence $f(u) < f(v)$.
<1>3. $f$ is injective on $(c,d)$.
Proof: a strictly increasing function is injective: if $f(u) = f(v)$ with $u \ne v$, say $u < v$, then $f(u) < f(v)$, contradiction.
<1>4. Q.E.D.
:::
