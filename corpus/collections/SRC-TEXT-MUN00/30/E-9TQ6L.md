---
schema: qual/card@1
id: E-9TQ6L
kind: exercise
title: Uncountably many limit points of an uncountable set in a second-countable space
classification:
  areas:
  - topology
  topics:
  - Countability
  - Limit Points
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ have a countable basis; let $A$ be an uncountable subset of $X$.
Show that uncountably many points of $A$ are limit points of $A$.
:::

::: solution
**Goal:** Prove that if $X$ is a second-countable topological space and $A \subseteq X$ is uncountable, then uncountably many points of $A$ are limit points of $A$ (i.e. $A \cap A'$ is uncountable).

<1>1. Identification of non-limit points (isolated points of $A$):
    *Proof:*
    <2>1. Let $I = A \setminus A'$ denote the set of points in $A$ that are not limit points of $A$.
    <2>2. By definition of limit points, for every $x \in I$, there exists an open neighborhood $U_x$ of $x$ in $X$ such that:
        $$U_x \cap A = \{x\}.$$

<1>2. Proof that $I$ is at most countable:
    *Proof:*
    <2>1. Let $\mathcal{B} = \{B_n\}_{n=1}^\infty$ be a countable basis for the topology of $X$.
    <2>2. For each $x \in I$, choose a basis element $B(x) \in \mathcal{B}$ such that $x \in B(x) \subseteq U_x$.
    <2>3. Since $x \in B(x) \subseteq U_x$, we have $B(x) \cap A \subseteq U_x \cap A = \{x\}$. Because $x \in B(x) \cap A$, it follows that:
        $$B(x) \cap A = \{x\}.$$
    <2>4. The assignment $\phi: I \to \mathcal{B}$ defined by $\phi(x) = B(x)$ is injective: if $\phi(x) = \phi(y)$, then $\{x\} = B(x) \cap A = B(y) \cap A = \{y\}$, forcing $x = y$.
    <2>5. Because $\mathcal{B}$ is countable and $\phi$ is injective, the set $I = A \setminus A'$ is at most countable.

<1>3. Conclusion:
    <2>1. We partition $A$ as:
        $$A = (A \cap A') \cup (A \setminus A') = (A \cap A') \cup I.$$
    <2>2. Since $A$ is uncountable and $I$ is countable, the set $A \cap A'$ of points of $A$ that are limit points of $A$ must be uncountable. Q.E.D.
:::
