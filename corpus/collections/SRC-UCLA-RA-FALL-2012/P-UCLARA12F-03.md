---
schema: qual/card@1
id: P-UCLARA12F-03
kind: problem
title: Nearest point to the origin in a closed convex set
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Convex Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $H$ be a Hilbert space and let $E\subseteq H$ be a closed convex subset.
Prove that there exists a unique $x\in E$ such that
$$
\norm{x}=\inf_{y\in E}\norm{y}.
$$
:::

::: {.solution}

Set
$$
d\coloneqq\inf_{y\in E}\norm{y}.
$$

::: pf

::: {.pf-step #s1-1}

There exists a sequence $(x_n)$ in $E$ such that
$$
\norm{x_n}\longrightarrow d.
$$


::: pf-proof

By the definition of the infimum, for each $n\ge1$ one can choose $x_n\in E$ with
$$
d\le\norm{x_n}<d+\frac1n.
$$

:::

:::

::: {.pf-step #s1-2}

The minimizing sequence $(x_n)$ is Cauchy in $H$.


::: pf-proof

Because $E$ is convex,
$$
\frac{x_n+x_m}{2}\in E.
$$
Therefore
$$
\norm{\frac{x_n+x_m}{2}}\ge d.
$$
The parallelogram identity gives
$$
\begin{aligned}
\norm{x_n-x_m}^2
&=2\norm{x_n}^2+2\norm{x_m}^2-\norm{x_n+x_m}^2\\
&=2\norm{x_n}^2+2\norm{x_m}^2
-4\norm{\frac{x_n+x_m}{2}}^2\\
&\le2\norm{x_n}^2+2\norm{x_m}^2-4d^2.
\end{aligned}
$$
As $n,m\to\infty$, the right-hand side tends to $0$ by step [](#s1-1){.pf-ref}. Hence $(x_n)$ is Cauchy.

:::

:::

::: {.pf-step #s1-3}

There exists $x\in E$ such that
$$
\norm{x}=d.
$$


::: pf-proof

Since $H$ is complete, step [](#s1-2){.pf-ref} gives a limit $x_n\to x$ in $H$. The set $E$ is closed, so $x\in E$. The norm is continuous, and therefore
$$
\norm{x}=\lim_{n\to\infty}\norm{x_n}=d.
$$

:::

:::

::: {.pf-step #s1-4}

The minimizing point is unique.


::: pf-proof

Suppose $x,y\in E$ both satisfy
$$
\norm{x}=\norm{y}=d.
$$
Convexity gives $(x+y)/2\in E$, so
$$
\norm{\frac{x+y}{2}}\ge d.
$$
Again by the parallelogram identity,
$$
\begin{aligned}
\norm{x-y}^2
&=2\norm{x}^2+2\norm{y}^2
-4\norm{\frac{x+y}{2}}^2\\
&\le4d^2-4d^2=0.
\end{aligned}
$$
Thus $x=y$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves existence and step [](#s1-4){.pf-ref} proves uniqueness.

:::

:::

:::
