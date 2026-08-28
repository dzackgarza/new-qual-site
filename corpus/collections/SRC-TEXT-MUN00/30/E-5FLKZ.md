---
schema: qual/card@1
id: E-5FLKZ
kind: exercise
title: Second countable spaces are first countable
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that every second countable space is first countable.
:::

::: {.remark}
The original exercise asked for the converse, which is false: an uncountable discrete space is first countable but not second countable.
:::

::: solution
**Goal:** Prove that every second-countable space $X$ is first-countable.

<1>1. Setting and hypothesis:
    Let $X$ be a second-countable topological space.
    By definition, $X$ possesses a countable basis $\mathcal{B} = \{B_n\}_{n=1}^\infty$ for its topology.

<1>2. Construction of a countable local basis at an arbitrary point:
    *Proof:*
    <2>1. Let $x \in X$ be an arbitrary point.
    <2>2. Define the subcollection of basic open sets containing $x$:
        $$\mathcal{B}_x = \{B \in \mathcal{B} \mid x \in B\}.$$
    <2>3. Because $\mathcal{B}_x \subseteq \mathcal{B}$ and $\mathcal{B}$ is countable, $\mathcal{B}_x$ is a countable collection of open neighborhoods containing $x$.

<1>3. Verification of the local basis property:
    *Proof:*
    <2>1. Let $U \subseteq X$ be an arbitrary open neighborhood of $x$.
    <2>2. Since $\mathcal{B}$ is a topological basis for $X$, there exists a basic open set $B \in \mathcal{B}$ such that $x \in B \subseteq U$.
    <2>3. Because $x \in B$, $B$ belongs to the subcollection $\mathcal{B}_x$ by construction.
    <2>4. Thus, every open neighborhood $U$ of $x$ contains an element of $\mathcal{B}_x$.

<1>4. Conclusion:
    $\mathcal{B}_x$ is a countable local basis at $x$. Since $x \in X$ was arbitrary, $X$ is first-countable. Q.E.D.
:::
