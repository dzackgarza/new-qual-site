---
schema: qual/card@1
id: P-RASP24E
kind: problem
title: "Support of a Radon measure on a one-point compactification of a discrete space"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
Let $X$ be a set equipped with the discrete topology, and let $X^* = X \cup \{\infty\}$ be the one-point compactification of $X$.
Let $\mu$ be a Radon measure on $X^*$ and define the support of $\mu$ as
$$
\operatorname{supp}(\mu) = \bigcap \{N : N \subseteq X^* \text{ is closed and } \mu(N^c) = 0\}.
$$
Prove that $\operatorname{supp}(\mu)$ is countable.
:::

::: solution
**Goal:** Prove that $\operatorname{supp}(\mu)$ is at most countable for any Radon measure $\mu$ on the one-point compactification $X^* = X \cup \{\infty\}$ of a discrete space $X$.

<1>1. Finiteness of the Radon measure:
    $X^*$ is compact Hausdorff, so the Radon measure $\mu$ is a finite Borel measure on $X^*$, meaning $\mu(X^*) < \infty$.
    *Proof:* By definition, a Radon measure on a compact Hausdorff space assigns finite measure to every compact set; since $X^*$ is itself compact, $\mu(X^*) < \infty$.

<1>2. Topological structure of singletons in $X$:
    For every $x \in X$, the singleton set $\{x\}$ is open in $X^*$.
    *Proof:* In the one-point compactification topology, open sets are open subsets of $X$ and sets of the form $(X \setminus K) \cup \{\infty\}$ where $K \subseteq X$ is compact. Since $X$ has the discrete topology, every subset of $X$ is open in $X$. In particular, $\{x\}$ is open in $X$ and does not contain $\infty$, so $\{x\}$ is open in $X^*$.

<1>3. Characterization of support points in $X$:
    A point $x \in X$ belongs to $\operatorname{supp}(\mu)$ if and only if $\mu(\{x\}) > 0$.
    *Proof:*
    <2>1. By definition, $\operatorname{supp}(\mu)^c = \bigcup \{U \subseteq X^* : U \text{ is open and } \mu(U) = 0\}$.
    <2>2. Hence $y \in \operatorname{supp}(\mu)$ if and only if every open neighborhood $U$ of $y$ in $X^*$ satisfies $\mu(U) > 0$.
    <2>3. For $x \in X$, $\{x\}$ is an open neighborhood of $x$ by <1>2.
    <2>4. If $\mu(\{x\}) = 0$, then $\{x\}$ is an open set of measure zero, so $\{x\} \subseteq \operatorname{supp}(\mu)^c$, which means $x \notin \operatorname{supp}(\mu)$.
    <2>5. If $\mu(\{x\}) > 0$, then every open neighborhood $U$ of $x$ contains $\{x\}$, so $\mu(U) \ge \mu(\{x\}) > 0$, which means $x \in \operatorname{supp}(\mu)$.
    <2>6. Thus $X \cap \operatorname{supp}(\mu) = \{x \in X : \mu(\{x\}) > 0\}$.

<1>4. Countability of $X \cap \operatorname{supp}(\mu)$:
    The set $S = \{x \in X : \mu(\{x\}) > 0\}$ is at most countable.
    *Proof:*
    <2>1. For each $n \in \mathbb{N}_{\ge 1}$, define $S_n = \{x \in X : \mu(\{x\}) \ge \frac{1}{n}\}$.
    <2>2. Then $S = \bigcup_{n=1}^\infty S_n$.
    <2>3. For any finite subset $\{x_1, \dots, x_k\} \subseteq S_n$, pairwise disjointness of singletons gives:
        $$\mu(X^*) \ge \mu\left(\bigcup_{j=1}^k \{x_j\}\right) = \sum_{j=1}^k \mu(\{x_j\}) \ge \frac{k}{n}.$$
    <2>4. Therefore $k \le n \mu(X^*)$, which proves that each $S_n$ is finite with $|S_n| \le n \mu(X^*) < \infty$.
    <2>5. As a countable union of finite sets, $S$ is at most countable.

<1>5. Conclusion: $\operatorname{supp}(\mu)$ is countable.
    *Proof:* Since $X^* = X \cup \{\infty\}$, we have
    $$\operatorname{supp}(\mu) = (X \cap \operatorname{supp}(\mu)) \cup (\{\infty\} \cap \operatorname{supp}(\mu)) \subseteq S \cup \{\infty\}.$$
    Since $S$ is at most countable by <1>4, $S \cup \{\infty\}$ is at most countable. Therefore, $\operatorname{supp}(\mu)$ is at most countable (countable). Q.E.D.
:::
