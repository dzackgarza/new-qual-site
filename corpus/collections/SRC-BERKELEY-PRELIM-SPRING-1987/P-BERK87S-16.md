---
schema: qual/card@1
id: P-BERK87S-16
kind: problem
title: The pointwise supremum of a uniformly bounded equicontinuous family is continuous
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used uniform boundedness to make the pointwise supremum finite. At an
    arbitrary point, equicontinuity bounds every member of the family by
    the same epsilon-delta estimate; taking suprema in both directions
    transfers that estimate to g.
---

::: {.problem}
Let $\mathcal F$ be a uniformly bounded, equicontinuous family of real-valued functions on a metric space $(X,d)$. Prove that
\[
g(x)=\sup\{f(x):f\in\mathcal F\}
\]
is continuous.
:::

::: {.solution}
::: pf

::: {.pf-step #g-finite}
The value $g(x)$ is finite for every $x\in X$.

::: pf-proof
Uniform boundedness gives a constant $M>0$ such that
$$
\abs{f(x)}\leq M
$$
for every $f\in\mathcal F$ and every $x\in X$. Hence
$$
-M\leq f(x)\leq M
$$
for all $f\in\mathcal F$, so the supremum defining $g(x)$ is a finite
real number.
:::

:::

::: {.pf-step #upper-bound}
Fix $x_0\in X$ and $\varepsilon>0$. There exists $\delta>0$ such
that, whenever $d(x,x_0)<\delta$,
$$
g(x)\leq g(x_0)+\frac{\varepsilon}{2}.
$$

::: pf-proof
By equicontinuity at $x_0$, there exists $\delta>0$ such that
$$
d(x,x_0)<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(x_0)}<\frac{\varepsilon}{2}
$$
for every $f\in\mathcal F$. Thus, for such $x$ and every
$f\in\mathcal F$,
$$
f(x)
<
f(x_0)+\frac{\varepsilon}{2}
\leq
g(x_0)+\frac{\varepsilon}{2}.
$$
Taking the supremum over $f\in\mathcal F$ gives
$$
g(x)\leq g(x_0)+\frac{\varepsilon}{2}.
$$
:::

:::

::: {.pf-step #lower-bound}
For the same $\delta$, whenever $d(x,x_0)<\delta$,
$$
g(x_0)\leq g(x)+\frac{\varepsilon}{2}.
$$

::: pf-proof
The equicontinuity estimate from step [](#upper-bound){.pf-ref} also gives, for every
$f\in\mathcal F$,
$$
f(x_0)
<
f(x)+\frac{\varepsilon}{2}
\leq
g(x)+\frac{\varepsilon}{2}.
$$
Taking the supremum over $f\in\mathcal F$ yields the stated inequality.
:::

:::

::: {.pf-step #continuous-at-x0}
The function $g$ is continuous at $x_0$.

::: pf-proof
By steps [](#upper-bound){.pf-ref} and [](#lower-bound){.pf-ref}, if $d(x,x_0)<\delta$, then
$$
\abs{g(x)-g(x_0)}
\leq
\frac{\varepsilon}{2}
<
\varepsilon.
$$
This is continuity at $x_0$.
:::

:::

::: pf-qed
The point $x_0\in X$ was arbitrary, so step [](#continuous-at-x0){.pf-ref} proves that $g$ is
continuous on $X$.
:::

:::
:::
