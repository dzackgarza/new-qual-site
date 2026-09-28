---
schema: qual/card@1
id: P-BKS14-1A
kind: problem
title: Sum a reciprocal cubic telescoping series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the telescoping decomposition, finite partial sums, and limiting value.
---

::: {.problem}
Find the sum of the series
\[
\frac1{1\cdot2\cdot3}+\frac1{2\cdot3\cdot4}+\frac1{3\cdot4\cdot5}+\cdots.
\]
:::

::: {.solution}
<1>1. For every integer $n\geq1$,
$$
\frac{1}{n(n+1)(n+2)}
=
\frac12
\left(
\frac{1}{n(n+1)}
-
\frac{1}{(n+1)(n+2)}
\right).
$$

::: {.proof}
The difference inside the parentheses is
$$
\begin{aligned}
\frac{1}{n(n+1)}
-
\frac{1}{(n+1)(n+2)}
&=
\frac{(n+2)-n}{n(n+1)(n+2)}\\
&=
\frac{2}{n(n+1)(n+2)}.
\end{aligned}
$$
Dividing by $2$ gives the identity.
:::

<1>2. The sum of the first $N$ terms is
$$
\sum_{n=1}^{N}
\frac{1}{n(n+1)(n+2)}
=
\frac14
-
\frac{1}{2(N+1)(N+2)}.
$$

::: {.proof}
By step <1>1,
$$
\begin{aligned}
\sum_{n=1}^{N}
\frac{1}{n(n+1)(n+2)}
&=
\frac12
\sum_{n=1}^{N}
\left(
\frac{1}{n(n+1)}
-
\frac{1}{(n+1)(n+2)}
\right)\\
&=
\frac12
\left(
\frac{1}{1\cdot2}
-
\frac{1}{(N+1)(N+2)}
\right)\\
&=
\frac14
-
\frac{1}{2(N+1)(N+2)}.
\end{aligned}
$$
All intermediate terms cancel.
:::

<1>3. The series has sum
$$
\boxed{\frac14}.
$$

::: {.proof}
Let $N\to\infty$ in step <1>2. The remainder term satisfies
$$
\frac{1}{2(N+1)(N+2)}
\longrightarrow0.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested sum.
:::
:::
