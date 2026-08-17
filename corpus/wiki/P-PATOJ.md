---
schema: qual/card@1
id: P-PATOJ
kind: problem
title: "Let $X$ be Hausdorff, and recall that the one-point\u2026"
classification:
  areas:
  - topology
  topics:
  - compactness
  - hausdorff-spaces
  - point-set
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Let $X$ be Hausdorff, and recall that the *one-point compactification* $\tilde X$ is given by the following:

- As a set, $\tilde X \definedas X\disjoint \theset{\infty}$.

- A subset $U\subseteq \tilde X$ is open iff either $U$ is open in $X$ or is of the form $U = V\disjoint \theset{\infty}$ where $V\subset X$ is arbitrary and $X\setminus V$ is compact.

Prove that this description defines a topology on $\tilde X$ making $\tilde X$ compact.

:::

:::{.concept}
\envlist
Definition: $(X, \tau)$ where $\tau \subseteq \mathcal P(X)$ is a *topological space* iff

- $\emptyset, X \in \tau$
- $\theset{U_i}_{i\in I} \subseteq \tau \implies \union_{i\in I} U_i \in \tau$
- $\theset{U_i}_{i\in \NN} \subseteq \tau \implies \intersect_{i\in \NN} U_i \in \tau$

:::

:::{.solution}
\envlist

We can write $\overline{(X, \tau)} = (X \disjoint \pt , \tau \union \tau')$ where $\tau' = \theset{U\disjoint \pt \suchthat X-U ~\text{is compact}}$. We need to show that $T \definedas \tau \union \tau'$ forms a topology. 

- We have $\emptyset,X \in \tau \implies \emptyset, X \in \tau \union \tau'$.
- We just need to check that $\tau'$ is closed under arbitrary unions. Let $\theset{U_i} \subset \tau'$, so $X-U_i = K_i$ a compact set for each $i$. Then $\union_{i} U_i = \union_i X- (X-U_i)= \union_i X - K_i = X - \union_i K_i$

:::

