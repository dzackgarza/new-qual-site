---
schema: qual/card@1
id: E-MUN-5-3
kind: problem
title: Containment and nonemptiness of infinite products
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 3; the stored statement matches.
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
    Read against Munkres, Topology (2000), §5 Exercise 3, printed p. 39; the four parts
    are stored as printed, including the parenthetical about changing a function's range
    in (a) and the cross-reference to the exercises of §19 in (c).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.3,
    printed pp. 69-70 (tmp/sources/munkres-solutions-whitman.pdf). His (b) replaces one
    coordinate of a chosen element of B, as the card does; his (d) has A union B
    contained in the product of the unions, with a counterexample to the converse, and
    the intersection equal to the product of the intersections. The card's (d) states
    the same inclusion and equality but does not write his counterexample; the strictness
    it asserts, that coordinates may come from different sides, is his reason. Its
    remark in (c), that for a countable family the converse is the countable axiom of
    choice and is not provable in ZF, is stronger than the manual's "this requires the
    Axiom of Choice" and is true; the book defers the point to the exercises of §19.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the four parts into numbered steps and supplied two things the prose asserted
    without argument: an explicit two-coordinate example showing the inclusion in (d) is strict
    (A_1 = A_2 = {1}, B_1 = B_2 = {2}, where the right-hand product contains (1,2)), and both
    inclusions of the intersection identity, which the prose left as a chain of equivalences. Also
    made explicit the convention under which an element of a product is a function, which is what
    the parenthetical in (a) is about. Checked: the replacement of a single coordinate produces a
    function on the index set with values in the right sets, and (b) uses only one element of B.
    Not re-read this session: the Whitman pages and Munkres printed p. 39.
---

::: {.exercise}

Let $A = A_{1} \times A_{2} \times \cdots$ and $B = B_{1} \times B_{2} \times \cdots$ .

(a) Show that if $B_{i} \subset A_{i}$ for all $i$, then $B \subset A$ . (Strictly speaking, if we are given a function mapping the index set $\ZZ_{+}$ into the union of the sets $B_{i}$, we must change its range before it can be considered as a function mapping $\ZZ_{+}$ into the union of the sets $A_{i}$ . We shall ignore this technicality when dealing with cartesian products).

(b) Show the converse of (a) holds if $B$ is nonempty.

(c) Show that if $A$ is nonempty, each $A_i$ is nonempty.
Does the converse hold?
(We will return to this question in the exercises of §19.)

(d) What is the relation between the set $A \cup B$ and the cartesian product of the sets $A_i \cup B_i$ ? What is the relation between the set $A \cap B$ and the cartesian product of the sets $A_i \cap B_i$ ?
:::

::: {.solution}

The four parts are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.3, printed pp. 69--70** (`tmp/sources/munkres-solutions-whitman.pdf`); the explicit strictness example in (d) and the two inclusions of the intersection identity are supplied below.

Following Munkres, an element of $A=\prod_{i\geq1}A_{i}$ is a function $x$ with domain $\ZZ_{+}$ such that $x_{i}\in A_{i}$ for every $i$; this is the convention that makes the parenthetical in part (a) unnecessary. Write $B=\prod_{i\geq1}B_{i}$ similarly.

::: pf

