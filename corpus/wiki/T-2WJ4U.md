---
schema: qual/card@1
id: T-2WJ4U
kind: theorem
title: "Hadamard factorization"
classification:
  areas:
  - complex-analysis
  topics:
  - weierstrass-factorization
  - entire-functions
  - zeros
relations: []
review: draft
---
:::{.theorem title="Hadamard factorization"}
Write
\[
E_{p}(z)= \begin{cases}
1-z & n=0 \\ 
(1-z) \exp \left(z+\frac{z^{2}}{2}+\cdots+\frac{z^{n}}{n}\right) & \text { otherwise }
\end{cases}
,\]
and define the **order** of an entire function $f$ to be the infimum over $p$ where there exists some $R$ such that $\abs{f(z)} \leq e^{\abs{z}^p}$ for $\abs{z} > R$.
Suppose $f$ is entire of order $p$, write $\ts{z_k}_{k\leq n}$ for its set of nonzero zeros repeated with multiplicity, and suppose $z=0$ is a zero of $f$ of order $m$.
Then there is a decomposition
\[
f(z) = z^m e^{g(z)}\prod_{k\geq 1} E_p\qty{z\over z_k}
,\]
where $\deg(g) \leq p$.
:::
