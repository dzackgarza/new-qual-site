---
schema: qual/card@1
id: E-LEN3V
kind: problem
title: Unions of intersecting sequences of connected subspaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 2, printed p. 152, with Lemma 23.2
    and Theorem 23.3; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.2, PDF pp. 1-2. The first set lies in one side
    of a would-be separation and then, inductively, so does each successive set, because
    consecutive sets meet; so the other side is empty. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

Let $\theset{A_n}$ be a sequence of connected subspaces of $X$, such that $A_n \cap A_{n+1} \neq \varnothing$ for all $n$.
Show that $\bigcup A_n$ is connected.
:::

::: {.solution}

The argument is **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.2 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the induction below is that solution's, and the statement was checked against Munkres, *Topology* (2000), §23 Exercise 2, with Lemma 23.1 and Lemma 23.2 on printed pp. 148--149. The card's earlier page reference, is corrected to p. 1.

::: pf

::: {.pf-step #separation-setup}
Suppose that $Y\coloneqq\bigcup_{n\in\NN}A_{n}$ admits a separation $Y=B\cup C$ into disjoint nonempty sets $B,C$ open in $Y$. Then every $A_{n}$ lies in $B$ or in $C$.

::: pf-proof
Each $A_{n}$ is a connected subspace of the space $Y$, and $B,C$ form a separation of $Y$; by Lemma 23.2 a connected subspace of a space with a separation lies entirely in one member of it.
:::

:::

::: {.pf-step #first-piece}
$A_{1}$ lies in $B$ or in $C$; after relabelling the separation, assume $A_{1}\subset B$.

::: pf-proof
The first assertion is step [](#separation-setup){.pf-ref} for $n=1$. The names of the two members of a separation are arbitrary, so exchanging them if necessary gives $A_{1}\subset B$ without loss of generality.
:::

:::

::: {.pf-step #induction}
$A_{n}\subset B$ for every $n$.

:::: pf-proof

::: {.pf-step #induction-step}
If $A_{n}\subset B$, then $A_{n+1}\subset B$.

::: pf-proof
By step [](#separation-setup){.pf-ref}, $A_{n+1}$ lies in $B$ or in $C$. If $A_{n+1}\subset C$, then a point of $A_{n}\cap A_{n+1}$, which is nonempty by hypothesis, would lie in $B\cap C=\varnothing$; so $A_{n+1}\subset B$.
:::

:::

::: {.pf-step}
The conclusion follows by induction on $n$ from step [](#first-piece){.pf-ref} and step [](#induction-step){.pf-ref}.

::: pf-proof
The natural numbers are generated from $1$ by the successor operation, so a property holding at $n=1$ and inherited from $n$ to $n+1$ holds at every $n$.
:::

:::

::::

:::

::: pf-step
No separation of $Y$ exists, so $Y$ is connected.

::: pf-proof
Under the supposition of step [](#separation-setup){.pf-ref} all the $A_{n}$ lie in $B$ by step [](#induction){.pf-ref}, hence $Y=\bigcup_{n}A_{n}\subset B$ and $C=Y-B=\varnothing$, contradicting the requirement that the members of a separation be nonempty. Hence no separation exists and $Y$ is connected by the definition of connectedness (§23).
:::

:::

:::

:::
