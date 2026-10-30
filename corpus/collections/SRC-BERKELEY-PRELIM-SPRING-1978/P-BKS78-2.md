---
schema: qual/card@1
id: P-BKS78-2
kind: problem
title: Continuous maps have closed graphs, but the converse can fail
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Prove that if $g:\RR^n\to\RR^n$ is continuous, then its graph is closed in $\RR^n\times\RR^n$.
Is the converse true?
:::

::: {.solution}
Let
$$
\Gamma_g
\coloneqq
\{(x,g(x)):x\in\RR^n\}
$$
denote the graph of $g$.

::: pf

::: {.pf-step #limits-in-graph}
If $g$ is continuous and
$$
(x_m,g(x_m))\longrightarrow(x,y)
$$
in $\RR^n\times\RR^n$, then
$$
y=g(x).
$$

::: pf-proof
Convergence in the product is coordinatewise, so
$$
x_m\longrightarrow x
$$
and
$$
g(x_m)\longrightarrow y.
$$
Continuity of $g$ gives
$$
g(x_m)\longrightarrow g(x).
$$
Limits in $\RR^n$ are unique, hence $y=g(x)$.
:::

:::

::: {.pf-step #continuous-closed-graph}
If $g$ is continuous, then $\Gamma_g$ is closed.

::: pf-proof
[](#limits-in-graph){.pf-ref} shows that every convergent sequence of points of $\Gamma_g$ has its limit again in $\Gamma_g$. Since $\RR^n\times\RR^n$ is a metric space, sequentially closed subsets are closed.
:::

:::

::: {.pf-step #counterexample}
The converse is false already for $n=1$.

::: pf-proof
Define
$$
h:\RR\longrightarrow\RR,
\qquad
h(x)=
\begin{cases}
\dfrac1x,&x\neq0,\\[4pt]
0,&x=0.
\end{cases}
$$
This function is not continuous at $0$, since
$$
h(1/m)=m
$$
does not tend to $h(0)=0$.
:::

:::

::: {.pf-step #counterexample-closed-graph}
The graph of the function $h$ from [](#counterexample){.pf-ref} is closed in $\RR^2$.

::: pf-proof
Suppose
$$
(x_m,h(x_m))\longrightarrow(x,y)
$$
in $\RR^2$.

If $x\neq0$, then $x_m\neq0$ for all sufficiently large $m$, so
$$
h(x_m)=\frac1{x_m}\longrightarrow\frac1x=h(x).
$$
Thus $y=h(x)$.

If $x=0$, then convergence of the second coordinates forces the sequence $h(x_m)$ to be bounded. There cannot be infinitely many indices with $x_m\neq0$ and $x_m\to0$, because along such indices
$$
\abs{h(x_m)}=\frac1{\abs{x_m}}\longrightarrow\infty.
$$
Hence $x_m=0$ eventually, so
$$
y=0=h(0).
$$
Thus every convergent sequence in the graph has its limit in the graph, which is therefore closed.
:::

:::

::: pf-step
Therefore
$$
\boxed{\text{continuity implies closed graph, but closed graph does not imply continuity}.}
$$

::: pf-proof
[](#continuous-closed-graph){.pf-ref} proves the implication, while [](#counterexample){.pf-ref} and [](#counterexample-closed-graph){.pf-ref} give a counterexample to the converse.
:::

:::

:::

:::
