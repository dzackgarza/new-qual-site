---
schema: qual/card@1
id: P-JCEPZ
kind: problem
title: Convergence and limit of $x_{n+1}=\frac{1+x_n}{2+x_n}$ with $x_1>0$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
  - Fixed Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UGA Fall 2021 real-analysis qualifying exam; repaired the legacy fixed-point calculation, whose positive root was off by a factor of 2, and supplied a genuine uniform contraction constant.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $\left\{x_{n}\right\}_{n-1}^{\infty}$ be a sequence of real numbers such that $x_{1}>0$ and
\[
x_{n+1}=1-\left(2+x_{n}\right)^{-1}=\frac{1+x_{n}}{2+x_{n}} \text {. }
\]
Prove that the sequence $\left\{x_{n}\right\}$ converges, and find its limit.
:::


::: {.solution}
Define
\[
T(x)=\frac{1+x}{2+x}=1-\frac1{2+x},\qquad x\ge0.
\]
Since $x_1>0$, induction gives $x_n>0$ for every $n$. Moreover $T$ maps $[0,\infty)$ into $[1/2,1)$.

For $x\ge0$,
\[
T'(x)=\frac1{(2+x)^2}\le\frac14.
\]
Hence by the mean value theorem,
\[
|T(x)-T(y)|\le\frac14|x-y|
\qquad(x,y\ge0).
\]
Thus $T$ is a contraction of the complete metric space $[0,\infty)$ into itself. By the Banach fixed-point theorem, the iterates $x_{n+1}=T(x_n)$ converge to the unique fixed point $L\ge0$.

The fixed-point equation is
\[
L=\frac{1+L}{2+L},
\]
so
\[
L^2+L-1=0.
\]
Therefore
\[
L=\frac{-1\pm\sqrt5}{2}.
\]
Only the positive root lies in $[0,\infty)$, hence
\[
\boxed{\lim_{n\to\infty}x_n=\frac{\sqrt5-1}{2}.}
\]
:::
