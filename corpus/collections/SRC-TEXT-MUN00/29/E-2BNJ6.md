---
schema: qual/card@1
id: E-2BNJ6
kind: problem
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

::: {.solution}
**Goal:** Prove that every subnet $(y_k)_{k \in K} = (x_{g(k)})_{k \in K}$ of a convergent net $(x_\alpha)_{\alpha \in J} \to x$ in a topological space $X$ also converges to $x$.

::: pf

::: pf-step
Target neighborhood:
Let $U$ be an arbitrary open neighborhood of $x$ in $X$.
:::

::: {.pf-step #parent-net-convergence}
Convergence of the parent net $(x_\alpha)$:
There exists an index $\alpha_0 \in J$ such that for all $\alpha \in J$:
$$\alpha_0 \preceq \alpha \implies x_\alpha \in U.$$

::: pf-proof
Follows directly from the definition of net convergence $(x_\alpha) \to x$.
:::

:::

::: pf-step
Cofinality of the subnet indexing map $g$:
There exists an element $k_0 \in K$ such that $\alpha_0 \preceq g(k_0)$.

::: pf-proof
By condition (ii), $g(K)$ is cofinal in $J$. Applying cofinality to the element $\alpha_0 \in J$ provides such a $k_0 \in K$.
:::

:::

::: pf-step
Monotonicity and convergence verification on $K$:
For every $k \in K$ with $k_0 \preceq k$, $y_k = x_{g(k)} \in U$.

::: pf-proof

::: pf-step
Let $k \in K$ satisfy $k_0 \preceq k$.
:::

::: pf-step
By condition (i), the map $g: K \to J$ is order-preserving, so $g(k_0) \preceq g(k)$.
:::

::: pf-step
By transitivity of the preorder $\preceq$ on $J$, $\alpha_0 \preceq g(k_0)$ and $g(k_0) \preceq g(k)$ imply:
$$\alpha_0 \preceq g(k).$$
:::

::: pf-step
By step [](#parent-net-convergence){.pf-ref}, since $\alpha_0 \preceq g(k)$, the net value satisfies $x_{g(k)} \in U$.
:::

::: pf-step
Therefore $y_k = (f \circ g)(k) = x_{g(k)} \in U$.
:::

:::

:::

::: pf-step
Conclusion:
For every open neighborhood $U$ of $x$, there exists $k_0 \in K$ such that $k_0 \preceq k \implies y_k \in U$. Hence the subnet $(y_k)_{k \in K}$ converges to $x$. Q.E.D.
:::

:::

:::
