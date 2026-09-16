---
schema: qual/card@1
id: P-WROEI
kind: problem
title: Galois group of $x^7-3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
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
Compute the Galois group of $p(x) = x^7 - 3$ over $\mathbb{Q}$.
:::

::: {.solution}
Let
\[
\alpha=3^{1/7},\qquad \zeta=\zeta_7.
\]
The polynomial $x^7-3$ is Eisenstein at $3$, so
\[
[\mathbb Q(\alpha):\mathbb Q]=7.
\]
Its splitting field is
\[
K=\mathbb Q(\alpha,\zeta).
\]
Since
\[
[\mathbb Q(\zeta):\mathbb Q]=6
\]
and the two degrees are coprime, the intersection of $\mathbb Q(\alpha)$ and $\mathbb Q(\zeta)$ is $\mathbb Q$. Hence
\[
[K:\mathbb Q]=42.
\]

Over $\mathbb Q(\zeta)$, define
\[
\sigma(\alpha)=\zeta\alpha,
\qquad \sigma(\zeta)=\zeta;
\]
then $\sigma$ has order $7$. Choose $3$ as a generator of $(\mathbb Z/7\mathbb Z)^\times$ and define
\[
\tau(\alpha)=\alpha,
\qquad \tau(\zeta)=\zeta^3;
\]
then $\tau$ has order $6$. They satisfy
\[
\tau\sigma\tau^{-1}=\sigma^3.
\]
Thus
\[
\operatorname{Gal}(K/\mathbb Q)
\cong C_7\rtimes C_6,
\]
where $C_6\cong(\mathbb Z/7\mathbb Z)^\times$ acts faithfully on $C_7$. Equivalently,
\[
\boxed{\operatorname{Gal}(K/\mathbb Q)\cong\operatorname{AGL}_1(\mathbb F_7)},
\]
the Frobenius group of order $42$.
:::
