---
schema: qual/card@1
id: E-H6CCW
kind: exercise
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
<1>1. Definition and properties of a directed set:
<2>1. A set $(J, \preceq)$ is a **directed set** if:
(i) $\preceq$ is a preorder on $J$ (reflexive: $\alpha \preceq \alpha$, and transitive: $\alpha \preceq \beta \land \beta \preceq \gamma \implies \alpha \preceq \gamma$), and
(ii) for every pair $\alpha_1, \alpha_2 \in J$, there exists an upper bound $\gamma \in J$ such that $\alpha_1 \preceq \gamma$ and $\alpha_2 \preceq \gamma$.
Proof: definition of a directed set.
<2>2. The subset $K \subseteq J$ inherits the relation $\preceq$.
Since reflexivity and transitivity hold on all elements of $J$, they hold on all elements of $K$.
Proof: restriction of a preorder to a subset.

<1>2. Existence of common upper bounds in $K$:
<2>1. Let $k_1, k_2 \in K$ be arbitrary elements.
Since $K \subseteq J$, $k_1, k_2 \in J$.
Proof: subset containment.
<2>2. Since $J$ is directed, there exists an element $\alpha \in J$ such that:
\[
k_1 \preceq \alpha \quad \text{and} \quad k_2 \preceq \alpha.
\]
Proof: directedness of $J$.
<2>3. Since $K$ is cofinal in $J$, there exists an element $\beta \in K$ such that:
\[
\alpha \preceq \beta.
\]
Proof: definition of cofinality of $K$ in $J$.
<2>4. By transitivity of $\preceq$:
\[
k_1 \preceq \alpha \text{ and } \alpha \preceq \beta \implies k_1 \preceq \beta,
\]
\[
k_2 \preceq \alpha \text{ and } \alpha \preceq \beta \implies k_2 \preceq \beta.
\]
Proof: transitivity of preorder $\preceq$.
<2>5. Thus $\beta \in K$ is a common upper bound for $k_1$ and $k_2$ in $K$.
Proof: <2>3 and <2>4.

<1>3. Conclusion:
$K$ with the inherited relation is a directed set. Q.E.D.
Proof: <1>1 and <1>2.
:::
