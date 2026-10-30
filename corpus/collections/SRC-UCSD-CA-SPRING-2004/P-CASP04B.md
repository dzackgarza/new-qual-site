---
schema: qual/card@1
id: P-CASP04B
kind: problem
title: "Schwarz-Pick inequality for self-maps of the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f \in \mathcal{O}(\DD)$ and assume that $\abs{f(z)} \leq 1$ in $\DD$.
Show that $$\frac{\abs{f(0)} - \abs{z}}{1 + \abs{f(0)}\abs{z}} \leq \abs{f(z)} \leq \frac{\abs{f(0)} + \abs{z}}{1 - \abs{f(0)}\abs{z}}.$$
:::

::: {.solution}
Put $a=f(0)$. If $f$ is constant the inequalities are immediate. Otherwise
$f(\DD)\subset\DD$, and Schwarz--Pick applied at $0$ gives
$$
\abs{\frac{f(z)-a}{1-\overline a f(z)}}\le \abs{z}.
$$
Set $A=\abs{a}$, $r=\abs{z}$, and $s=\abs{f(z)}$. Then
$$
\abs{f(z)-a}\le r\,\abs{1-\overline a f(z)}\le r(1+As).
$$
Using $A-s\le\abs{a-f(z)}$ gives
$$
A-s\le r(1+As),
$$
hence
$$
s\ge\frac{A-r}{1+Ar}.
$$
Likewise $s-A\le\abs{f(z)-a}$ gives
$$
s-A\le r(1+As),
$$
so
$$
s\le\frac{A+r}{1-Ar}.
$$
These are exactly the desired bounds.
:::
