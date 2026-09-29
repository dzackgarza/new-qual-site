---
schema: qual/card@1
id: P-BKF06-3B
kind: problem
title: Continuity of $x\mapsto\max_{y\in[0,1]}f(x,y)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained compact-neighborhood uniform
    continuity argument and the symmetric maximum estimate.
---

::: {.problem}
Let $f:\mathbb R\times[0,1]\to\mathbb R$ be continuous.
For $x\in\mathbb R$, define
\[
g(x)=\max\{f(x,y):y\in[0,1]\}.
\]
Show that $g$ is continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #max-exists}
For every $x\in\RR$, the maximum defining $g(x)$ exists.

::: pf-proof
For fixed $x$, the function
$$
y\longmapsto f(x,y)
$$
is continuous on the compact interval $[0,1]$. Hence it attains a
maximum there.
:::

:::

::: {.pf-step #uniform-continuity-delta}
Fix $a\in\RR$ and $\epsilon>0$. There exists
$\delta\in(0,1]$ such that
$$
\abs{x-z}<\delta
$$
and $x,z\in[a-1,a+1]$ imply
$$
\abs{f(x,y)-f(z,y)}<\epsilon
$$
for every $y\in[0,1]$.

::: pf-proof
The rectangle
$$
K=[a-1,a+1]\times[0,1]
$$
is compact. The restriction of $f$ to $K$ is therefore uniformly
continuous. Choose a uniform-continuity radius $\delta_0>0$ for
$\epsilon$, and set
$$
\delta=\min\{1,\delta_0\}.
$$
For points $(x,y),(z,y)\in K$, their Euclidean distance is
$\abs{x-z}$. Thus the displayed implication follows.
:::

:::

::: {.pf-step #g-close-bound}
Under the hypotheses of step [](#uniform-continuity-delta){.pf-ref},
$$
\abs{g(x)-g(z)}<\epsilon.
$$

::: pf-proof
By step [](#max-exists){.pf-ref}, choose $y_x\in[0,1]$ with
$$
g(x)=f(x,y_x).
$$
Then step [](#uniform-continuity-delta){.pf-ref} gives
$$
g(x)
=
f(x,y_x)
<
f(z,y_x)+\epsilon
\le
g(z)+\epsilon.
$$
Interchanging $x$ and $z$ gives
$$
g(z)<g(x)+\epsilon.
$$
Together these inequalities yield
$$
\abs{g(x)-g(z)}<\epsilon.
$$
:::

:::

::: {.pf-step #g-continuous-at-a}
The function $g$ is continuous at $a$.

::: pf-proof
If $\abs{x-a}<\delta$, where $\delta$ is from step [](#uniform-continuity-delta){.pf-ref}, then
$x,a\in[a-1,a+1]$. Applying step [](#g-close-bound){.pf-ref} with $z=a$ gives
$$
\abs{g(x)-g(a)}<\epsilon.
$$
This is continuity at $a$.
:::

:::

::: {.pf-step #g-continuous-everywhere}
Therefore
$$
\boxed{g\text{ is continuous on }\RR}.
$$

::: pf-proof
The point $a\in\RR$ in step [](#g-continuous-at-a){.pf-ref} was arbitrary.
:::

:::

::: pf-qed
Step [](#g-continuous-everywhere){.pf-ref} is the required conclusion.
:::

:::

:::
