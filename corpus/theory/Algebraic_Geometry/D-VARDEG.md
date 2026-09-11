---
schema: qual/card@1
id: D-VARDEG
kind: definition
title: Degree as an intersection count
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Intersection Theory
  - Hilbert Polynomial
relations:
- kind: uses
  target: D-L6ERW
- kind: related-to
  target: PR-JR7TS
review: draft
prompts:
- What is the degree of a projective variety?
- Why do the two definitions of degree agree?
---

::: {.definition title="Degree"}
Let $X \subseteq \PP^N$ be projective of dimension $n$.
The **degree** of $X$ is the number of points of
\[
X \intersect H_1 \intersect \cdots \intersect H_n
\]
for $H_1, \ldots, H_n$ general hyperplanes.
:::

::: {.proposition}
This number is finite, independent of the general hyperplanes chosen, and equals $n!$ times the leading coefficient of the Hilbert polynomial $P_X$.
:::

::: {.remark}
Two definitions and one question: why is the count the same for every general choice.
The answer is that cutting by a general hyperplane drops dimension by one and leaves the leading coefficient of the Hilbert polynomial alone, so the count is forced to be the Hilbert-theoretic number, which does not see the choice at all.

*General* is doing work — the hyperplanes must miss the singular locus and meet $X$ transversally — and dropping it is the standard error: a line tangent to a conic meets it in one point, not two, and the count is restored only by multiplicity.
That repair is Bézout, and it is the reason intersection numbers are defined with multiplicities from the start.
The word an examiner wants next is *degree is not intrinsic*: the twisted cubic and a line are the same abstract curve with degrees $3$ and $1$.
:::
