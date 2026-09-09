---
schema: qual/card@1
id: E-HAT-4.K-3
kind: problem
title: "$SP_n(I) = \\Delta^n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 3 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $SP_n(I) = \Delta^n$.

::: {.solution}
An element of the symmetric product
\[
SP_n(I)=I^n/\Sigma_n
\]
is an unordered \(n\)-tuple of points of \(I=[0,1]\). Every orbit has a unique representative whose coordinates are weakly increasing:
\[
0\le x_1\le x_2\le\cdots\le x_n\le1.
\]
Therefore the quotient map restricts to a continuous bijection
\[
Q=\{(x_1,\ldots,x_n):0\le x_1\le\cdots\le x_n\le1\}
\longrightarrow SP_n(I).
\]
The domain is compact and the target is Hausdorff, so this is a homeomorphism.

Now set
\[
y_0=x_1,
\qquad
y_i=x_{i+1}-x_i\ (1\le i<n),
\qquad
y_n=1-x_n.
\]
Then each \(y_i\ge0\) and
\[
y_0+\cdots+y_n=1.
\]
Conversely,
\[
x_j=y_0+\cdots+y_{j-1}.
\]
Thus \(Q\) is affinely homeomorphic to the standard \(n\)-simplex
\[
\Delta^n=\{(y_0,\ldots,y_n):y_i\ge0,\ \sum y_i=1\}.
\]
Hence
\[
\boxed{SP_n(I)\cong\Delta^n.}
\]
:::
