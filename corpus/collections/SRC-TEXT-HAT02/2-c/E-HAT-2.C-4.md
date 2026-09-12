---
schema: qual/card@1
id: E-HAT-2.C-4
kind: problem
title: Lefschetz number of simplicial homeomorphism equals Euler characteristic of fixed point set
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Euler Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
---

If $X$ is a finite simplicial complex and $f: X \to X$ is a simplicial homeomorphism, show that the Lefschetz number $\tau(f)$ equals the Euler characteristic of the set of fixed points of $f$.
In particular, $\tau(f)$ is the number of fixed points if the fixed points are isolated.
[Hint: Barycentrically subdivide $X$ to make the fixed point set a subcomplex.]

::: {.solution}
Let $F=\operatorname{Fix}(f)\subset X$.

<1>1. After barycentrically subdividing $X$, we may assume that $F$ is a subcomplex and that every simplex carried to itself by $f$ is fixed pointwise.
::: {.proof}
A vertex of the barycentric subdivision is the barycenter of a simplex $\sigma$ of the original complex. A simplex in the subdivision is a strictly nested chain
\[
\sigma_0\subsetneq\sigma_1\subsetneq\cdots\subsetneq\sigma_r.
\]
If $f$ carries this subdivided simplex to itself, it must preserve each vertex because the dimensions of the $\sigma_i$ are distinct. Hence it fixes the simplex pointwise. The union of such simplices is exactly the fixed-point set, so $F$ is a subcomplex.
:::

<1>2. On the simplicial chain group $C_n(X;\mathbb Q)$, the trace of $f_*$ equals the number $c_n(F)$ of $n$-simplices of $F$.
::: {.proof}
The simplicial homeomorphism $f$ permutes the oriented $n$-simplices. A simplex not carried to itself contributes zero to the diagonal of the matrix. By <1>1, a simplex carried to itself is fixed pointwise, hence preserves its chosen orientation and contributes $+1$. These are exactly the $n$-simplices of $F$.
:::

<1>3. The alternating trace on simplicial chains equals the alternating trace on homology:
\[
\sum_n(-1)^n\operatorname{tr}(f_*|C_n)
=
\sum_n(-1)^n\operatorname{tr}(f_*|H_n).
\]
::: {.proof}
For a finite chain complex of finite-dimensional vector spaces, apply additivity of trace to
\[
0\to Z_n\to C_n\to B_{n-1}\to0
\]
and
\[
0\to B_n\to Z_n\to H_n\to0.
\]
The boundary-space trace terms cancel in the alternating sum.
:::

<1>4. Therefore
\[
\boxed{\tau(f)=\sum_n(-1)^n c_n(F)=\chi(F).}
\]
::: {.proof}
Combine <1>2 and <1>3. The alternating number of simplices of a finite simplicial complex is its Euler characteristic.
:::

If the fixed points are isolated, the fixed subcomplex has only $0$-simplices, so
\[
\tau(f)=\#F.
\]
:::
