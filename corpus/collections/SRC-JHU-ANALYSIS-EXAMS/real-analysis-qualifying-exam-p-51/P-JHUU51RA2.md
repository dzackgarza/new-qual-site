---
schema: qual/card@1
id: P-JHUU51RA2
kind: problem
title: "A pointwise-convergent subsequence of sine sums with continuous limit"
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 2 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(c_n)$ be a sequence of positive real numbers and define
\[
f_n(x)=\sin(x+c_n^2)+\frac1{c_n}\sin(c_nx).
\]
Prove that $(f_n)$ has a subsequence converging pointwise to a continuous function.
:::

::: {.solution}
We split into two cases.

<1>1. The sequence $(c_n)$ has a bounded subsequence.
::: {.proof}
By Bolzano--Weierstrass, after passing to a subsequence we may assume
\[
c_n\to c\ge0.
\]
If $c>0$, then for every $x$,
\[
\sin(x+c_n^2)\to\sin(x+c^2)
\]
and
\[
\frac1{c_n}\sin(c_nx)\to\frac1c\sin(cx).
\]
Thus
\[
f_n(x)\to \sin(x+c^2)+\frac1c\sin(cx),
\]
a continuous function of $x$.

If $c=0$, then
\[
\sin(x+c_n^2)\to\sin x,
\]
while
\[
\frac1{c_n}\sin(c_nx)
=x\frac{\sin(c_nx)}{c_nx}\to x
\]
for every $x$, with the value at $x=0$ understood by continuity. Hence
\[
f_n(x)\to\sin x+x,
\]
again continuously.
:::

<1>2. The sequence $(c_n)$ has no bounded subsequence.
::: {.proof}
Then we can choose a subsequence, still denoted $(c_n)$, such that
\[
c_n\to\infty.
\]
The phases $c_n^2$ modulo $2\pi$ lie in the compact circle $\mathbb R/(2\pi\mathbb Z)$, so after passing to a further subsequence there exists $\theta\in[0,2\pi]$ such that
\[
c_n^2\pmod{2\pi}\to\theta.
\]
Therefore for every $x$,
\[
\sin(x+c_n^2)\to\sin(x+\theta).
\]
Also
\[
\left|\frac1{c_n}\sin(c_nx)\right|\le\frac1{c_n}\to0
\]
uniformly in $x$. Hence
\[
f_n(x)\to\sin(x+\theta),
\]
which is continuous.
:::

In either case, the original sequence has a subsequence converging pointwise to a continuous function.
:::
