---
schema: qual/card@1
id: E-DMMQW
kind: problem
title: Basis theorem for the box and product topologies
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Bases
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 1, printed p. 118, whose content is
    Theorem 19.2 on printed p. 115, with Theorem 19.1 and Lemma 13.2; the stored statement
    is the printed request and states the theorem.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.1, printed p. 189.
    The content is his: the products of basis elements are open in the box and product
    topologies, and through every point of an open set one can shrink a basis element of the
    space into the given basis element in each coordinate, so Lemma 13.2 applies.
    positron0802 PDF p. 14 checks the two basis conditions directly instead.
    (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked Theorem 19.2 as Munkres states it: that each
    product of basis elements is open in the box topology (and, with all but finitely many
    factors equal to X_alpha, in the product topology), and that every open set contains
    such a product through each of its points, which is the hypothesis of Lemma 13.2.
    Whitman, Exercise 19.1, printed p. 189. The printed theorem needed no repair.
---

::: {.exercise}

Prove Theorem 19.2: suppose the topology on each space $X_\alpha$ is given by a basis $\mathcal{B}_\alpha$.
The collection of all sets of the form $\prod_{\alpha \in J} B_\alpha$, where $B_\alpha \in \mathcal{B}_\alpha$ for each $\alpha$, serves as a basis for the box topology on $\prod_{\alpha \in J} X_\alpha$; and the collection of all sets of the same form, where $B_\alpha \in \mathcal{B}_\alpha$ for finitely many indices $\alpha$ and $B_\alpha = X_\alpha$ for all the remaining indices, serves as a basis for the product topology.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.1, printed p. 189** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument is his. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 19.1, PDF p. 14, checks the two basis conditions directly instead.

Let $\mathcal{B}_{\alpha}$ be a basis for the topology of $X_{\alpha}$, and let
$$
\mathcal{C}=\Big\{\prod_{\alpha\in J}B_{\alpha}\ \mid\ B_{\alpha}\in\mathcal{B}_{\alpha}\Big\},
$$
with the extra requirement $B_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$ in the product case.

::: pf

::: {.pf-step #open}
Every member of $\mathcal{C}$ is open in the box topology, and in the product topology under the extra requirement.

::: pf-proof
Each $B_{\alpha}$ is a basis element of $X_{\alpha}$, hence open there, so $\prod_{\alpha\in J}B_{\alpha}$ is a basis element of the box topology by its definition and is open. In the case of the product topology the additional hypothesis $B_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$ makes $\prod B_{\alpha}$ a basis element of the product topology by Theorem 19.1, so it is open there as well.
:::

:::

::: {.pf-step #shrink}
Let $U$ be open in the box topology (respectively in the product topology) and let $x\in U$. Then some $C\in\mathcal{C}$ satisfies $x\in C\subset U$, with $C$ formed from the corresponding class of basis elements.

::: pf-proof
By the definition of the box topology there is a set $\prod_{\alpha\in J}U_{\alpha}$ with all $U_{\alpha}$ open in $X_{\alpha}$ and $x\in\prod U_{\alpha}\subset U$; in the product topology such a set can be chosen with $U_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$. For each $\alpha$, since $\mathcal{B}_{\alpha}$ is a basis and $x_{\alpha}\in U_{\alpha}$, there is $B_{\alpha}\in\mathcal{B}_{\alpha}$ with $x_{\alpha}\in B_{\alpha}\subset U_{\alpha}$. Then $C=\prod_{\alpha\in J}B_{\alpha}$ contains $x$ and is contained in $\prod U_{\alpha}\subset U$. In the product case $B_{\alpha}\subset U_{\alpha}=X_{\alpha}$ gives $B_{\alpha}=X_{\alpha}$ wherever $U_{\alpha}=X_{\alpha}$, so $B_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$ and $C\in\mathcal{C}$ in the sense of the product topology.
:::

:::

::: {.pf-step}
$\mathcal{C}$ is a basis for the box topology, and with the extra requirement for the product topology.

::: pf-proof
Lemma 13.2 says that a collection $\mathcal{C}$ of open sets such that every neighbourhood of every point contains a member of $\mathcal{C}$ through the point is a basis for the topology. Step [](#open){.pf-ref} gives the openness, and step [](#shrink){.pf-ref} gives the shrinking, in each of the two topologies separately.
:::

:::

:::
:::
