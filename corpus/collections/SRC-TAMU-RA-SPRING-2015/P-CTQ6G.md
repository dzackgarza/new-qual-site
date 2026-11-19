---
schema: qual/card@1
id: P-CTQ6G
kind: problem
title: Isolated points iff the complement is not dense; countable complete metric spaces have dense isolated points
classification:
  areas:
    - real-analysis
  topics:
    - Metric Spaces
    - Baire Category
relations: []
review: draft
audit:
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Read against the exam retained at assets/attachments/j15.pdf (TAMU real-analysis
      qualifying exam, Spring 2015), problem 8, where both parts appear with the card's
      wording, including the definition of isolated as "{y} is both open and closed in Y".
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Rewritten into numbered steps from the card's own prose; no retained solution set for
      this exam covers the problem. Two gaps in the prose are filled. Part (ii) asserted
      that "O itself is a Baire space" because X is complete, which is true but needs the
      reason, namely that an open subset of a Baire space is Baire and complete metric
      spaces are Baire; this is now step 4. The prose then intersected the complements O
      minus {y} over all y in O, which is legitimate only because X, and hence O, is
      countable; the steps instead apply the Baire property to the countable cover of O by
      its singleton subsets, which gives a point isolated in O and then, since O is open in
      X, a point isolated in X inside O, contradicting the choice of O.
---

::: {.problem}
(i) A point $y$ in a metric space $Y$ is isolated if the set $\{y\}$ is both open and closed in $Y$.
Prove that $y\in Y$ is isolated if and only if the complement $\{y\}^c$ is not dense in $Y$.

(ii) Let $X$ be a countable nonempty complete metric space.
Prove that the set of isolated points is dense in $X$.
:::

::: {.solution}

The problem is problem 8 of the TAMU real-analysis qualifying exam, Spring 2015, retained at
`assets/attachments/j15.pdf`. No retained solution set covers it; the argument below is the
card's own, restructured as numbered steps.

Throughout $Y$ is a metric space, and a set is dense when its closure is the whole space,
equivalently when it meets every nonempty open set.

::: pf

::: {.pf-step #singletons-closed}

In a metric space, every singleton is closed.

::: pf-proof

If $z\ne y$ then the ball about $z$ of radius $d(y,z)/2$ does not contain $y$, so the
complement of $\theset{y}$ is open and $\theset{y}$ is closed. Hence in the definition the
condition on $\theset{y}$ that carries content is its openness.

:::

:::

::: {.pf-step #forward}

If $\theset{y}$ is open then $\theset{y}^{c}$ is not dense.

::: pf-proof

$\theset{y}$ is a nonempty open set, and $\theset{y}\cap\theset{y}^{c}=\emptyset$, so
$\theset{y}^{c}$ misses a nonempty open set and is not dense.

:::

:::

::: {.pf-step #converse}

If $\theset{y}^{c}$ is not dense then $\theset{y}$ is open.

::: pf-proof

By the definition of density there is a nonempty open set $O$ with
$O\cap\theset{y}^{c}=\emptyset$. Then $O\subseteq\theset{y}$; as $O$ is nonempty, $O$ has an
element, which must be $y$, so $O=\theset{y}$. Hence $\theset{y}$ is open, and closed by
step [](#singletons-closed){.pf-ref}.

:::

:::

::: {.pf-step #setup}

For (ii), let $I$ be the set of isolated points of $X$ and suppose $I$ is not dense; then
there is a nonempty open set $O\subseteq X$ with $O\cap I=\emptyset$, and $O$ is countable.

::: pf-proof

By the definition of density and step [](#converse){.pf-ref}'s criterion, failure of density
of $I$ gives a nonempty open $O$ disjoint from $I$. As $O\subseteq X$ and $X$ is countable,
$O$ is countable.

:::

:::

::: {.pf-step #baire}

$O$, with the induced metric, is a nonempty Baire space: it is not the union of countably
many closed subsets each with empty interior in $O$.

::: pf-proof

A complete metric space is a Baire space (Baire category theorem), and an open subset of a
Baire space, with the induced metric, is again a Baire space; $O$ is open in the complete
space $X$, so $O$ is Baire. It is nonempty by step [](#setup){.pf-ref}.

:::

:::

::: {.pf-step #isolated-in-O}

Some point of $O$ is an isolated point of $X$.

::: pf-proof

$O=\bigcup_{y\in O}\theset{y}$ is expressed as a countable union by step [](#setup){.pf-ref},
and each $\theset{y}$ is closed in $O$ since it is closed in $X$ (step
[](#singletons-closed){.pf-ref}). By step [](#baire){.pf-ref} some $\theset{y}$ with $y\in O$
does not have empty interior in $O$; so there is a nonempty set $V$, open in $O$, with
$V\subseteq\theset{y}$, and then $V=\theset{y}$ because $V$ has an element. As $O$ is open in
$X$, the set $V$ is open in $X$, so $\theset{y}$ is open in $X$ and $y\in I$.

:::

:::

::: {.pf-step #dense}

The set of isolated points of $X$ is dense in $X$.

::: pf-proof

Step [](#isolated-in-O){.pf-ref} produces a point of $I\cap O$, contradicting
$O\cap I=\emptyset$ from step [](#setup){.pf-ref}. So the assumption that $I$ is not dense is
false.

:::

:::

:::

:::
