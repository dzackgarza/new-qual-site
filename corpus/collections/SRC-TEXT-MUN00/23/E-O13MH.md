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
---

::: {.exercise}

Let $\mathcal{T}$ and $\mathcal{T}'$ be two topologies on $X$.
If $\mathcal{T}' \supset \mathcal{T}$, what does connectedness of $X$ in one topology imply about connectedness in the other?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.1, PDF p. 1** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both halves are theirs.

If $\mathcal{T}'\supset\mathcal{T}$ and $(X,\mathcal{T}')$ is connected, then $(X,\mathcal{T})$ is connected: a separation of $(X,\mathcal{T})$ would consist of sets open in $\mathcal{T}$, hence open in $\mathcal{T}'$, and would separate $(X,\mathcal{T}')$.

The converse fails: if $(X,\mathcal{T})$ is connected, $(X,\mathcal{T}')$ need not be. For $X=\{a,b\}$ take $\mathcal{T}=\{\varnothing,X\}$ and $\mathcal{T}'=\mathcal{P}(X)$; the first space is connected, the second is separated by $\{a\}$ and $\{b\}$.
:::
