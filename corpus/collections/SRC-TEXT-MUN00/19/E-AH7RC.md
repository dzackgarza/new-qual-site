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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked both directions for the product topology
    (the one-factor basis element for the easy direction, the finite index set and max of
    the N_alpha for the other) and Whitman's box counterexample, with the array x_in = 1 for
    n <= i and 1/(n-i) for n > i read with i the coordinate and n the sequence index. Card
    repair: the earlier prose had the two indices transposed, which made the coordinate
    sequences eventually 1 instead of eventually 1/(n-i). Whitman, Exercise 19.6, printed p.
    193. The printed statement needed no repair.
---

::: {.exercise}

Let $\mathbf{x}_1, \mathbf{x}_2, \ldots$ be a sequence of the points of the product space $\prod X_\alpha$.
Show that this sequence converges to the point $\mathbf{x}$ if and only if the sequence $\pi_\alpha(\mathbf{x}_1), \pi_\alpha(\mathbf{x}_2), \ldots$ converges to $\pi_\alpha(\mathbf{x})$ for each $\alpha$.
Is this fact true if one uses the box topology instead of the product topology?
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.6, printed p. 193** (`tmp/sources/munkres-solutions-whitman.pdf`); both directions of the product statement and the box counterexample are his. Card repair: his array $x_{ij}$ is indexed with $i$ the coordinate and $j$ the position in the sequence, and the statement below says so; an earlier version of this card read the two indices the other way round, which falsifies the convergence of the coordinate sequences.

Throughout, $(\mathbf{x}_{n})$ is a sequence of points of $\prod_{\alpha\in J}X_{\alpha}$ and $\pi_{\alpha}$ is the projection to $X_{\alpha}$.

::: pf

::: {.pf-step #only-if}
If $\mathbf{x}_{n}\to\mathbf{x}$ in the box topology — hence also in the product topology — then $\pi_{\alpha}(\mathbf{x}_{n})\to\pi_{\alpha}(\mathbf{x})$ for every $\alpha$.

::: pf-proof
Fix $\beta\in J$ and let $U$ be a neighbourhood of $\pi_{\beta}(\mathbf{x})$ in $X_{\beta}$. Put $B_{\alpha}=U$ for $\alpha=\beta$ and $B_{\alpha}=X_{\alpha}$ otherwise, and $B=\prod_{\alpha\in J}B_{\alpha}$; then $B$ is a basis element of the box topology and of the product topology, since $B_{\alpha}\ne X_{\alpha}$ for at most one $\alpha$, and $\mathbf{x}\in B$. So $B$ is a neighbourhood of $\mathbf{x}$ and there is $N$ with $\mathbf{x}_{n}\in B$ for all $n\ge N$. For such $n$, $\pi_{\beta}(\mathbf{x}_{n})\in B_{\beta}=U$. As $U$ was an arbitrary neighbourhood, $\pi_{\beta}(\mathbf{x}_{n})\to\pi_{\beta}(\mathbf{x})$.
:::

:::

::: {.pf-step #if}
If $\pi_{\alpha}(\mathbf{x}_{n})\to\pi_{\alpha}(\mathbf{x})$ for every $\alpha$, then $\mathbf{x}_{n}\to\mathbf{x}$ in the product topology.

::: pf-proof
Let $U$ be a neighbourhood of $\mathbf{x}$ and choose a basis element $B=\prod_{\alpha\in J}U_{\alpha}$ of the product topology with $\mathbf{x}\in B\subset U$. Here each $U_{\alpha}$ is open in $X_{\alpha}$ and $U_{\alpha}=X_{\alpha}$ for all $\alpha$ outside a finite set $I\subset J$. For $\alpha\in I$ the set $U_{\alpha}$ is a neighbourhood of $\pi_{\alpha}(\mathbf{x})$, so there is $N_{\alpha}$ with $\pi_{\alpha}(\mathbf{x}_{n})\in U_{\alpha}$ for all $n\ge N_{\alpha}$. Since $I$ is finite, $N=\max_{\alpha\in I}N_{\alpha}$ exists, and for $n\ge N$ and every $\alpha$ one has $\pi_{\alpha}(\mathbf{x}_{n})\in U_{\alpha}$, trivially for $\alpha\notin I$ because $U_{\alpha}=X_{\alpha}$. Hence $\mathbf{x}_{n}\in B\subset U$ for $n\ge N$, and $\mathbf{x}_{n}\to\mathbf{x}$.
:::

:::

::: {.pf-step #box-fails}
The statement fails for the box topology: in $\RR^{\omega}$ with the box topology the sequence whose $n$-th term is $\mathbf{x}_{n}=(\pi_{i}(\mathbf{x}_{n}))_{i}$ with $\pi_{i}(\mathbf{x}_{n})=x_{in}$, where $x_{in}=1$ for $n\le i$ and $x_{in}=1/(n-i)$ for $n>i$, converges in every coordinate to $0$ and does not converge to $\mathbf{0}$.

:::: pf-proof

::: {.pf-step #box-coordinates}
For each fixed coordinate $i$ the real sequence $(\pi_{i}(\mathbf{x}_{n}))_{n}$ converges to $0$.

::: pf-proof
For $n>i$ one has $x_{in}=1/(n-i)$, and $1/(n-i)\to0$ as $n\to\infty$; a sequence that is eventually equal to a sequence tending to $0$ tends to $0$. So $\pi_{i}(\mathbf{x}_{n})\to0=\pi_{i}(\mathbf{0})$.
:::

:::

::: {.pf-step #box-no-limit}
$\mathbf{x}_{n}$ does not converge to $\mathbf{0}$.

::: pf-proof
Let $U=\prod_{i\in\ZZ_{+}}(-1,1)$, a box-open set containing $\mathbf{0}$ since every factor is open and contains $0$. For each $n$ one has $\pi_{n}(\mathbf{x}_{n})=x_{nn}=1$ because $n\le n$, and $1\notin(-1,1)$; so $\mathbf{x}_{n}\notin U$ for every $n$. Hence no $N$ has $\mathbf{x}_{n}\in U$ for all $n\ge N$.
:::

:::

::: {.pf-step}
The box statement fails.

::: pf-proof
Steps [](#box-coordinates){.pf-ref} and [](#box-no-limit){.pf-ref} give a sequence all of whose coordinate sequences converge to the coordinates of $\mathbf{0}$ and which does not converge to $\mathbf{0}$ in the box topology.
:::

:::

:::

:::

::: {.pf-step}
The product statement holds and the box statement does not.

::: pf-proof
Steps [](#only-if){.pf-ref} and [](#if){.pf-ref} prove the equivalence for the product topology; step [](#box-fails){.pf-ref} answers the second question in the negative. The step that fails for the box topology is the maximum $\max_{\alpha\in I}N_{\alpha}$, which needs $I$ finite.
:::

:::

:::
:::
