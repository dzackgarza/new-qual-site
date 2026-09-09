---
schema: qual/card@1
id: E-T5ERF
kind: problem
title: $\|f\|_{(\infty,s)}\le c\|f\|_{(1,r)}$ for holomorphic $f$ near $D_r(z_0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Mean Value Property
  - Cauchy Estimates
  - Holomorphic Functions
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
Let $f$ be holomorphic in a neighborhood of the closed disk $\overline{D}_r(z_0)$.
Show that for any $s < r$, there exists a constant $c > 0$ (depending on $r$ and $s$) such that:
$$\|f\|_{(\infty, s)} \le c \|f\|_{(1, r)}$$
where $\|f\|_{(\infty, s)} = \sup_{z \in D_s(z_0)} |f(z)|$ and $\|f\|_{(1, r)} = \iint_{D_r(z_0)} |f(z)| \, dx \, dy$.
:::

::: solution
Let
\[
\delta=r-s>0.
\]
For $w\in D_s(z_0)$ one has
\[
D_\delta(w)\subset D_r(z_0).
\]

<1>1. The area mean-value formula for holomorphic functions gives
\[
f(w)=\frac1{\pi\delta^2}\iint_{D_\delta(w)}f(z)\,dA(z).
\]
Hence
\[
|f(w)|
\le\frac1{\pi\delta^2}\iint_{D_\delta(w)}|f(z)|\,dA(z)
\le\frac1{\pi(r-s)^2}\|f\|_{(1,r)}.
\]

<1>2. Taking the supremum over $w\in D_s(z_0)$ gives
\[
\|f\|_{(\infty,s)}
\le\frac1{\pi(r-s)^2}\|f\|_{(1,r)}.
\]
Thus one may take
\[
c=\frac1{\pi(r-s)^2}.
\]
:::
