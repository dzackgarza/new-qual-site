---
schema: qual/card@1
id: E-4FZVU
kind: problem
title: Continuity and convergence in the product, uniform, and box topologies
classification:
  areas:
  - topology
  topics:
  - Convergence
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 4, printed p. 127; the three maps,
    the four sequences and both questions are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.4, PDF pp. 18-19. The three maps are continuous
    in the product topology by Theorem 19.6 and discontinuous in the box topology, where a
    box of shrinking intervals has preimage the single point 0; in the uniform topology f
    fails and g and h are continuous. The sequences are decided as recorded: w only in the
    product topology, x and y in the product and uniform topologies, z in all three.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Consider the product, uniform, and box topologies on $\RR^\omega$.

(a) In which topologies are the following functions from $\RR$ to $\RR^\omega$ continuous?

$$
\begin{array}{l}
f(t) = (t, 2t, 3t, \ldots), \\
g(t) = (t, t, t, \ldots), \\
h(t) = (t, \tfrac{1}{2}t, \tfrac{1}{3}t, \ldots).
\end{array}
$$

(b) In which topologies do the following sequences converge?

$$
\mathbf{w}_1 = (1, 1, 1, 1, \dots), \quad \mathbf{x}_1 = (1, 1, 1, 1, \dots),
$$

$$
\mathbf{w}_2 = (0, 2, 2, 2, \dots), \quad \mathbf{x}_2 = (0, \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, \dots),
$$

$$
\mathbf{w}_3 = (0, 0, 3, 3, \dots), \quad \mathbf{x}_3 = (0, 0, \tfrac{1}{3}, \tfrac{1}{3}, \dots),
$$

$$
\mathbf{y}_1 = (1, 0, 0, 0, \dots), \quad \mathbf{z}_1 = (1, 1, 0, 0, \dots),
$$

$$
\mathbf{y}_2 = (\tfrac{1}{2}, \tfrac{1}{2}, 0, 0, \dots), \quad \mathbf{z}_2 = (\tfrac{1}{2}, \tfrac{1}{2}, 0, 0, \dots),
$$

$$
\mathbf{y}_3 = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}, 0, \dots), \quad \mathbf{z}_3 = (\tfrac{1}{3}, \tfrac{1}{3}, 0, 0, \dots).
$$
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.4, PDF pp. 18--19** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts and all four sequences are theirs.

(a) In the product topology $f,g,h$ are continuous, since each coordinate function ($t\mapsto it$, $t\mapsto t$, $t\mapsto t/i$) is continuous and Theorem 19.6 applies. In the box topology none of the three is continuous: the set
$$
B=(-1,1)\times\big(-\tfrac1{2^{2}},\tfrac1{2^{2}}\big)\times\cdots\times\big(-\tfrac1{n^{2}},\tfrac1{n^{2}}\big)\times\cdots
$$
is box-open and contains $\mathbf{0}$, and for each of the three maps the condition $f(t)\in B$ reads $\abs{it}<1/i^{2}$, $\abs{t}<1/i^{2}$, $\abs{t/i}<1/i^{2}$ for all $i$, that is $\abs{t}<1/i^{3}$, $\abs{t}<1/i^{2}$, $\abs{t}<1/i$ for all $i$: in every case only $t=0$. So the preimage is $\{0\}$, not open in $\RR$.

For the uniform topology: $f$ is not continuous, since $\bar\rho(f(t),\mathbf{0})=\sup_{i}\min\{\abs{it},1\}=1$ for every $t\ne0$, so $f^{-1}(B_{\bar\rho}(\mathbf{0},1))=\{0\}$. But $g$ and $h$ are continuous: for $s,t\in\RR$ with $\abs{s-t}<1$,
$$
\bar\rho(g(s),g(t))=\min\{\abs{s-t},1\}=\bar\rho(h(s),h(t)),
$$
because the $i$-th coordinate difference of $h(s),h(t)$ is $\abs{s-t}/i\le\abs{s-t}$, with equality at $i=1$; so given a ball of radius $\varepsilon$ around $g(t)$ or $h(t)$ the interval $(t-r,t+r)$ with $r=\min\{\varepsilon,1\}$ is mapped into it.

(b) The answers are: $\mathbf{w}_{i}$ converges in the product topology only; $\mathbf{x}_{i}$ and $\mathbf{y}_{i}$ converge in the product and uniform topologies but not in the box topology; $\mathbf{z}_{i}$ converges in all three.

*Product.* Each of the four sequences has, in each fixed coordinate, either the constant value $0$ for large $i$ or a value tending to $0$; so each converges to $\mathbf{0}$ coordinatewise, hence in the product topology (Exercise 19.6). Since the other two topologies are finer and Hausdorff, a limit there would also be $\mathbf{0}$.

*Uniform.* $\bar\rho(\mathbf{x}_{i},\mathbf{0})=\bar\rho(\mathbf{y}_{i},\mathbf{0})=\bar\rho(\mathbf{z}_{i},\mathbf{0})=1/i\to0$, so those three converge uniformly; but $\bar\rho(\mathbf{w}_{i},\mathbf{0})=\sup_{j}\min\{j,1\}=1$ for $i\ge2$ (the $i$-th coordinate of $\mathbf{w}_{i}$ is $i$), so $\mathbf{w}_{i}$ does not converge in the uniform topology.

*Box.* $\mathbf{z}_{i}=(1/i,1/i,0,0,\dots)$ converges to $\mathbf{0}$: for a box neighbourhood $\prod(-\varepsilon_{n},\varepsilon_{n})$ of $\mathbf{0}$ one has $1/i<\min\{\varepsilon_{1},\varepsilon_{2}\}$ for large $i$. But $\mathbf{w}_{i}\notin\prod(-1,1)$ for every $i$, and for $\mathbf{x}_{i}$ and $\mathbf{y}_{i}$ the box neighbourhood $\prod(-1/n^{2},1/n^{2})$ is not entered eventually: $\mathbf{x}_{i}$ has $i$-th coordinate $1/i\notin(-1/i^{2},1/i^{2})$, and $\mathbf{y}_{i}$ has $i$-th coordinate $1/i\notin(-1/i^{2},1/i^{2})$. So none of the other three converges in the box topology.
:::
