---
schema: qual/card@1
id: E-AMD-SF2B6RZ6
kind: problem
title: $HK$ is a subgroup of $G$ iff $HK=KH$
classification:
  areas:
  - algebra
  topics:
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against assets/Algebra/Review Doc/extracted/AlgebraQualNotes.md.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that $HK$ is a subgroup of $G$ iff $HK = KH$.
:::

::: {.solution}
<1>1. If \(HK\le G\), then \(HK=KH\).
::: {.proof}
Since \(HK\) is a subgroup, it is closed under inverses. Therefore
\[
HK=(HK)^{-1}=K^{-1}H^{-1}=KH,
\]
because \(H^{-1}=H\) and \(K^{-1}=K\).
:::

<1>2. Conversely, suppose \(HK=KH\). Then \(HK\) is nonempty and closed under \(xy^{-1}\).
::: {.proof}
The identity lies in \(HK\). Let
\[
x=h_1k_1,
\qquad
y=h_2k_2
\]
with \(h_1,h_2\in H\) and \(k_1,k_2\in K\). Then
\[
xy^{-1}=h_1k_1k_2^{-1}h_2^{-1}.
\]
Since \(k_1k_2^{-1}\in K\) and \(h_2^{-1}\in H\), the product
\[
(k_1k_2^{-1})h_2^{-1}\in KH=HK.
\]
Thus there exist \(h_3\in H\), \(k_3\in K\) with
\[
(k_1k_2^{-1})h_2^{-1}=h_3k_3.
\]
Hence
\[
xy^{-1}=h_1h_3k_3\in HK.
\]
:::

<1>3. Therefore \(HK\le G\) if and only if \(HK=KH\).
::: {.proof}
By <1>2, the nonempty subset \(HK\) satisfies the one-step subgroup criterion \(x,y\in HK\Rightarrow xy^{-1}\in HK\), so it is a subgroup. Together with <1>1 this proves the equivalence.
:::
:::
