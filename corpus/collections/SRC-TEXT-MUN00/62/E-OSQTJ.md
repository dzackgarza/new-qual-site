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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the Cornell argument, with the step that source compresses into a
    clause written out: the inclusion j: A -> S^2 - {a,b} is nullhomotopic because the identity of A is,
    the contracting homotopy being composed with the inclusion, whose values lie in A and therefore avoid
    a and b. That is what the Borsuk lemma needs --- its hypothesis is that f: A -> S^2 - a - b is
    nullhomotopic as a map into the punctured sphere, not merely that A is contractible --- and it is the
    point the card's earlier single sentence asserted without showing. The lemma is quoted in the book's
    own form, and the conclusion is drawn for arbitrary a, b in S^2 - A, which yields the connectedness
    of the complement and hence that A does not separate. Checked against Munkres, Topology (2000),
    Section 62 Exercise 2, printed p. 384.
---

::: {.exercise}

Let $A$ be a compact contractible subspace of $S^2$.
Show that $A$ does not separate $S^2$.
:::

::: {.solution}

The argument is problem (10) of **"MATH 4530 -- Topology. Practice Problems For Final solutions"**, the course solutions of Cornell's MATH 4530 (Fall 2010), printed p. 3 of the file, text at `tmp/sources/munkres-cornell-math4530-2010-practice-final-solutions.txt`: for arbitrary $a$ and $b$ in $S^{2}-A$ take $f$ the identity on $A$, apply the Borsuk lemma, and conclude that any two points of $S^{2}-A$ lie in one component. The step that source leaves as a clause --- that the inclusion $A\to S^{2}-\{a,b\}$ is nullhomotopic --- is written out here, since it is what the lemma needs and what the contractibility of $A$ supplies.

The statement was checked against Munkres, *Topology* (2000), §62 Exercise 2, with the Borsuk lemma (Lemma 62.2), the definition of a set separating a space on printed p. 381, the definition of contractibility in §51 and Theorem 18.2. Throughout, $A$ is a compact contractible subspace of $S^{2}$, so that $S^{2}-A$ is nonempty as soon as $A\neq S^{2}$, and $j\colon A\to S^{2}-\{a,b\}$ denotes the map $j(x)\coloneqq x$ for fixed points $a,b\in S^{2}-A$.

::: pf

::: {.pf-step #map}

$j\colon A\to S^{2}-\theset{a,b}$, $j(x)\coloneqq x$, is a continuous injective map of the compact space $A$.

::: pf-proof

Since $a,b\notin A$, every $x\in A$ satisfies $j(x)=x\in S^{2}-\theset{a,b}$, so $j$ takes its values in the stated codomain. It is the restriction of the identity of $S^{2}$ to the subspace $A$, hence continuous (Theorem 18.2(b)), and it is injective because it is the identity. The space $A$ is compact by hypothesis.

:::

:::

::: {.pf-step #contraction}

There are a point $c\in A$ and a homotopy $H\colon A\times I\to A$ with $H(x,0)=x$ and $H(x,1)=c$ for all $x\in A$.

::: pf-proof

$A$ is contractible, that is, its identity map is nullhomotopic (§51): nullhomotopic means homotopic to a constant map, so such an $H$ and such a $c$ exist.

:::

:::

::: {.pf-step #nullhomotopic}

$j$ is nullhomotopic as a map into $S^{2}-\theset{a,b}$.

::: pf-proof

Let $H$ and $c$ be as in step [](#contraction){.pf-ref} and let $\iota\colon A\to S^{2}-\theset{a,b}$ be the inclusion, which is $j$. Then
$$
H^{\prime}\coloneqq\iota\circ H\colon A\times I\to S^{2}-\theset{a,b}
$$
is continuous, being a composite of continuous maps (Theorem 18.2(c)), and it takes values in $S^{2}-\theset{a,b}$ because its values lie in $A$ and $a,b\notin A$. Moreover $H^{\prime}(x,0)=\iota(x)=j(x)$ and $H^{\prime}(x,1)=\iota(c)$, a constant. So $H^{\prime}$ is a homotopy from $j$ to the constant map at $c$, all of whose values avoid $a$ and $b$; that is exactly what nullhomotopy of $j$ as a map into the punctured sphere requires.

:::

:::

::: {.pf-step #borsuk}

For all $a,b\in S^{2}-A$ the points $a$ and $b$ lie in the same component of $S^{2}-A$.

::: pf-proof

The Borsuk lemma (Lemma 62.2) states that if $A$ is a compact space and $f\colon A\to S^{2}-\{a,b\}$ is continuous, injective and nullhomotopic, then $a$ and $b$ lie in the same component of $S^{2}-f(A)$. Steps [](#map){.pf-ref} and [](#nullhomotopic){.pf-ref} supply those three hypotheses for $f=j$, and $j(A)=A$; so $a$ and $b$ lie in the same component of $S^{2}-A$.

:::

:::

::: {.pf-step #connected}

$S^{2}-A$ is connected.

::: pf-proof

Let $p,q\in S^{2}-A$; by step [](#borsuk){.pf-ref} they lie in the same component of $S^{2}-A$, so $S^{2}-A$ has exactly one component. The components of a space are nonempty and cover it, so a space with one component is connected. Since $a\in S^{2}-A$ for the $a$ fixed in step [](#map){.pf-ref}, the set is nonempty as well.

:::

:::

::: pf-step

Therefore $A$ does not separate $S^{2}$.

::: pf-proof

$S^{2}$ is connected, and by definition a subset $A$ of a connected space separates it when the complement is *not* connected (printed p. 381). By step [](#connected){.pf-ref} the complement $S^{2}-A$ is connected, so $A$ does not separate $S^{2}$.

:::

:::

:::

:::
