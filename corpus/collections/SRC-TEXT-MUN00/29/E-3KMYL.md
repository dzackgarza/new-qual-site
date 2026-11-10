---
schema: qual/card@1
id: E-3KMYL
kind: problem
title: Local compactness of products
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 2, printed p. 186, with Tychonoff's
    theorem and the projections of §19; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.2, PDF pp. 21-22. Local compactness of a
    product forces every factor outside a finite set to be compact, through projections of a
    compact neighbourhood, and the converse assembles compact factors with compact
    neighbourhoods. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $\theset{X_\alpha}$ be an indexed family of nonempty spaces.

(a) Show that if $\prod X_\alpha$ is locally compact, then each $X_\alpha$ is locally compact and $X_\alpha$ is compact for all but finitely many values of $\alpha$.

(b) Prove the converse, assuming the Tychonoff theorem.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.2, PDF pp. 21--22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both directions are theirs.

(a) *If $\prod X_{\alpha}$ is locally compact then all but finitely many $X_{\alpha}$ are compact and the rest are locally compact.* Let $\mathbf{x}$ lie in a compact $C$ containing a neighbourhood of $\mathbf{x}$; that neighbourhood contains a product basis element $U=\prod U_{\alpha}$, with $U_{\alpha}=X_{\alpha}$ off a finite set $\{\alpha_{1},\dots,\alpha_{n}\}$. For $\beta$ outside that set, $\pi_{\beta}(C)$ is compact and contains $\pi_{\beta}(U)=X_{\beta}$; so $X_{\beta}$ is compact. For $\beta=\alpha_{i}$ and $x\in X_{\alpha_{i}}$, choose $\mathbf{x}$ with that coordinate and use the compact set $\pi_{\alpha_{i}}(C)$, which contains the neighbourhood $\pi_{\alpha_{i}}(U)$ of $x$: so $X_{\alpha_{i}}$ is locally compact.

(b) Conversely let each $X_{\alpha}$ be locally compact, all but finitely many compact, and let $\mathbf{x}\in\prod X_{\alpha}$. Choose a compact $C_{\alpha}$ containing a neighbourhood $U_{\alpha}$ of $x_{\alpha}$, taking $C_{\alpha}=U_{\alpha}=X_{\alpha}$ off a finite set. Then $\prod C_{\alpha}$ is compact (Tychonoff) and contains the neighbourhood $\prod U_{\alpha}$ of $\mathbf{x}$, so the product is locally compact.
:::
