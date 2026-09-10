---
schema: qual/card@1
id: P-A8AAB
kind: problem
title: If $A \oplus A \cong B \oplus B$ for finitely generated modules over a PID
  then $A \cong B$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared the PID, finite-generation, and direct-sum hypotheses with page 5 of the original scan, Rings and modules 4."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $R$ be a principal ideal domain and $A$ and $B$ be finitely generated $R$-modules.
Show that if $A \oplus A \cong B \oplus B$ then $A \cong B$.
:::

::: solution
<1>1. A finitely generated $R$-module $M$ has a decomposition
$$
M\cong R^{r_M}\oplus
\bigoplus_{p}\bigoplus_{e\geq1}
\bigl(R/(p^e)\bigr)^{m_M(p,e)},
$$
where $p$ runs through one representative of each associate class of
prime elements of $R$, the integers $r_M$ and $m_M(p,e)$ are
nonnegative, and only finitely many $m_M(p,e)$ are nonzero.
These integers are uniquely determined by $M$.

::: proof
This is the elementary-divisor form of the structure theorem for
finitely generated modules over a PID [@DF04]. Choosing one
representative of each associate class fixes the indexing of the
invariants for both $A$ and $B$. When $R$ is a field, there are no prime
elements and the displayed torsion sum is empty.
:::

<1>2. The assumed isomorphism implies equality of all invariants of
$A$ and $B$, and hence $A\cong B$.

::: proof
Taking a direct sum of two copies doubles the free rank and every
elementary-divisor multiplicity. Thus the uniqueness in step <1>1,
applied to $A\oplus A\cong B\oplus B$, gives
$$
2r_A=2r_B,\qquad
2m_A(p,e)=2m_B(p,e)\quad\text{for every }p,e.
$$
These are equalities of finite nonnegative integers, so division by
$2$ gives $r_A=r_B$ and $m_A(p,e)=m_B(p,e)$ for every pair $p,e$.
The decompositions of $A$ and $B$ in step <1>1 therefore have precisely
the same summands with the same multiplicities. Matching those
summands gives an $R$-module isomorphism $A\cong B$.
:::
:::
