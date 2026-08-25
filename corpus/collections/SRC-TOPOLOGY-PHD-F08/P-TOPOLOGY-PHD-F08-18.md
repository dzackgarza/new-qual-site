---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-18
kind: problem
title: No finite-sheeted covering of the circle has the stated index
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
It is known that if $p:\widetilde X\to X$ is a covering space and $x_0\in X$ then the cardinality of $p^{-1}(x_0)$ is the index of $p_*\pi_1(\widetilde X,y_0)$ in $\pi_1(X,x_0)$ where $p(y_0)=x_0$.
Use this fact to deduce that there is no $n$-sheeted covering of the circle $S^1$ for any finite $n$.
:::

::: remark
The source page prints a colon immediately before the arrow in the map notation; the map is rendered here with the conventional $\to$ notation.

The question as set cannot be answered, and the statement is left as the exam printed it rather than repaired.
There *are* $n$-sheeted coverings of $S^1$ for every finite $n$: the map $z \mapsto z^n$ is one, and it corresponds under the quoted fact to the subgroup $n\ZZ \leq \ZZ = \pi_1(S^1)$, which has index $n$.
Verified against the source, `assets/attachments/F08phdtop.pdf` page 2, Part Two question 6, where the sentence appears verbatim; the transcription is faithful and the error is the paper's.

That page is headed "January 2009" while this exam is recorded as Fall 2008.
:::
