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
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
(a) Suppose $D$ is an integral domain and $M$ is a flat $D$-module.
Prove that $M$ is torsion-free.

(b) Suppose $D$ is a PID and $M$ is a finitely generated flat $D$-module.
Prove that $M$ is a free $D$-module.
:::


::: {.solution}
<1>1. Let \(0\ne d\in D\). Multiplication by \(d\) gives an injective \(D\)-linear map
\[
D\xrightarrow{\cdot d}D.
\]
::: {.proof}
Because \(D\) is an integral domain, \(dx=0\) with \(d\ne0\) implies \(x=0\).
:::

<1>2. Since \(M\) is flat, tensoring the injection in <1>1 with \(M\) preserves injectivity. Thus
\[
M\cong D\otimes_D M\xrightarrow{\cdot d\otimes 1}D\otimes_D M\cong M
\]
is injective.
::: {.proof}
Flatness means that tensoring with \(M\) preserves injections, equivalently finite exact sequences on the left. Under the standard identifications \(D\otimes_D M\cong M\), the induced map is multiplication by \(d\) on \(M\).
:::

<1>3. Therefore \(M\) is torsion-free.
::: {.proof}
If \(0\ne d\in D\) and \(dm=0\), then injectivity of multiplication by \(d\) from <1>2 gives \(m=0\). This is precisely torsion-freeness. This proves part (a).
:::

<1>4. Now suppose \(D\) is a PID and \(M\) is finitely generated and flat. By part (a), \(M\) is torsion-free.
::: {.proof}
A PID is an integral domain, so <1>3 applies.
:::

<1>5. A finitely generated torsion-free module over a PID is free. Hence \(M\) is free.
::: {.proof}
By the structure theorem for finitely generated modules over a PID,
\[
M\cong D^r\oplus \bigoplus_{j=1}^s D/(a_j)
\]
for nonzero nonunits \(a_j\) when torsion summands occur. Torsion-freeness forces \(s=0\), so \(M\cong D^r\).
:::
:::
