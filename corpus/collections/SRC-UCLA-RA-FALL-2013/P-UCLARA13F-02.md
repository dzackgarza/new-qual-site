---
schema: qual/card@1
id: P-UCLARA13F-02
kind: problem
title: No holomorphic germ with prescribed values at inverse squares
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Show that there is no function $f$ holomorphic near $0\in\mathbb C$ such that, for all sufficiently large $n\in\mathbb N$,
\[
f(1/n^2)=\frac{n^2-1}{n^5}.
\]
:::

Suppose, for contradiction, that such a holomorphic function exists near $0$.

::: pf

::: pf-step

Since
\[
\frac1{n^2}\longrightarrow0
\]
and
\[
\frac{n^2-1}{n^5}\longrightarrow0,
\]
continuity of $f$ gives
\[
f(0)=0.
\]


::: pf-proof

For all sufficiently large $n$, the prescribed values satisfy
\[
f(1/n^2)=\frac{n^2-1}{n^5}.
\]
Taking $n\to\infty$ and using continuity at $0$ yields the conclusion.

:::

:::

::: pf-step

The difference quotient along $z_n=1/n^2$ is
\[
\frac{f(z_n)-f(0)}{z_n}
=\frac{n^2-1}{n^3}
=\frac1n-\frac1{n^3}.
\]


::: pf-proof

Use step <1>1 and divide the prescribed value by $1/n^2$.

:::

:::

::: pf-step

Hence
\[
f'(0)=0.
\]


::: pf-proof

The sequence $z_n\to0$ through nonzero points, and the difference quotients in step <1>2 tend to $0$. Since the complex derivative $f'(0)$ exists, every such sequence of difference quotients must converge to $f'(0)$.

:::

:::

::: pf-step

Since $f(0)=f'(0)=0$, holomorphicity implies
\[
f(z)=z^2g(z)
\]
for some function $g$ holomorphic near $0$.


::: pf-proof

The Taylor expansion of $f$ at $0$ has vanishing constant and linear coefficients by steps <1>1 and <1>3. Thus
\[
f(z)=\sum_{k\geq2}a_kz^k
=z^2\sum_{k\geq2}a_kz^{k-2},
\]
and the final series defines a holomorphic $g$ near $0$.

:::

:::

::: pf-step

Evaluating at $z_n=1/n^2$ gives
\[
g(1/n^2)
=n^4f(1/n^2)
=n-\frac1n.
\]


::: pf-proof

From step <1>4,
\[
g(1/n^2)=\frac{f(1/n^2)}{(1/n^2)^2}=n^4f(1/n^2).
\]
Substitute the prescribed value:
\[
n^4\frac{n^2-1}{n^5}=\frac{n^2-1}{n}=n-\frac1n.
\]

:::

:::

::: pf-step

The right-hand side of step <1>5 tends to $+\infty$, while the left-hand side must tend to the finite number $g(0)$.


::: pf-proof

Clearly $n-1/n\to+\infty$. But $g$ is holomorphic near $0$, hence continuous there, and $1/n^2\to0$, so
\[
g(1/n^2)\to g(0)\in\mathbb C.
\]
This is impossible.

:::

:::

::: pf-step

Therefore no such holomorphic function exists.


::: pf-proof

The assumed existence led to the contradiction in step <1>6.

:::

:::

::: pf-qed

Step <1>7 is the required conclusion.

:::

:::
