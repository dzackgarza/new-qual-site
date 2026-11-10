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
---

::: {.exercise}

Prove Theorem 19.2: suppose the topology on each space $X_\alpha$ is given by a basis $\mathcal{B}_\alpha$.
The collection of all sets of the form $\prod_{\alpha \in J} B_\alpha$, where $B_\alpha \in \mathcal{B}_\alpha$ for each $\alpha$, serves as a basis for the box topology on $\prod_{\alpha \in J} X_\alpha$; and the collection of all sets of the same form, where $B_\alpha \in \mathcal{B}_\alpha$ for finitely many indices $\alpha$ and $B_\alpha = X_\alpha$ for all the remaining indices, serves as a basis for the product topology.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.1, printed p. 189** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument is his. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 19.1, PDF p. 14, checks the two basis conditions directly instead.

Let $\mathcal{B}_{\alpha}$ be a basis for the topology of $X_{\alpha}$, and let
$$
\mathcal{C}=\Big\{\textstyle\prod_{\alpha\in J}B_{\alpha}\ \mid\ B_{\alpha}\in\mathcal{B}_{\alpha}\Big\},
$$
with the extra requirement $B_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$ in the case of the product topology.

*$\mathcal{C}$ consists of open sets.* Each $B_{\alpha}$ is open in $X_{\alpha}$, so $\prod B_{\alpha}$ is a basis element of the box topology by definition, and in the product case it is a basis element of the product topology because $B_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$ (Theorem 19.1, printed p. 114). So every member of $\mathcal{C}$ is open.

*$\mathcal{C}$ is a basis for the topology.* Let $U$ be open in the box (respectively product) topology and let $x\in U$; we find $C\in\mathcal{C}$ with $x\in C\subset U$. By the definition of the box (respectively product) topology there is a basis element $\prod U_{\alpha}$ with
$$
x\in\prod U_{\alpha}\subset U,
$$
where each $U_{\alpha}$ is open in $X_{\alpha}$ and, in the product case, $U_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$. Since $\mathcal{B}_{\alpha}$ is a basis, for each $\alpha$ there is $B_{\alpha}\in\mathcal{B}_{\alpha}$ with $x_{\alpha}\in B_{\alpha}\subset U_{\alpha}$; when $U_{\alpha}=X_{\alpha}$ take $B_{\alpha}=X_{\alpha}$. Then $C=\prod B_{\alpha}$ lies in $\mathcal{C}$ (in the product case $B_{\alpha}=X_{\alpha}$ wherever $U_{\alpha}=X_{\alpha}$, hence for all but finitely many $\alpha$), and
$$
x\in C=\prod B_{\alpha}\subset\prod U_{\alpha}\subset U .
$$
By Lemma 13.2 (printed p. 80) a collection of open sets through which every neighbourhood of every point can be shrunk is a basis for the topology. Hence $\mathcal{C}$ is a basis for the box topology, respectively for the product topology.
:::
