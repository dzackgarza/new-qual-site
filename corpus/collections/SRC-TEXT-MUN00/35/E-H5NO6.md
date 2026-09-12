---
schema: qual/card@1
id: E-H5NO6
kind: problem
title: Retracts of Hausdorff spaces and the plane
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
---

::: {.exercise}

Let $Z$ be a topological space.
If $Y$ is a subspace of $Z$, we say that $Y$ is a retract of $Z$ if there is a continuous map $r: Z \to Y$ such that $r(y) = y$ for each $y \in Y$.

(a) Show that if $Z$ is Hausdorff and $Y$ is a retract of $Z$, then $Y$ is closed in $Z$.

(b) Let $A$ be a two-point set in $\mathbb{R}^2$.
Show that $A$ is not a retract of $\mathbb{R}^2$.

(c) Let $S^1$ be the unit circle in $\mathbb{R}^2$; show that $S^1$ is a retract of $\mathbb{R}^2 - \ts{\mathbf{0}}$, where $\mathbf{0}$ is the origin.
Can you conjecture whether or not $S^1$ is a retract of $\mathbb{R}^2$?
:::

::: {.solution}
(a) Let \(i:Y\hookrightarrow Z\) be inclusion and \(r:Z\to Y\) a retraction. Then
\[
R=i\circ r:Z\to Z
\]
is continuous, and
\[
Y=\{z\in Z:R(z)=z\}.
\]
Since \(Z\) is Hausdorff, the equalizer of \(R\) and the identity map is closed. Hence \(Y\) is closed in \(Z\).

(b) If a two-point set \(A\subset\mathbb R^2\) were a retract, the retraction \(r:\mathbb R^2\to A\) would be a continuous surjection. But \(\mathbb R^2\) is connected, so its continuous image \(A\) would be connected, whereas a two-point subspace of the Hausdorff plane is disconnected. Contradiction.

(c) The radial map
\[
r:\mathbb R^2\setminus\{0\}\to S^1,
\qquad
r(x)=\frac{x}{\|x\|},
\]
is continuous and restricts to the identity on \(S^1\), so \(S^1\) is a retract of the punctured plane.

One should conjecture that \(S^1\) is not a retract of the whole plane. This is true; it is the classical no-retraction theorem for the disk/circle, proved later by algebraic-topological methods.
:::
