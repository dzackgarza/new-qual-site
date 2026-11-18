---
schema: qual/card@1
id: E-MUN-6-2
kind: problem
title: Subsets of finite sets are finite
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §6 Exercise 2, printed p. 44; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.2,
    printed p. 76 (tmp/sources/munkres-solutions-whitman.pdf). He splits B = A from B a
    proper subset, using Theorem 6.2 for the proper case; the card instead proves
    directly that every subset of a section {1,...,n} is finite, which reaches the same
    conclusion without quoting 6.2. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the induction on n with an empty case
    and a successor case, the transfer of finiteness to a subset, and the contrapositive
    as the final step. Re-read against the retained solution at the cited page, Whitman
    Exercise 6.2 printed p. 76, and the induction that the card proves directly is
    unchanged. The printed book text was not re-read; the statement's source check on
    this card is the earlier event.
---

::: {.exercise}

Show that if $B$ is not finite and $B \subset A$, then $A$ is not finite.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.2, printed p. 76** (`tmp/sources/munkres-solutions-whitman.pdf`), which argues through the book's Theorem 6.2 that a proper subset of a finite set is finite; the card proves that input directly instead, by induction on $n$.

A set $S$ is finite when $S=\varnothing$ or there is a bijection of $S$ with $\{1,\dots,n\}$ for some $n\in\ZZ_{+}$; this is the book's definition.

::: pf

::: {.pf-step #sections}
For every $n\ge0$, every subset of $\{1,\dots,n\}$ is finite.

::: pf-proof
Induction on $n$, with the two cases below.

::: {.pf-step #zero}
Every subset of $\{1,\dots,0\}=\varnothing$ is finite.

::: pf-proof
The only subset of $\varnothing$ is $\varnothing$, which is finite by the definition.
:::

:::

::: {.pf-step #successor}
If every subset of $\{1,\dots,n\}$ is finite, then every subset of $\{1,\dots,n+1\}$ is finite.

::: pf-proof
Let $C\subset\{1,\dots,n+1\}$. If $n+1\notin C$, then $C\subset\{1,\dots,n\}$ is finite by the induction hypothesis. If $n+1\in C$, then $C-\{n+1\}\subset\{1,\dots,n\}$ is finite by the induction hypothesis, so either $C-\{n+1\}=\varnothing$ and the bijection $n+1\mapsto1$ exhibits $C$ in bijection with $\{1\}$, or there is a bijection $h:C-\{n+1\}\to\{1,\dots,m\}$, and extending it by $h(n+1)=m+1$ gives a bijection $C\to\{1,\dots,m+1\}$. Hence $C$ is finite.
:::

:::

:::

:::

::: {.pf-step #transfer}
If $A$ is finite and $B\subset A$, then $B$ is finite.

::: pf-proof
If $A=\varnothing$ then $B=\varnothing$ is finite. Otherwise there is a bijection $h:A\to\{1,\dots,n\}$; the image $h(B)$ is a subset of $\{1,\dots,n\}$, hence finite by step [](#sections){.pf-ref}, and $h$ restricts to a bijection $B\to h(B)$, so $B$ is in bijection with the finite set $h(B)$. Composing that bijection with a bijection of $h(B)$ onto some $\{1,\dots,m\}$ (or noting $h(B)=\varnothing$ if it is empty) gives a bijection of $B$ with $\{1,\dots,m\}$, so $B$ is finite.
:::

:::

::: {.pf-step}
If $B$ is not finite and $B\subset A$, then $A$ is not finite.

::: pf-proof
Were $A$ finite, step [](#transfer){.pf-ref} applied to $B\subset A$ would make $B$ finite, contradicting the hypothesis. So $A$ is not finite: the statement is the contrapositive of step [](#transfer){.pf-ref}, as claimed.
:::

:::

:::
:::
