---
schema: qual/card@1
id: E-DKMHL
kind: problem
title: Element orders divide the order of a finite group
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that the order of any element in a finite group divides the order of the group.
:::


::: {.solution}
Let $G$ be finite and let $g\in G$.

<1>1. The cyclic subgroup $\langle g\rangle$ has order equal to the order of $g$.
::: {.proof}
By definition, the order $|g|$ is the least positive integer $n$ such that $g^n=e$. Then
\[
\langle g\rangle=\{e,g,g^2,\ldots,g^{n-1}\}
\]
has exactly $n=|g|$ elements.
:::

<1>2. Lagrange's theorem gives
\[
|G|=[G:\langle g\rangle]\,|\langle g\rangle|.
\]
::: {.proof}
The left cosets of the subgroup $\langle g\rangle$ partition the finite group $G$, and each coset has $|\langle g\rangle|$ elements. Their number is the index $[G:\langle g\rangle]$.
:::

<1>3. Therefore $|g|$ divides $|G|$.
::: {.proof}
By <1>1 and <1>2,
\[
|G|=[G:\langle g\rangle]\,|g|,
\]
and the index is a positive integer.
:::
:::
