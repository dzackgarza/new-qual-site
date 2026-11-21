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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Eight steps asserted their claim with no justification and each now carries one: the finiteness of
    the Radon measure from the compactness of $X^*$, the openness of a singleton from the one-point
    compactification's description of its open sets, the complement of the support as the union of the
    open null sets, the neighbourhood criterion for membership in the support in both directions, the
    singleton as an open neighbourhood, the two implications of the characterization, and the closing
    count which splits the support into its part in $X$ and its part at $\infty$. Two steps carried their
    argument in a run-in "*Proof:*" line inside the claim and now state the assertion with the argument in
    the proof; the container step carried a label and now states its claim; a "Goal" paragraph restating
    the problem is gone; and the closing pf-qed, which only pointed at the steps above, is replaced by a
    step that derives the count. Sources are cited by numbered statement: the definition of a Radon
    measure and the definition of the one-point compactification. No page reference is written in the
    body of this card or in the event above. The statement is unchanged. The collection retains the UCSD
    real analysis qualifying exam of Spring 2024 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Let $X$ be a set equipped with the discrete topology, and let $X^* = X \cup \{\infty\}$ be the one-point compactification of $X$.
Let $\mu$ be a Radon measure on $X^*$ and define the support of $\mu$ as
$$
\operatorname{supp}(\mu) = \bigcap \{N : N \subseteq X^* \text{ is closed and } \mu(N^c) = 0\}.
$$
Prove that $\operatorname{supp}(\mu)$ is countable.
:::

::: {.solution}

::: pf

::: {.pf-step #finite}

$X^*$ is compact Hausdorff, so the Radon measure $\mu$ is a finite Borel measure on $X^*$, meaning $\mu(X^*) < \infty$.

::: pf-proof
A Radon measure on a compact Hausdorff space is finite: the definition requires every compact set to have finite measure, and the whole space is compact, so $\mu(X^*) < \infty$.
:::

:::

::: {.pf-step #s2}

For every $x \in X$, the singleton set $\{x\}$ is open in $X^*$.

::: pf-proof
In the one-point compactification the open sets are the open subsets of $X$ together with the sets $(X \setminus K) \cup \{\infty\}$ for $K$ compact in $X$. Since $X$ is discrete, every subset of $X$ is open there, so $\{x\}$ is open in $X$; it does not contain $\infty$, hence it is open in $X^*$.
:::

:::

::: {.pf-step #characterization}

A point $x \in X$ belongs to $\operatorname{supp}(\mu)$ if and only if $\mu(\{x\}) > 0$.

::: pf-proof

::: pf-step

By definition, $\operatorname{supp}(\mu)^c = \bigcup \{U \subseteq X^* : U \text{ is open and } \mu(U) = 0\}$.


::: pf-proof
The support is the intersection of the closed sets whose complement is null, so its complement is the union of the complements of those sets, and the complement of a closed set is open and has measure zero by the defining property. Conversely an open set $U$ with $\mu(U) = 0$ has closed complement $N$ with $\mu(N^c) = \mu(U) = 0$, so $N$ is one of the sets intersected and $U = N^c$ appears in the union. Hence the complement of the support is exactly the union of the open null sets.
:::

:::

::: pf-step

Hence $y \in \operatorname{supp}(\mu)$ if and only if every open neighborhood $U$ of $y$ in $X^*$ satisfies $\mu(U) > 0$.


::: pf-proof
If $U$ is an open neighbourhood of $y$ with $\mu(U) = 0$ then $y \notin \operatorname{supp}(\mu)$ because $y$ lies outside the closed set $X^* \setminus U$, which has null complement in the intersection defining the support. Conversely if $y \notin \operatorname{supp}(\mu)$ then $y$ fails to lie in some closed $N$ with $\mu(N^c) = 0$, so $X^* \setminus N$ is an open neighbourhood of $y$ of measure zero. Taking the contrapositive gives the stated equivalence.
:::

:::

::: pf-step

For $x \in X$, $\{x\}$ is an open neighborhood of $x$ by step [](#s2){.pf-ref}.


::: pf-proof
The singleton $\{x\}$ is open in $X^*$ by the previous part, and it contains $x$, so it is an open neighbourhood of $x$.
:::

:::

::: pf-step

If $\mu(\{x\}) = 0$, then $\{x\}$ is an open set of measure zero, so $\{x\} \subseteq \operatorname{supp}(\mu)^c$, which means $x \notin \operatorname{supp}(\mu)$.


::: pf-proof
The set $\{x\}$ is an open neighbourhood of $x$ of measure zero, so the criterion of the characterization step fails at $x$ and $x$ is not in the support; equivalently $\{x\}$ lies in the complement of the support, which is the union of the open null sets.
:::

:::

::: pf-step

If $\mu(\{x\}) > 0$, then every open neighborhood $U$ of $x$ contains $\{x\}$, so $\mu(U) \ge \mu(\{x\}) > 0$, which means $x \in \operatorname{supp}(\mu)$.


::: pf-proof
Every open neighbourhood $U$ of $x$ contains the point $x$ and hence contains $\{x\}$, and a measure is monotone under inclusion, so $\mu(U) \ge \mu(\{x\}) > 0$; the characterization step then puts $x$ in the support.
:::

:::

::: pf-step

Thus $X \cap \operatorname{supp}(\mu) = \{x \in X : \mu(\{x\}) > 0\}$.


::: pf-proof
For $x \in X$ the two previous steps show that membership of $x$ in the support is equivalent to $\mu(\{x\}) > 0$, which is the stated description of the intersection of the support with $X$.
:::

:::

:::

:::

::: {.pf-step #s4}

The set $S = \{x \in X : \mu(\{x\}) > 0\}$ is at most countable.

::: pf-proof

For each $n \ge 1$ let $S_n = \{x \in X : \mu(\{x\}) \ge 1/n\}$, so $S = \bigcup_{n\ge1} S_n$.
For distinct $x_1,\dots,x_k \in S_n$, disjointness of the singletons gives
$$\mu(X^*) \ge \sum_{j=1}^k \mu(\{x_j\}) \ge \frac{k}{n},$$
so $\cardinality{S_n} \le n\,\mu(X^*) < \infty$.
A countable union of finite sets is at most countable.

:::

:::

::: pf-step
$\operatorname{supp}(\mu)$ is at most countable.

::: pf-proof
The space is $X^* = X \cup \{\infty\}$, so the support is the union of its intersection with $X$ and its intersection with $\{\infty\}$. The first is the set $S$ of points with $\mu(\{x\}) > 0$ by step [](#characterization){.pf-ref}, which is at most countable by step [](#s4){.pf-ref}, and the second is either empty or the single point $\infty$. A union of an at most countable set with a set of at most one point is at most countable.
:::

:::

:::

:::
