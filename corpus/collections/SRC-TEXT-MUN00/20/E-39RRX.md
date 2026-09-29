---
schema: qual/card@1
id: E-39RRX
kind: problem
title: Four topologies on $\ell^2$ and the Hilbert cube
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be the subset of $\mathbb{R}^\omega$ consisting of all sequences $\mathbf{x}$ such that $\sum x_i^2$ converges.
Then the formula

$$
d(\mathbf{x}, \mathbf{y}) = \left[ \sum_{i=1}^{\infty} (x_i - y_i)^2 \right]^{1/2}
$$

defines a metric on $X$.
(See Exercise 10.) On $X$ we have the three topologies it inherits from the box, uniform, and product topologies on $\mathbb{R}^\omega$.
We have also the topology given by the metric $d$, which we call the $\ell^2$-topology.

(a) Show that on $X$, we have the inclusions

$$
\text{box topology} \supset \ell^2\text{-topology} \supset \text{uniform topology}.
$$

(b) The set $\mathbb{R}^\infty$ of all sequences that are eventually zero is contained in $X$.
Show that the four topologies that $\mathbb{R}^\infty$ inherits as a subspace of $X$ are all distinct.

(c) The set

$$
H = \prod_{n \in \mathbb{Z}_+} [0, 1/n]
$$

is contained in $X$; it is called the Hilbert cube.
Compare the four topologies that $H$ inherits as a subspace of $X$.
:::

::: {.solution}
Write $\mathcal T_{\mathrm{box}}$, $\mathcal T_d$, $\mathcal T_{\bar\rho}$, and $\mathcal T_{\mathrm{prod}}$ for the box, $\ell^2$, uniform, and product topologies on $X$ and on its subspaces.
On $\mathbb R^\omega$, $\mathcal T_{\mathrm{prod}}\subseteq\mathcal T_{\bar\rho}\subseteq\mathcal T_{\mathrm{box}}$, and these inclusions pass to subspaces.

::: pf

::: {.pf-step #uniform-subset-l2}
On $X$, $\mathcal T_{\bar\rho}\subseteq\mathcal T_d$.

::: pf-proof
For $\mathbf x,\mathbf y\in X$, $\bar\rho(\mathbf x,\mathbf y)\le\sup_i\abs{x_i-y_i}\le d(\mathbf x,\mathbf y)$, so $B_d(\mathbf x,\varepsilon)\subseteq B_{\bar\rho}(\mathbf x,\varepsilon)$.
:::

:::

::: {.pf-step #l2-subset-box}
On $X$, $\mathcal T_d\subseteq\mathcal T_{\mathrm{box}}$.

::: pf-proof
Given $\mathbf x\in X$ and $\varepsilon>0$, put $\varepsilon_i=\varepsilon\,2^{-(i+1)/2}$, so $\sum_i\varepsilon_i^2=\varepsilon^2/2$.
For $\mathbf y$ in the box neighborhood $U=X\cap\prod_i(x_i-\varepsilon_i,x_i+\varepsilon_i)$, $d(\mathbf x,\mathbf y)^2\le\sum_i\varepsilon_i^2<\varepsilon^2$, so $U\subseteq B_d(\mathbf x,\varepsilon)$.
:::

:::

::: {.pf-step #part-b}
On $\mathbb R^\infty$, $\mathcal T_{\mathrm{prod}}\subsetneq\mathcal T_{\bar\rho}\subsetneq\mathcal T_d\subsetneq\mathcal T_{\mathrm{box}}$.

::: pf-proof
The inclusions hold by steps [](#uniform-subset-l2){.pf-ref} and [](#l2-subset-box){.pf-ref}. Each is strict because a sequence in $\mathbb R^\infty$ converges to $\mathbf 0$ in the coarser topology but not in the finer one; $\mathbf e_n$ denotes the sequence with $1$ in place $n$ and $0$ elsewhere.
The sequence $\mathbf e_n$ converges to $\mathbf 0$ coordinatewise, but $\bar\rho(\mathbf e_n,\mathbf 0)=1$.
The sequence $\mathbf y_n$ with its first $n$ coordinates $1/\sqrt n$ and the rest $0$ has $\bar\rho(\mathbf y_n,\mathbf 0)=1/\sqrt n\to0$, but $d(\mathbf y_n,\mathbf 0)=1$.
The sequence $\mathbf w_n=\frac1n\mathbf e_n$ has $d(\mathbf w_n,\mathbf 0)=\frac1n\to0$, but $\mathbf w_n$ lies outside the box neighborhood $\prod_i(-\frac1{i^2},\frac1{i^2})$ for every $n\ge2$, since $\frac1n\ge\frac1{n^2}$.
:::

:::

::: {.pf-step #part-c}
On $H$, $\mathcal T_{\mathrm{prod}}=\mathcal T_{\bar\rho}=\mathcal T_d\subsetneq\mathcal T_{\mathrm{box}}$.

::: pf-proof
Let $\mathbf x\in H$ and $\varepsilon>0$.
Choose $N$ with $\sum_{i>N}1/i^2<\varepsilon^2/2$, and let $W$ be the set of $\mathbf y\in H$ with $\abs{y_i-x_i}<\varepsilon/\sqrt{2N}$ for $i\le N$, a basic product neighborhood of $\mathbf x$ in $H$.
For $\mathbf y\in W$, $\abs{x_i-y_i}\le1/i$ for all $i$ because $x_i,y_i\in[0,1/i]$, so
$$
d(\mathbf x,\mathbf y)^2<N\cdot\frac{\varepsilon^2}{2N}+\sum_{i>N}\frac1{i^2}<\varepsilon^2.
$$
Hence $\mathcal T_d\subseteq\mathcal T_{\mathrm{prod}}$ on $H$, and with step [](#uniform-subset-l2){.pf-ref} the first three topologies agree.
The set $H\cap\prod_n[0,\frac1{n^2})$ is box-open in $H$ and contains $\mathbf 0$, but every basic product neighborhood of $\mathbf 0$ in $H$ leaves some coordinate $n\ge2$ unrestricted and so contains the point $\frac1n\mathbf e_n\notin\prod_n[0,\frac1{n^2})$.
:::

:::

::: pf-qed
Steps [](#uniform-subset-l2){.pf-ref} and [](#l2-subset-box){.pf-ref} prove (a), step [](#part-b){.pf-ref} proves (b), and step [](#part-c){.pf-ref} answers (c).
:::

:::

:::
