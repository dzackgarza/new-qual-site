---
schema: qual/card@1
id: E-AMD-BTVLG2S2
kind: problem
title: $|HK|=|H||K|/|H\cap K|$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Let $H, K \leq G$ a finite group, and without using the normalizers of $H$ or $K$, show that $\abs{HK} = \abs{H} \abs{K}/\abs{H\intersect K}$.
:::

::: {.solution}
Consider the surjection
\[
\mu:H\times K\to HK,\qquad (h,k)\mapsto hk.
\]
Fix $x=h_0k_0\in HK$. Then
\[
hk=x=h_0k_0
\]
if and only if
\[
d:=h_0^{-1}h=k_0k^{-1}\in H\cap K.
\]
Equivalently,
\[
(h,k)=(h_0d,d^{-1}k_0)
\]
for a unique $d\in H\cap K$. Hence every fiber of $\mu$ has cardinality $|H\cap K|$.

Therefore
\[
|H||K|=|H\times K|=|HK|\,|H\cap K|,
\]
so
\[
\boxed{|HK|=\frac{|H||K|}{|H\cap K|}}.
\]
:::
