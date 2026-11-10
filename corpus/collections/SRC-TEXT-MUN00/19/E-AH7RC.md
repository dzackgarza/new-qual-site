---
schema: qual/card@1
id: E-AH7RC
kind: problem
title: Convergence in products via coordinate convergence
classification:
  areas:
  - topology
  topics:
  - Convergence
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 6, printed p. 118, with the
    definitions of the box and product topologies and of convergence; both questions of the
    stored statement are printed there.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.6, printed p. 193.
    His are both directions in the product topology, the second using the finiteness of the
    set of coordinates in which a basis element differs from the whole space, and the
    counterexample in the box topology with x_ij = 1 for j <= i and 1/(j-i) otherwise, whose
    coordinate sequences tend to 0 while no term of the sequence lies in the box
    (-1,1)^omega. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Let $\mathbf{x}_1, \mathbf{x}_2, \ldots$ be a sequence of the points of the product space $\prod X_\alpha$.
Show that this sequence converges to the point $\mathbf{x}$ if and only if the sequence $\pi_\alpha(\mathbf{x}_1), \pi_\alpha(\mathbf{x}_2), \ldots$ converges to $\pi_\alpha(\mathbf{x})$ for each $\alpha$.
Is this fact true if one uses the box topology instead of the product topology?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.6, printed p. 193** (`tmp/sources/munkres-solutions-whitman.pdf`); both directions of the product statement and the box counterexample are his.

**In the product topology, $\mathbf{x}_{n}\to\mathbf{x}$ if and only if $\pi_{\alpha}(\mathbf{x}_{n})\to\pi_{\alpha}(\mathbf{x})$ for every $\alpha$.**

*Only if.* Let $\beta\in J$ and let $U$ be a neighbourhood of $\pi_{\beta}(\mathbf{x})$ in $X_{\beta}$. Put $B_{\alpha}=U$ for $\alpha=\beta$ and $B_{\alpha}=X_{\alpha}$ otherwise; then $B=\prod B_{\alpha}$ is a basis element, in the box topology as well as the product topology, containing $\mathbf{x}$. So there is $N$ with $\mathbf{x}_{n}\in B$ for $n\ge N$, and then $\pi_{\beta}(\mathbf{x}_{n})\in B_{\beta}=U$ for those $n$.

*If.* Let $U$ be a neighbourhood of $\mathbf{x}$ and choose a basis element $\prod U_{\alpha}\subset U$ with $\mathbf{x}\in\prod U_{\alpha}$. In the product topology $U_{\alpha}=X_{\alpha}$ for $\alpha$ outside a finite set $I$, and for each $\alpha\in I$ the set $U_{\alpha}$ is a neighbourhood of $\pi_{\alpha}(\mathbf{x})$, so there is $N_{\alpha}$ with $\pi_{\alpha}(\mathbf{x}_{n})\in U_{\alpha}$ for $n\ge N_{\alpha}$. As $I$ is finite, $N=\max_{\alpha\in I}N_{\alpha}$ exists; for $n\ge N$ and every $\alpha$ then $\pi_{\alpha}(\mathbf{x}_{n})\in U_{\alpha}$ (for $\alpha\notin I$ trivially), so $\mathbf{x}_{n}\in\prod U_{\alpha}\subset U$.

**The statement fails for the box topology.** In $\RR^{\omega}$ with the box topology put $x_{ij}=1$ for $j\le i$ and $x_{ij}=1/(j-i)$ for $j>i$, and let $\mathbf{x}_{i}$ be the sequence $(x_{i1},x_{i2},\dots)$. For fixed $j$ the real sequence $(x_{ij})_{i}$ is eventually $1/(j-i)$, which tends to $0$; so $\pi_{j}(\mathbf{x}_{i})\to0$ for every $j$. But $\mathbf{x}_{i}$ does not converge to $\mathbf{0}$: the box-open set $U=\prod_{j}(-1,1)$ contains $\mathbf{0}$, yet $\pi_{i}(\mathbf{x}_{i})=x_{ii}=1\notin(-1,1)$, so $\mathbf{x}_{i}\notin U$ for every $i$. The point of failure is the step taking $\max_{\alpha\in I}N_{\alpha}$, which needs $I$ finite.
:::
