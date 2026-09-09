---
schema: qual/card@1
id: P-OPZJH
kind: problem
title: $(\FF_9)^\times$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Cyclic Groups
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
What is the structure of the multiplicative group $(\mathbb{F}_9)^\times$?
Construct $\mathbb{F}_9$ as a quotient ring and find an explicit primitive generator of $(\mathbb{F}_9)^\times$.
:::

::: solution
The polynomial
\[
x^2+1\in\mathbb F_3[x]
\]
has no root in $\mathbb F_3$, hence is irreducible. Thus
\[
\mathbb F_9\cong\mathbb F_3[i],
\qquad i^2=-1=2.
\]
Its multiplicative group has order $8$, and the multiplicative group of a finite field is cyclic, so
\[
(\mathbb F_9)^\times\cong C_8.
\]

Take
\[
\alpha=1+i.
\]
Then
\[
\alpha^2=1+2i+i^2=2i,
\]
and hence
\[
\alpha^4=(2i)^2=4i^2=2\neq1,
\qquad
\alpha^8=2^2=1.
\]
Therefore $\alpha$ has order $8$, so it is a primitive generator. Hence
\[
\boxed{(\mathbb F_9)^\times=\langle1+i\rangle\cong C_8.}
\]
:::
