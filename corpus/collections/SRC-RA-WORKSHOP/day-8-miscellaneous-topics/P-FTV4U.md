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

::: problem
Define $f \colon [0,1] \to [-1,1]$ by $$f(x):= \begin{cases} x\sin\big({\frac{1}{x}}\big) & 0 < x \leq 1 \\ 0 & x = 0 \end{cases}$$ Determine, with justification, whether $f$ is if bounded variation on the interval $[0,1]$.
:::
::: {.solution}
<1>1. $f$ is NOT of bounded variation on $[0,1]$.
::: {.proof}
show the total variation is infinite by evaluating at a sequence of points with large accumulated oscillation.
:::

<1>2. Consider the points $t_k = \frac{2}{(2k+1)\pi} \in (0, 1]$, $k = 0, 1, 2, \ldots$ (the critical points where $\sin(1/t_k) = \pm 1$).
::: {.proof}
$1/t_k = (2k+1)\pi/2$, so $\sin(1/t_k) = \pm 1$ alternating with $k$; and $t_k \downarrow 0$.
:::

<1>3. At these points $|f(t_k)| = t_k$ (since $|\sin(1/t_k)| = 1$), and $f$ alternates sign: $f(t_k) = (-1)^k t_k$.
::: {.proof}
$f(t_k) = t_k \sin((2k+1)\pi/2) = t_k \cdot (-1)^k$.
:::

<1>4. For the partition $0 = t_{K} < t_{K-1} < \cdots < t_1 < t_0 = 2/\pi$ (with $f(0) = 0$), the variation sum is $\sum_{k=0}^{K-1}|f(t_{k+1}) - f(t_k)| = \sum_{k=0}^{K-1}(t_k + t_{k+1})$.
::: {.proof}
$f(t_k) = (-1)^k t_k$ and $f(t_{k+1}) = (-1)^{k+1} t_{k+1}$ have opposite signs (and $f(0) = 0$), so $|f(t_k) - f(t_{k+1})| = t_k + t_{k+1}$ exactly; write $t_K = 0$.
:::

<1>5. $V(f) \ge \sum_{k=0}^{K-1}(t_k + t_{k+1}) = t_0 + 2\sum_{k=1}^{K-1} t_k + t_K \ge 2\sum_{k=1}^{K-1} t_k$; and $\sum_{k=1}^{K-1} t_k = \frac{2}{\pi}\sum_{k=1}^{K-1}\frac{1}{2k+1} \to \infty$.
::: {.proof}
the harmonic tail $\sum \frac{1}{2k+1}$ diverges.
:::

<1>6. Q.E.D.: $V_{[0,1]}(f) = \infty$, so $f \notin \text{BV}[0,1]$.
::: {.proof}
<1>4 and <1>5 give arbitrarily large finite-variation lower bounds; $f$ is continuous (including at $0$) but has unbounded variation.
:::
:::
