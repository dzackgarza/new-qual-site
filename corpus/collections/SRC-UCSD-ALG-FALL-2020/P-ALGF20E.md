---
schema: qual/card@1
id: P-ALGF20E
kind: problem
title: Flat implies torsion-free; converse for f.g.\ modules over a PID
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
  note: Checked against Problem 5 of the official UCSD Algebra Qualifying Exam, Fall 2020 source; both flatness assertions agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified torsion-freeness by tensoring multiplication by a nonzero scalar, and the PID converse via the finitely generated module structure theorem.
---

::: problem
Suppose that $D$ is an integral domain and $M$ is a $D$-module.

(1) Prove that if $M$ is flat, then it is torsion-free.

(2) Prove that if $D$ is a PID, and $M$ is finitely generated and torsion-free, then $M$ is flat.
:::

::: {.solution}
<1>1. If $M$ is flat, then multiplication by every nonzero $d\in D$ is injective on $M$.
::: {.proof}
Fix $0\ne d\in D$. Since $D$ is an integral domain, multiplication by $d$ gives an injective $D$-linear map
\[
0\longrightarrow D\xrightarrow{\,\cdot d\,}D.
\]
Because $M$ is flat, tensoring with $M$ preserves this injection:
\[
0\longrightarrow D\otimes_D M
\xrightarrow{\,(\cdot d)\otimes 1_M\,}
D\otimes_D M.
\]
Under the canonical identification
\[
D\otimes_D M\cong M,
\qquad
a\otimes m\longmapsto am,
\]
this map is exactly
\[
M\longrightarrow M,
\qquad
m\longmapsto dm.
\]
Hence $dm=0$ implies $m=0$.
:::

<1>2. Therefore every flat $D$-module is torsion-free.
::: {.proof}
Torsion-freeness over a domain means precisely that for every $0\ne d\in D$, the equation $dm=0$ forces $m=0$. This is <1>1.
:::

<1>3. If $D$ is a PID and $M$ is finitely generated and torsion-free, then $M$ is a finite-rank free $D$-module.
::: {.proof}
By the structure theorem for finitely generated modules over a PID,
\[
M\cong D^r\oplus T
\]
for some $r\ge0$, where $T$ is the torsion submodule of $M$. Since $M$ is torsion-free,
\[
T=0.
\]
Thus
\[
M\cong D^r.
\]
:::

<1>4. Every free $D$-module is flat.
::: {.proof}
For a free module $D^r$ and any $D$-module $X$,
\[
X\otimes_D D^r\cong X^r.
\]
Finite direct sums preserve injections and exact sequences. Hence the functor
\[
-\otimes_D D^r
\]
is exact, so $D^r$ is flat.
:::

<1>5. If $D$ is a PID and $M$ is finitely generated and torsion-free, then $M$ is flat.
::: {.proof}
By <1>3, $M$ is free, and by <1>4 every free module is flat. This proves part (2).
:::
:::
