---
schema: qual/card@1
id: E-9IGGV
kind: exercise
title: Closures of a non-locally-finite collection may be locally finite
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Give an example of a collection of sets $\mathcal{A}$ that is not locally finite, such that the collection $\mathcal{B} = \ts{\overline{A} \mid A \in \mathcal{A}}$ is locally finite.
:::

::: solution
**Goal:** Provide an explicit example of a collection of subsets $\mathcal{A}$ of a topological space $X$ that is not locally finite, but whose collection of closures $\mathcal{B} = \{\overline{A} \mid A \in \mathcal{A}\}$ is locally finite.

<1>1. Definition of local finiteness:
    A collection $\mathcal{F}$ of subsets of $X$ is locally finite if every point $x \in X$ has an open neighborhood that intersects only finitely many members of $\mathcal{F}$.

<1>2. Construction of the example:
    *Proof:*
    <2>1. Let $X = \mathbb{R}$ equipped with the standard Euclidean topology.
    <2>2. For each integer $n \ge 2$, define the subset:
        $$A_n = (0, 1) \setminus \left\{\frac{1}{n}\right\}.$$
    <2>3. Define the collection $\mathcal{A} = \{A_n \mid n \ge 2\}$.
    <2>4. The sets $\{A_n\}_{n=2}^\infty$ are pairwise distinct because $\frac{1}{m} \in A_n$ for all $m \neq n$, while $\frac{1}{n} \notin A_n$.

<1>3. $\mathcal{A}$ is not locally finite:
    *Proof:*
    <2>1. Consider the point $x = \frac{1}{2} \in \mathbb{R}$.
    <2>2. Let $U$ be an arbitrary open neighborhood of $x = \frac{1}{2}$ in $\mathbb{R}$.
    <2>3. There exists $\varepsilon > 0$ such that $(\frac{1}{2} - \varepsilon, \frac{1}{2} + \varepsilon) \subseteq U \cap (0, 1)$.
    <2>4. For every $n \ge 3$, the interval $(\frac{1}{2} - \varepsilon, \frac{1}{2} + \varepsilon)$ contains points other than $\frac{1}{n}$, so $U \cap A_n \neq \varnothing$.
    <2>5. Thus $U$ intersects infinitely many distinct elements $A_n \in \mathcal{A}$.
    <2>6. Hence $\mathcal{A}$ is not locally finite at $\frac{1}{2}$.

<1>4. $\mathcal{B} = \{\overline{A} \mid A \in \mathcal{A}\}$ is locally finite:
    *Proof:*
    <2>1. For every $n \ge 2$, the topological closure of $A_n = (0, 1) \setminus \{1/n\}$ in the Euclidean metric is:
        $$\overline{A}_n = [0, 1].$$
    <2>2. As a set of subsets of $\mathbb{R}$, the collection of closures collapses to a single set:
        $$\mathcal{B} = \{ \overline{A}_n \mid n \ge 2 \} = \{ [0, 1] \}.$$
    <2>3. Since $\mathcal{B}$ is a finite collection (consisting of exactly $1$ set), every open neighborhood of any point $x \in \mathbb{R}$ intersects at most $1$ member of $\mathcal{B}$.
    <2>4. Therefore $\mathcal{B}$ is locally finite.

<1>5. Conclusion:
    $\mathcal{A} = \{(0, 1) \setminus \{1/n\} \mid n \ge 2\}$ is an infinite collection of sets that is not locally finite, but whose collection of closures $\mathcal{B} = \{[0, 1]\}$ is locally finite. Q.E.D.
:::
