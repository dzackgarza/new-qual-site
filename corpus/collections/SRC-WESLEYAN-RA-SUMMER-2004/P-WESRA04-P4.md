---
schema: qual/card@1
id: P-WESRA04-P4
kind: problem
title: The graph of a measurable function has planar measure zero
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Product Measures]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.3, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f:[0,1]\to[0,1]$ be Lebesgue measurable.
Prove that its graph
\[
\Gamma_f=\{(x,f(x)):x\in[0,1]\}
\]
has measure zero with respect to the completed product measure $m\times m$ on $[0,1]^2$.
:::

::: {.solution}
Since Lebesgue measure is the completion of Borel measure, there exists a Borel measurable function $h:[0,1]\to[0,1]$ such that
\[
f=h\quad\text{almost everywhere}.
\]
Let
\[
N=\{x:f(x)\ne h(x)\}.
\]
Then $m(N)=0$.

The graph of $h$ is Borel measurable.
Indeed, the map
\[
(x,y)\longmapsto h(x)-y
\]
is Borel measurable on $[0,1]^2$, and
\[
\Gamma_h=\{(x,y):h(x)-y=0\}
\]
is therefore Borel.

For every $x\in[0,1]$, the vertical section of $\Gamma_h$ is the singleton
\[
(\Gamma_h)_x=\{h(x)\},
\]
which has one-dimensional Lebesgue measure zero.
Tonelli's theorem gives
\[
(m\times m)(\Gamma_h)
=\int_0^1 m((\Gamma_h)_x)\,dx
=0.
\]

Finally,
\[
\Gamma_f\triangle\Gamma_h\subseteq N\times[0,1].
\]
The set $N\times[0,1]$ has product measure zero.
Since the product measure in the problem is completed, every subset of this null set is measurable.
Hence $\Gamma_f$ is measurable and
\[
(m\times m)(\Gamma_f)=0.
\]
Thus
\[
\boxed{\Gamma_f\text{ is measurable and has planar measure }0.}
\]
:::
