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
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Recasts the proof explicitly as Hatcher's own proof of Theorem 2C.3, pp.180-181, read with
    coefficients in an arbitrary field F. The card now includes Hatcher's retraction step, the
    positive uniform distance and two subdivisions producing g with g(sigma) disjoint from sigma,
    the induced chain endomorphism on H_n(K^n,K^{n-1};F), and the trace form of Theorem 2.44
    over F. No independent fixed-point argument is being given a source label.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Checked every step against the book. The retraction leaves fixed points unchanged and makes
    r_* projection onto a direct summand, so the Lefschetz number is preserved over F. Hatcher's
    metric construction gives g( sigma) cap sigma empty, hence zero diagonal in every field;
    additivity of trace on finite-dimensional exact sequences then gives zero on homology.
---
---

::: {.problem}
Verify that the Lefschetz fixed point theorem holds also when $\tau(f)$ is defined using homology with coefficients in a field $F$.
:::

::: {.solution}
Read **Hatcher's proof of Theorem 2C.3, printed pp. 180--181**, with coefficients in the field $F$. Its geometric and algebraic steps need no change.

::: pf

::: {.pf-step #retract}
The general case reduces to a finite simplicial complex, with the Lefschetz number unchanged.

::: pf-proof
Let $r:K\to X$ be a retraction of a finite simplicial complex $K$ onto $X$. As in the book, $fr:K\to K$ has exactly the same fixed points as $f:X\to X$. Since $r_*:H_n(K;F)\to H_n(X;F)$ is projection onto a direct summand,
$$
\operatorname{tr}(f_*r_*)=\operatorname{tr}(f_*)
$$
in every degree. Hence $\tau_F(fr)=\tau_F(f)$.
:::

:::

::: {.pf-step #distance}
If $f$ has no fixed points on a finite simplicial complex $X$, there are subdivisions $L$ of $X$ and $K$ of $L$, and a simplicial map $g:K\to L$ homotopic to $f$, such that
$$
g(\sigma)\cap\sigma=\varnothing
$$
for every simplex $\sigma$ of $K$.

::: pf-proof
Use Hatcher's metric $d$ on $X$. Compactness and $d(x,f(x))>0$ give an $\varepsilon>0$ with $d(x,f(x))>\varepsilon$ for every $x$. Choose $L$ so all simplex stars have diameter less than $\varepsilon/2$, then use simplicial approximation to choose $K$ and $g$. For $x\in\sigma$, $g(\sigma)$ lies within $\varepsilon/2$ of $f(x)$ while $\sigma$ lies within $\varepsilon/2$ of $x$, so $g(\sigma)\cap\sigma=\varnothing$. This is exactly the construction on pp. 180--181 and does not involve coefficients.
:::

:::

::: {.pf-step #chains}
The induced endomorphism of the simplicial cellular chain complex over $F$ has alternating trace zero.

::: pf-proof
For each $n$, $g(K^n)\subset K^n$, so $g$ induces an endomorphism of $H_n(K^n,K^{n-1};F)$. These are finite-dimensional $F$-vector spaces. By step [](#distance){.pf-ref}, no $n$-simplex maps with a nonzero coefficient to itself, hence the matrix has zero diagonal and therefore zero trace. The alternating sum is consequently zero.
:::

:::

::: {.pf-step #trace}
The alternating trace on homology is also zero, so $\tau_F(f)=0$.

::: pf-proof
This is Theorem 2.44 with trace replacing rank, exactly as in Hatcher. Trace is additive for an endomorphism of a short exact sequence of finite-dimensional $F$-vector spaces. Applying that to cycles, boundaries, and homology makes the boundary trace terms cancel in the alternating sum, so the alternating trace on chains equals the alternating trace on homology. Step [](#chains){.pf-ref} gives the former as zero, and homotopy invariance gives $\tau_F(f)=\tau_F(g)=0$.
:::

:::

:::

Taking the contrapositive gives the theorem: $\tau_F(f)\ne0$ implies that $f$ has a fixed point.
:::
