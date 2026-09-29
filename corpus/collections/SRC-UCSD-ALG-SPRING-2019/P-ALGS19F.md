---
schema: qual/card@1
id: P-ALGS19F
kind: problem
title: "Flat modules are torsion-free; finitely generated flat over PID is free"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
(a) Suppose $D$ is an integral domain and $M$ is a flat $D$-module.
Prove that $M$ is torsion-free.

(b) Suppose $D$ is a PID and $M$ is a finitely generated flat $D$-module.
Prove that $M$ is a free $D$-module.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let \(0\neq d\in D\). Multiplication by \(d\) gives an injective \(D\)-linear map
\[
\mu_d:D\longrightarrow D,
\qquad x\longmapsto dx.
\]

::: pf-proof

Because \(D\) is an integral domain and \(d\neq0\), the equality \(dx=0\) implies \(x=0\).

:::

:::

::: {.pf-step #s2}

If \(M\) is flat, then multiplication by \(d\) on \(M\) is injective.

::: pf-proof

Tensor the injection \(\mu_d:D\to D\) from step [](#s1){.pf-ref} with the flat \(D\)-module \(M\). Flatness preserves injectivity, so
\[
\mu_d\otimes_D 1_M:D\otimes_D M\longrightarrow D\otimes_D M
\]
is injective. Under the canonical identifications \(D\otimes_D M\cong M\), this map is exactly \(m\mapsto dm\).

:::

:::

::: {.pf-step #s3}

Thus every flat \(D\)-module is torsion-free.

::: pf-proof

Suppose \(0\neq d\in D\) and \(dm=0\) for some \(m\in M\). By step [](#s2){.pf-ref}, multiplication by \(d\) is injective on \(M\), so \(m=0\). This is precisely torsion-freeness.

:::

:::

::: {.pf-step #s4}

Now suppose \(D\) is a PID and \(M\) is finitely generated and flat. Then \(M\) is torsion-free.

::: pf-proof

Apply part (a), namely step [](#s3){.pf-ref}, since every PID is an integral domain.

:::

:::

::: {.pf-step #s5}

By the structure theorem for finitely generated modules over a PID, there are an integer \(r\ge0\) and nonzero nonunits \(d_1,\dots,d_s\in D\) such that
\[
M\cong D^r\oplus\bigoplus_{j=1}^s D/(d_j).
\]

::: pf-proof

This is the invariant-factor form of the structure theorem for finitely generated modules over a PID.

:::

:::

::: pf-step

The torsion-free condition forces \(s=0\), so \(M\cong D^r\) is free.

::: pf-proof

If a summand \(D/(d_j)\) were present, the nonzero class of \(1\) would be annihilated by the nonzero element \(d_j\), producing torsion. This contradicts step [](#s4){.pf-ref}. Hence no torsion summand occurs, and step [](#s5){.pf-ref} reduces to \(M\cong D^r\).

:::

:::

:::

:::
