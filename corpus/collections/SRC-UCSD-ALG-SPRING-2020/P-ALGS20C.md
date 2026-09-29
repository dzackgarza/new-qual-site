---
schema: qual/card@1
id: P-ALGS20C
kind: problem
title: "Noetherian domain: every finitely generated module is a direct sum of cyclic modules if and only if it is a PID"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
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

::: {.problem}
Let $R$ be a Noetherian integral domain.
Show that the following conditions are equivalent:

(1) Every finitely generated $R$-module is a direct sum of cyclic $R$-modules.

(2) $R$ is a PID.
:::

::: {.solution}

::: pf

::: pf-step

Assume first that \(R\) is a PID. Then every finitely generated \(R\)-module is a direct sum of cyclic \(R\)-modules.

::: pf-proof

This is the structure theorem for finitely generated modules over a PID: every finitely generated \(R\)-module is isomorphic to
\[
R^r\oplus R/(d_1)\oplus\cdots\oplus R/(d_t)
\]
for suitable \(r,t\) and nonzero \(d_i\) with \(d_i\mid d_{i+1}\). Each summand is cyclic.

:::

:::

::: pf-step

Conversely, assume every finitely generated \(R\)-module is a direct sum of cyclic modules. Let \(I\lhd R\) be an ideal. Since \(R\) is Noetherian, \(I\) is finitely generated.

::: pf-proof

By definition, every ideal of a Noetherian ring is finitely generated as an \(R\)-module.

:::

:::

::: pf-step

If \(I\ne0\), then the decomposition hypothesis gives
\[
I=C_1\oplus\cdots\oplus C_t
\]
with each \(C_j\) cyclic. Every nonzero cyclic summand \(C_j\) is isomorphic to \(R\).

::: pf-proof

Write \(C_j=Rc_j\subseteq I\subseteq R\). If \(c_j\ne0\), the map \(R\to C_j\), \(r\mapsto rc_j\), is injective because \(R\) is a domain, and it is surjective by definition. Thus \(C_j\cong R\).

:::

:::

::: {.pf-step #s4}

At most one summand \(C_j\) is nonzero.

::: pf-proof

Let \(K=\operatorname{Frac}(R)\). Since \(I\subseteq R\), tensoring with \(K\) gives an injection
\[
I\otimes_R K\hookrightarrow R\otimes_R K\cong K,
\]
so \(\dim_K(I\otimes_R K)\le1\). On the other hand, each nonzero \(C_j\cong R\) contributes one copy of \(K\) after tensoring. Hence if two distinct summands were nonzero, \(I\otimes_RK\) would have dimension at least \(2\), contradiction.

:::

:::

::: pf-step

Therefore every ideal of \(R\) is principal, so \(R\) is a PID.

::: pf-proof

The zero ideal is principal. If \(I\ne0\), then by step [](#s4){.pf-ref} exactly one cyclic summand is nonzero, so \(I\) itself is cyclic as an \(R\)-module, say \(I=Ra\). Thus every ideal is principal. Since \(R\) is an integral domain, it is a PID.

:::

:::

:::

:::
