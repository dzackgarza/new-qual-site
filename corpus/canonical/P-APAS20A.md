---
schema: qual/card@1
id: P-APAS20A
kind: problem
title: Extremal dimensions of $\ker(\phi^2)$ and $\ker((\phi-\mathrm{id})^2)$ from partial matrix data
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $\phi\colon\mathbb{C}^8\to\mathbb{C}^8$ be a linear map whose matrix with respect to the standard basis is of the form
\[
\begin{pmatrix}
1 & * & * & * & * & * & * & * \\
0 & 1 & * & * & * & * & * & * \\
0 & 0 & 1 & * & * & * & * & * \\
0 & 0 & 0 & 1 & * & * & * & * \\
0 & 0 & 0 & 0 & 0 & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix},
\]
where $*$ represents an unknown value. Suppose moreover that we are told
\[
\dim\ker\phi=2,\qquad
\dim\ker(\phi-\mathrm{id})=2,\qquad
\phi^5-2\phi^4+\phi^3=0.
\]
Determine, with proof, the maximum and minimum possible values of
\[
\dim\ker(\phi^2)\qquad\text{and}\qquad\dim\ker\bigl((\phi-\mathrm{id})^2\bigr).
\]
:::
