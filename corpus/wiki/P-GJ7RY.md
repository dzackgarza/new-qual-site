---
schema: qual/card@1
id: P-GJ7RY
kind: problem
title: $C([0,1])$ is complete in the uniform norm but not in the $L^1$ norm
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Completeness
  - Norms
relations: []
review: draft
solved: true
---

Let $C([0, 1])$ denote the space of all continuous real-valued functions on $[0, 1]$.
  
a. Prove that $C([0, 1])$ is complete under the uniform norm $\norm{f}_u := \displaystyle\sup_{x\in [0,1]} |f (x)|$.

b. Prove that $C([0, 1])$ is not complete under the $L^1\dash$norm $\norm{f}_1 = \displaystyle\int_0^1 |f (x)| ~dx$.

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Let $\theset{f_n}$ be  a Cauchy sequence in $C(I, \norm{\wait}_\infty)$, so $\lim_n\lim_m \norm{f_m - f_n}_\infty = 0$, we will show it converges to some $f$ in this space.
- For each fixed $x_0 \in [0, 1]$, the sequence of real numbers $\theset{f_n(x_0)}$ is Cauchy in $\RR$ since
$$
x_0\in I \implies \abs{f_m(x_0) - f_n(x_0)} \leq \sup_{x\in I} \abs{f_m(x) - f_n(x)} \definedas \norm{f_m - f_n}_\infty \converges{m>n\to\infty}\to 0,
$$
- Since $\RR$ is complete, this sequence converges and we can define $f(x) \definedas \lim_{k\to \infty} f_n(x)$.
- Thus $f_n\to f$ pointwise by construction
- Claim: $\norm{f - f_n} \converges{n\to\infty}\to 0$, so $f_n$ converges to $f$ in $C([0, 1], \norm{\wait}_\infty)$.

  - Proof:
    - Fix $\eps > 0$; we will show there exists an $N$ such that $n\geq N \implies \norm{f_n - f} < \eps$
    - Fix an $x_0 \in I$. Since $f_n \to f$ pointwise, choose $N_1$ large enough so that $$n\geq N_1 \implies \abs{f_n(x_0) - f(x_0)} < \eps/2.$$
    - Since $\norm{f_n - f_m}_\infty \to 0$, choose and $N_2$ large enough so that $$n, m \geq N_2 \implies \norm{f_n - f_m}_\infty < \eps/2.$$
    - Then for $n, m \geq \max(N_1, N_2)$, we have
  \[
        \abs{f_n(x_0) - f(x_0)} 
  &=    \abs{f_n(x_0) - f(x_0) + f_m(x_0) - f_m(x_0)} \\
  &=    \abs{f_n(x_0) - f_m(x_0) + f_m(x_0) - f(x_0)} \\
  &\leq \abs{f_n(x_0) - f_m(x_0)} + \abs{f_m(x_0) - f(x_0)} \\
  &<  \abs{f_n(x_0) - f_m(x_0)} + {\eps \over 2} \\
  &\leq  \sup_{x\in I} \abs{f_n(x) - f_m(x)} + {\eps \over 2} \\
  &<  \norm{f_n - f_m}_\infty + {\eps \over 2} \\
  &\leq  {\eps \over 2} + {\eps \over 2} \\ 
  \implies \abs{f_n(x_0) - f(x_0)} &< \eps\\
  \implies \sup_{x\in I} \abs{f_n(x_0) - f(x_0)} &\leq \sup_{x\in I} \eps \quad\text{by order limit laws} \\
  \implies \norm{f_n - f} &\leq \eps\\
  .\]

- $f$ is the uniform limit of continuous functions and thus continuous, so $f\in C([0, 1])$.

:::

:::{.proof title="of b"}
\envlist

- It suffices to produce a Cauchy sequence that does not converge to a continuous function. 

- Take the following sequence of functions:
  - $f_1$ increases linearly from 0 to 1 on $[0, 1/2]$ and is 1 on $[1/2, 1]$
  - $f_2$ is 0 on $[0, 1/4]$ increases linearly from 0 to 1 on $[1/4, 1/2]$ and is 1 on $[1/2, 1]$
  - $f_3$ is 0 on $[0, 3/8]$ increases linearly from 0 to 1 on $[3/8, 1/2]$ and is 1 on $[1/2, 1]$
  - $f_3$ is 0 on $[0, (1/2 - 3/8)/2]$ increases linearly from 0 to 1 on $[(1/2 - 3/8)/2, 1/2]$ and is 1 on $[1/2, 1]$

  > Idea: take sequence starting points for the triangles: $0, 0 + {1\over 4}, 0 + {1 \over 4} + {1\over 8}, \cdots$ which converges to $1/2$ since $\sum_{k=1}^\infty{1\over 2^k} = -{1\over 2} + \sum_{k=0}^\infty  {1\over 2^k}$.

- Then each $f_n$ is clearly integrable, since its graph is contained in the unit square.
- $\theset{f_n}$ is Cauchy: geometrically subtracting areas yields a single triangle whose area tends to 0.
- But $f_n$ converges to $\chi_{[{1\over 2}, 1]}$ which is discontinuous.

:::{.remark}
show that $\int_0^1 \abs{f_n(x) - f_m(x)} \,dx \to 0$ rigorously, show that no $g\in L^1([0, 1])$ can converge to this indicator function.
:::

:::

:::

