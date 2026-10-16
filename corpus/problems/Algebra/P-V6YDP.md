---
schema: qual/card@1
id: P-V6YDP
kind: problem
title: $\sqrt{IJ}=\sqrt I\cap\sqrt J$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
relations: []
review: draft
---

::: {.problem}
Show that
\[
\sqrt{IJ}=\sqrt I\cap\sqrt J.
\]
:::

::: {.solution}
Since $IJ\subseteq I\cap J$,
\[
\sqrt{IJ}\subseteq\sqrt I\cap\sqrt J.
\]
Conversely, if $x\in\sqrt I\cap\sqrt J$, choose $m,n$ with $x^m\in I$ and $x^n\in J$. Then
\[
x^{m+n}=x^mx^n\in IJ,
\]
so $x\in\sqrt{IJ}$.
:::