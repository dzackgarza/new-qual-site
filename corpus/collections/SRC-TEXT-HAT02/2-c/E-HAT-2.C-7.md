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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 7, printed page
    184; the statement matches word for word. Proof checked: with field coefficients
    the Hopf trace formula holds verbatim (additivity of trace on the short exact
    sequences of cycles, boundaries and homology, with the boundary terms cancelling
    in the alternating sum), and Hatcher's proof of Theorem 2C.3 (p. 180) uses only
    a subdivision and a simplicial map g homotopic to f with g(σ) ∩ σ = ∅ together
    with the trace formula, both of which are coefficient-independent over a field.
    No defect.
---
---

::: {.problem}
Verify that the Lefschetz fixed point theorem holds also when $\tau(f)$ is defined using homology with coefficients in a field $F$.
:::

::: {.solution}
Let $F$ be a field and define
$$
\tau_F(f)=\sum_n(-1)^n\operatorname{tr}\bigl(f_*:H_n(X;F)\to H_n(X;F)\bigr).
$$

::: pf

::: {.pf-step #s1}

For a finite chain complex of finite-dimensional $F$-vector spaces and a chain endomorphism $T$, one has
$$
\sum_n(-1)^n\operatorname{tr}(T\restrict C_n)
=
\sum_n(-1)^n\operatorname{tr}(T_*\restrict H_n).
$$

::: pf-proof

Use the invariant subspaces $B_n\subset Z_n\subset C_n$. Additivity of trace in short exact sequences gives
$$
\operatorname{tr}(T\restrict C_n)=\operatorname{tr}(T\restrict Z_n)+\operatorname{tr}(T\restrict B_{n-1})
$$
and
$$
\operatorname{tr}(T\restrict Z_n)=\operatorname{tr}(T\restrict B_n)+\operatorname{tr}(T_*\restrict H_n).
$$
Summing with alternating signs cancels the boundary terms.

:::

:::

::: {.pf-step #s2}

If $f:X\to X$ has no fixed points, then after the subdivisions and simplicial approximation used in Hatcher's proof of the Lefschetz theorem there is a simplicial map $g$ homotopic to $f$ such that
$$
g(\sigma)\cap\sigma=\varnothing
$$
for every simplex $\sigma$ of the domain subdivision.

::: pf-proof

This is the geometric part of Hatcher's proof and is independent of the coefficient ring.

:::

:::

::: {.pf-step #s3}

The induced map on each simplicial chain group has trace zero over $F$.

::: pf-proof

The condition in step [](#s2){.pf-ref} says that no oriented simplex maps with a nonzero coefficient to itself, so the matrix of the chain map has zero diagonal. This statement is valid over every field.

:::

:::

::: pf-step

Hence a fixed-point-free map has
$$
\tau_F(f)=0.
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s3){.pf-ref} the alternating trace on homology equals the zero alternating trace on chains. Homotopy invariance identifies the homology maps of $f$ and $g$.

:::

:::

:::

Taking the contrapositive proves the field-coefficient Lefschetz theorem:
$$
\boxed{\tau_F(f)\ne0\Longrightarrow f\text{ has a fixed point}.}
$$
:::
