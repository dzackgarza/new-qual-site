---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-03
kind: problem
title: A local closure condition implies regularity
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the retained problem set at assets/attachments/Day_3_-_Separation_Problems.pdf,
    problem (3) (June '04 #A3): "Show that for a topological space X, if every x in X has a
    neighborhood whose closure is a regular space, then X is regular." The card's statement is that
    problem verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, and the one step the prose compressed
    is now argued: the closure of V computed in X equals its closure computed in the subspace
    closure of N, because V is contained in that closed set. Also recorded the two-sided form of the
    neighbourhood criterion for regularity, so that the final step is a use of a proved equivalence
    rather than a convention, and that x lies in the open G chosen inside N cap U. No retained
    published solution covers this problem.
---

::: {.problem}
Show that for a topological space $X$, if every $x\in X$ has a neighborhood whose closure is a regular space, then $X$ is regular.
:::

::: {.solution}
This is Problem 3 (June '04 #A3) of the retained Day 3 separation-axioms problem set (`assets/attachments/Day_3_-_Separation_Problems.pdf`, p. 1). No published solution set is transcribed: the argument is the card's own.

::: pf

::: {.pf-step #criterion}
A space is regular if and only if for every $x$ and every open $U\ni x$ there is an open $V$ with $x\in V$ and $\overline{V}\subset U$.

::: pf-proof
This is the neighbourhood form of regularity (Munkres Lemma 31.1(a), printed p. 196): in a regular space a point and a neighbourhood of it can be separated by a neighbourhood whose closure is contained in the given one. Conversely, if the displayed property holds and $x\notin B$ with $B$ closed, apply it to the open set $X\setminus B$ to get $V$ with $x\in V$ and $\overline{V}\cap B=\varnothing$, which is the separation demanded of a regular space.
:::
:::

::: {.pf-step #hypothesis}
Let $x\in X$ and let $U$ be an open neighbourhood of $x$. There is an open $G$ with $x\in G\subset N\cap U$, where $N$ is a neighbourhood of $x$ whose closure is regular.

::: pf-proof
By hypothesis $x$ has a neighbourhood $N$ such that $\overline{N}$ with the subspace topology is regular. A neighbourhood contains an open set about $x$, and $N\cap U$ is a neighbourhood of $x$ since both factors are; so there is an open $G$ of $X$ with $x\in G\subset N\cap U$.
:::
:::

::: {.pf-step #subspace}
$G$ is open in the subspace $\overline{N}$, and there is a set $W$, open in $\overline{N}$, with $x\in W$ and $\overline{W}^{\,\overline{N}}\subset G$.

::: pf-proof
$G\subset N\subset\overline{N}$ and $G$ is open in $X$, so $G=G\cap\overline{N}$ is open in the subspace $\overline{N}$. Since $x\in G$ and $G$ is an $\overline{N}$-open neighbourhood of $x$, step [](#criterion){.pf-ref} applied inside the regular space $\overline{N}$ gives $W$, open in $\overline{N}$, with $x\in W$ and the closure of $W$ in $\overline{N}$ contained in $G$.
:::
:::

::: {.pf-step #lift}
$V=O\cap G$, where $O$ is open in $X$ with $W=O\cap\overline{N}$, is open in $X$, contains $x$, and satisfies $\overline{V}^{\,X}\subset U$.

::: pf-proof
Such $O$ exists because $W$ is open in the subspace. Then $V$ is open in $X$, being the intersection of open sets, and $x\in V$ because $x\in W\subset O$ and $x\in G$. Also $V\subset W\subset\overline{N}$, so $\overline{V}^{\,X}\subset\overline{N}$, since $\overline{N}$ is closed in $X$; hence
$$\overline{V}^{\,X}=\overline{V}^{\,X}\cap\overline{N}=\overline{V}^{\,\overline{N}}\subset\overline{W}^{\,\overline{N}}\subset G\subset U,$$
using that $V\subset W$ and monotonicity of closure. So every $x$ and every open neighbourhood $U$ of it admit such a $V$, and step [](#criterion){.pf-ref} makes $X$ regular.
:::
:::
:::

:::
