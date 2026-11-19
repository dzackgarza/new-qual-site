---
schema: qual/card@1
id: E-O13MH
kind: problem
title: Connectedness under refinement of topologies
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
    Read against Munkres, Topology (2000), §23 Exercise 1, printed p. 152; the stored
    statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.1, PDF p. 1. A separation in the coarser
    topology is one in the finer, so connectedness in the finer topology gives it in the
    coarser; the two-point set with the indiscrete and the discrete topology shows the
    converse fails. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the prose solution as a Lamport proof. Re-read the retained set's Exercise 23.1 in its
    text version (tmp/sources/positron-ch3.txt, the lines beginning "Exercise 23.1") against the
    steps: the set states both halves in one sentence, the implication because a separation in the
    coarser topology is one in the finer, and the failure of the converse by an unnamed two-point
    example. The example is supplied on the card, the indiscrete and the discrete topology on
    {a,b}, and each half is now a step whose justification is the definition of a separation
    (§23). The statement is unchanged and no additional hypothesis is claimed.
---

::: {.exercise}

Let $\mathcal{T}$ and $\mathcal{T}'$ be two topologies on $X$.
If $\mathcal{T}' \supset \mathcal{T}$, what does connectedness of $X$ in one topology imply about connectedness in the other?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.1, PDF p. 1** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both halves are theirs.

A separation of a space is a pair of disjoint nonempty open sets whose union is the space (§23).

::: pf

::: {.pf-step #finer-implies-coarser}
If $\mathcal{T}'\supset\mathcal{T}$ and $(X,\mathcal{T}')$ is connected, then $(X,\mathcal{T})$ is connected.

::: pf-proof
Suppose $U,V$ separate $(X,\mathcal{T})$. Then $U$ and $V$ are disjoint, nonempty, and their union is $X$, and both are open in $\mathcal{T}$, hence open in the finer topology $\mathcal{T}'$ because $\mathcal{T}\subset\mathcal{T}'$. The same pair would then separate $(X,\mathcal{T}')$, contradicting its connectedness.
:::

:::

::: {.pf-step #converse-fails}
The converse fails: a connected $(X,\mathcal{T})$ may have $(X,\mathcal{T}')$ disconnected for a finer $\mathcal{T}'$.

::: pf-proof
Take $X=\theset{a,b}$, $\mathcal{T}=\{\varnothing,X\}$ and $\mathcal{T}'=\mathcal{P}(X)$. The only nonempty open set of $\mathcal{T}$ is $X$ itself, so no two disjoint nonempty $\mathcal{T}$-open sets exist and $(X,\mathcal{T})$ has no separation. In $\mathcal{T}'$ the sets $\{a\}$ and $\{b\}$ are nonempty, disjoint and open, and their union is $X$, so they separate $(X,\mathcal{T}')$.
:::

:::

::: {.pf-step #answer}
Connectedness in the finer topology implies connectedness in the coarser, and connectedness in the coarser topology does not imply it in the finer.

::: pf-proof
Step [](#finer-implies-coarser){.pf-ref} gives the implication, one direction only, and step [](#converse-fails){.pf-ref} exhibits a pair of topologies on one set for which the coarser space is connected and the finer one is not. Hence connectedness of $X$ in one topology implies connectedness in the other only when the connected topology is the finer of the two, and no implication runs in the reverse direction.
:::

:::

:::
:::
