---
schema: qual/card@1
id: P-7GW6D
kind: problem
title: A Galois group that is neither $S_n$ nor $A_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What's a Galois group that's not $S_n$ or $A_n$?
:::

::: {.solution}
A concrete example is the splitting field of \(x^4-2\) over \(\mathbb Q\). If \(\alpha=\sqrt[4]{2}\), its splitting field is \(K=\mathbb Q(\alpha,i)\), of degree \(8\). The automorphisms
\[
r(\alpha)=i\alpha,\quad r(i)=i,
\qquad
s(\alpha)=\alpha,\quad s(i)=-i
\]
satisfy
\[
r^4=s^2=1,\qquad srs=r^{-1}.
\]
Hence
\[
\operatorname{Gal}(K/\mathbb Q)\cong D_4,
\]
the dihedral group of order \(8\). Since no symmetric or alternating group has order \(8\), this is neither \(S_n\) nor \(A_n\) for any \(n\).

Many other examples exist; for instance \(\operatorname{Gal}(\mathbb Q(\zeta_7)/\mathbb Q)\cong(\mathbb Z/7\mathbb Z)^\times\cong C_6\).
:::