::: {.pf-step #a}
If $B_{i}\subset A_{i}$ for every $i$, then $B\subset A$.

::: pf-proof
Let $x\in B$. Then $x$ is a function with domain $\ZZ_{+}$ and $x_{i}\in B_{i}$ for every $i$; since $B_{i}\subset A_{i}$, also $x_{i}\in A_{i}$ for every $i$, so the same function $x$ satisfies the condition defining $A$ and lies in $A$.
:::

:::

::: {.pf-step #b}
If $B\neq\varnothing$ and $B\subset A$, then $B_{i}\subset A_{i}$ for every $i$.

::: pf-proof
Choose $x\in B$, possible because $B$ is nonempty. Fix an index $i$ and let $b\in B_{i}$. Define $y$ by $y_{j}=x_{j}$ for $j\neq i$ and $y_{i}=b$; this is a function with domain $\ZZ_{+}$. For $j\neq i$, $y_{j}=x_{j}\in B_{j}$; for $j=i$, $y_{i}=b\in B_{i}$. So $y\in B\subset A$, whence $y_{i}\in A_{i}$, that is $b\in A_{i}$. As $b\in B_{i}$ was arbitrary, $B_{i}\subset A_{i}$.
:::

:::

::: {.pf-step #b-sharp}
The hypothesis $B\neq\varnothing$ in step [](#b){.pf-ref} cannot be dropped.

::: pf-proof
Let $B_{1}=\varnothing$ and $A_{1}=\{1\}$, with $B_{i}=A_{i}=\{1\}$ for $i\geq2$. Then $B=\varnothing\subset A$, but $B_{1}\not\subset A_{1}$.
:::

:::

::: {.pf-step #c}
If $A\neq\varnothing$ then every $A_{i}$ is nonempty.

::: pf-proof
Choose $x\in A$; then $x_{i}\in A_{i}$ exhibits an element of $A_{i}$, for each $i$ separately.
:::

:::

::: {.pf-step #c-converse}
The converse of step [](#c){.pf-ref} is not a theorem of the other axioms: producing an element of $\prod_{i}A_{i}$ from the nonemptiness of the $A_{i}$ means choosing one element from each $A_{i}$, that is a choice function for the family $\{A_{i}\}$.

::: pf-proof
An element of the product is by definition a function $x$ on the index set with $x_{i}\in A_{i}$ for every $i$, which is exactly a choice function for the family. For a finite family such a function is produced by finitely many applications of the rule of existential instantiation, and for a countable family the assertion is the countable axiom of choice; for an arbitrary infinite family it is the axiom of choice itself, which is independent of the remaining axioms of set theory. Munkres defers the question to the exercises of §19, and nothing in parts (a), (b) and (d) uses it.
:::

:::

::: {.pf-step #d-union}
$A\cup B\subset\prod_{i}(A_{i}\cup B_{i})$.

::: pf-proof
If $x\in A\cup B$ then $x\in A$ or $x\in B$. In the first case $x_{i}\in A_{i}\subset A_{i}\cup B_{i}$ for every $i$; in the second $x_{i}\in B_{i}\subset A_{i}\cup B_{i}$ for every $i$. Either way $x$ satisfies the condition defining $\prod_{i}(A_{i}\cup B_{i})$.
:::

:::

::: {.pf-step #d-strict}
The inclusion of step [](#d-union){.pf-ref} can be strict.

::: pf-proof
Take $A_{1}=A_{2}=\{1\}$ and $B_{1}=B_{2}=\{2\}$, and let $A_{i}=B_{i}=\{1\}$ for $i\geq3$. Then $A=\{(1,1,1,\dots)\}$ and $B=\{(2,2,2,\dots)\}$, while $\prod_{i}(A_{i}\cup B_{i})$ contains the function $(1,2,1,1,\dots)$, whose first coordinate comes from $A_{1}$ and whose second comes from $B_{2}$; that function lies in neither $A$ nor $B$. Hence $A\cup B$ is a proper subset of the product of the unions.
:::

:::

::: {.pf-step #d-inter}
$A\cap B=\prod_{i}(A_{i}\cap B_{i})$.

::: pf-proof
$x\in A\cap B$ means $x\in A$ and $x\in B$, that is $x_{i}\in A_{i}$ for every $i$ and $x_{i}\in B_{i}$ for every $i$; this is equivalent to $x_{i}\in A_{i}\cap B_{i}$ for every $i$, which is the condition for $x\in\prod_{i}(A_{i}\cap B_{i})$. Both implications are immediate, so the two sets are equal.
:::

:::

::: {.pf-step}
Parts (a), (b), (c) and (d) hold, with the qualifications stated: the converse in (b) needs $B\neq\varnothing$, the converse in (c) is a choice principle, and in (d) the union gives only an inclusion while the intersection gives an equality.

::: pf-proof
Steps [](#a){.pf-ref}, [](#b){.pf-ref} with [](#b-sharp){.pf-ref}, [](#c){.pf-ref} with [](#c-converse){.pf-ref}, and [](#d-union){.pf-ref}, [](#d-strict){.pf-ref}, [](#d-inter){.pf-ref} are the four parts with their exact hypotheses.
:::

:::

:::

:::
