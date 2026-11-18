---
schema: qual/card@1
id: E-LY1GZ
kind: problem
title: Connected sets crossing a set and its complement meet the boundary
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Boundary
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 6, printed p. 152, with the
    definition of boundary in Exercise 17.19 and Lemma 23.1; the stored statement is the
    printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.6, PDF p. 2. If a connected set meeting both A
    and its complement missed the boundary, its two traces would be a separation, since
    neither would contain a limit point of the other. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

Let $A \subset X$.
Show that if $C$ is a connected subspace of $X$ that intersects both $A$ and $X - A$, then $C$ intersects $\operatorname{Bd} A$.
:::

::: {.solution}

The argument is **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.6, PDF p. 2 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the handling of limit points below is that solution's, and the statement was checked against Munkres, *Topology* (2000), §23 Exercise 6, printed p. 152, with Lemma 23.1 on printed p. 148. Closures and limit points are taken in $X$.

::: pf

::: {.pf-step #pieces}
$P\coloneqq C\cap A$ and $Q\coloneqq C\cap(X-A)$ are disjoint, nonempty, and $P\cup Q=C$.

::: pf-proof
Both intersections are nonempty by hypothesis, and they are disjoint because $A\cap(X-A)=\varnothing$; their union is $C\cap(A\cup(X-A))=C$.
:::

:::

::: {.pf-step #boundary}
$\operatorname{Bd}A=\overline{A}\cap\overline{X-A}$.

::: pf-proof
This is the definition of the boundary of $A$ in $X$ (§17, printed p. 101): the intersection of the closures of $A$ and of its complement.
:::

:::

::: {.pf-step #no-boundary-point}
Suppose that $C\cap\operatorname{Bd}A=\varnothing$. Then no point of $C$ lies in both $\overline{A}$ and $\overline{X-A}$.

::: pf-proof
By step [](#boundary){.pf-ref}, a point of $C$ lying in both closures would lie in $C\cap\operatorname{Bd}A$, which is assumed empty.
:::

:::

::: {.pf-step #no-limit-points}
Under the supposition of step [](#no-boundary-point){.pf-ref}, $Q$ contains no limit point of $P$ and $P$ contains no limit point of $Q$.

:::: pf-proof

::: {.pf-step #q-no-limit-of-p}
If $x\in Q$ is a limit point of $P$, contradiction.

::: pf-proof
A limit point of $P$ lies in $\overline{P}\subset\overline{A}$, so $x\in\overline{A}$; and $x\in Q\subset X-A\subset\overline{X-A}$. As $x\in Q\subset C$, this puts $x$ in $C\cap\operatorname{Bd}A$, contrary to step [](#no-boundary-point){.pf-ref}.
:::

:::

::: {.pf-step #p-no-limit-of-q}
If $x\in P$ is a limit point of $Q$, contradiction.

::: pf-proof
Symmetrically, such an $x$ lies in $\overline{Q}\subset\overline{X-A}$ because $Q\subset X-A$, and in $P\subset A\subset\overline{A}$; with $x\in P\subset C$ this again puts $x$ in $C\cap\operatorname{Bd}A$.
:::

:::

::::

:::

::: pf-step
Therefore $C\cap\operatorname{Bd}A\neq\varnothing$.

::: pf-proof
Under the contrary supposition, steps [](#pieces){.pf-ref} and [](#no-limit-points){.pf-ref} exhibit $P,Q$ as disjoint nonempty subsets of $C$ with union $C$, neither containing a limit point of the other, which by Lemma 23.1 (printed p. 148) is a separation of $C$. That contradicts the connectedness of $C$, so the supposition fails and $C$ meets $\operatorname{Bd}A$.
:::

:::

:::

:::
