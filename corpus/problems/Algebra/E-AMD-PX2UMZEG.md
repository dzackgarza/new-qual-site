---
schema: qual/card@1
id: E-AMD-PX2UMZEG
kind: problem
title: Intersections, products, and sums of ideals are ideals
classification:
  areas:
  - algebra
  topics:
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against assets/Algebra/Review Doc/extracted/AlgebraQualNotes.md, Extra Problems / Ring Theory / Ideals.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that intersections, products, and sums of ideals are ideals.
:::

::: {.solution}
<1>1. The intersection of any nonempty family of ideals of \(R\) is an ideal.
::: {.proof}
Let \(\{I_\alpha\}_{\alpha\in A}\) be ideals and set \(I=\bigcap_{\alpha\in A}I_\alpha\). Since \(0\in I_\alpha\) for every \(\alpha\), \(0\in I\). If \(x,y\in I\), then \(x-y\in I_\alpha\) for every \(\alpha\), hence \(x-y\in I\). If \(r\in R\) and \(x\in I\), then \(rx,xr\in I_\alpha\) for every \(\alpha\), so \(rx,xr\in I\). Thus \(I\) is a two-sided ideal.
:::

<1>2. If \(I,J\trianglelefteq R\), then
\[
I+J=\{a+b:a\in I,\ b\in J\}
\]
is an ideal.
::: {.proof}
We have \(0=0+0\in I+J\). If \(a+b,c+d\in I+J\), with \(a,c\in I\) and \(b,d\in J\), then
\[
(a+b)-(c+d)=(a-c)+(b-d)\in I+J.
\]
For \(r\in R\),
\[
r(a+b)=ra+rb\in I+J,
\qquad
(a+b)r=ar+br\in I+J,
\]
because \(I\) and \(J\) are ideals. Hence \(I+J\trianglelefteq R\).
:::

<1>3. If \(I,J\trianglelefteq R\), their product
\[
IJ=\left\{\sum_{k=1}^n a_kb_k:n\ge0,\ a_k\in I,\ b_k\in J\right\}
\]
is an ideal.
::: {.proof}
The empty sum is \(0\), so \(0\in IJ\). Finite sums of products are closed under addition and additive inverses. If
\[
x=\sum_{k=1}^n a_kb_k\in IJ
\]
and \(r\in R\), then
\[
rx=\sum_{k=1}^n (ra_k)b_k\in IJ
\]
because \(ra_k\in I\), while
\[
xr=\sum_{k=1}^n a_k(b_kr)\in IJ
\]
because \(b_kr\in J\). Thus \(IJ\trianglelefteq R\).
:::

<1>4. Therefore intersections, sums, and products of ideals are ideals.
::: {.proof}
This is exactly <1>1--<1>3. Finite sums of more than two ideals follow by induction from <1>2, and finite products from <1>3.
:::
:::
