---
schema: qual/card@1
id: T-5SKNT
kind: theorem
title: Symmetry principle
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Holomorphic Functions
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, and put $\Omega^+\coloneqq\Omega\cap\ts{\Im z>0}$, $\Omega^-\coloneqq\Omega\cap\ts{\Im z<0}$, and $I\coloneqq\Omega\cap\RR$.
Let $f^+$ be [[D-E7A5W|holomorphic]] on $\Omega^+$ and $f^-$ holomorphic on $\Omega^-$, and suppose both extend continuously to $I$ with $f^+(x)=f^-(x)$ for all $x\in I$.
Then the function
$$
f(z)\coloneqq
\begin{cases}
f^+(z) & z\in\Omega^+,\\
f^-(z) & z\in\Omega^-,\\
f^+(z)=f^-(z) & z\in I,
\end{cases}
$$
is holomorphic on $\Omega$.
:::
