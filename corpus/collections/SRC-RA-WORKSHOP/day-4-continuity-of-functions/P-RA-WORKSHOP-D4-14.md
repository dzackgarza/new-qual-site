---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-14
kind: problem
title: Prove Theorem 3.4
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
relations:
- kind: uses
  target: T-RA-WORKSHOP-D4-3-4
review: draft
---

::: {.problem}
Prove Theorem 3.4.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Set up a sup.
Proof: assume $f(a) < f(b)$ and fix $x$ with $f(a) < x < f(b)$.
Let $E = \{t \in [a,b] : f(t) \le x\}$; then $a \in E$ (so $E \ne \varnothing$) and $E$ is bounded above by $b$.
Let $c = \sup E$.
<1>2. $c \in (a,b)$.
Proof: by continuity at $a$, since $f(a) < x$, there is $\delta > 0$ with $f < x$ on $[a, a+\delta)$, so $c \ge a + \delta > a$.
By continuity at $b$, since $f(b) > x$, there is $\delta' > 0$ with $f > x$ on $(b-\delta', b]$, so $E \subseteq [a, b-\delta']$ and $c \le b - \delta' < b$.
<1>3. $f(c) = x$.
Proof: suppose $f(c) < x$.
By continuity at $c$ there is $\delta > 0$ with $f(t) < x$ for $t \in (c - \delta, c + \delta)$; then $c + \delta/2 \in E$, contradicting $c = \sup E$.
Suppose $f(c) > x$.
By continuity at $c$ there is $\delta > 0$ with $f(t) > x$ on $(c - \delta, c + \delta)$, so no point of $(c - \delta, c]$ lies in $E$, making $c - \delta$ an upper bound of $E$ smaller than $c$ — contradiction.
Hence $f(c) = x$.
<1>4. Q.E.D. Proof: $c \in (a,b)$ with $f(c) = x$; the case $f(a) > f(b)$ follows by applying this to $-f$, and $f(a) = f(b)$ cannot occur with $f(a) < x < f(b)$.
:::
