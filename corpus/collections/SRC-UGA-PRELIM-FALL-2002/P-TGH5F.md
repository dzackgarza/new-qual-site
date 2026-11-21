---
schema: qual/card@1
id: P-TGH5F
kind: problem
title: A finite spanning set in $\RR^n$ contains a basis of its span
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $v_1, \dots, v_k$ be vectors in $\RR^n$.
Define the span $V = \langle v_1, \dots, v_k \rangle$ of the vectors.
Prove that there is a subset of the vectors $v_1, \dots, v_k$ that forms a basis for $V$.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper (`assets/attachments/grad_prelim_Fall02.pdf`) and no solutions sheet accompanies it, so the argument below is the card's own. It is the maximal-independent-subset argument; the one lemma the earlier version of the card asserted in passing — that adjoining a vector outside the span to an independent set preserves independence — is proved here, since that is the whole content of the maximality step.

Throughout, $v_{1},\dots,v_{k}\in\RR^{n}$ and $V=\langle v_{1},\dots,v_{k}\rangle$ is their span, the smallest subspace of $\RR^{n}$ containing all of them.

::: pf

::: {.pf-step #maximal}
Among the linearly independent subsets of the finite set $\theset{v_{1},\dots,v_{k}}$ there is one of maximal cardinality.

::: pf-proof
A subset of a finite set is finite, and there are finitely many subsets of $\theset{v_{1},\dots,v_{k}}$, so the collection $\mathcal{I}$ of linearly independent subsets is finite; it is nonempty because the empty set is linearly independent. A finite nonempty set of integers — the cardinalities of the members of $\mathcal{I}$ — has a maximum, attained at some $S\in\mathcal{I}$.
:::

:::

::: {.pf-step #adjoin}
Let $S$ be linearly independent and let $v\notin\langle S\rangle$. Then $S\cup\theset{v}$ is linearly independent.

::: pf-proof
Suppose $\sum_{s\in S}a_{s}s+bv=0$ with all coefficients zero except finitely many. If $b\neq0$ then $v=-\frac1b\sum_{s}a_{s}s$ lies in $\langle S\rangle$, contrary to the hypothesis; so $b=0$, and then $\sum_{s}a_{s}s=0$, which forces $a_{s}=0$ for all $s$ because $S$ is linearly independent.
:::

:::

::: {.pf-step #spans}
The maximal $S=\theset{v_{i_{1}},\dots,v_{i_{r}}}$ spans $V$.

::: pf-proof
Each $v_{j}$ lies in $\langle S\rangle$: otherwise $S\cup\theset{v_{j}}$ would be linearly independent by step [](#adjoin){.pf-ref}, and it strictly contains $S$, contradicting the maximal cardinality of $S$ among independent subsets. Since $\langle S\rangle$ is a subspace containing every $v_{j}$, it contains the span $V$ of those vectors; and conversely $\langle S\rangle\subset V$ because $S\subset\theset{v_{1},\dots,v_{k}}$. Hence $\langle S\rangle=V$.
:::

:::

::: pf-step
Therefore $S$ is a basis of $V$, so a subset of $v_{1},\dots,v_{k}$ is a basis of their span.

::: pf-proof
$S$ is linearly independent by step [](#maximal){.pf-ref}, being a member of $\mathcal{I}$, and it spans $V$ by step [](#spans){.pf-ref}; a linearly independent spanning subset of $V$ is a basis of $V$. As $S\subseteq\theset{v_{1},\dots,v_{k}}$, it is the required subset of the given vectors.
:::

:::

:::

:::
