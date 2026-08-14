---
schema: qual/card@1
id: P-5VEUZ
kind: problem
title: "Suppose $\\theset{f_n}_{n\\in \\NN}$ is a sequence of continuous functions $f_n: [0, 1]\\to \\RR$ such that $f_n(x) \\geq f_{n+1}(x) \\geq 0 \\quad \\forall n\\in \\NN,\\, \\forall x\\in [0, 1]$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - sequences-of-functions
  - compactness
  - continuity
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of continuous functions $f_n: [0, 1]\to \RR$ such that 
\[  
f_n(x) \geq f_{n+1}(x) \geq 0 \quad \forall n\in \NN,\, \forall x\in [0, 1]
.\]
Prove that if $\theset{f_n}$ converges pointwise to $0$ on $[0, 1]$ then it converges to $0$ uniformly on $[0, 1]$.
:::

:::{.solution}
Let $\eps>0$, we want to show that there exists an $N_0$ such that $n\geq N_0$ implies $\norm{f_n}_\infty<\eps$.
Fix $x$, by pointwise convergence pick $M_x = M_x(x, \eps)$ so that $n\geq M \implies \abs{f_n(x)} < \eps$.
By continuity, this bound holds in some neighborhood $U_x \ni x$.
Produce a cover $\ts{U_x}_{x\in [0, 1]}\covers [0, 1]$; by compactness produce a finite subcover $\ts{U_1, \cdots, U_m} \covers [0, 1]$.
Each $U_i$ corresponds to some $x_i$ and some $M_{x_i}$, so choose $N_0 > \max_{i\leq m} \ts{M_{x_i}}$.
Then $n\geq N_0 \implies N\geq M_{x_i}$ for each $i$, so $\abs{f_n(x)} < \eps$ for each $x\in [0, 1]$ since $x\in U_i$ for some $i$.
So $\sup_{x\in X} \abs{f_n(x)} = \norm{f_n}_{\infty } < \eps$.
:::

