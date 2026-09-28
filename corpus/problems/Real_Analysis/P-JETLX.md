---
schema: qual/card@1
id: P-JETLX
kind: problem
title: $L^1((0,2\pi))$ functions as $g+h$ with $g\in L^2$ and $\|h\|_1$ arbitrarily
  small
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Density
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $f\in L^1((0, 2\pi))$.

i. Show that for an \( \epsilon>0 \) one can write $f = g+h$ where $g\in L^2((0, 2\pi))$ and $\norm{H}_1 < \epsilon$.
:::
::: {.solution}
<1>1. It suffices to treat real $f \ge 0$.

::: {.proof}
Write $f = u^+ - u^- + i(v^+ - v^-)$ with $u = \operatorname{Re} f$, $v = \operatorname{Im} f$. If each of the four nonnegative parts is $g_j + h_j$ with $g_j \in L^2$ and $\|h_j\|_1 < \eps/4$, the corresponding combinations give $f = g + h$ with $g \in L^2$ and $\|h\|_1 < \eps$.
:::

<1>2. For $f \ge 0$ and $M > 0$, put $g_M = \min(f, M)$ and $h_M = f - g_M = (f - M)^+$. Then $g_M \in L^2((0,2\pi))$.

::: {.proof}
$0 \le g_M \le M$ and $g_M \le f$, so $\int g_M^2 \le M\int g_M \le M\|f\|_1$.
:::

<1>3. $\|h_M\|_1 \to 0$ as $M \to \infty$.

::: {.proof}
$h_M \to 0$ at every point where $f < \infty$, hence a.e., and $0 \le h_M \le f \in L^1$, so dominated convergence applies.
:::

<1>4. Q.E.D.

::: {.proof}
By steps <1>1--<1>3, choosing $M$ with $\|h_M\|_1 < \eps$ gives $f = g_M + h_M$ with $g_M \in L^2$.
:::
:::

::: {.remark}
In the statement, $\norm{H}_1$ is read as $\norm{h}_1$.
:::
