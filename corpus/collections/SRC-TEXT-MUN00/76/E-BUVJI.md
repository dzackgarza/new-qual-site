---
schema: qual/card@1
id: E-BUVJI
kind: problem
title: Two reduction sequences for the same scheme disagree
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

Consider the space $X$ obtained from two polygonal regions by means of the labelling schemes $w_1 = abcc$ and $w_2 = c^{-1}c^{-1}ab$.
The sequence of elementary operations

$$
\begin{array}{rl}
abcc \text{ and } c^{-1}c^{-1}ab & \to ccab \text{ and } b^{-1}a^{-1}cc \text{ by permuting and flipping} \\
& \to ccaa^{-1}cc \text{ by pasting} \\
& \to cccc \text{ by cancelling}
\end{array}
$$

indicates that $X$ is homeomorphic to the four-fold dunce cap.
The sequence of operations

$$
\begin{array}{rl}
abcc \text{ and } c^{-1}c^{-1}ab & \to abcc^{-1}ab \text{ by pasting} \\
& \to abab \text{ by cancelling}
\end{array}
$$

indicates that $X$ is homeomorphic to $P^2$.
But these two spaces are not homeomorphic.
Which (if either) argument is correct?
:::

::: {.solution}
The first argument is valid and the second is not.

For the first sequence, after the indicated permutation and flip we have
\[
ccab\qquad\text{and}\qquad b^{-1}a^{-1}cc.
\]
The label \(b\) now occurs exactly on the two edges being pasted, with opposite exponents, so the pasting operation is legitimate and gives
\[
ccaa^{-1}cc.
\]
Here the adjacent \(a,a^{-1}\) pair satisfies the hypotheses of the cancelling operation: the label \(a\) appears nowhere else and the words on either side, \(cc\) and \(cc\), each have length at least two. Thus cancellation gives
\[
cccc.
\]
Hence this sequence is a valid sequence of elementary operations.

The second sequence starts by trying to paste the original schemes
\[
abcc,\qquad c^{-1}c^{-1}ab
\]
along a pair of \(c\)-edges. But the label \(c\) occurs four times in the total scheme. Therefore the two selected edges are not the only edges required to be identified with one another. The inverse-cutting theorem does not permit replacing the two polygons by a single polygon along such a pair: once those edges become an interior seam, the remaining required \(c\)-identifications are not represented by the resulting boundary word.

Thus
\[
abcc,\ c^{-1}c^{-1}ab\not\longmapsto abcc^{-1}ab
\]
by the elementary pasting operation. The subsequent cancellation is irrelevant because the first step is invalid.

Therefore only the first argument is correct, and \(X\) is represented by the scheme \(cccc\), i.e. by the four-fold dunce-cap scheme, not by the claimed \(abab\) scheme.
:::
