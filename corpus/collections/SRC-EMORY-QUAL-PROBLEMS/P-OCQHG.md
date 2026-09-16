---
schema: qual/card@1
id: P-OCQHG
kind: problem
title: The field of fractions of a PID that is not a field is not a finitely generated
  module
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked the nonfield PID and fraction-field hypotheses in Linear Algebra 4 on PDF page 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked that a finite generating set has one nonzero common denominator and that divisibility of the entire fraction field forces equality with the original ring."
---

::: problem
Let $R$ be a principal ideal domain that is not a field, and write $F$ for its field of fractions.
Prove that $F$ is not a finitely generated $R$-module.
:::

::: solution
<1>1. Finite generation of $F$ would give a nonzero
$d\in R$ with $dF\subseteq R$.

::: proof
Suppose $F$ is generated over $R$ by finitely many
fractions $a_i/b_i$, where $a_i,b_i\in R$ and
$b_i\ne0$. Since $F\ne0$, the generating family
may be taken nonempty. Set $d=\prod_i b_i$, which
is nonzero because $R$ is a domain. Each
$d(a_i/b_i)=a_i\prod_{j\ne i}b_j$ belongs to $R$.
Multiplying any $R$-linear combination of the
generators by $d$ therefore gives an element of $R$.
Thus $dF\subseteq R$.
:::

<1>2. This forces $R$ to be a field, a contradiction.

::: proof
Since $d$ is a nonzero element of the field $F$,
multiplication by $d$ is a bijection of $F$ onto
itself: $x=d(x/d)$ for every $x\in F$. Thus
$F=dF\subseteq R$. The reverse inclusion is the
defining inclusion into the fraction field, so
$R=F$, contradicting the hypothesis that $R$ is
not a field. Hence $F$ is not finitely generated.
The argument uses only that $R$ is a nonfield
integral domain; principality is not needed.
:::
:::
