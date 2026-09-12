---
schema: qual/card@1
id: P-ALGS12D
kind: problem
title: Flat modules over domains are torsionfree; flat f.g. modules over a PID
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
  date: 2026-09-08
  note: Compared with Problem 4 of the official UCSD Spring 2012 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Reduced torsionfreeness to tensoring multiplication by a nonzero scalar and then applied the PID structure theorem.
---

::: problem
Let $R$ be a commutative ring.
Recall that an $R$-module $Q$ is flat if $-\otimes_R Q$ is an exact functor; namely, given any short exact sequence of $R$-modules $0 \to M \to N \to P \to 0$, the sequence
\[
0 \to M \otimes_R Q \to N \otimes_R Q \to P \otimes_R Q \to 0
\]
remains exact.

(a) Let $Q$ be any module over an integral domain $R$.
Show that if $Q$ is flat, then $Q$ is torsionfree.

(b) In terms of the classification theorem for modules over PIDs, characterize exactly which finitely generated modules over a PID $R$ are flat.
:::

::: {.solution}
<1>1. Let \(R\) be an integral domain and \(0\neq r\in R\). Multiplication by \(r\) gives an injective \(R\)-linear map
\[
R\xrightarrow{\cdot r}R.
\]
::: {.proof}
If \(ra=0\) in the domain \(R\) and \(r\neq0\), then \(a=0\). Hence multiplication by \(r\) is injective.
:::

<1>2. If \(Q\) is flat, multiplication by every nonzero \(r\in R\) is injective on \(Q\).
::: {.proof}
From <1>1 we have a short exact sequence
\[
0\longrightarrow R\xrightarrow{\cdot r}R\longrightarrow R/rR\longrightarrow0.
\]
Tensoring with the flat module \(Q\) preserves exactness, so
\[
0\longrightarrow R\otimes_R Q
 \xrightarrow{(\cdot r)\otimes 1}
R\otimes_R Q
\]
is exact.
Under the canonical identification \(R\otimes_RQ\cong Q\), the displayed map is precisely
\[
Q\xrightarrow{\cdot r}Q.
\]
Therefore it is injective.
:::

<1>3. Every flat module over an integral domain is torsionfree.
::: {.proof}
Suppose \(q\in Q\) and \(0\neq r\in R\) satisfy \(rq=0\). By <1>2, multiplication by \(r\) on \(Q\) is injective, so \(q=0\). This is exactly torsionfreeness.
:::

<1>4. Let \(R\) be a PID and let \(M\) be finitely generated.
By the structure theorem,
\[
M\cong R^s\oplus T,
\]
where \(T\) is a finite direct sum of nonzero cyclic torsion modules \(R/(d_i)\) if the torsion part is nonzero.
::: {.proof}
This is the classification theorem for finitely generated modules over a PID.
:::

<1>5. A finitely generated \(R\)-module over a PID is flat if and only if its torsion part \(T\) in <1>4 is zero.
::: {.proof}
If \(M\) is flat, then <1>3 implies that \(M\) is torsionfree.
Hence the torsion summand \(T\) must vanish.

Conversely, if \(T=0\), then \(M\cong R^s\) is free.
Every free module is flat because tensoring with a direct sum of copies of \(R\) is a direct sum of copies of the original exact sequence and therefore preserves exactness.
:::

<1>6. Thus the finitely generated flat modules over a PID are exactly the finitely generated free modules.
::: {.proof}
This is the equivalence established in <1>5.
:::
:::
