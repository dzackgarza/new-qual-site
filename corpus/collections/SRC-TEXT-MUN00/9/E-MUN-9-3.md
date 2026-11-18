---
schema: qual/card@1
id: E-MUN-9-3
kind: problem
title: Infinite sets from sequences of injections
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §9 Exercise 3, printed p. 61; the stored statement matches, including the second question about avoiding the choice axiom.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.3, printed pp. 102-103 (tmp/sources/munkres-solutions-whitman.pdf). He defines an injection recursively, choosing at each stage the least index whose value is new, which is the same device the card uses; the card takes an explicit enumeration of the pairs (n,k) instead of his recursion on sections, so no principle of recursive definition is invoked.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the answer into numbered steps and supplied three things it used silently: that an
    injection carries a finite set to a set of the same cardinality, so an injection of an
    (N+1)-element set into an N-element set is impossible; that the diagonal enumeration of the
    pairs (n,k) is a bijection, so every pair occurs exactly once; and that the set of admissible
    indices in the recursion for r_{m+1} is nonempty, which is where the infinitude of S enters.
    Also corrected the earlier wording about recursion: the sequence r_m is produced by the
    recursion theorem for the well-ordered set Z_+, which is a theorem of ZF, and the claim that no
    choice is used rests on every stage being a least element, not on doing without recursion.
    Not re-read this session: the Whitman pages and Munkres printed p. 61.
---

::: {.exercise}

Suppose that $A$ is a set and $\{f_n\}_{n \in \ZZ_+}$ is a given indexed family of injective functions

$$
f_n\colon \{1, \dots, n\} \longrightarrow A.
$$

Show that $A$ is infinite.
Can you define an injective function $f: \ZZ_+ \to A$ without using the choice axiom?
:::

::: {.solution}

The device of always taking a least index, which is what avoids the choice axiom, is **Dan Whitman's**, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.3, printed pp. 102--103 (`tmp/sources/munkres-solutions-whitman.pdf`), applied here to an explicit enumeration of the pairs $(n,k)$.

Suppose $A$ is a set and $\{f_{n}\}_{n\in\ZZ_{+}}$ is an indexed family of injective functions $f_{n}\colon\{1,\dots,n\}\to A$.

::: pf

::: {.pf-step #infinite}
$A$ is infinite.

::: pf-proof
An injective map carries a finite set onto a subset of the same cardinality, so $f_{n}(\{1,\dots,n\})$ has exactly $n$ elements. If $A$ were finite with $\cardinality{A}=N$, then $f_{N+1}$ would inject an $(N+1)$-element set into an $N$-element set; but the image would then have $N+1$ distinct elements inside a set with $N$ elements, which is impossible. So $A$ is infinite.
:::

:::

::: {.pf-step #enumeration}
There is an explicit bijection $j\mapsto(n_{j},k_{j})$ from $\ZZ_{+}$ onto $P=\{(n,k)\mid 1\leq k\leq n\}$.

::: pf-proof
For each integer $s\geq2$ the pairs in $P$ with $n+k=s$ are the finitely many with $k=1,\dots,s-1$ and $n=s-k$; list them in increasing $k$. Concatenating these lists for $s=2,3,4,\dots$ gives a sequence in which every pair of $P$ occurs exactly once, since $n+k$ is determined by the pair and its position within the list for $s=n+k$ is determined by $k$. The rule is explicit, so no choice is involved.
:::

:::

::: {.pf-step #S}
With $a_{j}\coloneqq f_{n_{j}}(k_{j})$, the set $S=\{a_{j}\mid j\geq1\}$ is infinite.

::: pf-proof
Let $n\geq1$ and $1\leq k\leq n$. By step [](#enumeration){.pf-ref} there is exactly one $j$ with $(n_{j},k_{j})=(n,k)$, and then $a_{j}=f_{n}(k)$; hence $f_{n}(\{1,\dots,n\})\subset S$, a subset with $n$ elements. Since $n$ is arbitrary, $S$ has subsets of every finite cardinality and so cannot be finite.
:::

:::

::: {.pf-step #recursion}
There is a strictly increasing sequence $r_{1}<r_{2}<\cdots$ of positive integers with $a_{r_{1}},a_{r_{2}},\dots$ pairwise distinct.

::: pf-proof
Put $r_{1}=1$; having chosen $r_{1}<\cdots<r_{m}$ with $a_{r_{1}},\dots,a_{r_{m}}$ distinct, let $r_{m+1}$ be the least $j>r_{m}$ with $a_{j}\notin\{a_{r_{1}},\dots,a_{r_{m}}\}$. That set of indices is nonempty: if every $j>r_{m}$ had $a_{j}\in\{a_{r_{1}},\dots,a_{r_{m}}\}$, then $S\subset\{a_{1},\dots,a_{r_{m}}\}$, which is finite, contradicting step [](#S){.pf-ref}. A least element exists because $\ZZ_{+}$ is well ordered, and it is unique, so the sequence is defined by the recursion theorem on the well-ordered set $\ZZ_{+}$, a theorem of ZF.
:::

:::

::: {.pf-step #injection}
$F(m)\coloneqq a_{r_{m}}$ defines an injection $F\colon\ZZ_{+}\to A$ without the axiom of choice.

::: pf-proof
$F$ takes values in $A$, and it is injective because the values $a_{r_{m}}$ are pairwise distinct by step [](#recursion){.pf-ref}. Nothing was chosen: the family $\{f_{n}\}$ is given as one indexed object, the enumeration of the pairs is an explicit formula, and at each stage the next index is the least element of a set of integers, determined by that set.
:::

:::

:::

:::
