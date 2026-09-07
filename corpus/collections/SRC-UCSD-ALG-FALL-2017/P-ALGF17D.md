---
schema: qual/card@1
id: P-ALGF17D
kind: problem
title: Finitely generated module over a PID is flat iff torsion-free
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 4 of the official UCSD Algebra Qualifying Exam, Fall 2017; the definition of flatness and the claimed equivalence agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the tensor proof that flat modules over a domain are torsion-free and the PID structure-theorem argument that finite torsion-free modules are free and hence flat.
---

::: {.problem}
Let $R$ be a commutative ring with $1$.
An $R$-module $M$ is called flat if whenever $f \colon N \to P$ is an injective $R$-linear map of $R$-modules then the induced map
\[
M \otimes_R N \longrightarrow M \otimes_R P
\]
is also injective.
If $R$ is a PID and $M$ is a finitely generated $R$-module then show that $M$ is flat if and only if it is torsion free.
:::

::: {.solution}
<1>1. If $M$ is flat, then $M$ is torsion-free.
::: {.proof}
Assume $R$ is a PID and $M$ is flat.
Since a PID is an integral domain, multiplication by any nonzero element $r\in R$ defines an injective $R$-linear map
\[
\mu_r:R\longrightarrow R,
\qquad
x\longmapsto rx.
\]
Flatness of $M$ implies that the induced map
\[
1_M\otimes\mu_r:
M\otimes_RR\longrightarrow M\otimes_RR
\]
is injective.
Under the canonical identification
\[
M\otimes_RR\cong M,
\qquad
m\otimes a\longmapsto am,
\]
this map is exactly multiplication by $r$ on $M$:
\[
m\longmapsto rm.
\]
Hence
\[
rm=0,
\qquad
r\neq0
\]
forces $m=0$.
Thus $M$ is torsion-free.
:::

<1>2. If $M$ is finitely generated and torsion-free, then $M$ is free.
::: {.proof}
By the structure theorem for finitely generated modules over a PID,
\[
M\cong R^s\oplus T,
\]
where $T$ is the torsion submodule, equivalently a finite direct sum of cyclic modules of the form
\[
R/(d_i)
\]
with nonzero nonunits $d_i\in R$.
If $M$ is torsion-free, then
\[
T=0.
\]
Therefore
\[
M\cong R^s
\]
for some $s\ge0$, so $M$ is free.
:::

<1>3. Every free module is flat.
::: {.proof}
Let $F$ be a free $R$-module, say
\[
F\cong\bigoplus_{j\in J}R.
\]
For any $R$-module $N$,
\[
F\otimes_RN
\cong
\bigoplus_{j\in J}N.
\]
If $f:N\to P$ is injective, then the induced map
\[
F\otimes_RN\longrightarrow F\otimes_RP
\]
identifies with the direct sum of copies of $f$:
\[
\bigoplus_{j\in J}N
\longrightarrow
\bigoplus_{j\in J}P.
\]
A direct sum of injective maps is injective.
Hence $F$ is flat.
:::

<1>4. Therefore a finitely generated module over a PID is flat if and only if it is torsion-free.
::: {.proof}
If $M$ is flat, <1>1 gives torsion-freeness.
If $M$ is torsion-free and finitely generated, <1>2 makes it free, and <1>3 then makes it flat.
:::
:::
