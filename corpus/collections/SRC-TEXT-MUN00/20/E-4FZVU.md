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
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the product, uniform, and box topologies on $\mathbb{R}^\omega$.

(a) In which topologies are the following functions from $\mathbb{R}$ to $\mathbb{R}^\omega$ continuous?

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
The uniform topology is given by $\bar\rho(\mathbf a,\mathbf b)=\sup_k\min\{\abs{a_k-b_k},1\}$, and $\mathcal T_{\mathrm{prod}}\subseteq\mathcal T_{\bar\rho}\subseteq\mathcal T_{\mathrm{box}}$.
A map into $\mathbb R^\omega$ is product-continuous exactly when its coordinates are continuous, and a sequence converges in the product topology exactly when it converges coordinatewise.
Continuity or convergence in a finer topology implies it in a coarser one.
Let $U=\prod_k(-\frac1{k^2},\frac1{k^2})$, a box neighborhood of $\mathbf 0$.
In (b), $\mathbf w_n$ and $\mathbf x_n$ have $n-1$ leading zeros followed by the constant $n$, respectively $\frac1n$; $\mathbf y_n$ has $n$ entries $\frac1n$ followed by zeros; $\mathbf z_n$ has two entries $\frac1n$ followed by zeros.

<1>1. $f$ is continuous $\boxed{\text{in the product topology only}}$.

::: {.proof}
Its coordinates $t\mapsto kt$ are continuous.
For $t\ne0$, $\bar\rho(f(t),f(0))=\sup_k\min\{k\abs t,1\}=1$, so $f$ is not uniformly continuous at $0$, hence not box-continuous.
:::

<1>2. $g$ and $h$ are continuous $\boxed{\text{in the product and uniform topologies, not in the box topology}}$.

::: {.proof}
Their coordinates $t\mapsto t$ and $t\mapsto t/k$ are continuous.
$\bar\rho(g(t),g(s))=\min\{\abs{t-s},1\}$ and $\bar\rho(h(t),h(s))=\min\{\sup_k\abs{t-s}/k,1\}=\min\{\abs{t-s},1\}$.
In the box topology, $g^{-1}\bigl(\prod_k(-\frac1k,\frac1k)\bigr)=\{0\}$ and $h^{-1}(U)=\{t:\abs t<\frac1k\text{ for all }k\}=\{0\}$, which are not open.
:::

<1>3. $(\mathbf w_n)$ converges to $\mathbf 0$ $\boxed{\text{in the product topology only}}$.

::: {.proof}
For each $k$, the $k$-th coordinate of $\mathbf w_n$ is $0$ once $n>k$.
But $\bar\rho(\mathbf w_n,\mathbf 0)=1$ for every $n$, and the product limit $\mathbf 0$ is the only possible limit in the finer Hausdorff topologies.
:::

<1>4. $(\mathbf x_n)$ and $(\mathbf y_n)$ converge to $\mathbf 0$ $\boxed{\text{in the product and uniform topologies, not in the box topology}}$.

::: {.proof}
$\bar\rho(\mathbf x_n,\mathbf 0)=\bar\rho(\mathbf y_n,\mathbf 0)=\frac1n\to0$.
The $n$-th coordinate of both $\mathbf x_n$ and $\mathbf y_n$ is $\frac1n\ge\frac1{n^2}$, so neither sequence ever enters $U$.
:::

<1>5. $(\mathbf z_n)$ converges to $\mathbf 0$ $\boxed{\text{in all three topologies}}$.

::: {.proof}
Let $\prod_k(-a_k,a_k)$ be a box neighborhood of $\mathbf 0$.
The coordinates of $\mathbf z_n$ beyond the second are $0$, so $\mathbf z_n$ lies in it once $\frac1n<\min\{a_1,a_2\}$.
Every box neighborhood of $\mathbf 0$ contains one of this form.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 answer (a), and steps <1>3, <1>4, and <1>5 answer (b).
:::
:::
