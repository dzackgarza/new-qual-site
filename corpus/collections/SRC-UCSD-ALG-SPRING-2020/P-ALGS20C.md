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

::: problem
Let $R$ be a Noetherian integral domain.
Show that the following conditions are equivalent:

(1) Every finitely generated $R$-module is a direct sum of cyclic $R$-modules.

(2) $R$ is a PID.
:::


::: {.solution}
<1>1. Assume first that \(R\) is a PID. Then every finitely generated \(R\)-module is a direct sum of cyclic \(R\)-modules.
::: {.proof}
This is the structure theorem for finitely generated modules over a PID: every finitely generated \(R\)-module is isomorphic to
\[
R^r\oplus R/(d_1)\oplus\cdots\oplus R/(d_t)
\]
for suitable \(r,t\) and nonzero \(d_i\) with \(d_i\mid d_{i+1}\). Each summand is cyclic.
:::

<1>2. Conversely, assume every finitely generated \(R\)-module is a direct sum of cyclic modules. Let \(I\lhd R\) be an ideal. Since \(R\) is Noetherian, \(I\) is finitely generated.
::: {.proof}
By definition, every ideal of a Noetherian ring is finitely generated as an \(R\)-module.
:::

<1>3. If \(I\ne0\), then the decomposition hypothesis gives
\[
I=C_1\oplus\cdots\oplus C_t
\]
with each \(C_j\) cyclic. Every nonzero cyclic summand \(C_j\) is isomorphic to \(R\).
::: {.proof}
Write \(C_j=Rc_j\subseteq I\subseteq R\). If \(c_j\ne0\), the map \(R\to C_j\), \(r\mapsto rc_j\), is injective because \(R\) is a domain, and it is surjective by definition. Thus \(C_j\cong R\).
:::

<1>4. At most one summand \(C_j\) is nonzero.
::: {.proof}
Let \(K=\operatorname{Frac}(R)\). Since \(I\subseteq R\), tensoring with \(K\) gives an injection
\[
I\otimes_R K\hookrightarrow R\otimes_R K\cong K,
\]
so \(\dim_K(I\otimes_R K)\le1\). On the other hand, each nonzero \(C_j\cong R\) contributes one copy of \(K\) after tensoring. Hence if two distinct summands were nonzero, \(I\otimes_RK\) would have dimension at least \(2\), contradiction.
:::

<1>5. Therefore every ideal of \(R\) is principal, so \(R\) is a PID.
::: {.proof}
The zero ideal is principal. If \(I\ne0\), then by <1>4 exactly one cyclic summand is nonzero, so \(I\) itself is cyclic as an \(R\)-module, say \(I=Ra\). Thus every ideal is principal. Since \(R\) is an integral domain, it is a PID.
:::
:::
