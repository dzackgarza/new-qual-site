---
schema: qual/card@1
id: P-BERK85S-01
kind: problem
title: Increasing derivative implies monotonicity of $f(x)/x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
Let $f:[0,\infty)\to\mathbb R$ be continuous and differentiable, with $f(0)=0$, and suppose $f'$ is increasing on $[0,\infty)$. Prove that
\[
g(x)=
\begin{cases}
f(x)/x,&x>0,\\
f'(0),&x=0
\end{cases}
\]
is increasing.
:::
