---
schema: qual/card@1
id: P-RAF21D
kind: problem
title: "Pointwise bounded continuous functions are uniformly bounded on some interval (Banach-Steinhaus)"
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Boundedness Principle
  - Baire Category
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let functions $f_n \in C([0, 1])$ satisfy $\sup_n |f_n(x)| < \infty$ for each $x \in [0, 1]$.
Show that there are $0 \leq a < b \leq 1$ such that $\sup_n \|f_n \chi_{(a,b)}\|_u < \infty$.
:::

::: solution
<1>1. Form closed pointwise-boundedness sets.
::: proof
For each integer $m\ge1$, define
\[
E_m:=\{x\in[0,1]: |f_n(x)|\le m\text{ for every }n\}.
\]
Since each $f_n$ is continuous,
\[
E_m=\bigcap_{n=1}^\infty\{x:|f_n(x)|\le m\}
\]
is closed in $[0,1]$.

The pointwise boundedness hypothesis says that for every $x\in[0,1]$ there exists some $m$ with $x\in E_m$. Hence
\[
[0,1]=\bigcup_{m=1}^\infty E_m.
\]
:::

<1>2. Apply the Baire Category Theorem.
::: proof
The compact metric space $[0,1]$ is complete. By the Baire Category Theorem, it cannot be a countable union of closed sets all having empty interior. Therefore some $E_{m_0}$ has nonempty interior relative to $[0,1]$.

Choose $0\le a<b\le1$ such that
\[
(a,b)\subset E_{m_0}.
\]
Then for every $n$ and every $x\in(a,b)$,
\[
|f_n(x)|\le m_0.
\]
Consequently
\[
\|f_n\chi_{(a,b)}\|_u\le m_0
\]
for every $n$, and hence
\[
\boxed{\sup_n\|f_n\chi_{(a,b)}\|_u<\infty.}
\]
:::
:::
