---
schema: qual/card@1
id: E-BI0O0
kind: problem
title: Interior and boundary of a subset
classification:
  areas:
  - topology
  topics:
  - Boundary
  - Interior
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 19, printed p. 102, with the
    definition of boundary printed there and of interior in §17; parts (a) to (d) are stored
    as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.19, printed pp.
    173-175. His are (a) that the interior and the boundary are disjoint and fill the
    closure, (b) that an empty boundary is the same as being both open and closed, and (c)
    that for open U the boundary is the closure minus U, with the converse. For (d) the
    counterexample used is positron0802's on PDF p. 9, R - {0} in the usual topology, his
    own on printed p. 174 being the same set in the finite complement topology.
    (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 with seven steps: the disjointness of $\operatorname{Int}A$ and $\operatorname{Bd}A$, the decomposition of $\overline{A}$, both directions of (b), both of (c), and the counterexample of (d). Each was re-checked against the definitions of interior and boundary. No statement change.
---

::: {.exercise}

If $A \subset X$, we define the boundary of $A$ by the equation

$$
\operatorname{Bd} A = \overline{A} \cap \overline{(X - A)}.
$$

(a) Show that $\operatorname{Int} A$ and $\operatorname{Bd} A$ are disjoint, and $\overline{A} = \operatorname{Int} A \cup \operatorname{Bd} A$.

(b) Show that $\operatorname{Bd} A = \varnothing$ if and only if $A$ is both open and closed.

(c) Show that $U$ is open if and only if $\operatorname{Bd} U = \overline{U} - U$.

(d) If $U$ is open, is it true that $U = \operatorname{Int}(\overline{U})$?
Justify your answer.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.19, printed pp. 173--175** (`tmp/sources/munkres-solutions-whitman.pdf`); (a), (b) and (c) are his. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 17.19, PDF p. 9, gives the same three and a simpler counterexample for (d), which is the one used below; Whitman's printed p. 174 uses $\RR-\{0\}$ in the finite complement topology instead.

Throughout $A\subset X$, $\operatorname{Bd}A=\overline{A}\cap\overline{(X-A)}$, and $\operatorname{Int}A$ is the union of the open subsets of $A$: it is open, and it is the set of points having a neighbourhood contained in $A$.

::: pf

::: {.pf-step #disjoint-from-closure}

$\operatorname{Int}A$ and $\operatorname{Bd}A$ are disjoint.

::: pf-proof

If $x\in\operatorname{Int}A$ there is a neighbourhood $U$ of $x$ with $U\subset A$, so $U\cap(X-A)=\varnothing$ and therefore $x\notin\overline{X-A}$; hence $x\notin\operatorname{Bd}A$.

:::

:::

::: {.pf-step #decomposition}

$\overline{A}=\operatorname{Int}A\cup\operatorname{Bd}A$.

::: pf-proof

Both $\operatorname{Int}A$ and $\operatorname{Bd}A$ are contained in $\overline{A}$, so $\operatorname{Int}A\cup\operatorname{Bd}A\subset\overline{A}$. Conversely let $x\in\overline{A}$. If $x\in\operatorname{Int}A$ the point is in the union; if not, then no neighbourhood of $x$ is contained in $A$, so every neighbourhood of $x$ meets $X-A$, which gives $x\in\overline{X-A}$ and hence $x\in\operatorname{Bd}A$.

:::

:::

::: pf-step

If $\operatorname{Bd}A=\varnothing$ then $A$ is both open and closed.

::: pf-proof

By step [](#decomposition){.pf-ref} and step [](#disjoint-from-closure){.pf-ref}, $\overline{A}=\operatorname{Int}A$, and $\operatorname{Int}A\subset A\subset\overline{A}$, so $A=\operatorname{Int}A=\overline{A}$; the first equality says that $A$ is open and the second that $A$ is closed.

:::

:::

::: pf-step

If $A$ is both open and closed then $\operatorname{Bd}A=\varnothing$.

::: pf-proof

Here $\overline{X-A}=X-A$ because $A$ is open, and $\overline{A}=A$ because $A$ is closed, so
$$
\operatorname{Bd}A=\overline{A}\cap\overline{(X-A)}=A\cap(X-A)=\varnothing .
$$

:::

:::

::: pf-step

If $U$ is open then $\operatorname{Bd}U=\overline{U}-U$.

::: pf-proof

Since $U$ is open, $\overline{X-U}=X-U$, so
$$
\operatorname{Bd}U=\overline{U}\cap\overline{(X-U)}=\overline{U}\cap(X-U)=\overline{U}-U .
$$

:::

:::

::: pf-step

If $\operatorname{Bd}U=\overline{U}-U$ then $U$ is open.

::: pf-proof

Let $x\in U$. Then $x\in\overline{U}$ and $x\notin\overline{U}-U=\operatorname{Bd}U$, so $x\notin\overline{X-U}$; hence some neighbourhood $V$ of $x$ misses $X-U$, that is $V\subset U$. So every point of $U$ is an interior point and $U=\operatorname{Int}U$ is open.

:::

:::

::: pf-step

(d) An open $U$ need not satisfy $U=\operatorname{Int}\overline{U}$.

::: pf-proof

In $\RR$ with the usual topology let $U=\RR-\{0\}$, which is open. Then $\overline{U}=\RR$ and $\operatorname{Int}\overline{U}=\RR$, while $U\ne\RR$; so $U\subsetneq\operatorname{Int}\overline{U}$. The inclusion $U\subset\operatorname{Int}\overline{U}$ does hold for every open $U$, since $\overline{U}$ contains the open set $U$.

:::

:::

:::
:::
