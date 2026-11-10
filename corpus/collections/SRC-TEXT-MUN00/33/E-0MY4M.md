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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S33.pdf, Exercise 33.4 (Theorem 2), pages 1-2 of the file
    (tmp/sources/munkres-solutions-poulsen-S33.pdf, Internet Archive snapshot 20200331153844),
    checked against Munkres, Topology (2000), Section 33 Exercise 4, printed p. 213, and Theorem 21.6
    (the uniform limit of continuous functions is continuous). The two implications are the card's:
    a zero set is the intersection of the preimages of [0, 1/n); and for a closed G_delta A = cap U_n
    Urysohn's lemma gives f_n vanishing on A and equal to 1 off U_n, whose weighted sum vanishes
    exactly on A. The card writes the weights 2^{-n} and applies the Weierstrass M-test where Moller
    writes 2^{-i} and cites Theorem 21.6. No correction to the mathematics was needed.
---

::: {.exercise}

Recall that $A$ is a "$G_\delta$ set" in $X$ if $A$ is the intersection of a countable collection of open sets of $X$.

Theorem.
Let $X$ be normal.
There exists a continuous function $f: X \to [0, 1]$ such that $f(x) = 0$ for $x \in A$, and $f(x) > 0$ for $x \notin A$, if and only if $A$ is a closed $G_\delta$ set in $X$.

A function satisfying the requirements of this theorem is said to vanish precisely on $A$.
:::

::: {.solution}

::: pf

::: pf-step
Direct implication ($\implies$): Zero sets of continuous functions are closed $G_\delta$ sets.

::: pf-proof

::: pf-step
Suppose $f: X \to [0, 1]$ is continuous and $A = \{x \in X : f(x) = 0\} = f^{-1}(\{0\})$.
:::

::: pf-step
Since $\{0\}$ is closed in $[0, 1]$ and $f$ is continuous, $A$ is closed in $X$.
:::

::: pf-step
For each $n \in \ZZ_+$, let $U_n = f^{-1}([0, \frac{1}{n})) = \{x \in X : f(x) < \frac{1}{n}\}$.
:::

::: pf-step
Since $[0, \frac{1}{n})$ is open in the subspace topology of $[0, 1]$, each $U_n$ is open in $X$.
:::

::: pf-step
$x \in \bigcap_{n=1}^\infty U_n \iff \forall n \ge 1, 0 \le f(x) < \frac{1}{n} \iff f(x) = 0 \iff x \in A$.
:::

::: pf-step
Thus $A = \bigcap_{n=1}^\infty U_n$ is a countable intersection of open sets, so $A$ is a $G_\delta$ set in $X$.
:::

:::

:::

::: pf-step
Reverse implication ($\impliedby$): Constructing a continuous function vanishing on a closed $G_\delta$ set.

::: pf-proof

::: pf-step
Suppose $A \subseteq X$ is closed and $A = \bigcap_{n=1}^\infty U_n$, where each $U_n$ is open in $X$.
:::

::: pf-step
For each $n \ge 1$, the complement $X \setminus U_n$ is closed in $X$ and disjoint from $A$ (since $A \subseteq U_n$).
:::

::: pf-step
Since $X$ is normal and $A, X \setminus U_n$ are disjoint closed sets, Urysohn's Lemma provides a continuous function $f_n: X \to [0, 1]$ such that:
$$f_n(x) = 0 \text{ for } x \in A, \qquad f_n(x) = 1 \text{ for } x \in X \setminus U_n.$$
:::

::: pf-step
Define $f: X \to [0, 1]$ by the infinite series:
$$f(x) = \sum_{n=1}^\infty \frac{1}{2^n} f_n(x).$$
:::

::: pf-step
Uniform convergence and continuity: For all $x \in X$, $\abs{\frac{1}{2^n} f_n(x)} \le \frac{1}{2^n}$. Since $\sum_{n=1}^\infty \frac{1}{2^n} = 1 < \infty$, the Weierstrass $M$-test proves that the series converges uniformly on $X$. Because each partial sum is continuous, the limit function $f$ is continuous.
:::

::: pf-step
Vanishing on $A$: If $x \in A$, then $f_n(x) = 0$ for all $n \ge 1$, so $f(x) = \sum_{n=1}^\infty 0 = 0$.
:::

::: pf-step
Positivity outside $A$: If $x \notin A$, then $x \notin \bigcap_{n=1}^\infty U_n$, so there exists some $k \ge 1$ such that $x \notin U_k$, meaning $x \in X \setminus U_k$.
:::

::: pf-step
Then $f_k(x) = 1$, and since $f_n(x) \ge 0$ for all $n$:
$$f(x) \ge \frac{1}{2^k} f_k(x) = \frac{1}{2^k} > 0.$$
:::

::: pf-step
Thus $f(x) = 0 \iff x \in A$, so $f$ vanishes precisely on $A$. Q.E.D.
:::

:::

:::

:::

:::
