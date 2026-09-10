---
schema: qual/card@1
id: E-TUPHD
kind: problem
title: Pasting schemes for two polygonal regions
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

Consider the quotient space $X$ obtained from two polygonal regions by means of the labelling schemes $w_1 = acbc^{-1}$ and $w_2 = cdba^{-1}d$.

(a) If one pastes these regions together along the edges labelled "a," one can represent $X$ as the quotient space of a single 7-sided region $P$.
What is a labelling scheme for $P$?
What sequence of elementary operations is involved in obtaining this scheme?

(b) Repeat (a), pasting along the edges labelled "b".

(c) Explain why one cannot paste along the edges labelled "c" to obtain the scheme $acbdba^{-1}d$ as a way of representing $X$.
:::

::: {.solution}
Write
\[
w_1=acbc^{-1},\qquad w_2=cdba^{-1}d.
\]
Recall that the pasting operation is the inverse of cutting: after cyclically permuting and, if necessary, flipping one polygon, one may replace schemes of the form
\[
y_0e,\qquad e^{-1}y_1
\]
by the single scheme \(y_0y_1\), provided the two indicated \(e\)-edges are the only edges to be pasted to one another.

(a) To paste along the \(a\)-edges, cyclically permute both words:
\[
acbc^{-1}\sim cbc^{-1}a,
\qquad
cdba^{-1}d\sim a^{-1}dcdb.
\]
Now the pasting operation gives
\[
cbc^{-1}a\quad\text{and}\quad a^{-1}dcdb
\longmapsto
\boxed{cbc^{-1}dcdb}.
\]
Thus one valid 7-sided scheme is \(cbc^{-1}dcdb\).

(b) The two \(b\)-edges have the same exponent, so first flip the second polygon:
\[
cdba^{-1}d\longmapsto d^{-1}ab^{-1}d^{-1}c^{-1}.
\]
Then cyclically permute:
\[
acbc^{-1}\sim c^{-1}acb,
\qquad
d^{-1}ab^{-1}d^{-1}c^{-1}\sim b^{-1}d^{-1}c^{-1}d^{-1}a.
\]
Pasting along \(b,b^{-1}\) yields
\[
\boxed{c^{-1}acd^{-1}c^{-1}d^{-1}a}.
\]
Any cyclic permutation, global relabelling, or simultaneous reversal of a label gives an equivalent answer.

(c) The proposed move along \(c\) is not an elementary pasting operation. In the total original scheme the label \(c\) occurs three times: twice in \(w_1\), as \(c\) and \(c^{-1}\), and once in \(w_2\). Hence if one glues one \(c\)-edge from each polygon, the chosen edges are still required by the original quotient relation to be identified with the third \(c\)-edge. After turning the first two into an interior seam, that extra identification is no longer encoded by a boundary labelling scheme. This violates the hypothesis for the inverse cutting/pasting operation. Therefore the word
\[
acbdba^{-1}d
\]
does not arise from the stated quotient by a valid pasting along \(c\).
:::
