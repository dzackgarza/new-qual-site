---
schema: qual/card@1
id: P-6VMUH
kind: problem
title: Galois group of $x^4-3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Compute the **Galois group** of the polynomial $f(x) = x^4 - 3$ over $\mathbb{Q}$, and describe its action on the roots.
:::

::: solution
Let \(\alpha=\sqrt[4]{3}\). The roots are \(\alpha,i\alpha,-\alpha,-i\alpha\), so the splitting field is
\[
K=\mathbb Q(\alpha,i).
\]
Eisenstein at \(3\) gives \([\mathbb Q(\alpha):\mathbb Q]=4\). Since \(\mathbb Q(\alpha)\subset\mathbb R\), we have \(i\notin\mathbb Q(\alpha)\), hence \([K:\mathbb Q]=8\).

Define
\[
r(\alpha)=i\alpha,\qquad r(i)=i,
\]
and let \(s\) be complex conjugation:
\[
s(\alpha)=\alpha,\qquad s(i)=-i.
\]
Then \(r\) has order \(4\), \(s\) has order \(2\), and
\[
srs=r^{-1}.
\]
Thus \(\langle r,s\rangle\cong D_4\) has order \(8\), so it is the whole Galois group. On the ordered roots \((\alpha,i\alpha,-\alpha,-i\alpha)\),
\[
r=(1\ 2\ 3\ 4),\qquad s=(2\ 4).
\]
Therefore
\[
\operatorname{Gal}(K/\mathbb Q)\cong D_4
\]
(the dihedral group of order \(8\)).
:::
