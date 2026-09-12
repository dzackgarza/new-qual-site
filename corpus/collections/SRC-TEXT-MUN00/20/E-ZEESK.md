---
schema: qual/card@1
id: E-ZEESK
kind: problem
title: The metric is continuous exactly for its own topology
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
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

Let $X$ be a metric space with metric $d$.

(a) Show that $d: X \times X \to \mathbb{R}$ is continuous.

(b) Let $X'$ denote a space having the same underlying set as $X$.
Show that if $d: X' \times X' \to \mathbb{R}$ is continuous, then the topology of $X'$ is finer than the topology of $X$.

One can summarize the result of this exercise as follows: if $X$ has a metric $d$, then the topology induced by $d$ is the coarsest topology relative to which the function $d$ is continuous.
:::

::: {.solution}
(a) The triangle inequality gives the reverse-triangle estimate
\[
|d(x,y)-d(x',y')|
\le d(x,x')+d(y,y').
\]
Indeed
\[
d(x,y)\le d(x,x')+d(x',y')+d(y',y),
\]
and reversing the two pairs gives the opposite inequality. Therefore, given $\varepsilon>0$, if
\[
d(x,x')<\varepsilon/2,\qquad d(y,y')<\varepsilon/2,
\]
then
\[
|d(x,y)-d(x',y')|<\varepsilon.
\]
Thus $d:X\times X\to\mathbb R$ is continuous.

(b) Assume $d:X'\times X'\to\mathbb R$ is continuous, where $X'$ has the same underlying set. Fix $a\in X'$. The map
\[
j_a:X'\to X'\times X',\qquad j_a(x)=(a,x)
\]
is continuous, so
\[
x\longmapsto d(a,x)=d\circ j_a(x)
\]
is continuous. Hence for every $r>0$ the metric ball
\[
B_d(a,r)=\{x:d(a,x)<r\}
\]
is open in $X'$. Since metric balls form a basis for the topology of $X$, every $X$-open set is $X'$-open. Therefore the topology of $X'$ is finer than the metric topology of $X$.
:::
