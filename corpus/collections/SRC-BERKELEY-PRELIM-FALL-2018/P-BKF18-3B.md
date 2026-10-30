---
schema: qual/card@1
id: P-BKF18-3B
kind: problem
title: Continuous open maps $\RR\to\RR$ are monotone
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Prove that a continuous function from $\RR$ to $\RR$ which maps open sets to open sets must be monotone.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A continuous open map $f\colon\RR\to\RR$ is injective.

::: pf-proof

Suppose $x<y$ and $f(x)=f(y)$. By continuity, $f$ has a maximum $M$ and a minimum $m$ on $[x,y]$. If $M=m$, then $f((x,y))$ is a single point, which is not open. Otherwise one of $M,m$ differs from $f(x)=f(y)$, so it is attained at a point of $(x,y)$. Say $M$ is attained there. Then $M\in f((x,y))\subseteq(-\infty,M]$, so $f((x,y))$ contains no neighborhood of $M$ and is not open. The case of $m$ is the same.

:::

:::

::: {.pf-step #s2}

A continuous injective map $\RR\to\RR$ is strictly monotone.

::: pf-proof

Suppose $a<b<c$ and $f(b)$ is not between $f(a)$ and $f(c)$; say $f(b)>\max(f(a),f(c))$. Any value $v$ with $\max(f(a),f(c))<v<f(b)$ is attained on $(a,b)$ and on $(b,c)$ by the intermediate value theorem, against injectivity. The case $f(b)<\min(f(a),f(c))$ is the same. So for all $a<b<c$, $f(b)$ lies strictly between $f(a)$ and $f(c)$.

Fix $s<t$, say with $f(s)<f(t)$. For any $u<v$, apply the previous paragraph to the ordered set of points among $s,t,u,v$: each middle value lies between its neighbours, so the sign of $f(v)-f(u)$ equals the sign of $f(t)-f(s)$. So $f$ is strictly increasing. The case $f(s)>f(t)$ gives strictly decreasing.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that $f$ is strictly monotone.

:::

:::

:::
