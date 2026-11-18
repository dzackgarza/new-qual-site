---
schema: qual/card@1
id: E-RWKRJ
kind: problem
title: Continuous maps with continuous sections are quotient maps
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 2, printed p. 144, with the
    definition of quotient map printed there; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.2, PDF p. 27. A continuous section makes the
    map a quotient, since U = (p o f)^{-1}(U) = f^{-1}(p^{-1}(U)); a retraction is a
    quotient map because the inclusion is a continuous section of it. (tmp/sources/munkres-
    solutions-positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the same two arguments, neither of which needed
    repair. The one addition is that a retraction is regarded as a map onto its image, which is what
    puts the surjectivity of part (a) at its disposal; the subspace topology on that image is the
    book's. The statement was checked against Munkres, Topology (2000), Section 22 Exercise 2, printed
    p. 144, and the definition of a quotient map on printed p. 137.
---

::: {.exercise}

(a) Let $p: X \to Y$ be a continuous map.
Show that if there is a continuous map $f: Y \to X$ such that $p \circ f$ equals the identity map of $Y$, then $p$ is a quotient map.

(b) If $A \subset X$, a retraction of $X$ onto $A$ is a continuous map $r: X \to A$ such that $r(a) = a$ for each $a \in A$.
Show that a retraction is a quotient map.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.2, PDF p. 27** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs, and Whitman, printed p. 252, gives the same two arguments. The statement was checked against Munkres, *Topology* (2000), §22 Exercise 2, printed p. 144, with the definition of a quotient map printed on p. 137; the set $A$ of part (b) carries the subspace topology, that being the topology the exercise gives it. Throughout, $p^{-1}(U)=\theset{x\in X\mid p(x)\in U}$.

::: pf

::: {.pf-step #a}

(a) If $p\colon X\to Y$ is continuous and $f\colon Y\to X$ is continuous with $p\circ f=\mathrm{id}_{Y}$, then $p$ is a quotient map.

:::: pf-proof

Suppose $p$ and $f$ are as stated.

::: {.pf-step #surjective}

$p$ is surjective.

::: pf-proof

For $y\in Y$ one has $p(f(y))=y$, since $p\circ f$ is the identity of $Y$; so every $y$ lies in the image of $p$.

:::

:::

::: {.pf-step #open-iff}

For $U\subset Y$, $U$ is open in $Y$ if and only if $p^{-1}(U)$ is open in $X$.

::: pf-proof

If $U$ is open then $p^{-1}(U)$ is open, because $p$ is continuous. Conversely, suppose $p^{-1}(U)$ is open in $X$. Then
$$
U=\mathrm{id}_{Y}^{-1}(U)=(p\circ f)^{-1}(U)=f^{-1}\big(p^{-1}(U)\big),
$$
the middle equality because $p\circ f=\mathrm{id}_{Y}$, and $(p\circ f)^{-1}(U)=f^{-1}(p^{-1}(U))$ for composable maps; so $U$ is the preimage under the continuous map $f$ of the open set $p^{-1}(U)$, hence open in $Y$.

:::

:::

::: pf-step

(a) $p$ is a quotient map.

::: pf-proof

A quotient map is a surjective continuous map $p$ under which a set $U\subset Y$ is open exactly when $p^{-1}(U)$ is open (§22, printed p. 137). The map $p$ is continuous by hypothesis, surjective by step [](#surjective){.pf-ref}, and satisfies the openness condition by step [](#open-iff){.pf-ref}.

:::

:::

::::

:::

::: {.pf-step #b}

(b) A retraction $r\colon X\to A$ is a quotient map.

:::: pf-proof

Let $r\colon X\to A$ be a retraction, that is, $r$ is continuous and $r(a)=a$ for every $a\in A$, and regard it as a map onto $A$.

::: {.pf-step #inclusion}

The inclusion $i\colon A\to X$, $i(a)=a$, is continuous and $r\circ i=\mathrm{id}_{A}$.

::: pf-proof

$A$ carries the subspace topology, and the inclusion of a subspace is continuous (§18, printed p. 109). For $a\in A$ one has $r(i(a))=r(a)=a$, because $r$ is a retraction, so $r\circ i$ is the identity of $A$.

:::

:::

::: pf-step

(b) $r$, regarded as a map of $X$ onto $A$, is a quotient map.

::: pf-proof

The map $r$ is continuous, takes values in $A$, and satisfies $r(a)=a$ for $a\in A$; so, as a map onto $A$, it meets the hypothesis of part [](#a){.pf-ref} with $p=r$ and $f=i$, since $i$ is continuous and $r\circ i=\mathrm{id}_{A}$ by step [](#inclusion){.pf-ref}. Hence $r$ is a quotient map.

:::

:::

::::

:::

:::

:::
