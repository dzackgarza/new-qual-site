---
schema: qual/card@1
id: P-BKF12-2B
kind: problem
title: Sums of the alternating harmonic series and a rearrangement
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 2B in the retained Fall 2012 Berkeley prelim exam
    and independently reviewed the retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the alternating-harmonic evaluation and justified convergence of
    the displayed rearranged series through its block partial sums.
---

::: {.problem}
(a) Find the sum $1-1/2+1/3-1/4+\cdots$.

(b) Find the sum $1-1/2-1/4+1/3-1/6-1/8+1/5-1/10-1/12+\cdots$.
:::

::: {.solution}
For $N\ge1$, let
$$
S_N\coloneqq\sum_{k=1}^N\frac{(-1)^{k+1}}{k}.
$$

<1>1. The alternating harmonic series has sum
$$
\boxed{\log 2}.
$$

::: {.proof}
For $0\le x\le1$,
$$
1-x+x^2-\cdots+(-x)^{N-1}
=\frac{1-(-x)^N}{1+x}.
$$
Integrating from $0$ to $1$ gives
$$
S_N
=\log2-(-1)^N\int_0^1\frac{x^N}{1+x}\,dx.
$$
The remainder satisfies
$$
\left|
\int_0^1\frac{x^N}{1+x}\,dx
\right|
\le\int_0^1x^N\,dx
=\frac1{N+1},
$$
so $S_N\to\log2$.
:::

<1>2. If $T_{3N}$ denotes the partial sum of the series in part (b)
through its first $N$ three-term blocks, then
$$
T_{3N}=\frac12S_{2N}.
$$

::: {.proof}
The $k$th three-term block is
$$
\frac1{2k-1}-\frac1{4k-2}-\frac1{4k}
=\frac1{2(2k-1)}-\frac1{4k}.
$$
Therefore
$$
\begin{aligned}
T_{3N}
&=\sum_{k=1}^N
\left(
\frac1{2(2k-1)}-\frac1{4k}
\right)\\
&=\frac12
\sum_{k=1}^N
\left(
\frac1{2k-1}-\frac1{2k}
\right)\\
&=\frac12S_{2N}.
\end{aligned}
$$
:::

<1>3. The series in part (b) converges to
$$
\boxed{\frac12\log2}.
$$

::: {.proof}
By steps <1>1 and <1>2,
$$
T_{3N}\longrightarrow\frac12\log2.
$$
The one or two terms between $T_{3N}$ and the next block endpoint have
absolute values tending to $0$ as $N\to\infty$. Hence the partial
sums with indices $3N+1$ and $3N+2$ have the same limit as
$T_{3N}$, so the full sequence of partial sums converges to
$\frac12\log2$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 answers part (a), and step <1>3 answers part (b).
:::
:::
