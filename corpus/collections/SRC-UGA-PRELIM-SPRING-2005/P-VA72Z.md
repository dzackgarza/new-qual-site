---
schema: qual/card@1
id: P-VA72Z
kind: problem
title: Convergence of $\sum a_n^2$ under conditional and absolute convergence of $\sum
  a_n$
classification:
  areas:
  - prelim
  topics:
  - Series of Numbers
  - Convergence Tests
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
a. Provide examples to show that the series $\sum_{n=1}^{\infty} a_n^2$ may or may not converge when the series $\sum_{n=1}^{\infty} a_n$ converges conditionally.
b. Prove that if the series $\sum_{n=1}^{\infty} a_n$ converges absolutely, then the series $\sum_{n=1}^{\infty} a_n^2$ must converge.
:::


::: {.solution}
<1>1. Conditional convergence of $\sum a_n$ can occur while $\sum a_n^2$ converges.
::: {.proof}
Take
\[
a_n=\frac{(-1)^{n+1}}{n}.
\]
Then $\sum a_n$ converges by the alternating-series test, but not absolutely because $\sum 1/n$ diverges. Thus $\sum a_n$ converges conditionally. On the other hand,
\[
\sum_{n=1}^\infty a_n^2=\sum_{n=1}^\infty \frac1{n^2}
\]
converges.
:::

<1>2. Conditional convergence of $\sum a_n$ can also occur while $\sum a_n^2$ diverges.
::: {.proof}
Take
\[
a_n=\frac{(-1)^{n+1}}{\sqrt n}.
\]
The series $\sum a_n$ converges by the alternating-series test because $1/\sqrt n$ decreases to $0$, but it is not absolutely convergent because $\sum 1/\sqrt n$ diverges. Hence $\sum a_n$ converges conditionally. However,
\[
\sum_{n=1}^\infty a_n^2=\sum_{n=1}^\infty \frac1n
\]
diverges.
:::

<1>3. If $\sum a_n$ converges absolutely, then $\sum a_n^2$ converges.
::: {.proof}
Absolute convergence means
\[
\sum_{n=1}^\infty |a_n|<\infty.
\]
Therefore $a_n\to0$, so there exists $N$ such that $|a_n|\le1$ for all $n\ge N$. For such $n$,
\[
0\le a_n^2=|a_n|^2\le |a_n|.
\]
Thus $\sum_{n=N}^\infty a_n^2$ converges by comparison with $\sum_{n=N}^\infty |a_n|$. Adding the finitely many initial terms gives convergence of $\sum_{n=1}^\infty a_n^2$.
:::
:::
