---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-14
kind: problem
title: Intermediate Value Theorem
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
relations:
- kind: uses
  target: T-RA-WORKSHOP-D4-3-4
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $a<b$ and let $f\colon[a,b]\to\RR$ be continuous with $f(a)<f(b)$.
Prove that for every $y\in\RR$ with $f(a)<y<f(b)$ there exists $c\in(a,b)$ such that $f(c)=y$.
:::

::: {.solution}

::: pf

::: pf-step

The set $E\coloneqq\{t\in[a,b]:f(t)\leq y\}$ has a supremum $c\in[a,b]$.

::: pf-proof

Since $f(a)<y$, the point $a$ belongs to $E$. Every element of $E$ is at most $b$. Thus $E$ is nonempty and bounded above, so completeness of $\RR$ gives $c\coloneqq\sup E\in[a,b]$.

:::

:::

::: {.pf-step #s2}

The supremum satisfies $a<c<b$.

::: pf-proof

Continuity at $a$ and $f(a)<y$ give some $\eta>0$ such that $f(t)<y$ whenever $t\in[a,b]$ and $\abs{t-a}<\eta$. Choosing $t\in(a,\min\{b,a+\eta\})$ shows $t\in E$, hence $c\geq t>a$.

Continuity at $b$ and $f(b)>y$ give some $\theta>0$ such that $f(t)>y$ whenever $t\in[a,b]$ and $\abs{t-b}<\theta$. Therefore every element of $E$ is at most $b-\min\{\theta/2,(b-a)/2\}$, so $c<b$.

:::

:::

::: pf-step

The point $c\in(a,b)$ satisfies $f(c)=y$.

::: pf-proof

Step [](#s2){.pf-ref} gives $c\in(a,b)$.

Suppose $f(c)<y$. By continuity at $c$, there is $\delta>0$ such that $f(t)<y$ for $t\in[a,b]$ with $\abs{t-c}<\delta$. Since $c<b$, one may choose $t\in(c,\min\{b,c+\delta\})$. Then $t\in E$ and $t>c$, contradicting that $c$ is an upper bound of $E$.

Suppose instead $f(c)>y$. Continuity at $c$ gives $\delta>0$ such that $f(t)>y$ whenever $t\in[a,b]$ and $\abs{t-c}<\delta$. By the defining property of the supremum, there is $t\in E$ with $c-\min\{\delta/2,(c-a)/2\}<t\leq c$. This contradicts $f(t)>y$. Both strict inequalities are impossible, hence $f(c)=y$.

:::

:::

:::

:::
