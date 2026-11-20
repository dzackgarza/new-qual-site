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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Nine steps asserted their claim with no justification and the card is now three steps each deriving its
    claim: that a point of $A$ outside $A'$ has a neighbourhood meeting $A$ only in itself, which is the
    negation of the definition of a limit point; that the set of those points is at most countable, via an
    injection into a countable basis, with the injectivity derived from $B(x) \cap A = \{x\}$; and that
    $A \cap A'$ is uncountable, from $A = (A \cap A') \cup I$ together with the countability of $I$ and the
    uncountability of $A$. The three label-claims are replaced by the assertions their proofs establish.
    Sources are cited by numbered statement: Munkres, Topology, Section 30 Exercise 3, and the definition of
    a limit point; no page reference is written in the body of this card or in the event above. The
    statement is unchanged. The transcription correction recorded above is untouched: the contradiction is
    not with second countability directly but with the countability of $A$.
---

::: {.exercise}

Let $X$ have a countable basis; let $A$ be an uncountable subset of $X$.
Show that uncountably many points of $A$ are limit points of $A$.
:::

::: {.solution}
Write $A'$ for the set of limit points of $A$ in $X$; we show that $A \cap A'$ is uncountable.

::: pf

::: {.pf-step #isolated}
Every $x \in I = A \setminus A'$ has an open neighbourhood $U_x$ in $X$ with $U_x \cap A = \{x\}$.

::: pf-proof
A point $x$ of $A$ fails to be a limit point of $A$ exactly when some neighbourhood of $x$ meets $A$ in no point other than $x$ itself, since a limit point is one every neighbourhood of which meets $A$ in a point different from it. For such an $x$ choose an open neighbourhood $U_x$ of $x$ with $U_x \cap A \subseteq \{x\}$; then $x \in A$ and $x \in U_x$ give the reverse inclusion, so $U_x \cap A = \{x\}$.
:::

:::

::: {.pf-step #countable}
$I = A \setminus A'$ is at most countable.

::: pf-proof
Let $\mathcal{B} = \{B_n\}_{n=1}^\infty$ be a countable basis. For $x \in I$ pick a basis element $B(x)$ with $x \in B(x) \subseteq U_x$, possible because the basis elements inside $U_x$ that contain $x$ form a neighbourhood base at $x$. Then $B(x) \cap A \subseteq U_x \cap A = \{x\}$ and $x \in B(x) \cap A$, so $B(x) \cap A = \{x\}$. The assignment $\phi(x) = B(x)$ is injective: if $B(x) = B(y)$ then $\{x\} = B(x) \cap A = B(y) \cap A = \{y\}$, so $x = y$. An injection of $I$ into the countable set $\mathcal{B}$ makes $I$ at most countable.
:::

:::

::: pf-step

$A \cap A'$ is uncountable, that is, uncountably many points of $A$ are limit points of $A$.

::: pf-proof
The set $A$ is the union of $A \cap A'$ and $A \setminus A' = I$, which are disjoint, so $A = (A \cap A') \cup I$. The set $I$ is at most countable by step [](#countable){.pf-ref}, and a union of two at most countable sets is at most countable; since $A$ is uncountable, $A \cap A'$ cannot be at most countable, hence it is uncountable.
:::

:::

:::

:::
