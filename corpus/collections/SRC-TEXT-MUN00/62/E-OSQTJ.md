---
schema: qual/card@1
id: E-OSQTJ
kind: problem
title: Compact contractible subsets of the sphere do not separate
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 2, printed p. 384. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The proof is the contrapositive of Lemma 62.2, the
    Borsuk lemma (printed p. 382), which the earlier card cited in paraphrase and without a page; the statement
    of the lemma is now reproduced and applied to the inclusion map, and the identification
    S^2 - {a,b} = R^2 - {0} up to homeomorphism is made explicit. Checked against Lemma 62.1 (printed p. 381)
    and the definition of a nullhomotopic map.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of this exercise (issue #144). Problem
    (10) of "MATH 4530 - Topology. Practice Problems For Final solutions", the course solutions of
    Cornell's MATH 4530 (Fall 2010),
    https://pi.math.cornell.edu/~matsumura/math4530/2010Fall4530PracticeForFinalSol.pdf, printed p. 3
    of the file, text at tmp/sources/munkres-cornell-math4530-2010-practice-final-solutions.txt,
    states the same argument: for arbitrary a and b in S^2 - A take f the identity on A, apply the
    Borsuk lemma, and conclude that any two points of S^2 - A lie in one component. The solution on
    the card is that argument transcribed, with the two points of the printed text written out: that
    A is compact and f injective is the hypothesis, and that f is nullhomotopic is the composite of a
    contraction of A with the inclusion, whose values lie in A. It replaces the card's earlier proof,
    which proved the contrapositive through the same lemma; the statement, the page and the lemma are
    unchanged. Checked against Lemma 62.2 (printed p. 382).
---

::: {.exercise}

Let $A$ be a compact contractible subspace of $S^2$.
Show that $A$ does not separate $S^2$.
:::

::: {.solution}

Let $A$ be a compact contractible subspace of $S^2$, and let $a$ and $b$ be any two points of $S^2-A$. Let $f:A\to S^2-\theset{a,b}$ be the inclusion.

The map $f$ satisfies the hypotheses of the Borsuk lemma, Lemma 62.2 (printed p. 382), except that its nullhomotopy has to be checked. The space $A$ is compact and $f$ is injective. Because $A$ is contractible there is a point $a_0\in A$ and a homotopy $H:A\times I\to A$ from the identity of $A$ to the constant map at $a_0$; composing $H$ with the inclusion of $A$ in $S^2-\theset{a,b}$ gives a homotopy from $f$ to the constant map at $a_0$ whose values all lie in $A\subseteq S^2-\theset{a,b}$. So $f$ is nullhomotopic.

The Borsuk lemma now gives that $a$ and $b$ lie in the same component of
$$
S^2-f(A)=S^2-A.
$$
The points $a,b\in S^2-A$ were arbitrary, so any two points of $S^2-A$ lie in a single component: the space $S^2-A$ is connected, that is, $A$ does not separate $S^2$.
:::
