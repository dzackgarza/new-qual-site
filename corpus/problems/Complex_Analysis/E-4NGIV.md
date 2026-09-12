---
schema: qual/card@1
id: E-4NGIV
kind: problem
title: Entire doubly periodic functions are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that an entire doubly periodic function is constant.
:::

::: solution
Let $\omega_1,\omega_2$ be two real-linearly independent periods of the entire function $f$. Consider the closed fundamental parallelogram
$$
P=\{t_1\omega_1+t_2\omega_2:0\le t_1,t_2\le1\}.
$$
It is compact, so continuity of $f$ gives
$$
M=\max_{z\in P}|f(z)|<\infty.
$$

Every $z\in\mathbb C$ can be written
$$
z=z_0+m\omega_1+n\omega_2
$$
with $m,n\in\mathbb Z$ and $z_0\in P$. By periodicity,
$$
f(z)=f(z_0),
$$
so $|f(z)|\le M$ for all $z\in\mathbb C$. Thus $f$ is bounded and entire; Liouville's theorem implies that $f$ is constant.
:::
