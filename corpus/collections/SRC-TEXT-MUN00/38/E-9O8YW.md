---
schema: qual/card@1
id: E-9O8YW
kind: problem
title: Connectedness of X and of its Stone-Cech compactification
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

::: solution
**Goal:** Prove that a completely regular space $X$ is connected if and only if its Stone-Čech compactification $\beta(X)$ is connected.

<1>1. Forward direction ($\implies$): If $X$ is connected, then $\beta(X)$ is connected.
    *Proof:*
    <2>1. $X$ is embedded as a dense subspace in its Stone-Čech compactification $\beta(X)$, meaning $\overline{X} = \beta(X)$.
    <2>2. If a subspace $X$ is connected, then its topological closure $\overline{X}$ in any ambient space is connected (Theorem 23.4).
    <2>3. Since $X$ is connected, $\beta(X) = \overline{X}$ is connected.

<1>2. Reverse direction ($\impliedby$): If $\beta(X)$ is connected, then $X$ is connected.
    *Proof:*
    <2>1. Suppose for contradiction that $X$ is disconnected, so there exists a separation $X = A \cup B$, where $A$ and $B$ are non-empty, disjoint open (and closed) subsets of $X$.
    <2>2. Define $f: X \to \{0, 1\} \subset [0, 1]$ by:
        $$f(x) = \begin{cases} 0 & \text{if } x \in A, \\ 1 & \text{if } x \in B. \end{cases}$$
    <2>3. Since $A$ and $B$ are clopen in $X$, $f$ is continuous.
    <2>4. Because $[0, 1]$ is compact Hausdorff, the universal mapping property of the Stone-Čech compactification gives a unique continuous extension:
        $$\tilde{f}: \beta(X) \to [0, 1] \quad \text{such that } \tilde{f}|_X = f.$$
    <2>5. The set $\{0, 1\}$ is closed in $[0, 1]$, so the preimage $\tilde{f}^{-1}(\{0, 1\})$ is a closed subset of $\beta(X)$.
    <2>6. Since $X \subseteq \tilde{f}^{-1}(\{0, 1\})$ and $X$ is dense in $\beta(X)$, we have:
        $$\beta(X) = \overline{X} \subseteq \tilde{f}^{-1}(\{0, 1\}).$$
    <2>7. Thus the continuous image $\tilde{f}(\beta(X))$ is contained in the discrete two-point space $\{0, 1\}$.
    <2>8. Because $\beta(X)$ is connected and $\tilde{f}$ is continuous, the image $\tilde{f}(\beta(X))$ must be a connected subset of $\{0, 1\}$, hence a single point.
    <2>9. However, $A \neq \varnothing \implies 0 \in \tilde{f}(\beta(X))$ and $B \neq \varnothing \implies 1 \in \tilde{f}(\beta(X))$, so $\tilde{f}(\beta(X)) = \{0, 1\}$, which is disconnected.
    <2>10. This contradiction shows that $X$ must be connected.

<1>3. Conclusion:
    $X$ is connected if and only if $\beta(X)$ is connected. Q.E.D.
:::
