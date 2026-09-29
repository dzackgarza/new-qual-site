---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W5
kind: problem
title: Equicontinuity upgrades pointwise convergence to uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Uniform Convergence
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that if $\{f_n\}$ is an equicontinuous sequence of functions on a compact set $K$ and $f_n\to f$ pointwise on $K$, then $f_n\to f$ uniformly on $K$.
:::

:::: {.solution}
**Goal:** Show $\{f_n\}$ equicontinuous on compact $K$ with $f_n \to f$ pointwise implies $f_n \to f$ uniformly on $K$.

::: pf

::: {.pf-step #s1}
$f$ is continuous.

::: pf-proof
Fix $x_0$ and $\varepsilon > 0$; by equicontinuity choose $\delta$ with $\|x-x_0\| < \delta \Rightarrow |f_n(x) - f_n(x_0)| < \varepsilon/3$ for all $n$.
For $\|x - x_0\| < \delta$, let $n \to \infty$ in $|f_n(x) - f_n(x_0)| < \varepsilon/3$ to get $|f(x) - f(x_0)| \le \varepsilon/3 < \varepsilon$.
So $f$ is continuous at $x_0$.
:::

:::

::: pf-step
Fix $\varepsilon > 0$.
By equicontinuity, for each $x \in K$ there is $\delta_x > 0$ with $\|y - x\| < \delta_x \Rightarrow |f_n(y) - f_n(x)| < \varepsilon/3$ for all $n$.

::: pf-proof
This is the definition of equicontinuity: the same $\delta_x$ works uniformly over all $n$.
:::

:::

::: pf-step
Choose finitely many $x_1, \ldots, x_m$ such that $K \subseteq \bigcup_i B(x_i, \delta_{x_i}/2)$.

::: pf-proof
The open cover $\{B(x, \delta_x/2) : x \in K\}$ of the compact set $K$ has a finite subcover.
:::

:::

::: {.pf-step #s4}
For each $i$, choose $N_i$ with $|f_n(x_i) - f(x_i)| < \varepsilon/3$ for all $n \ge N_i$.

::: pf-proof
This is pointwise convergence $f_n(x_i) \to f(x_i)$ at the point $x_i$.
:::

:::

::: pf-step
Set $N = \max_i N_i$.
For $n \ge N$ and any $x \in K$: pick $i$ with $x \in B(x_i, \delta_{x_i}/2)$; then $|f_n(x) - f(x)| \le |f_n(x) - f_n(x_i)| + |f_n(x_i) - f(x_i)| + |f(x_i) - f(x)|$.

::: pf-proof
This is the triangle inequality applied to the three differences.
:::

:::

::: pf-step
Each of the three terms is $< \varepsilon/3$ for $n \ge N$.

::: pf-proof

::: {.pf-step #s6-1}
$|f_n(x) - f_n(x_i)| < \varepsilon/3$: $\|x - x_i\| < \delta_{x_i}/2 < \delta_{x_i}$, equicontinuity.
:::

::: {.pf-step #s6-2}
$|f_n(x_i) - f(x_i)| < \varepsilon/3$: $n \ge N \ge N_i$, by step [](#s4){.pf-ref}.
:::

::: {.pf-step #s6-3}
$|f(x_i) - f(x)| < \varepsilon/3$: since $|f_n(x) - f_n(x_i)| < \varepsilon/3$ for all $n$ (equicontinuity with $\|x - x_i\| < \delta_{x_i}$), let $n \to \infty$; continuity of $f$ from step [](#s1){.pf-ref} also works with a suitable $\delta$.

::: pf-proof
Pointwise convergence $f_n \to f$ at both $x$ and $x_i$ gives $|f(x) - f(x_i)| = \lim_n |f_n(x) - f_n(x_i)| \le \varepsilon/3$.
:::

:::

::: pf-qed
Steps [](#s6-1){.pf-ref}, [](#s6-2){.pf-ref}, and [](#s6-3){.pf-ref} sum to $|f_n(x) - f(x)| < \varepsilon$ for all $x \in K$, $n \ge N$: uniform convergence.
:::

:::

:::

:::
::::
