---
schema: qual/card@1
id: E-MUN-3-3
kind: problem
title: A symmetric transitive relation need not be reflexive
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 3, printed p. 28. The exercise
    prints the bogus argument about a relation C that is symmetric and transitive
    implying aCa, and asks for the flaw; the card states the argument as printed and
    answers it.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.3,
    printed pp. 19-20 (tmp/sources/munkres-solutions-whitman.pdf). The diagnosis - the
    argument needs a b with aCb, so it proves only that a is related to itself when it
    is related to something - and the four-element counterexample are his.
---

::: {.exercise}

Here is a "proof" that every relation $C$ that is both symmetric and transitive is also reflexive: "Since $C$ is symmetric, $aCb$ implies $bCa$. Since $C$ is transitive, $aCb$ and $bCa$ together imply $aCa$, as desired." Find the flaw in this argument.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.3, printed pp. 19--20** (`tmp/sources/munkres-solutions-whitman.pdf`); the diagnosis and the counterexample below are his.

The reasoning from $aCb$ to $aCa$ is valid: symmetry gives $bCa$, transitivity then gives $aCa$. What it proves is that $aCa$ holds whenever $a$ is related to something, that is, whenever there is a $b$ with $aCb$. Reflexivity requires $aCa$ for **every** $a\in A$, and for an $a$ that is related to nothing the hypothesis $aCb$ is never available.

The defect is real and not a gap in the writing. Let
$$
A=\{1,2,3,4\},
\qquad
C=\{(i,j)\mid i,j\in\{1,2,3\}\}\subset A\times A .
$$
Then $C$ is symmetric, since it contains $(i,j)$ exactly when it contains $(j,i)$, and transitive, since $iCj$ and $jCk$ force $i,k\in\{1,2,3\}$ and hence $iCk$. But $(4,4)\notin C$, so $C$ is not reflexive. The element $4$ is related to nothing at all, which is exactly the case the argument cannot reach.
:::
