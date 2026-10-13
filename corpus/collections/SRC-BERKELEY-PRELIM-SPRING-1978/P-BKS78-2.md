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
Prove that if $g:\mathbb R^n\to\mathbb R^n$ is continuous, then its graph is closed in $\mathbb R^n\times\mathbb R^n$.
Is the converse true?
:::

::: {.solution}
Let
$$
\Gamma_g
\coloneqq
\{(x,g(x)):x\in\mathbb R^n\}
$$
denote the graph of $g$.

<1>1. If $g$ is continuous and
$$
(x_m,g(x_m))\longrightarrow(x,y)
$$
in $\mathbb R^n\times\mathbb R^n$, then
$$
y=g(x).
$$

::: {.proof}
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
Limits in $\mathbb R^n$ are unique, hence $y=g(x)$.
:::

<1>2. If $g$ is continuous, then $\Gamma_g$ is closed.

::: {.proof}
Step <1>1 shows that every convergent sequence of points of $\Gamma_g$ has its limit again in $\Gamma_g$. Since $\mathbb R^n\times\mathbb R^n$ is a metric space, sequentially closed subsets are closed.
:::

<1>3. The converse is false already for $n=1$.

::: {.proof}
Define
$$
h:\mathbb R\longrightarrow\mathbb R,
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

<1>4. The graph of the function $h$ from step <1>3 is closed in $\mathbb R^2$.

::: {.proof}
Suppose
$$
(x_m,h(x_m))\longrightarrow(x,y)
$$
in $\mathbb R^2$.

If $x\neq0$, then $x_m\neq0$ for all sufficiently large $m$, so
$$
h(x_m)=\frac1{x_m}\longrightarrow\frac1x=h(x).
$$
Thus $y=h(x)$.

If $x=0$, then convergence of the second coordinates forces the sequence $h(x_m)$ to be bounded. There cannot be infinitely many indices with $x_m\neq0$ and $x_m\to0$, because along such indices
$$
|h(x_m)|=\frac1{|x_m|}\longrightarrow\infty.
$$
Hence $x_m=0$ eventually, so
$$
y=0=h(0).
$$
Thus every convergent sequence in the graph has its limit in the graph, which is therefore closed.
:::

<1>5. Therefore
$$
\boxed{\text{continuity implies closed graph, but closed graph does not imply continuity}.}
$$

::: {.proof}
Step <1>2 proves the implication, while steps <1>3--<1>4 give a counterexample to the converse.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers both parts.
:::
:::
