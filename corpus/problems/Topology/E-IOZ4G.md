---
schema: qual/card@1
id: E-IOZ4G
kind: exercise
title: Every indiscrete space is separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Show that any topological space $X$ equipped with the indiscrete (trivial) topology is separable.
:::

::: solution
**Goal:** Prove that an indiscrete topological space $X$ is separable by exhibiting a countable dense subset.

<1>1. Definition of the Indiscrete Topology:
    *Proof:*
    <2>1. Let $X$ be any non-empty set equipped with the indiscrete (trivial) topology:
        $$\mathcal{T}_{\text{indiscrete}} = \{\varnothing, X\}.$$
    <2>2. The only non-empty open subset in this topology is the entire space $X$ itself.

<1>2. Dense Subsets in the Indiscrete Topology:
    *Proof:*
    <2>1. A subset $D \subseteq X$ is **dense** in $X$ if the closure of $D$ is the whole space: $\overline{D} = X$.
    <2>2. Equivalently, $D$ is dense if and only if $D$ intersects every non-empty open set $U \in \mathcal{T}_{\text{indiscrete}}$.
    <2>3. Since the only non-empty open set is $X$, any non-empty subset $D \subseteq X$ satisfies $D \cap X = D \ne \varnothing$.
    <2>4. Therefore, **every non-empty subset $D \subseteq X$ is dense in $X$**.

<1>3. Existence of a Countable Dense Subset:
    *Proof:*
    <2>1. If $X = \varnothing$, $X$ is vacuously separable (empty set is finite).
    <2>2. If $X \ne \varnothing$, choose any single point $x_0 \in X$.
    <2>3. The singleton subset $D = \{x_0\}$ is finite (hence at most countable).
    <2>4. By Step <1>2, $\{x_0\}$ intersects the only non-empty open set $X$, so:
        $$\overline{\{x_0\}} = X.$$
    <2>5. Thus $D = \{x_0\}$ is a countable dense subset of $X$.

<1>4. Conclusion:
    Any space with the indiscrete topology contains a singleton dense subset $\{x_0\}$, and is therefore separable. Q.E.D.
:::
