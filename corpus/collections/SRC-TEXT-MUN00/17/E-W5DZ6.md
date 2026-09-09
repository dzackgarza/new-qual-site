---
schema: qual/card@1
id: E-W5DZ6
kind: problem
title: Closure of a product equals the product of closures
classification:
  areas:
  - topology
  topics:
  - Closure
  - Product Topology
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

Let $A \subset X$ and $B \subset Y$.
Show that in the space $X \times Y$,

$$
\overline{A \times B} = \overline{A} \times \overline{B}.
$$
:::

::: {.solution}
First, $A\times B\subseteq\overline A\times\overline B$, and the latter set is closed by the preceding product result. Hence
\[
\overline{A\times B}\subseteq\overline A\times\overline B.
\]
For the reverse inclusion, let $(x,y)\in\overline A\times\overline B$. A basic neighborhood of $(x,y)$ has the form $U\times V$ with $x\in U$, $y\in V$. Since $x\in\overline A$ and $y\in\overline B$,
\[
U\cap A\neq\varnothing,\qquad V\cap B\neq\varnothing.
\]
Choose $a\in U\cap A$ and $b\in V\cap B$. Then $(a,b)\in(U\times V)\cap(A\times B)$. Thus every basic neighborhood of $(x,y)$ meets $A\times B$, so
\[
(x,y)\in\overline{A\times B}.
\]
Therefore
\[
\boxed{\overline{A\times B}=\overline A\times\overline B}.
\]
:::
