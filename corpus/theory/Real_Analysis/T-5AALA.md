---
schema: qual/card@1
id: T-5AALA
kind: theorem
title: Parseval
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Bases
relations: []
review: draft
---

:::{.theorem}
Let $\ts{u_n}_{n\in A}$ be an orthonormal set in a Hilbert space $\mch$.
TFAE:

- Completeness: $\ts{u_n}$ is a complete basis, i.e. $\inner{x}{u_n}=0$ for all $n$ implies $x=0$
- Parseval's identity:
\[
\sum_{n\in A} \abs{ \inner{x}{u_n} }^2 = \norm{x}^2_{\mch}
.\]

- Every $x\in \mch$ can be expressed uniquely as 
\[
x = \sum_{n\in A} \inner{x}{u_n}u_n
,\]
where the sum has only countably many nonzero terms.
:::
