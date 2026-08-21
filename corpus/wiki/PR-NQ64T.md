---
schema: qual/card@1
id: PR-NQ64T
kind: proposition
title: Radius of Convergence by the Root Test
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
relations: []
review: draft
---

:::{.proposition title="Radius of Convergence by the Root Test"}
For $f(z) = \sum_{k\in \NN} c_k z^k$, defining
\[
{1\over R} \da \limsup_{k} \abs{a_k}^{1\over k}
,\]
then $f$ converges absolutely and uniformly for $D_R \da\abs{z} < R$ and diverges for $\abs{z} > R$.
So the radius of convergence is given by
\[
R = {1\over \limsup_n \abs{a_n}^{1\over n}}
.\]

Moreover $f$ is holomorphic in $D_R$, can be differentiated term-by-term, and $f' = \sum_{k\in \NN} n c_k z^k$.
:::
