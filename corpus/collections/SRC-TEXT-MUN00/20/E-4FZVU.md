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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.4, PDF pp. 18--19** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts and all four sequences are theirs, and the box and uniform criteria used in (b) are made explicit in steps [](#hier){.pf-ref} and [](#b-box){.pf-ref}.

Write $\mathbf{0}=(0,0,\ldots)$, and $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{i}\min\theset{\abs{x_{i}-y_{i}},1}$ for the uniform metric.

::: pf

::: {.pf-step #hier}
The product topology is contained in the uniform topology, which is contained in the box topology; all three are Hausdorff; and if a sequence converges in one of them then it converges to the same point in each coarser one.

::: pf-proof
The inclusions are Theorem 20.4 (printed p. 124). The product of Hausdorff spaces is Hausdorff, and adding open sets preserves the Hausdorff property, so all three are Hausdorff. If $\mathbf{x}_{n}\to\mathbf{x}$ in a topology and every open set of a coarser topology is open in it, then every neighbourhood of $\mathbf{x}$ in the coarser topology is one in the finer, so $\mathbf{x}_{n}\to\mathbf{x}$ there too; and limits in a Hausdorff space are unique, since two distinct limits would have disjoint neighbourhoods that the sequence would eventually have to lie in at once.
:::

:::

::: {.pf-step #a-product}
(a) In the product topology $f$, $g$ and $h$ are continuous.

::: pf-proof
For each $i$ the $i$-th coordinate function of $f$ is $t\mapsto i\,t$, of $g$ is $t\mapsto t$, and of $h$ is $t\mapsto t/i$; each is continuous, since $\abs{ct-cs}=\abs{c}\abs{t-s}$. A map into a product is continuous exactly when all its coordinate functions are (Theorem 19.6, printed p. 117).
:::

:::

::: {.pf-step #a-box}
(a) In the box topology none of $f$, $g$, $h$ is continuous.

::: pf-proof
The set $B=\prod_{i\ge1}\big(-1/i^{2},\,1/i^{2}\big)$ is open in the box topology and contains $\mathbf{0}$. Now $f(t)\in B$ means $\abs{i\,t}<1/i^{2}$ for all $i$, that is $\abs{t}<1/i^{3}$ for all $i$; $g(t)\in B$ means $\abs{t}<1/i^{2}$ for all $i$; $h(t)\in B$ means $\abs{t/i}<1/i^{2}$, that is $\abs{t}<1/i$, for all $i$. Each of these conditions holds exactly for $t=0$, since $1/i^{3},1/i^{2},1/i\to0$. So each of the three preimages of $B$ is $\{0\}$, which is not open in $\RR$; each map is discontinuous.
:::

:::

::: {.pf-step #a-uniform-f}
(a) In the uniform topology $f$ is not continuous.

::: pf-proof
Let $B_{\bar\rho}(\mathbf{0},1)=\theset{\mathbf{x}\mid\bar\rho(\mathbf{x},\mathbf{0})<1}$. For $t\ne0$ choose $i$ with $i\abs{t}\ge1$; then $\min\theset{\abs{i\,t},1}=1$, so $\bar\rho(f(t),\mathbf{0})=1$ and $f(t)\notin B_{\bar\rho}(\mathbf{0},1)$. For $t=0$ one has $f(0)=\mathbf{0}\in B_{\bar\rho}(\mathbf{0},1)$. So $f^{-1}\big(B_{\bar\rho}(\mathbf{0},1)\big)=\{0\}$ is not open, and $f$ is discontinuous — hence also discontinuous in the finer box topology, by step [](#hier){.pf-ref}.
:::

:::

::: {.pf-step #a-uniform-gh}
(a) In the uniform topology $g$ and $h$ are continuous.

::: pf-proof
For $s,t\in\RR$ the $i$-th coordinate difference of $g(s),g(t)$ is $\abs{s-t}$, so $\bar\rho(g(s),g(t))=\min\theset{\abs{s-t},1}$; for $h$ it is $\abs{s-t}/i\le\abs{s-t}$, and it equals $\abs{s-t}$ at $i=1$, so again $\bar\rho(h(s),h(t))=\min\theset{\abs{s-t},1}$. Given $\varepsilon>0$ take $\delta=\min\theset{\varepsilon,1}$: then $\abs{s-t}<\delta$ gives $\bar\rho(g(s),g(t))<\varepsilon$ and the same for $h$, so both are continuous at every $t$. Being continuous in the uniform topology, they are continuous in the coarser product topology (step [](#hier){.pf-ref}), agreeing with step [](#a-product){.pf-ref}.
:::

:::

::: {.pf-step #b-product}
(b) All four sequences converge to $\mathbf{0}$ in the product topology.

::: pf-proof
Fix a coordinate $j$. In the four sequences the $j$-th coordinate is: for $\mathbf{w}$, $j$ for $n\le j$ and $0$ for $n>j$; for $\mathbf{x}$ and $\mathbf{y}$, $1/n$ for $n\le j$ and $0$ for $n>j$; for $\mathbf{z}$, $1/n$ for $n\le2$ and $0$ for $n>2$. In every case the $j$-th coordinates tend to $0$. A sequence in a product space converges to $\mathbf{x}$ exactly when each of its coordinate sequences converges to $x_{j}$ (Exercise 19.6, printed p. 118).
:::

:::

::: {.pf-step #b-uniform}
(b) In the uniform topology $\mathbf{x}$, $\mathbf{y}$, $\mathbf{z}$ converge to $\mathbf{0}$ and $\mathbf{w}$ does not converge.

::: pf-proof
$\mathbf{x}_{n}$ and $\mathbf{y}_{n}$ have all coordinates equal to $1/n$ in $n$ places and $0$ elsewhere, and $\mathbf{z}_{n}=(1/n,1/n,0,0,\ldots)$, so $\bar\rho(\mathbf{x}_{n},\mathbf{0})=\bar\rho(\mathbf{y}_{n},\mathbf{0})=\bar\rho(\mathbf{z}_{n},\mathbf{0})=\min\theset{1/n,1}=1/n\to0$, and the three converge to $\mathbf{0}$. But $\mathbf{w}_{n}$ has $n$-th coordinate $n$, so $\bar\rho(\mathbf{w}_{n},\mathbf{0})\ge\min\theset{n,1}=1$ for every $n$, and $\mathbf{w}_{n}$ stays outside the neighbourhood $B_{\bar\rho}(\mathbf{0},1)$ of the only possible limit $\mathbf{0}$ of step [](#b-product){.pf-ref} and step [](#hier){.pf-ref}.
:::

:::

::: {.pf-step #b-box}
(b) In the box topology $\mathbf{z}$ converges to $\mathbf{0}$, and $\mathbf{w}$, $\mathbf{x}$, $\mathbf{y}$ do not converge.

:::: {.pf-proof}

::: {.pf-step #b-box-z}
Every box neighbourhood of $\mathbf{0}$ contains $\mathbf{z}_{n}$ for all large $n$.

::: pf-proof
A box neighbourhood of $\mathbf{0}$ contains a box $\prod_{i}(-\varepsilon_{i},\varepsilon_{i})$ with all $\varepsilon_{i}>0$. For $n\ge2$, $\mathbf{z}_{n}$ has positive entries $1/n$ only in coordinates $1$ and $2$, so $\mathbf{z}_{n}$ lies in that box as soon as $1/n<\min\theset{\varepsilon_{1},\varepsilon_{2}}$, which holds for all large $n$.
:::

:::

::: {.pf-step #b-box-not}
Each of $\mathbf{w}_{n}$, $\mathbf{x}_{n}$, $\mathbf{y}_{n}$ avoids a fixed box neighbourhood of $\mathbf{0}$ for every $n$, so none converges.

::: pf-proof
Any limit in the box topology is a limit in the product topology, hence $\mathbf{0}$ by step [](#b-product){.pf-ref} and step [](#hier){.pf-ref}; so it suffices to exhibit a box neighbourhood of $\mathbf{0}$ that the sequence never enters. For $\mathbf{w}_{n}$ take $\prod_{i}(-1,1)$: the $n$-th coordinate of $\mathbf{w}_{n}$ is $n\ge1$. For $\mathbf{x}_{n}$ and $\mathbf{y}_{n}$ take $\prod_{i}(-1/i^{2},\,1/i^{2})$: the $n$-th coordinate of $\mathbf{x}_{n}$ is $1/n$, and the $n$-th coordinate of $\mathbf{y}_{n}$ is $1/n$ as well, and $1/n\ge1/n^{2}$, so neither lies in that box, for any $n$.
:::

:::

::::

:::

::: {.pf-qed}
In (a) the product topology has all three maps continuous and the box topology none, while in the uniform topology $g$ and $h$ are continuous and $f$ is not; in (b) $\mathbf{w}$ converges in the product topology only, $\mathbf{x}$ and $\mathbf{y}$ in the product and uniform topologies but not the box topology, and $\mathbf{z}$ in all three.
:::

:::

:::
