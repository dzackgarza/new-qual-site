---
schema: qual/card@1
id: E-HAT-1.2-17
kind: problem
title: $\pi_1(\RR^2 - \QQ^2)$ is uncountable
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The old solution used winding numbers about irrational points, which are not removed; replaced by rectangles with irrational sides, separated by winding about a removed rational point.
---

::: {.problem}
Show that $\pi_1(\RR^2 - \QQ^2)$ is uncountable.
:::

::: {.solution}
Let $X=\RR^2-\QQ^2$, let $u=\sqrt2$, and take the basepoint $(u,u)\in X$.

::: pf

::: {.pf-step #s1}

For each irrational $s>u$, the boundary $\gamma_s$ of the rectangle $[u,s]\times[u,u+1]$, traversed counterclockwise from $(u,u)$, is a loop in $X$.

::: pf-proof

A point of $\QQ^2$ has both coordinates rational.
Each side of the rectangle lies on a line $x=u$, $x=s$, $y=u$ or $y=u+1$, and $u$, $s$, $u+1$ are irrational.

:::

:::

::: {.pf-step #s2}

If $q\in\QQ^2$ and $\gamma,\gamma'$ are loops in $X$ that are homotopic in $X$, then their winding numbers about $q$ are equal.

::: pf-proof

Since $X\subseteq\RR^2-\{q\}$, a homotopy in $X$ is a homotopy in $\RR^2-\{q\}$, and the winding number about $q$ is the image of the class of the loop under $\pi_1(\RR^2-\{q\})\cong\pi_1(S^1)\cong\ZZ$.

:::

:::

::: {.pf-step #s3}

If $u<s<s'$ are irrational, then $[\gamma_s]\ne[\gamma_{s'}]$ in $\pi_1(X,(u,u))$.

::: pf-proof

By density of $\QQ$ choose rational $a\in(s,s')$ and $b\in(u,u+1)$, and let $q=(a,b)$.
The point $q$ is outside the rectangle bounded by $\gamma_s$ and inside the rectangle bounded by $\gamma_{s'}$, so the winding numbers about $q$ are $0$ and $1$.
Step [](#s2){.pf-ref} gives the claim.

:::

:::

::: pf-qed

The map $s\mapsto[\gamma_s]$ from the uncountable set of irrationals $s>u$ to $\pi_1(X)$ is injective by step [](#s3){.pf-ref}, so $\pi_1(\RR^2-\QQ^2)$ is uncountable.

:::

:::

:::
