---
schema: qual/card@1
id: P-CAFA15C
kind: problem
title: "Polynomial with non-increasing real coefficients has no roots inside the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
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
Let $a_0, a_1, \dots, a_n$ be a strictly positive, non-increasing sequence of real numbers:
$$a_0 \ge a_1 \ge a_2 \ge \cdots \ge a_n > 0.$$
Prove that the polynomial:
$$P(z) = a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n$$
has **no roots inside the open unit disk** $|z| < 1$ (Eneström–Kakeya Theorem).
:::

::: solution
Set $P(z)=\sum_{k=0}^na_kz^k$. Then
$$
(1-z)P(z)=a_0-\left(\sum_{k=1}^n(a_{k-1}-a_k)z^k+a_nz^{n+1}\right).
$$
For $|z|<1$,
$$
\left|\sum_{k=1}^n(a_{k-1}-a_k)z^k+a_nz^{n+1}\right|
\le \sum_{k=1}^n(a_{k-1}-a_k)|z|^k+a_n|z|^{n+1}
< \sum_{k=1}^n(a_{k-1}-a_k)+a_n=a_0.
$$
The inequality is strict because $a_n>0$ and $|z|^{n+1}<1$. Therefore $|(1-z)P(z)|>0$. Since $1-z\ne0$ for $|z|<1$, one gets $P(z)\ne0$ throughout the open unit disk.
:::
