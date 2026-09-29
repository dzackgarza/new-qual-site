---
schema: qual/card@1
id: E-9O8YW
kind: problem
title: $X$ is connected if and only if $\beta(X)$ is connected
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be completely regular.
Show that $X$ is connected if and only if $\beta(X)$ is connected.
[Hint: If $X = A \cup B$ is a separation of $X$, let $f(x) = 0$ for $x \in A$ and $f(x) = 1$ for $x \in B$.]
:::

::: {.solution}

::: pf

::: {.pf-step #forward-direction}
Forward direction ($\implies$): If $X$ is connected, then $\beta(X)$ is connected.

::: pf-proof

::: pf-step
$X$ is embedded as a dense subspace in its Stone-Čech compactification $\beta(X)$, meaning $\overline{X} = \beta(X)$.
:::

::: pf-step
If a subspace $X$ is connected, then its topological closure $\overline{X}$ in any ambient space is connected.
:::

::: pf-step
Since $X$ is connected, $\beta(X) = \overline{X}$ is connected.
:::

:::

:::

::: {.pf-step #reverse-direction}
Reverse direction ($\impliedby$): If $\beta(X)$ is connected, then $X$ is connected.

::: pf-proof

::: pf-step
Suppose for contradiction that $X$ is disconnected, so there exists a separation $X = A \cup B$, where $A$ and $B$ are non-empty, disjoint open (and closed) subsets of $X$.
:::

::: pf-step
Define $f: X \to \{0, 1\} \subset [0, 1]$ by:
$$f(x) = \begin{cases} 0 & \text{if } x \in A, \\ 1 & \text{if } x \in B. \end{cases}$$
:::

::: pf-step
Since $A$ and $B$ are clopen in $X$, $f$ is continuous.
:::

::: pf-step
Because $[0, 1]$ is compact Hausdorff, the universal mapping property of the Stone-Čech compactification gives a unique continuous extension:
$$\tilde{f}: \beta(X) \to [0, 1] \quad \text{such that } \tilde{f}|_X = f.$$
:::

::: pf-step
The set $\{0, 1\}$ is closed in $[0, 1]$, so the preimage $\tilde{f}^{-1}(\{0, 1\})$ is a closed subset of $\beta(X)$.
:::

::: pf-step
Since $X \subseteq \tilde{f}^{-1}(\{0, 1\})$ and $X$ is dense in $\beta(X)$, we have:
$$\beta(X) = \overline{X} \subseteq \tilde{f}^{-1}(\{0, 1\}).$$
:::

::: pf-step
Thus the continuous image $\tilde{f}(\beta(X))$ is contained in the discrete two-point space $\{0, 1\}$.
:::

::: pf-step
Because $\beta(X)$ is connected and $\tilde{f}$ is continuous, the image $\tilde{f}(\beta(X))$ must be a connected subset of $\{0, 1\}$, hence a single point.
:::

::: pf-step
However, $A \neq \varnothing \implies 0 \in \tilde{f}(\beta(X))$ and $B \neq \varnothing \implies 1 \in \tilde{f}(\beta(X))$, so $\tilde{f}(\beta(X)) = \{0, 1\}$, which is disconnected.
:::

::: pf-step
This contradiction shows that $X$ must be connected.
:::

:::

:::

::: pf-qed
Steps [](#forward-direction){.pf-ref} and [](#reverse-direction){.pf-ref} give the two implications.
:::

:::

:::
