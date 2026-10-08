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
Prove Theorem 3.4.
:::

::: {.solution}
Let $a<b$, let $f:[a,b]\to\mathbb R$ be continuous with $f(a)<f(b)$, and fix $y\in(f(a),f(b))$, as in [[T-RA-WORKSHOP-D4-3-4|Theorem 3.4]].

<1>1. The set $E:=\{t\in[a,b]:f(t)\leq y\}$ has a supremum $c\in[a,b]$.

::: {.proof}
Since $f(a)<y$, the point $a$ belongs to $E$. Every element of $E$ is at most $b$. Thus $E$ is nonempty and bounded above, so completeness of $\mathbb R$ gives $c:=\sup E\in[a,b]$.
:::

<1>2. The supremum satisfies $a<c<b$.

::: {.proof}
Continuity at $a$ and $f(a)<y$ give some $\eta>0$ such that $f(t)<y$ whenever $t\in[a,b]$ and $|t-a|<\eta$. Choosing $t\in(a,\min\{b,a+\eta\})$ shows $t\in E$, hence $c\geq t>a$.

Continuity at $b$ and $f(b)>y$ give some $\theta>0$ such that $f(t)>y$ whenever $t\in[a,b]$ and $|t-b|<\theta$. Therefore every element of $E$ is at most $b-\min\{\theta/2,(b-a)/2\}$, so $c<b$.
:::

<1>3. The point $c$ satisfies $f(c)=y$.

::: {.proof}
Suppose $f(c)<y$. By continuity at $c$, there is $\delta>0$ such that $f(t)<y$ for $t\in[a,b]$ with $|t-c|<\delta$. By step <1>2, one may choose $t\in(c,\min\{b,c+\delta\})$. Then $t\in E$ and $t>c$, contradicting that $c$ is an upper bound of $E$.

Suppose instead $f(c)>y$. Continuity at $c$ gives $\delta>0$ such that $f(t)>y$ whenever $t\in[a,b]$ and $|t-c|<\delta$. By the defining property of the supremum, there is $t\in E$ with $c-\min\{\delta/2,(c-a)/2\}<t\leq c$. This contradicts $f(t)>y$. Both strict inequalities are impossible, hence $f(c)=y$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 provide $c\in(a,b)$ with $f(c)=y$, as required.
:::
:::
