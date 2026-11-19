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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subsections suffice, and the 15
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    trailing Q.E.D. was dropped. The mathematics is unchanged: a continuous $f$ vanishing on $A$ makes $A$
    the preimage of $\{0\}$ and a countable intersection of the open sets $\{f<1/n\}$; conversely
    Urysohn's lemma applied to $A$ and $X\setminus U_n$ produces $f_n$, and $\sum2^{-n}f_n$ converges
    uniformly by the $M$-test, vanishes on $A$ and is positive off it. Checked against Munkres, Topology
    (2000), section 33 Exercise 5. Nothing in the statement was changed.

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

::: pf-proof
This is the hypothesis of the forward implication.
:::

:::

::: pf-step
Since $\{0\}$ is closed in $[0, 1]$ and $f$ is continuous, $A$ is closed in $X$.

::: pf-proof
The preimage of a closed set under a continuous map is closed.
:::

:::

::: pf-step
For each $n \in \ZZ_+$, let $U_n = f^{-1}([0, \frac{1}{n})) = \{x \in X : f(x) < \frac{1}{n}\}$.

::: pf-proof
This is a definition of a countable family of open sets attached to $f$.
:::

:::

::: pf-step
Since $[0, \frac{1}{n})$ is open in the subspace topology of $[0, 1]$, each $U_n$ is open in $X$.

::: pf-proof
Preimages of open sets under a continuous map are open.
:::

:::

::: pf-step
$x \in \bigcap_{n=1}^\infty U_n \iff \forall n \ge 1, 0 \le f(x) < \frac{1}{n} \iff f(x) = 0 \iff x \in A$.

::: pf-proof
The intersection of the intervals $[0,1/n)$ over all $n$ is $\{0\}$.
:::

:::

::: pf-step
Thus $A = \bigcap_{n=1}^\infty U_n$ is a countable intersection of open sets, so $A$ is a $G_\delta$ set in $X$.

::: pf-proof
The family is countable by construction and the equality was just shown.
:::

:::

:::

:::

::: pf-step
Reverse implication ($\impliedby$): Constructing a continuous function vanishing on a closed $G_\delta$ set.

::: pf-proof

::: pf-step
Suppose $A \subseteq X$ is closed and $A = \bigcap_{n=1}^\infty U_n$, where each $U_n$ is open in $X$.

::: pf-proof
This is the hypothesis of the converse.
:::

:::

::: pf-step
For each $n \ge 1$, the complement $X \setminus U_n$ is closed in $X$ and disjoint from $A$ (since $A \subseteq U_n$).

::: pf-proof
The complement of an open set is closed.
:::

:::

::: pf-step
Since $X$ is normal and $A, X \setminus U_n$ are disjoint closed sets, Urysohn's Lemma provides a continuous function $f_n: X \to [0, 1]$ such that:
$$f_n(x) = 0 \text{ for } x \in A, \qquad f_n(x) = 1 \text{ for } x \in X \setminus U_n.$$

::: pf-proof
Urysohn's lemma applied to the disjoint closed sets $A$ and $X\setminus U_n$ gives a continuous $f_n$ that is $1$ on $A$ and $0$ on that complement.
:::

:::

::: pf-step
Define $f: X \to [0, 1]$ by the infinite series:
$$f(x) = \sum_{n=1}^\infty \frac{1}{2^n} f_n(x).$$

::: pf-proof
This is a definition: a series of continuous functions whose sup norms are summable.
:::

:::

::: pf-step
Uniform convergence and continuity: For all $x \in X$, $\abs{\frac{1}{2^n} f_n(x)} \le \frac{1}{2^n}$. Since $\sum_{n=1}^\infty \frac{1}{2^n} = 1 < \infty$, the Weierstrass $M$-test proves that the series converges uniformly on $X$. Because each partial sum is continuous, the limit function $f$ is continuous.

::: pf-proof
$\abs{2^{-n}f_n}\le2^{-n}$ and $\sum2^{-n}$ converges, so the Weierstrass $M$-test gives uniform convergence, and a uniform limit of continuous functions is continuous.
:::

:::

::: pf-step
Vanishing on $A$: If $x \in A$, then $f_n(x) = 0$ for all $n \ge 1$, so $f(x) = \sum_{n=1}^\infty 0 = 0$.

::: pf-proof
Each $f_n$ vanishes on $A$, so every term of the series does.
:::

:::

::: pf-step
Positivity outside $A$: If $x \notin A$, then $x \notin \bigcap_{n=1}^\infty U_n$, so there exists some $k \ge 1$ such that $x \notin U_k$, meaning $x \in X \setminus U_k$.

::: pf-proof
If $x\notin A=\bigcap_n U_n$ then $x\notin U_k$ for some $k$, and $f_k(x)=1$ there.
:::

:::

::: pf-step
Then $f_k(x) = 1$, and since $f_n(x) \ge 0$ for all $n$:
$$f(x) \ge \frac{1}{2^k} f_k(x) = \frac{1}{2^k} > 0.$$

::: pf-proof
All terms are non-negative and the $k$-th contributes $2^{-k}$.
:::

:::

::: pf-step
Thus $f(x) = 0 \iff x \in A$, so $f$ vanishes precisely on $A$.

::: pf-proof
The two preceding steps give both directions, and the series is continuous by the $M$-test.
:::

:::

:::

:::

:::

:::
