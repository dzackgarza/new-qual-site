---
schema: qual/card@1
id: E-9TQ6L
kind: problem
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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Amit Rajaraman, "Munkres Solutions" (MA 406
    course notes, last updated 31 March 2021), Exercise 4.30.3, printed p. 12
    (tmp/sources/munkres-solutions-amitrajaraman-ma406.pdf), and independently checked against
    "Doug's World", "Munkres - Topology - Chapter 4 Solutions" (30 August 2017; the file names no
    author), Problem 30.3, printed p. 1 (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); the
    exercise is printed on p. 194 of Munkres, Topology (2000). Corrections: Rajaraman ends "since
    A - A' is countable, this contradicts the second countability of X", which is not the
    contradiction -- the injection x -> B(x) of the non-limit points into a countable basis shows
    that A - A' is countable, and that together with the countability of A cap A' makes the
    uncountable A countable. The card states that conclusion, which is Doug's World's argument at
    printed p. 1.
---

::: {.exercise}

Let $X$ have a countable basis; let $A$ be an uncountable subset of $X$.
Show that uncountably many points of $A$ are limit points of $A$.
:::

::: {.solution}
Write $A'$ for the set of limit points of $A$ in $X$; we show that $A \cap A'$ is uncountable.

::: pf

::: pf-step
Identification of non-limit points (isolated points of $A$):

::: pf-proof

::: pf-step
Let $I = A \setminus A'$ denote the set of points in $A$ that are not limit points of $A$.
:::

::: pf-step
By definition of limit points, for every $x \in I$, there exists an open neighborhood $U_x$ of $x$ in $X$ such that:
$$U_x \cap A = \{x\}.$$
:::

:::

:::

::: pf-step
Proof that $I$ is at most countable:

::: pf-proof

::: pf-step
Let $\mathcal{B} = \{B_n\}_{n=1}^\infty$ be a countable basis for the topology of $X$.
:::

::: pf-step
For each $x \in I$, choose a basis element $B(x) \in \mathcal{B}$ such that $x \in B(x) \subseteq U_x$.
:::

::: pf-step
Since $x \in B(x) \subseteq U_x$, we have $B(x) \cap A \subseteq U_x \cap A = \{x\}$. Because $x \in B(x) \cap A$, it follows that:
$$B(x) \cap A = \{x\}.$$
:::

::: pf-step
The assignment $\phi: I \to \mathcal{B}$ defined by $\phi(x) = B(x)$ is injective: if $\phi(x) = \phi(y)$, then $\{x\} = B(x) \cap A = B(y) \cap A = \{y\}$, forcing $x = y$.
:::

::: pf-step
Because $\mathcal{B}$ is countable and $\phi$ is injective, the set $I = A \setminus A'$ is at most countable.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof

::: pf-step
We partition $A$ as:
$$A = (A \cap A') \cup (A \setminus A') = (A \cap A') \cup I.$$
:::

::: pf-step
Since $A$ is uncountable and $I$ is countable, the set $A \cap A'$ of points of $A$ that are limit points of $A$ must be uncountable.
:::

:::

:::

:::

:::
