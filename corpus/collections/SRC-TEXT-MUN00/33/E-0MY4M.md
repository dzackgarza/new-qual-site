---
schema: qual/card@1
id: E-0MY4M
kind: problem
title: Functions vanishing precisely on a closed G-delta set
classification:
  areas:
  - topology
  topics:
  - Urysohn Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Recall that $A$ is a "$G_\delta$ set" in $X$ if $A$ is the intersection of a countable collection of open sets of $X$.

Theorem.
Let $X$ be normal.
There exists a continuous function $f: X \to [0, 1]$ such that $f(x) = 0$ for $x \in A$, and $f(x) > 0$ for $x \notin A$, if and only if $A$ is a closed $G_\delta$ set in $X$.

A function satisfying the requirements of this theorem is said to vanish precisely on $A$.
:::

::: solution
**Goal:** Prove that in a normal space $X$, a subset $A \subseteq X$ is the zero set of a continuous function $f: X \to [0, 1]$ if and only if $A$ is a closed $G_\delta$ set.

<1>1. Direct implication ($\implies$): Zero sets of continuous functions are closed $G_\delta$ sets.
    *Proof:*
    <2>1. Suppose $f: X \to [0, 1]$ is continuous and $A = \{x \in X : f(x) = 0\} = f^{-1}(\{0\})$.
    <2>2. Since $\{0\}$ is closed in $[0, 1]$ and $f$ is continuous, $A$ is closed in $X$.
    <2>3. For each $n \in \mathbb{Z}_+$, let $U_n = f^{-1}([0, \frac{1}{n})) = \{x \in X : f(x) < \frac{1}{n}\}$.
    <2>4. Since $[0, \frac{1}{n})$ is open in the subspace topology of $[0, 1]$, each $U_n$ is open in $X$.
    <2>5. $x \in \bigcap_{n=1}^\infty U_n \iff \forall n \ge 1, 0 \le f(x) < \frac{1}{n} \iff f(x) = 0 \iff x \in A$.
    <2>6. Thus $A = \bigcap_{n=1}^\infty U_n$ is a countable intersection of open sets, so $A$ is a $G_\delta$ set in $X$.

<1>2. Reverse implication ($\impliedby$): Constructing a continuous function vanishing on a closed $G_\delta$ set.
    *Proof:*
    <2>1. Suppose $A \subseteq X$ is closed and $A = \bigcap_{n=1}^\infty U_n$, where each $U_n$ is open in $X$.
    <2>2. For each $n \ge 1$, the complement $X \setminus U_n$ is closed in $X$ and disjoint from $A$ (since $A \subseteq U_n$).
    <2>3. Since $X$ is normal and $A, X \setminus U_n$ are disjoint closed sets, Urysohn's Lemma provides a continuous function $f_n: X \to [0, 1]$ such that:
        $$f_n(x) = 0 \text{ for } x \in A, \qquad f_n(x) = 1 \text{ for } x \in X \setminus U_n.$$
    <2>4. Define $f: X \to [0, 1]$ by the infinite series:
        $$f(x) = \sum_{n=1}^\infty \frac{1}{2^n} f_n(x).$$
    <2>5. Uniform convergence and continuity: For all $x \in X$, $|\frac{1}{2^n} f_n(x)| \le \frac{1}{2^n}$. Since $\sum_{n=1}^\infty \frac{1}{2^n} = 1 < \infty$, the Weierstrass $M$-test proves that the series converges uniformly on $X$. Because each partial sum is continuous, the limit function $f$ is continuous.
    <2>6. Vanishing on $A$: If $x \in A$, then $f_n(x) = 0$ for all $n \ge 1$, so $f(x) = \sum_{n=1}^\infty 0 = 0$.
    <2>7. Positivity outside $A$: If $x \notin A$, then $x \notin \bigcap_{n=1}^\infty U_n$, so there exists some $k \ge 1$ such that $x \notin U_k$, meaning $x \in X \setminus U_k$.
    <2>8. Then $f_k(x) = 1$, and since $f_n(x) \ge 0$ for all $n$:
        $$f(x) \ge \frac{1}{2^k} f_k(x) = \frac{1}{2^k} > 0.$$
    <2>9. Thus $f(x) = 0 \iff x \in A$, so $f$ vanishes precisely on $A$. Q.E.D.
:::
