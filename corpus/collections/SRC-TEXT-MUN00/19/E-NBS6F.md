---
schema: qual/card@1
id: E-NBS6F
kind: problem
title: Products of Hausdorff spaces in the box and product topologies
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 3, printed p. 118, whose content is
    Theorem 19.4 on printed p. 116; the stored statement states the theorem.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.3, printed p. 191.
    The proof is his: separate the coordinates in one factor where the points differ and
    take the whole of the other factors, which is a basis element of both the box and the
    product topology. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Prove Theorem 19.4: if each space $X_\alpha$ is a Hausdorff space, then $\prod X_\alpha$ is a Hausdorff space in both the box and product topologies.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.3, printed p. 191** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof is his.

Let each $X_{\alpha}$ be Hausdorff and let $x\ne y$ in $\prod X_{\alpha}$. Then $x_{\beta}\ne y_{\beta}$ for some $\beta$, and since $X_{\beta}$ is Hausdorff there are disjoint open sets $W_{x}\ni x_{\beta}$ and $W_{y}\ni y_{\beta}$.

Define, for each $\alpha$,
$$
U_{\alpha}=\begin{cases}W_{x},&\alpha=\beta,\\ X_{\alpha},&\alpha\ne\beta,\end{cases}
\qquad
V_{\alpha}=\begin{cases}W_{y},&\alpha=\beta,\\ X_{\alpha},&\alpha\ne\beta.\end{cases}
$$
The sets $U=\prod U_{\alpha}$ and $V=\prod V_{\alpha}$ are basis elements of the product topology — and hence also of the box topology, which has more open sets — because each $U_{\alpha},V_{\alpha}$ is open and only at $\alpha=\beta$ does either differ from $X_{\alpha}$. Clearly $x\in U$ and $y\in V$.

Finally $U\cap V=\varnothing$: a point $z$ of both would satisfy $z_{\beta}\in U_{\beta}=W_{x}$ and $z_{\beta}\in V_{\beta}=W_{y}$, contradicting $W_{x}\cap W_{y}=\varnothing$. So $\prod X_{\alpha}$ is Hausdorff in both topologies.
:::
