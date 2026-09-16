---
schema: qual/card@1
id: P-JHUFA02CAB
kind: problem
title: Monotone convergence for an increasing sequence with bounded integrals
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Convergence
  - Interchange of Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the preserved JHU Fall 2002 Real Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $f_1(x)\le f_2(x)\le\cdots\le f_n(x)\le\cdots$ on a set $A$, where the functions $f_n$ are integrable and $\int_A f_n(x)\,dx\le M$ for some constant $M$.
Show that the limit
\[
f(x)=\lim_{n\to\infty}f_n(x)
\]
exists and is finite almost everywhere on $A$, and that
\[
\lim_{n\to\infty}\int_A f_n(x)\,dx=\int_A f(x)\,dx.
\]
:::

::: {.solution}
Set
\[
g_n:=f_n-f_1.
\]
Then each $g_n$ is measurable, nonnegative, and
\[
0=g_1\le g_2\le\cdots.
\]
Moreover
\[
\int_A g_n
=\int_A f_n-\int_A f_1
\le M-\int_A f_1<\infty.
\]

Let
\[
g(x):=\lim_{n\to\infty}g_n(x)\in[0,\infty].
\]
By the Monotone Convergence Theorem,
\[
\int_A g
=\lim_{n\to\infty}\int_A g_n
\le M-\int_A f_1<\infty.
\]
Hence $g(x)<\infty$ for almost every $x\in A$. Therefore
\[
f(x):=f_1(x)+g(x)
=\lim_{n\to\infty}f_n(x)
\]
exists and is finite almost everywhere.

Finally,
\[
\begin{aligned}
\lim_{n\to\infty}\int_A f_n
&=\int_A f_1+\lim_{n\to\infty}\int_A g_n\\
&=\int_A f_1+\int_A g\\
&=\int_A f.
\end{aligned}
\]
Thus the pointwise monotone limit is finite almost everywhere and the integrals converge to the integral of the limit.
:::
