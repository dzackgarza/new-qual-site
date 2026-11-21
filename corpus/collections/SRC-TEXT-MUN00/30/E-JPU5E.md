---
schema: qual/card@1
id: E-JPU5E
kind: problem
title: Lindelofness and separability pass to continuous images
classification:
  areas:
  - topology
  topics:
  - Countability
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 30 Exercise 11, printed p. 31
    (tmp/sources/munkres-solutions-anadeore.pdf), checked against Munkres, Topology (2000),
    Section 30 Exercise 11, printed p. 194, and Theorem 18.1 for the preimage form of continuity.
    Doug's World, "Munkres - Topology - Chapter 4 Solutions", Problem 30.11, printed p. 3, proves
    the same two implications. Corrections: Orellana closes the separable half with the garbled
    display "f(D) = f(D) == f(X)", which asserts the conclusion rather than deriving it; the card
    derives it from an arbitrary nonempty open W of f(X), whose preimage is nonempty open in X and
    therefore meets D. Her Lindelof half also passes through a cover of f(X) by sets "open in X";
    the card uses a cover of f(X) by sets open in f(X) and their preimages under f, which are open
    in X, and then uses surjectivity of f onto f(X).
---

::: {.exercise}

Let $f: X \to Y$ be continuous.
Show that if $X$ is Lindelöf, or if $X$ has a countable dense subset, then $f(X)$ satisfies the same condition.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the two conditions treated as the two independent steps they are.

Let $f:X\to Y$ be continuous and let $Z=f(X)$ carry the subspace topology; then $f$ is a continuous surjection onto $Z$.

::: pf

::: {.pf-step #lindelof}
If $X$ is Lindelöf then $Z$ is Lindelöf.

::: pf-proof
Let $\theset{U_{i}}_{i\in I}$ be a cover of $Z$ by sets open in $Z$. Each $f^{-1}(U_{i})$ is open in $X$ by continuity, and the family $\theset{f^{-1}(U_{i})}$ covers $X$: for $x\in X$ the point $f(x)$ lies in some $U_{i}$, so $x\in f^{-1}(U_{i})$. Lindelöfness gives a countable subfamily $\theset{f^{-1}(U_{i_{k}})}_{k\ge1}$ covering $X$. Since $f$ maps $X$ onto $Z$, every $z\in Z$ equals $f(x)$ for some $x\in X$, and $x\in f^{-1}(U_{i_{k}})$ gives $z\in U_{i_{k}}$; so $\theset{U_{i_{k}}}$ covers $Z$. Hence every open cover of $Z$ has a countable subcover.
:::

:::

::: {.pf-step #separable}
If $X$ has a countable dense subset $D$, then $f(D)$ is a countable dense subset of $Z$.

::: pf-proof
$f(D)$ is countable, being the image of a countable set. For density let $W$ be a nonempty open subset of $Z$. Then $f^{-1}(W)$ is open in $X$ by continuity, and it is nonempty: $W$ contains some $z=f(x)$ with $x\in X$. As $D$ is dense there is $d\in D\cap f^{-1}(W)$, and then $f(d)\in W\cap f(D)$. So $f(D)$ meets every nonempty open set of $Z$.
:::

:::

::: {.pf-qed}
By steps [](#lindelof){.pf-ref} and [](#separable){.pf-ref} the continuous image $f(X)$ is Lindelöf when $X$ is, and has a countable dense subset when $X$ does.
:::

:::

:::
