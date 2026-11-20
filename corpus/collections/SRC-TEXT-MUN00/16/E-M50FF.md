---
schema: qual/card@1
id: E-M50FF
kind: problem
title: Transitivity of the subspace topology
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 1, printed p. 91, with the
    definition of the subspace topology on printed p. 88; the stored statement is the
    printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.1, printed p. 149.
    The content is his: A inherits from Y the sets A cap (Y cap U) and from X the sets A cap
    U, and these agree because A is contained in Y. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

Show that if $Y$ is a subspace of $X$, and $A$ is a subset of $Y$, then the topology $A$ inherits as a subspace of $Y$ is the same as the topology it inherits as a subspace of $X$.
:::

::: {.solution}

The argument is **Dan Whitman**, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.1, manual p. 148, PDF p. 151 (`tmp/sources/munkres-solutions-whitman.pdf`); both inclusions below are his, and the statement and the definition of the subspace topology were checked against Munkres, *Topology* (2000), §16 Exercise 1, and §16.

Throughout, $\mathcal{T}$ is the topology of $X$, $\mathcal{T}_{Y}\coloneqq\theset{Y\cap U\mid U\in\mathcal{T}}$ is the subspace topology of $Y$, and
$$
\mathcal{T}_{A}\coloneqq\theset{A\cap V\mid V\in\mathcal{T}_{Y}},\qquad
\mathcal{T}_{A}'\coloneqq\theset{A\cap U\mid U\in\mathcal{T}}
$$
are the topologies that $A$ inherits from $Y$ and from $X$.

::: pf

::: {.pf-step #first-inclusion}
$\mathcal{T}_{A}\subset\mathcal{T}_{A}'$.

::: pf-proof
Let $W\in\mathcal{T}_{A}$, so $W=A\cap V$ for some $V\in\mathcal{T}_{Y}$, and $V=Y\cap U$ for some $U\in\mathcal{T}$. Then
$$
W=A\cap(Y\cap U)=(A\cap Y)\cap U=A\cap U,
$$
the last equality because $A\subset Y$. Since $U\in\mathcal{T}$, this exhibits $W$ as a member of $\mathcal{T}_{A}'$, and $W$ was arbitrary.
:::

:::

::: {.pf-step #second-inclusion}
$\mathcal{T}_{A}'\subset\mathcal{T}_{A}$.

::: pf-proof
Let $W\in\mathcal{T}_{A}'$, so $W=A\cap U$ with $U\in\mathcal{T}$. Put $V\coloneqq Y\cap U$, which lies in $\mathcal{T}_{Y}$ by definition of the subspace topology. Then
$$
W=A\cap U=(A\cap Y)\cap U=A\cap(Y\cap U)=A\cap V,
$$
using $A\subset Y$ again, so $W\in\mathcal{T}_{A}$.
:::

:::

::: pf-step
The two subspace topologies on $A$ coincide.

::: pf-proof
Steps [](#first-inclusion){.pf-ref} and [](#second-inclusion){.pf-ref} give $\mathcal{T}_{A}\subset\mathcal{T}_{A}'$ and $\mathcal{T}_{A}'\subset\mathcal{T}_{A}$, that is $\mathcal{T}_{A}=\mathcal{T}_{A}'$; so $A$ inherits the same topology whether it is regarded as a subspace of $Y$ or of $X$.
:::

:::

:::

:::
