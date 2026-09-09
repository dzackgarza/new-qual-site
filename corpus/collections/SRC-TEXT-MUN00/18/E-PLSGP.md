---
schema: qual/card@1
id: E-PLSGP
kind: problem
title: Epsilon-delta continuity implies open-set continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Prove that for functions $f: \mathbb{R} \to \mathbb{R}$, the $\epsilon$-$\delta$ definition of continuity implies the open set definition.
:::

::: {.solution}
Assume the epsilon-delta definition. Let $V\subseteq\mathbb R$ be open. We show $f^{-1}(V)$ is open.

Take $x\in f^{-1}(V)$. Since $f(x)\in V$ and $V$ is open, choose $\varepsilon>0$ with
\[
(f(x)-\varepsilon,f(x)+\varepsilon)\subseteq V.
\]
By epsilon-delta continuity at $x$, there is $\delta>0$ such that
\[
|t-x|<\delta\implies |f(t)-f(x)|<\varepsilon.
\]
Thus
\[
(x-\delta,x+\delta)\subseteq f^{-1}(V).
\]
Every point of $f^{-1}(V)$ therefore has an open interval contained in $f^{-1}(V)$, so $f^{-1}(V)$ is open. Hence $f$ is continuous in the open-set sense.
:::
