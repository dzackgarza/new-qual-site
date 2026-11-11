---
schema: qual/card@1
id: E-AKPMH
kind: problem
title: The irrationals are a Baire space
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 6 (printed p. 299) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book: the irrationals
    are the intersection of the countably many open dense sets R - {q_n}, and the criterion of Lemma 48.1 is
    applied in R, which is a Baire space by Theorem 48.2, to the countable family consisting of the dense open
    sets W_k of the subspace and the sets R - {q_n}. What was corrected: the card asserted that an open set of R
    whose trace on the irrationals is dense there must be dense in R, which is true but is a step of the
    argument, and it is now proved: an open interval missed by W_k would give a nonempty relatively open piece of
    the irrationals disjoint from V_k. The final step, that a set dense in R and contained in the irrationals is
    dense in the irrationals, is the definition of the subspace topology.
---

::: {.exercise}

Show that the irrationals are a Baire space.
:::

::: {.solution}
Let $\irrationals = \RR \setminus \QQ$ with the subspace topology.

::: pf

::: pf-step
Representation of $\irrationals$ as a $G_\delta$ subset of $\RR$:

::: pf-proof

::: pf-step
Enumerate the countable set of rational numbers as $\QQ = \{q_n\}_{n=1}^\infty$.
:::

::: pf-step
For each $n \ge 1$, the singleton $\{q_n\}$ is closed in $\RR$, so $U_n = \RR \setminus \{q_n\}$ is an open and dense subset of $\RR$.
:::

::: pf-step
The subspace of irrational numbers is:
$$\irrationals = \RR \setminus \QQ = \bigcap_{n=1}^\infty U_n.$$
:::

:::

:::

::: {.pf-step #s2}
Verification of the dense open intersection condition:

::: pf-proof

::: pf-step
Let $\{V_k\}_{k=1}^\infty$ be a countable sequence of dense open subsets of the subspace $\irrationals$.
:::

::: pf-step
Since each $V_k$ is open in $\irrationals$, there exists an open set $W_k \subseteq \RR$ such that $V_k = W_k \cap \irrationals$.
:::

::: pf-step
The open set $W_k$ is dense in $\RR$: if it missed a nonempty open interval $I$, then $I\cap\irrationals$ would be a nonempty relatively open subset of $\irrationals$ disjoint from $V_k=W_k\cap\irrationals$, contradicting density of $V_k$ in $\irrationals$ (which is dense in $\RR$).
:::

::: pf-step
The combined collection $\{W_k\}_{k=1}^\infty \cup \{U_n\}_{n=1}^\infty$ is a countable family of open and dense subsets of $\RR$.
:::

::: pf-step
By the Baire category theorem, the complete metric space $\RR$ is a Baire space, so the countable intersection:
$$\bigcap_{k=1}^\infty W_k \cap \bigcap_{n=1}^\infty U_n = \left(\bigcap_{k=1}^\infty W_k\right) \cap \irrationals = \bigcap_{k=1}^\infty V_k$$
is dense in $\RR$.
:::

::: pf-step
Since this intersection lies in $\irrationals$ and is dense in $\RR$, it is dense in the subspace $\irrationals$.
:::

:::

:::

::: pf-qed
By step [](#s2){.pf-ref}, every countable intersection of dense open subsets of $\irrationals$ is dense in $\irrationals$.
:::

:::

:::
