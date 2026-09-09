---
schema: qual/card@1
id: P-BQVDL
kind: problem
title: A subgroup of index equal to the smallest prime dividing $|G|$ is normal
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Group Actions
  - Cosets and Lagrange
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
Let $G$ be a finite group, and let $H \le G$ be a subgroup of index $[G : H] = p$, where $p$ is the smallest prime dividing $|G|$.
Prove that $H$ is a **normal** subgroup of $G$ ($H \trianglelefteq G$).
:::

::: solution
Let \(G\) act on the \(p\) left cosets of \(H\). This gives
\[
\rho:G\to S_p,
\]
and let \(K=\ker\rho\). Then \(K\trianglelefteq G\), \(K\le H\), and
\[
[G:K]=|\operatorname{im}\rho|\mid p!.
\]
Since \([G:H]=p\),
\[
[G:K]=p[H:K],
\]
so \([H:K]\mid (p-1)!\).

On the other hand, \([H:K]\mid |G|\). If \([H:K]>1\), choose a prime \(q\mid[H:K]\). Then \(q\mid|G|\), so by minimality of \(p\) we have \(q\ge p\). But \(q\mid(p-1)!\), so \(q<p\), a contradiction. Hence \([H:K]=1\), so \(H=K\trianglelefteq G\).
:::
