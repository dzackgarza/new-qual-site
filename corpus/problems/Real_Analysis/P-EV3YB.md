---
schema: qual/card@1
id: P-EV3YB
kind: problem
title: A uniformly continuous map preserves uniform convergence under composition
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Uniform Continuity
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{g_n}$ is a uniformly convergent sequence of functions from $\RR$ to $\RR$ and $f:\RR\to \RR$ is uniformly continuous.
Prove that the sequence $\theset{f\circ g_n}$ is uniformly convergent.
:::

::: {.solution}
::: pf

::: {.pf-step #delta}
Fix $\varepsilon>0$. There is $\delta>0$ such that $\abs{f(y_1)-f(y_2)}<\varepsilon$ for all $y_1,y_2\in\RR$ with $\abs{y_1-y_2}<\delta$.

::: pf-proof
This is the uniform continuity of $f$.
:::

:::

::: {.pf-step #cauchy}
There is $N$ such that $\sup_{x\in\RR}\abs{g_i(x)-g_j(x)}<\delta$ for all $i,j\ge N$.

::: pf-proof
A uniformly convergent sequence is uniformly Cauchy: if $g_n\to g$ uniformly, choose $N$ with $\sup_x\abs{g_n(x)-g(x)}<\delta/2$ for $n\ge N$ and apply the triangle inequality.
:::

:::

::: pf-step
$\theset{f\circ g_n}$ is uniformly convergent.

::: pf-proof
For $i,j\ge N$ and every $x\in\RR$, step [](#cauchy){.pf-ref} gives $\abs{g_i(x)-g_j(x)}<\delta$, so step [](#delta){.pf-ref} with $y_1=g_i(x)$ and $y_2=g_j(x)$ gives $\abs{f(g_i(x))-f(g_j(x))}<\varepsilon$.
Since $N$ depends only on $\varepsilon$, the sequence $\theset{f\circ g_n}$ is uniformly Cauchy on $\RR$.
A uniformly Cauchy sequence of real-valued functions converges uniformly: it converges pointwise because $\RR$ is complete, and letting $j\to\infty$ in the Cauchy estimate bounds the distance to the limit by $\varepsilon$ uniformly in $x$.
:::

:::

:::

:::
