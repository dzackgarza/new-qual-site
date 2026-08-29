---
schema: qual/card@1
id: E-DR5LY
kind: exercise
title: Hadamard expansion of $\sin$
classification:
  areas:
  - complex-analysis
  topics:
  - Weierstrass Factorization
  - Entire Functions
  - Zeros
  - Trigonometry
relations: []
review: draft
---

:::{.exercise}
Find a Hadamard expansion of $\sin(\pi z)$.
:::


:::{.solution}
$\sin(\pi z)$ has order 1, and its zero set is $z_k = k$ for $k\in \ZZ$.
So one can write
\[
\sin(\pi z) = ze^{az+b} \prod_{k\in \ZZ\smz} \qty{1 - {z\over k}}e^{z\over k} = ze^{az+b} \prod_{k\geq 1}\qty{1 - {z^2\over k^2}}
.\]
Determine $e^b = \pi$ by considering $\sin(\pi z)/z$ as $z\to 0$, and use that $\sin(\pi z)$ is odd and the product factor is even to conclude $e^{az}$ is even and thus equal to 1.
This yields
\[
\sin(\pi z) = \pi z \prod_{k\geq 1}{1- {z^2\over k^2}}
.\]


:::




