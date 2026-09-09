---
schema: qual/card@1
id: P-JHUFA07ANF
kind: problem
title: "An open dense subset of R with measure one"
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, Fall 2007, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Does there exist an open dense subset of $\mathbb R$ with Lebesgue measure equal to one?
Either construct an example or prove that one does not exist.
:::

::: {.solution}
<1>1. Construct an open dense set of finite positive measure.
::: {.proof}
Enumerate the rationals as $\mathbb Q=\{q_1,q_2,\ldots\}$ and set
\[
U=\bigcup_{n=1}^\infty \left(q_n-2^{-n-3},q_n+2^{-n-3}\right).
\]
Then $U$ is open.
It contains $\mathbb Q$, so it is dense in $\mathbb R$.
Moreover, by countable subadditivity,
\[
m(U)\le \sum_{n=1}^\infty 2^{-n-2}=\frac14<\infty.
\]
Since $U$ contains a nonempty open interval, $m(U)>0$.
Thus
\[
0<m(U)<\infty.
\]
:::

<1>2. Dilate to obtain measure exactly one.
::: {.proof}
Let $a=m(U)>0$ and define
\[
V=a^{-1}U=\{a^{-1}x:x\in U\}.
\]
A nonzero dilation is a homeomorphism of $\mathbb R$, so $V$ is again open and dense.
By the scaling property of Lebesgue measure,
\[
m(V)=a^{-1}m(U)=1.
\]
Hence an open dense subset of $\mathbb R$ of Lebesgue measure exactly one does exist.
:::
:::
