---
schema: qual/card@1
id: E-WX8FM
kind: problem
title: Homeomorphisms extend to one-point compactifications
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Homeomorphisms
relations: []
review: draft
---

::: {.exercise}

If $f: X_1 \to X_2$ is a homeomorphism of locally compact Hausdorff spaces, show $f$ extends to a homeomorphism of their one-point compactifications.
:::

::: {.solution}
Let \(X_i^*=X_i\cup\{\infty_i\}\) be the one-point compactifications. Define
\[
f^*:X_1^*\to X_2^*,\qquad f^*(x)=f(x)\ (x\in X_1),\quad f^*(\infty_1)=\infty_2.
\]
This is bijective, with inverse extending \(f^{-1}\).

Continuity at ordinary points follows from continuity of \(f\). Let \(U\) be a neighborhood of \(\infty_2\). Then
\[
X_2^*\setminus U=K
\]
is a compact subset of \(X_2\). Since \(f^{-1}(K)\) is compact in \(X_1\),
\[
(f^*)^{-1}(U)=X_1^*\setminus f^{-1}(K)
\]
is a neighborhood of \(\infty_1\). Hence \(f^*\) is continuous at \(\infty_1\). The same argument applies to the inverse, so \(f^*\) is a homeomorphism.
:::
