---
schema: qual/card@1
id: P-LHIOI
kind: problem
title: If $A=Ra$ with $ra=0$ and $(r,s)=(1)$, then $A=sA$ and $A[s]=0$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Cyclic Groups
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $R$ be a commutative ring, let $A=Ra$ be a cyclic $R$-module, and suppose
\[
ra=0,
\qquad
(r,s)=R.
\]
Show that
\[
A=sA
\qquad\text{and}\qquad
A[s]=\{x\in A:sx=0\}=0.
\]
:::

::: {.solution}
Choose $u,v\in R$ with
\[
ur+vs=1.
\]
Then
\[
a=(ur+vs)a=u(ra)+v(sa)=vsa=s(va),
\]
so $a\in sA$. Since $a$ generates $A$, this gives
\[
A\subseteq sA.
\]
The reverse inclusion is automatic, hence
\[
A=sA.
\]

Now let $x\in A[s]$. Since $A=Ra$, write $x=ta$. Then
\[
rx=rta=t(ra)=0,
\]
and by definition $sx=0$. Therefore
\[
x=(ur+vs)x=u(rx)+v(sx)=0.
\]
Hence
\[
A[s]=0.
\]
:::
