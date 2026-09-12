---
schema: qual/card@1
id: P-KVE3S
kind: problem
title: $C^1([a,b])$ is Banach under $\sup|f|+\sup|f'|$
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Norms
  - Completeness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2017 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2017.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: problem
Show that the space $C^1([a,b])$ is a Banach space when equipped with the norm
\[
\|f\|:=\sup_{x\in[a,b]}|f(x)|+\sup_{x\in[a,b]}|f'(x)|.
\]
:::

::: solution
Let $(f_n)$ be Cauchy in this norm. Then both $(f_n)$ and $(f_n')$ are Cauchy in the uniform norm on $[a,b]$. Since $C([a,b])$ is complete, there exist continuous functions $f,g$ such that
\[
f_n\to f,
\qquad
f_n'\to g
\]
uniformly on $[a,b]$.

Fix $x\in[a,b]$. By the Fundamental Theorem of Calculus,
\[
f_n(x)-f_n(a)=\int_a^x f_n'(t)\,dt.
\]
Passing to the limit, using uniform convergence on both sides, gives
\[
f(x)-f(a)=\int_a^x g(t)\,dt.
\]
Because $g$ is continuous, the Fundamental Theorem of Calculus implies
\[
f\in C^1([a,b])
\qquad\text{and}\qquad
f'=g.
\]
Therefore
\[
\|f_n-f\|
=\|f_n-f\|_\infty+\|f_n'-f'\|_\infty
\longrightarrow0.
\]
Thus every Cauchy sequence converges in the given norm, so
\[
\boxed{C^1([a,b])\text{ is Banach}.}
\]
:::
