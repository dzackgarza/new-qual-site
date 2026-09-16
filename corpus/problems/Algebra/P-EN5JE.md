---
schema: qual/card@1
id: P-EN5JE
kind: problem
title: $|HK| = |H||K|/|H \cap K|$
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
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Let $H, K \leq G$ a finite group, and without using the normalizers of $H$ or $K$, show that $\abs{HK} = \abs{H} \abs{K}/\abs{H\intersect K}$.
:::

::: {.solution}
Consider the surjection
\[
\phi:H\times K\longrightarrow HK,
\qquad
\phi(h,k)=hk.
\]
Fix $hk\in HK$. If $x\in H\cap K$, then
\[
\phi(hx,x^{-1}k)=hk.
\]
Conversely, if $h_1k_1=hk$, then
\[
h^{-1}h_1=kk_1^{-1}\in H\cap K.
\]
Writing this element as $x$ gives
\[
(h_1,k_1)=(hx,x^{-1}k).
\]
Hence every fiber of $\phi$ has exactly $|H\cap K|$ elements. Counting $H\times K$ by fibers yields
\[
|H||K|=|HK|\,|H\cap K|,
\]
so
\[
|HK|=\frac{|H||K|}{|H\cap K|}.
\]
:::
