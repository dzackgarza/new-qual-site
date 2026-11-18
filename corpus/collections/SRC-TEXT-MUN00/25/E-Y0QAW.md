---
schema: qual/card@1
id: E-Y0QAW
kind: problem
title: Quotients of locally connected spaces are locally connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 8, printed p. 162, with Theorem 25.3
    and the hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.8, PDF p. 10. The preimage of a component of an
    open set is a union of components of the preimage of the open set, hence open, hence the
    component is open in the quotient. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps along the book's hint; checked that the image of a
    component of the open preimage lies in the component C of U, that the preimage of C is a
    union of such components, that those are open since X is locally connected (Theorem
    25.3), and that C is open because p is a quotient map. positron0802, Chapter 3 Exercise
    25.8, PDF p. 10. The printed statement needed no repair.
---

::: {.exercise}

Let $p: X \to Y$ be a quotient map.
Show that if $X$ is locally connected, then $Y$ is locally connected.
[Hint: If $C$ is a component of the open set $U$ of $Y$, show that $p^{-1}(C)$ is a union of components of $p^{-1}(U)$.]
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.8, PDF p. 10** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument follows the book's hint.

Recall (Theorem 25.3) that a space is locally connected exactly when the components of each of its open sets are open.

::: pf

::: {.pf-step #trace}
If $D$ is a component of $p^{-1}(U)$ and $D$ meets $p^{-1}(C)$, then $D\subset p^{-1}(C)$.

::: pf-proof
$p(D)$ is connected, being a continuous image of the connected set $D$, and it is contained in $p\big(p^{-1}(U)\big)\subset U$. It meets $C$, because $D$ meets $p^{-1}(C)$. As $C$ is a component of $U$, hence a maximal connected subset of $U$, a connected subset of $U$ meeting it lies in it: $p(D)\subset C$. Therefore $D\subset p^{-1}\big(p(D)\big)\subset p^{-1}(C)$.
:::

:::

::: {.pf-step #union}
$p^{-1}(C)$ is a union of components of $p^{-1}(U)$.

::: pf-proof
Let $x\in p^{-1}(C)\subset p^{-1}(U)$. The component $D$ of $p^{-1}(U)$ containing $x$ meets $p^{-1}(C)$ at $x$, so $D\subset p^{-1}(C)$ by step [](#trace){.pf-ref}. Every point of $p^{-1}(C)$ thus lies in a component of $p^{-1}(U)$ contained in $p^{-1}(C)$, and conversely each such component lies in $p^{-1}(C)$; so $p^{-1}(C)$ is the union of those components.
:::

:::

::: {.pf-step #open-preimage}
$p^{-1}(C)$ is open in $X$.

::: pf-proof
$U$ is open in $Y$, so $p^{-1}(U)$ is open in $X$ because $p$ is continuous. The components of the open set $p^{-1}(U)$ are therefore open in $X$, since $X$ is locally connected (Theorem 25.3), and $p^{-1}(C)$ is a union of some of them by step [](#union){.pf-ref}; a union of open sets is open.
:::

:::

::: {.pf-step #open-image}
$C$ is open in $Y$.

::: pf-proof
$p^{-1}(C)$ is open in $X$ by step [](#open-preimage){.pf-ref}, and $C\subset Y$ satisfies $C=p\big(p^{-1}(C)\big)$ because $p$ is surjective. As $p$ is a quotient map, a subset of $Y$ whose preimage is open is itself open, so $C$ is open.
:::

:::

::: {.pf-step}
$Y$ is locally connected.

::: pf-proof
Let $U$ be open in $Y$. Step [](#open-image){.pf-ref} shows that each component $C$ of $U$ is open, and $U$ was arbitrary, so by Theorem 25.3 the space $Y$ is locally connected.
:::

:::

:::
:::
