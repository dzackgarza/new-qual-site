---
title: Operators and their norms
order: 20
problems:
  topics:
  - Bounded Operators
  - Operator Theory
  - Dual Spaces
---

# Operators and their norms

For a linear map between normed spaces, continuity is equivalent to boundedness, and the optimal bound is the operator norm
\[
\|T\|=\sup_{\|x\|\le 1}\|Tx\|.
\]
Thus a continuity question about a linear operator is an inequality question.
The dual space \(X^*\), equipped with this norm, is Banach even when \(X\) itself is not complete.

[[T-5IWCG]]

[[T-QBTWN]]

[[T-W5SDY]]

Compactness is stronger than boundedness: a compact operator sends the unit ball to a relatively compact set.
Consequently a compact-operator problem usually has two separate steps—prove boundedness, then prove precompactness of the image rather than trying to infer compactness from an operator-norm estimate alone.

[[FF-BSYDE]]

::: {.remark title="Bounded is continuous"}
For linear maps between normed spaces, bounded, continuous, and continuous at a single point are the same condition.
So every continuity question about a linear operator is a computation of $\sup_{\norm x = 1}\norm{Tx}$, and that is the only computation in the subject.
:::
