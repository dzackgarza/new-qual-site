---
schema: qual/card@1
id: E-0SFDE
kind: problem
title: The line as a countable union of sets with empty interior
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
    The located published solution is "Solutions to exercises for Mathematics 205A" (University of California,
    Riverside, Fall 2014), Part 3, section "III.3: Implications of completeness", answer to Munkres §48
    Exercise 2 on the set's own printed pp. 6-7 (in tmp/sources/munkres-solutions-ucr-math205-gentop.pdf, PDF
    pp. 47-48). Its argument is not cited as the proof: it takes a Q-basis of R, the Q-subspace W spanned by
    all basis vectors but 1, and the countable family of cosets c + W, and then states that each coset "has a
    nonempty interior" and argues that it does not, so its conclusion contradicts its own claim; what the
    argument actually shows is that each coset meets Q in exactly one point and therefore has empty interior,
    and the cosets are not closed, being dense, so the family is a counterexample. The card keeps its own
    counterexample instead, which is shorter and complete: R is the union of the irrationals and the countably
    many rational singletons, each has empty interior, and the irrationals are not closed. Checked against
    Munkres, Topology (2000), §48 Exercise 2, printed p. 299, with Theorem 48.2 and the density of Q and of the
    irrationals in R; the card's closing references to four step labels that no step carried are replaced by
    the prose sentence that closes the argument.
---

::: {.exercise}

The Baire category theorem implies that $\RR$ cannot be written as a countable union of closed subsets having empty interiors.
Show this fails if the sets are not required to be closed.
:::

::: {.solution}

::: pf

::: pf-step

Construction of the partition:
    1. Let $\QQ$ be the set of rational numbers in $\RR$. Since $\QQ$ is countably infinite, choose an enumeration $\QQ = \{q_1, q_2, q_3, \dots\}$.
    2. Let $A_0 = \RR \setminus \QQ$ be the set of all irrational numbers.
    3. For each $n \in \ZZ_+$, let $A_n = \{q_n\}$.
    4. Then $\bigcup_{n=0}^\infty A_n = (\RR \setminus \QQ) \cup \bigcup_{n=1}^\infty \{q_n\} = (\RR \setminus \QQ) \cup \QQ = \RR$.

:::

::: pf-step

Each singleton $A_n = \{q_n\}$ has empty interior for $n \ge 1$:
    *Proof:* Every non-empty open subset of $\RR$ contains an open interval $(a, b)$ with $a < b$, which contains uncountably many points. Since $A_n$ contains exactly one point, $A_n$ contains no open interval. Thus $\operatorname{Int}(A_n) = \emptyset$.

:::

::: pf-step

The set of irrationals $A_0 = \RR \setminus \QQ$ has empty interior:
    *Proof:* If $\operatorname{Int}(\RR \setminus \QQ) \neq \emptyset$, it would contain a non-empty open interval $(a, b)$ with $a < b$. By the density of $\QQ$ in $\RR$, there exists a rational number $q \in (a, b) \subset \RR \setminus \QQ$, which contradicts $q \in \QQ$. Thus $\operatorname{Int}(A_0) = \emptyset$.

:::

::: pf-step

$A_0$ is not closed in $\RR$:
    *Proof:* By the density of the irrationals in $\RR$, the closure of $A_0 = \RR \setminus \QQ$ is $\overline{\RR \setminus \QQ} = \RR \neq A_0$.

:::

:::

So $\RR$ is the countable union of the sets $A_0, A_1, A_2, \ldots$, each of which has empty interior, and the first of them is not closed: the failure of the Baire category theorem here is exactly the loss of the closedness hypothesis, the other summands being closed singletons.
:::
