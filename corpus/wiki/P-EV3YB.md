---
schema: qual/card@1
id: P-EV3YB
kind: problem
title: "Suppose $\\theset{g_n}$ is a uniformly convergent sequence of functions\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - sequences-of-functions
  - uniform-continuity
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $\theset{g_n}$ is a uniformly convergent sequence of functions from $\RR$ to $\RR$ and $f:\RR\to \RR$ is uniformly continuous.
Prove that the sequence $\theset{f\circ g_n}$ is uniformly convergent.
:::

:::{.solution}
Uniformly convergent means that $\norm{g_i - g_j}_{\infty} \to 0$, so $\sup_{x\in X}\abs{g_i(x)-g_j(x)} \convergesto{i, j\to\infty} 0$.
We want to show that given $\eps$ we can find $N_0$ such that $i, j > N_0$ yields
\[
\sup_{x\in X}\abs{ f\circ g_i(x) - f\circ g_j(x) } < \eps
.\]

Fix $\eps> 0$, then choose $\delta_1 = \delta_1(\eps)$ by uniform continuity of $f$ to guarantee
\[
\abs{y_1 - y_2} \leq \delta_1 \implies \abs{f(y_1) - f(y_2) } < \eps \, \forall y_1, y_2\in X
.\]
Now by uniform convergence of $\ts{g_n}$, choose $N_0 = N_0(\delta_1)$ such that 
\[
i, j \geq N_0 \implies \abs{ g_i(x) - g_j(x) } < \delta_1 \, \forall x\in X
.\]

Now writing $y_1 \da g_i(x), y_2 \da g_j(x)$, choose $i, j > N_0$ yields
\[
\abs{y_1 - y_2} \da \abs{g_i(x) - g_j(x) } < \delta_1 \\
\implies \abs{f(y_1) - f(y_2)} \da \abs{f(g_i(x)) - f(g_j(x))} < \eps
,\]
and taking the supremum over $x\in X$ preserves the inequality since $\delta_1$ and consequently $N_0$ only depend on $\eps$.
:::

