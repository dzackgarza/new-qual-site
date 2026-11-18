---
schema: qual/card@1
id: E-R3NOE
kind: problem
title: Products of subspaces are subspaces
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 2, printed p. 118, whose content is
    Theorem 19.3 on printed p. 115, with Lemma 16.1; the stored statement states the
    theorem.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.2, printed p. 190.
    Both inclusions are his: the trace of an ambient box or product basis element is the
    corresponding basis element of the product of the subspaces, and conversely every basis
    element of that product arises as such a trace. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

Prove Theorem 19.3: let $A_\alpha$ be a subspace of $X_\alpha$, for each $\alpha \in J$.
Then $\prod A_\alpha$ is a subspace of $\prod X_\alpha$ if both products are given the box topology, or if both products are given the product topology.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.2, printed p. 190** (`tmp/sources/munkres-solutions-whitman.pdf`); the two inclusions of bases are his, kept as separate steps because the theorem is exactly their coincidence.

Let $A_{\alpha}$ be a subspace of $X_{\alpha}$ for each $\alpha\in J$, and write $\prod A_{\alpha}$ for the product of the subspaces. The subspace topology that $\prod A_{\alpha}$ inherits from $\prod X_{\alpha}$ has as a basis the traces $B\cap\prod A_{\alpha}$ of the basis elements $B$ of the ambient space (Lemma 16.1, printed p. 89).

::: pf

::: {.pf-step #trace}
If $B=\prod U_{\alpha}$ is a basis element of $\prod X_{\alpha}$ in the box (respectively product) topology, then $B\cap\prod A_{\alpha}=\prod(U_{\alpha}\cap A_{\alpha})$, and that set is a basis element of $\prod A_{\alpha}$ in the corresponding topology.

::: pf-proof
For a point $x$, one has $x\in B\cap\prod A_{\alpha}$ exactly when $x_{\alpha}\in U_{\alpha}$ and $x_{\alpha}\in A_{\alpha}$ for every $\alpha$, which is $x\in\prod(U_{\alpha}\cap A_{\alpha})$. Each $V_{\alpha}=U_{\alpha}\cap A_{\alpha}$ is open in $A_{\alpha}$. In the product case $U_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$, and for those $\alpha$ one gets $V_{\alpha}=X_{\alpha}\cap A_{\alpha}=A_{\alpha}$, so $\prod V_{\alpha}$ is a product basis element of $\prod A_{\alpha}$.
:::

:::

::: {.pf-step #cover}
Every basis element of $\prod A_{\alpha}$ is of that form.

::: pf-proof
Let $\prod V_{\alpha}$ be a box (respectively product) basis element of $\prod A_{\alpha}$. For each $\alpha$ choose $U_{\alpha}$ open in $X_{\alpha}$ with $V_{\alpha}=U_{\alpha}\cap A_{\alpha}$, taking $U_{\alpha}=X_{\alpha}$ in the coordinates where $V_{\alpha}=A_{\alpha}$; such a choice is possible because $V_{\alpha}$ is open in $A_{\alpha}$. Then $\prod U_{\alpha}$ is a box basis element of $\prod X_{\alpha}$, and it is a product basis element when only finitely many $V_{\alpha}$ differ from $A_{\alpha}$; by step [](#trace){.pf-ref} its trace is $\prod V_{\alpha}$.
:::

:::

::: {.pf-qed}
The basis of the subspace topology on $\prod A_{\alpha}$ is, by steps [](#trace){.pf-ref} and [](#cover){.pf-ref}, exactly the basis of the box topology of $\prod A_{\alpha}$ when both products carry the box topology, and exactly the basis of the product topology of $\prod A_{\alpha}$ when both carry the product topology. Two topologies with a common basis coincide, so the theorem holds in both cases.
:::

:::

:::
