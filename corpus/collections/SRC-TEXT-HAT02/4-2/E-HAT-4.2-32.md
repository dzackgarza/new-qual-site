---
schema: qual/card@1
id: E-HAT-4.2-32
kind: exercise
title: "Fiber bundles $S^k \\to S^m \\to S^n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

Show that if $S^k \to S^m \to S^n$ is a fiber bundle, then $k = n-1$ and $m = 2n-1$.

::: solution
**Theorem.**  
For a sphere bundle $S^k\to S^m\to S^n$, one has $k=n-1$ and $m=2n-1$.

*Proof by cohomological spectral sequence.*

1. In the Serre spectral sequence for
   $S^k\to S^m\overset{p}{\to} S^n$, with $\mathbb Z$-coefficients,
   \[
   E_2^{p,q}=H^p(S^n;H^q(S^k;\mathbb Z)).
   \]
2. The only nonzero entries are:
   \[
   E_2^{0,0}\cong E_2^{n,0}\cong E_2^{0,k}\cong E_2^{n,k}\cong\mathbb Z.
   \]
3. Since $S^m$ has cohomology only in degrees $0,m$, the class at $(n,0)$
   must be killed in the spectral sequence.
4. The only differential that can hit $(n,0)$ is
   \[
   d_{k+1}:E_{k+1}^{0,k}\to E_{k+1}^{k+1,0}.
   \]
   Hence $k+1=n$.
5. Then the class at $(n,0)$ is killed and the class at $(n,k)$ survives to total degree
   \[
   n+k=2n-1,
   \]
   giving the top cohomology of $S^{2n-1}$.

Therefore $k=n-1$ and $m=2n-1$. ∎
:::
