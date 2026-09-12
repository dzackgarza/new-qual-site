---
schema: qual/card@1
id: E-AMD-CY7I27YM
kind: problem
title: Algebraic extensions are transitive
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $L/K/F$ with $K/F$ algebraic and $L/K$ algebraic then $L$ is algebraic.
:::

::: {.solution}
Let $\alpha\in L$. Since $L/K$ is algebraic, $\alpha$ satisfies a nonzero polynomial
\[
p(x)=a_0+a_1x+\cdots+a_nx^n\in K[x].
\]
Because $K/F$ is algebraic, the finitely many coefficients $a_i$ are algebraic over $F$. Hence
\[
F_0:=F(a_0,\dots,a_n)
\]
is a finite extension of $F$.

Now $p\in F_0[x]$, so $\alpha$ is algebraic over $F_0$. Therefore $F_0(\alpha)/F_0$ is finite. By the tower law,
\[
[F_0(\alpha):F]=[F_0(\alpha):F_0][F_0:F]<\infty.
\]
Thus $\alpha$ is algebraic over $F$. Since $\alpha\in L$ was arbitrary, $L/F$ is algebraic.
:::
