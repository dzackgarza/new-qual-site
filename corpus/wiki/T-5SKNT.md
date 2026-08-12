---
schema: qual/card@1
id: T-5SKNT
kind: theorem
title: "Symmetry Principle"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---

::: {.theorem title="Symmetry Principle"}
Suppose that $f^+$ is holomorphic on $\Omega^+$ and $f^-$ is holomorphic on $\Omega^-$, and $f$ extends continuously to $I$ with $f^+(x) = f^-(x)$ for $x\in I$.
Then the following piecewise-defined function is holomorphic on $\Omega$:
\[
f(z) 
\da
\begin{cases}
f^+(z) & z\in \Omega^+ 
\\
f^-(z) & z\in \Omega^-
\\
f^+(z) = f^-(z) & z\in I.
\end{cases}
\]
:::
