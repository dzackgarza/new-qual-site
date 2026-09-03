---
schema: qual/card@1
id: E-1QFIO
kind: problem
title: Intersections and unions of families of topologies
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

(a) If $\ts{\mathcal{T}_\alpha}$ is a family of topologies on $X$, show that $\bigcap \mathcal{T}_\alpha$ is a topology on $X$.
Is $\bigcup \mathcal{T}_\alpha$ a topology on $X$?

(b) Let $\ts{\mathcal{T}_\alpha}$ be a family of topologies on $X$.
Show that there is a unique smallest topology on $X$ containing all the collections $\mathcal{T}_\alpha$, and a unique largest topology contained in all $\mathcal{T}_\alpha$.

(c) If $X = \ts{a, b, c}$, let

$$
\mathcal{T}_1 = \ts{\varnothing, X, \ts{a}, \ts{a, b}} \quad \text{and} \quad \mathcal{T}_2 = \ts{\varnothing, X, \ts{a}, \ts{b, c}}.
$$

Find the smallest topology containing $\mathcal{T}_1$ and $\mathcal{T}_2$, and the largest topology contained in $\mathcal{T}_1$ and $\mathcal{T}_2$.
:::

::: solution
**Goal:** Prove intersection and union properties of families of topologies, establish lattice bounds on topologies, and compute the meet and join of specific topologies on a 3-point set.

<1>1. Part (a): Intersections and unions of topologies.
    *Proof:*
    <2>1. Let $\mathcal{T} = \bigcap_\alpha \mathcal{T}_\alpha$.
        - $\emptyset, X \in \mathcal{T}_\alpha$ for every $\alpha$, so $\emptyset, X \in \mathcal{T}$.
        - Let $\{U_\beta\}_{\beta \in B} \subseteq \mathcal{T}$. For each $\alpha$, $\{U_\beta\}_{\beta \in B} \subseteq \mathcal{T}_\alpha$, so $\bigcup_{\beta \in B} U_\beta \in \mathcal{T}_\alpha$. Thus $\bigcup_{\beta \in B} U_\beta \in \mathcal{T}$.
        - Let $U_1, \dots, U_n \in \mathcal{T}$. For each $\alpha$, $U_1, \dots, U_n \in \mathcal{T}_\alpha$, so $\bigcap_{i=1}^n U_i \in \mathcal{T}_\alpha$. Thus $\bigcap_{i=1}^n U_i \in \mathcal{T}$.
        - Therefore $\bigcap_\alpha \mathcal{T}_\alpha$ is a topology on $X$.
    <2>2. The union $\bigcup_\alpha \mathcal{T}_\alpha$ is not generally a topology.
        - Counterexample: On $X = \{a, b, c\}$, let $\mathcal{T}_A = \{\emptyset, X, \{a\}\}$ and $\mathcal{T}_B = \{\emptyset, X, \{b\}\}$.
        - The union is $\mathcal{T}_A \cup \mathcal{T}_B = \{\emptyset, X, \{a\}, \{b\}\}$.
        - $\{a\} \cup \{b\} = \{a, b\} \notin \mathcal{T}_A \cup \mathcal{T}_B$, so it is not closed under unions.

<1>2. Part (b): Existence and uniqueness of supremum and infimum topologies.
    *Proof:*
    <2>1. Largest topology contained in all $\mathcal{T}_\alpha$:
        - By <1>1, $\mathcal{T}_{\text{inf}} = \bigcap_\alpha \mathcal{T}_\alpha$ is a topology on $X$ and $\mathcal{T}_{\text{inf}} \subseteq \mathcal{T}_\alpha$ for all $\alpha$.
        - If $\mathcal{T}'$ is any topology with $\mathcal{T}' \subseteq \mathcal{T}_\alpha$ for all $\alpha$, then $\mathcal{T}' \subseteq \bigcap_\alpha \mathcal{T}_\alpha = \mathcal{T}_{\text{inf}}$. Thus $\mathcal{T}_{\text{inf}}$ is the unique largest.
    <2>2. Smallest topology containing all $\mathcal{T}_\alpha$:
        - Consider the family $\mathfrak{F} = \{\mathcal{T} : \mathcal{T} \text{ is a topology on } X \text{ and } \bigcup_\alpha \mathcal{T}_\alpha \subseteq \mathcal{T}\}$.
        - $\mathfrak{F}$ is non-empty because the power set $\mathcal{P}(X)$ (discrete topology) belongs to $\mathfrak{F}$.
        - Define $\mathcal{T}_{\text{sup}} = \bigcap_{\mathcal{T} \in \mathfrak{F}} \mathcal{T}$. By <1>1, $\mathcal{T}_{\text{sup}}$ is a topology on $X$.
        - By construction, $\bigcup_\alpha \mathcal{T}_\alpha \subseteq \mathcal{T}_{\text{sup}}$, and every topology containing all $\mathcal{T}_\alpha$ belongs to $\mathfrak{F}$ and hence contains $\mathcal{T}_{\text{sup}}$. Thus $\mathcal{T}_{\text{sup}}$ is the unique smallest.

<1>3. Part (c): Computation on $X = \{a, b, c\}$.
    *Proof:*
    <2>1. Largest topology contained in $\mathcal{T}_1$ and $\mathcal{T}_2$:
        $$\mathcal{T}_1 \cap \mathcal{T}_2 = \{\emptyset, X, \{a\}\}.$$
    <2>2. Smallest topology containing $\mathcal{T}_1$ and $\mathcal{T}_2$:
        - Subbasis: $\mathcal{S} = \{\{a\}, \{a, b\}, \{b, c\}\}$.
        - Finite intersections of subbasis elements yield the basis:
          $$\mathcal{B} = \{\emptyset, X, \{a\}, \{b, c\}, \{a, b\}, \{a, b\} \cap \{b, c\} = \{b\}\}.$$
        - Arbitrary unions of elements in $\mathcal{B}$:
          $$\mathcal{T}_{\text{sup}} = \{\emptyset, X, \{a\}, \{b\}, \{a, b\}, \{b, c\}\}.$$
    Q.E.D.
:::
