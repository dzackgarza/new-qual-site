---
schema: qual/card@1
id: P-F06PG
kind: problem
title: Product of continuous functions is continuous, by $\varepsilon$-$\delta$
classification:
  areas:
  - prelim
  topics:
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f, g: \mathbb{R} \to \mathbb{R}$ be continuous for all $x$.
Using an $\varepsilon$-$\delta$ argument, show that $f(x)g(x)$ is continuous for all $x$.
:::

::: {.solution}
Fix $a\in\mathbb R$ and let $\varepsilon>0$. Since $f$ is continuous at $a$, choose $\delta_0>0$ such that
\[
|x-a|<\delta_0\Longrightarrow |f(x)-f(a)|<1.
\]
Then, for such $x$,
\[
|f(x)|\le |f(a)|+1=:M.
\]
By continuity of $g$ at $a$, choose $\delta_1>0$ such that
\[
|x-a|<\delta_1\Longrightarrow |g(x)-g(a)|<\frac{\varepsilon}{2M}.
\]
By continuity of $f$ at $a$, choose $\delta_2>0$ such that
\[
|x-a|<\delta_2\Longrightarrow |f(x)-f(a)|<\frac{\varepsilon}{2(|g(a)|+1)}.
\]
Set
\[
\delta=\min\{\delta_0,\delta_1,\delta_2\}.
\]
If $|x-a|<\delta$, then
\[
\begin{aligned}
|f(x)g(x)-f(a)g(a)|
&\le |f(x)|\,|g(x)-g(a)|+|g(a)|\,|f(x)-f(a)|\\
&< M\frac{\varepsilon}{2M}
+|g(a)|\frac{\varepsilon}{2(|g(a)|+1)}\\
&<\varepsilon.
\end{aligned}
\]
Thus $fg$ is continuous at $a$. Since $a$ was arbitrary, $fg$ is continuous on $\mathbb R$.
:::
