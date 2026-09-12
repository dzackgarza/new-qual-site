---
schema: qual/card@1
id: E-UX2C4
kind: problem
title: Behavior of limit point compactness under images, closed subsets, and Hausdorff ambient spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $X$ be limit point compact.

(a) If $f: X \to Y$ is continuous, does it follow that $f(X)$ is limit point compact?

(b) If $A$ is a closed subset of $X$, does it follow that $A$ is limit point compact?

(c) If $X$ is a subspace of the Hausdorff space $Z$, does it follow that $X$ is closed in $Z$?

We comment that it is not in general true that the product of two limit point compact spaces is limit point compact, even if the Hausdorff condition is assumed.
But the examples are fairly sophisticated.
See [S-S], Example 112.
:::

::: {.solution}
(a) Yes. Let \(B\subset f(X)\) be infinite. For each \(b\in B\), choose one point \(x_b\in X\) with \(f(x_b)=b\). Then
\[
A=\{x_b:b\in B\}
\]
is infinite, so it has a limit point \(x\in X\). We claim \(f(x)\) is a limit point of \(B\). Let \(V\) be a neighborhood of \(f(x)\). Then \(f^{-1}(V)\) is a neighborhood of \(x\), so it contains some \(x_b\in A\) distinct from \(x\). Since the points of \(A\) were chosen with distinct images, we may choose such a point with \(b\ne f(x)\). Thus \(V\) contains a point of \(B\setminus\{f(x)\}\). Therefore \(f(X)\) is limit point compact.

(b) Yes. Let \(A\subset X\) be closed, and let \(B\subset A\) be infinite. Since \(X\) is limit point compact, \(B\) has a limit point \(x\in X\). Every limit point of \(B\subset A\) lies in \(\overline A=A\), so \(x\in A\). Hence \(A\) is limit point compact.

(c) No. Let
\[
X=[0,\omega_1)
\]
with the order topology, regarded as a subspace of the Hausdorff compact ordinal space
\[
Z=[0,\omega_1].
\]
The space \(X\) is countably compact: every countable subset of \(X\) has supremum \(<\omega_1\), and the standard order-topology argument gives a cluster point; equivalently, every countable open cover has a finite subcover. Hence, since \(X\) is \(T_1\), it is limit point compact by the preceding exercise. But \(X\) is not closed in \(Z\), since its closure contains the missing endpoint \(\omega_1\). Thus a limit point compact subspace of a Hausdorff space need not be closed.
:::
