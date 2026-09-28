---
schema: qual/card@1
id: P-BOH76
kind: problem
title: Groups of order $p^2$ and of order $pq$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Semidirect Products
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

::: {.problem}
(1) What are the groups of order $p^2$ for $p$ prime?
(2) What are the groups of order $pq$ for distinct primes $p < q$?
(3) What if $q \equiv 1 \pmod p$?
:::

::: {.solution}
For \(|G|=p^2\), the center of the \(p\)-group \(G\) is nontrivial. If \(|Z(G)|=p\), then \(G/Z(G)\) is cyclic, which forces \(G\) abelian; hence in fact \(Z(G)=G\). Therefore
\[
G\cong C_{p^2}\quad\text{or}\quad C_p\times C_p.
\]

Now let \(|G|=pq\) with primes \(p<q\). Sylow gives
\[
n_q\equiv1\pmod q,\qquad n_q\mid p,
\]
so \(n_q=1\). Thus the Sylow \(q\)-subgroup \(Q\cong C_q\) is normal. If \(P\cong C_p\) is a Sylow \(p\)-subgroup, then
\[
G\cong C_q\rtimes_\theta C_p,
\qquad
\theta:C_p\to\operatorname{Aut}(C_q)\cong C_{q-1}.
\]

If \(p\nmid q-1\), the homomorphism \(\theta\) is trivial, hence
\[
G\cong C_q\times C_p\cong C_{pq}.
\]
If \(p\mid q-1\), then \(C_{q-1}\) has a unique subgroup of order \(p\). Thus there are exactly two isomorphism classes: the cyclic group \(C_{pq}\), and one nonabelian semidirect product
\[
\langle x,y\mid x^q=y^p=1,\ yxy^{-1}=x^r\rangle,
\]
where \(r\in(\mathbb Z/q\mathbb Z)^\times\) has order \(p\).
:::
