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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.2, printed p. 190** (`tmp/sources/munkres-solutions-whitman.pdf`); the two inclusions are his.

Let $A_{\alpha}$ be a subspace of $X_{\alpha}$ for each $\alpha\in J$. By Lemma 16.1 (printed p. 89) the subspace topology that $\prod A_{\alpha}$ inherits from $\prod X_{\alpha}$ has as a basis the traces $B\cap\prod A_{\alpha}$ of the basis elements $B$ of the ambient space. It is enough to show that this basis coincides with the basis defining the box (respectively product) topology of the product of the subspaces, namely the sets $\prod V_{\alpha}$ with $V_{\alpha}$ open in $A_{\alpha}$ and, in the product case, $V_{\alpha}=A_{\alpha}$ for all but finitely many $\alpha$.

*Trace of an ambient basis element.* If $B=\prod U_{\alpha}$ is a box basis element of $\prod X_{\alpha}$, put $V_{\alpha}=U_{\alpha}\cap A_{\alpha}$, which is open in $A_{\alpha}$. Then for any point $x$,
$$
x\in B\cap\prod A_{\alpha}\iff \forall\alpha\ (x_{\alpha}\in U_{\alpha}\ \text{and}\ x_{\alpha}\in A_{\alpha})\iff x\in\prod V_{\alpha}.
$$
So $B\cap\prod A_{\alpha}=\prod V_{\alpha}$. If $B$ is a product basis element then $U_{\alpha}=X_{\alpha}$ for all but finitely many $\alpha$, and for those $\alpha$ one has $V_{\alpha}=X_{\alpha}\cap A_{\alpha}=A_{\alpha}$; so $\prod V_{\alpha}$ is a product basis element of $\prod A_{\alpha}$.

*Every basis element of the product of the subspaces is such a trace.* If $\prod V_{\alpha}$ is a box (respectively product) basis element of $\prod A_{\alpha}$, choose $U_{\alpha}$ open in $X_{\alpha}$ with $V_{\alpha}=U_{\alpha}\cap A_{\alpha}$, taking $U_{\alpha}=X_{\alpha}$ where $V_{\alpha}=A_{\alpha}$. Then $\prod U_{\alpha}$ is a box basis element of $\prod X_{\alpha}$, and it is a product basis element there when only finitely many $V_{\alpha}$ differ from $A_{\alpha}$; and the computation above gives $\prod V_{\alpha}=\prod U_{\alpha}\cap\prod A_{\alpha}$.

So the two bases coincide and $\prod A_{\alpha}$ carries the subspace topology in both the box and the product case.
:::
