---
schema: qual/card@1
id: E-H6CCW
kind: problem
title: Cofinal subsets of directed sets
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

A subset $K$ of $J$ is said to be cofinal in $J$ if for each $\alpha \in J$, there exists $\beta \in K$ such that $\alpha \preceq \beta$.
Show that if $J$ is a directed set and $K$ is cofinal in $J$, then $K$ is a directed set.
:::

::: {.solution}

::: pf

::: {.pf-step #directed-set-definition}
Definition and properties of a directed set:

::: pf-proof

::: pf-step
A set $(J, \preceq)$ is a **directed set** if:
(i) $\preceq$ is a preorder on $J$ (reflexive: $\alpha \preceq \alpha$, and transitive: $\alpha \preceq \beta \land \beta \preceq \gamma \implies \alpha \preceq \gamma$), and
(ii) for every pair $\alpha_1, \alpha_2 \in J$, there exists an upper bound $\gamma \in J$ such that $\alpha_1 \preceq \gamma$ and $\alpha_2 \preceq \gamma$.

::: pf-proof
definition of a directed set.
:::

:::

::: pf-step
The subset $K \subseteq J$ inherits the relation $\preceq$.
Since reflexivity and transitivity hold on all elements of $J$, they hold on all elements of $K$.

::: pf-proof
restriction of a preorder to a subset.
:::

:::

:::

:::

::: {.pf-step #common-upper-bounds-in-k}
Existence of common upper bounds in $K$:

::: pf-proof

::: pf-step
Let $k_1, k_2 \in K$ be arbitrary elements.
Since $K \subseteq J$, $k_1, k_2 \in J$.

::: pf-proof
subset containment.
:::

:::

::: pf-step
Since $J$ is directed, there exists an element $\alpha \in J$ such that:
\[
k_1 \preceq \alpha \quad \text{and} \quad k_2 \preceq \alpha.
\]

::: pf-proof
directedness of $J$.
:::

:::

::: {.pf-step #cofinal-upper-bound}
Since $K$ is cofinal in $J$, there exists an element $\beta \in K$ such that:
\[
\alpha \preceq \beta.
\]

::: pf-proof
definition of cofinality of $K$ in $J$.
:::

:::

::: {.pf-step #transitivity-gives-upper-bound}
By transitivity of $\preceq$:
\[
k_1 \preceq \alpha \text{ and } \alpha \preceq \beta \implies k_1 \preceq \beta,
\]
\[
k_2 \preceq \alpha \text{ and } \alpha \preceq \beta \implies k_2 \preceq \beta.
\]

::: pf-proof
transitivity of preorder $\preceq$.
:::

:::

::: pf-step
Thus $\beta \in K$ is a common upper bound for $k_1$ and $k_2$ in $K$.

::: pf-proof
Steps [](#cofinal-upper-bound){.pf-ref} and [](#transitivity-gives-upper-bound){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion:
$K$ with the inherited relation is a directed set. Q.E.D.

::: pf-proof
Steps [](#directed-set-definition){.pf-ref} and [](#common-upper-bounds-in-k){.pf-ref}.
:::

:::

:::

:::
