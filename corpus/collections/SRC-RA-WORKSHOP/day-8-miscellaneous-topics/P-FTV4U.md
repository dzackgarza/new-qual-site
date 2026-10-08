---
schema: qual/card@1
id: P-FTV4U
kind: problem
title: "Bounded variation of x sin(1/x) on the unit interval"
classification:
  areas:
  - real-analysis
  topics:
  - Variation
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Define $f \colon [0,1] \to [-1,1]$ by $$f(x):= \begin{cases} x\sin\big({\frac{1}{x}}\big) & 0 < x \leq 1 \\ 0 & x = 0 \end{cases}$$ Determine, with justification, whether $f$ is if bounded variation on the interval $[0,1]$.
:::
::: {.solution}
<1>1. For each $k\geq0$, define $t_k=2/((2k+1)\pi)$. Then $0<t_{k+1}<t_k\leq1$, $t_k\to0$, and $f(t_k)=(-1)^kt_k$.
::: {.proof}
The numbers $t_k$ decrease to zero because their denominators increase without bound. Moreover $1/t_k=(2k+1)\pi/2$, so $\sin(1/t_k)=(-1)^k$ and the asserted values follow.
:::

<1>2. For every integer $K\geq1$, the finite sequence
\[
P_K:\quad0<t_K<t_{K-1}<\cdots<t_0<1
\]
is part of a partition of $[0,1]$, and its variation sum is at least $\sum_{k=0}^{K-1}(t_k+t_{k+1})$.

::: {.proof}
Adjoin both endpoints $0,1$ to the displayed sequence. By step <1>1, consecutive values $f(t_{k+1})$ and $f(t_k)$ have opposite signs, so
\[
|f(t_k)-f(t_{k+1})|=t_k+t_{k+1}.
\]
All other increments in the partition variation sum are nonnegative; in particular the initial increment from $0$ to $t_K$ is $|f(t_K)-f(0)|=t_K$ and has not been identified with any $t_k$.
:::

<1>3. The variation sums of these partitions are unbounded as $K\to\infty$.

::: {.proof}
By step <1>2, the sum is at least
\[
\sum_{k=0}^{K-1}(t_k+t_{k+1})
=t_0+2\sum_{k=1}^{K-1}t_k+t_K
\geq\frac4\pi\sum_{k=1}^{K-1}\frac1{2k+1}.
\]
For $k\geq1$, $2k+1\leq3k$, so the right-hand side is at least $\frac4{3\pi}\sum_{k=1}^{K-1}1/k$, which diverges.
:::

<1>4. The function $f$ is not of bounded variation on $[0,1]$.

::: {.proof}
Total variation is the supremum of all finite partition variation sums. By step <1>3, those sums are unbounded, so $V_{[0,1]}(f)=\infty$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves $f\notin\mathrm{BV}[0,1]$.
:::
:::
