---
schema: qual/card@1
id: E-HAT-2.C-7
kind: problem
title: Lefschetz fixed point theorem with field coefficients
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
---

::: {.problem}
Verify that the Lefschetz fixed point theorem holds also when $\tau(f)$ is defined using homology with coefficients in a field $F$.
:::

::: {.solution}
Let $F$ be a field and define
\[
\tau_F(f)=\sum_n(-1)^n\operatorname{tr}\bigl(f_*:H_n(X;F)\to H_n(X;F)\bigr).
\]

<1>1. For a finite chain complex of finite-dimensional $F$-vector spaces and a chain endomorphism $T$, one has
\[
\sum_n(-1)^n\operatorname{tr}(T|C_n)
=
\sum_n(-1)^n\operatorname{tr}(T_*|H_n).
\]
::: {.proof}
Use the invariant subspaces $B_n\subset Z_n\subset C_n$. Additivity of trace in short exact sequences gives
\[
\operatorname{tr}(T|C_n)=\operatorname{tr}(T|Z_n)+\operatorname{tr}(T|B_{n-1})
\]
and
\[
\operatorname{tr}(T|Z_n)=\operatorname{tr}(T|B_n)+\operatorname{tr}(T_*|H_n).
\]
Summing with alternating signs cancels the boundary terms.
:::

<1>2. If $f:X\to X$ has no fixed points, then after the subdivisions and simplicial approximation used in Hatcher's proof of the Lefschetz theorem there is a simplicial map $g$ homotopic to $f$ such that
\[
g(\sigma)\cap\sigma=\varnothing
\]
for every simplex $\sigma$ of the domain subdivision.
::: {.proof}
This is the geometric part of Hatcher's proof and is independent of the coefficient ring.
:::

<1>3. The induced map on each simplicial chain group has trace zero over $F$.
::: {.proof}
The condition in <1>2 says that no oriented simplex maps with a nonzero coefficient to itself, so the matrix of the chain map has zero diagonal. This statement is valid over every field.
:::

<1>4. Hence a fixed-point-free map has
\[
\tau_F(f)=0.
\]
::: {.proof}
By <1>1 and <1>3 the alternating trace on homology equals the zero alternating trace on chains. Homotopy invariance identifies the homology maps of $f$ and $g$.
:::

Taking the contrapositive proves the field-coefficient Lefschetz theorem:
\[
\boxed{\tau_F(f)\ne0\Longrightarrow f\text{ has a fixed point}.}
\]
:::
