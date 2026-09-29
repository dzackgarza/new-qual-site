---
schema: qual/card@1
id: P-AGDIVDEGREE
kind: problem
title: The degree of a divisor
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Degree
  - Definitions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's follow-up asking for the degree of a divisor on a curve.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What is the degree of a divisor?
:::

::: {.solution}
Let $C$ be a proper integral curve over a field $k$ and let
\[
D=\sum_{p\in C^{(1)}}n_p[p]
\]
be a Weil divisor.

::: pf

::: {.pf-step #degree-definition}
The degree of $D$ is
\[
\boxed{
\deg D
=\sum_p n_p[\kappa(p):k].
}
\]

::: pf-proof
Each closed point $p$ has degree
\[
\deg[p]=[\kappa(p):k].
\]
Degree is extended additively from prime divisors to all Weil divisors, giving the displayed formula.
:::

:::

::: {.pf-step #degree-alg-closed}
If $k$ is algebraically closed, then
\[
\boxed{\deg D=\sum_p n_p.}
\]

::: pf-proof
Every closed point of a finite-type $k$-curve has residue field $k$ when $k$ is algebraically closed, so
\[
[\kappa(p):k]=1
\]
for all $p$.  Apply step [](#degree-definition){.pf-ref}.
:::

:::

::: {.pf-step #cartier-degree}
For a Cartier divisor $D$ on a smooth curve,
\[
\boxed{\deg D=\deg\mathcal O_C(D).}
\]

::: pf-proof
On a smooth curve, Cartier and Weil divisors are canonically identified.  The associated invertible sheaf $\mathcal O_C(D)$ has degree equal to the degree of the corresponding Weil divisor; equivalently,
\[
\deg\mathcal O_C(D)
=\chi(\mathcal O_C(D))-\chi(\mathcal O_C)
=\deg D
\]
by Riemann--Roch.
:::

:::

::: {.pf-step #principal-degree-zero}
Every principal divisor has degree zero:
\[
\boxed{\deg\operatorname{div}(f)=0
\qquad(f\in K(C)^*).}
\]

::: pf-proof
The principal divisor $\operatorname{div}(f)$ corresponds to the trivial line bundle, because multiplication by $f$ gives
\[
\mathcal O_C(\operatorname{div}(f))\cong\mathcal O_C.
\]
Applying step [](#cartier-degree){.pf-ref} gives
\[
\deg\operatorname{div}(f)=\deg\mathcal O_C=0.
\]

Equivalently, the total order of the zeros of a rational function, counted with residue-field degrees, equals the total order of its poles.
:::

:::

::: {.pf-step #degree-descends}
Consequently degree descends to divisor classes and to the Picard group:
\[
\deg:\operatorname{Pic}(C)\longrightarrow\mathbb Z.
\]

::: pf-proof
Linearly equivalent divisors differ by a principal divisor, whose degree is zero by step [](#principal-degree-zero){.pf-ref}.  Thus degree is constant on linear-equivalence classes.  On a smooth curve these classes identify with line bundles.
:::

:::

::: pf-qed
Step [](#degree-definition){.pf-ref} is the definition, with steps [](#degree-alg-closed){.pf-ref}, [](#cartier-degree){.pf-ref}, [](#principal-degree-zero){.pf-ref} and [](#degree-descends){.pf-ref} recording its standard equivalent forms and consequences.
:::

:::
:::
