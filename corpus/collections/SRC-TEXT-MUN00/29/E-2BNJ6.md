---
schema: qual/card@1
id: E-2BNJ6
kind: exercise
title: Subnets of convergent nets converge
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $f: J \to X$ be a net in $X$; let $f(\alpha) = x_\alpha$.
If $K$ is a directed set and $g: K \to J$ is a function such that

(i) $i \preceq j \implies g(i) \preceq g(j)$,

(ii) $g(K)$ is cofinal in $J$,

then the composite function $f \circ g: K \to X$ is called a subnet of $(x_\alpha)$.
Show that if the net $(x_\alpha)$ converges to $x$, so does any subnet.
:::

::: solution
**Goal:** Prove that every subnet $(y_k)_{k \in K} = (x_{g(k)})_{k \in K}$ of a convergent net $(x_\alpha)_{\alpha \in J} \to x$ in a topological space $X$ also converges to $x$.

<1>1. Target neighborhood:
    Let $U$ be an arbitrary open neighborhood of $x$ in $X$.

<1>2. Convergence of the parent net $(x_\alpha)$:
    There exists an index $\alpha_0 \in J$ such that for all $\alpha \in J$:
    $$\alpha_0 \preceq \alpha \implies x_\alpha \in U.$$
    *Proof:* Follows directly from the definition of net convergence $(x_\alpha) \to x$.

<1>3. Cofinality of the subnet indexing map $g$:
    There exists an element $k_0 \in K$ such that $\alpha_0 \preceq g(k_0)$.
    *Proof:* By condition (ii), $g(K)$ is cofinal in $J$. Applying cofinality to the element $\alpha_0 \in J$ provides such a $k_0 \in K$.

<1>4. Monotonicity and convergence verification on $K$:
    For every $k \in K$ with $k_0 \preceq k$, $y_k = x_{g(k)} \in U$.
    *Proof:*
    <2>1. Let $k \in K$ satisfy $k_0 \preceq k$.
    <2>2. By condition (i), the map $g: K \to J$ is order-preserving, so $g(k_0) \preceq g(k)$.
    <2>3. By transitivity of the preorder $\preceq$ on $J$, $\alpha_0 \preceq g(k_0)$ and $g(k_0) \preceq g(k)$ imply:
        $$\alpha_0 \preceq g(k).$$
    <2>4. By <1>2, since $\alpha_0 \preceq g(k)$, the net value satisfies $x_{g(k)} \in U$.
    <2>5. Therefore $y_k = (f \circ g)(k) = x_{g(k)} \in U$.

<1>5. Conclusion:
    For every open neighborhood $U$ of $x$, there exists $k_0 \in K$ such that $k_0 \preceq k \implies y_k \in U$. Hence the subnet $(y_k)_{k \in K}$ converges to $x$. Q.E.D.
:::
