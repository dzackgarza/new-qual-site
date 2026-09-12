---
schema: qual/card@1
id: P-RMRPT
kind: problem
title: Characters of the multiplicative group of a finite field
classification:
  areas:
  - algebra
  topics:
  - Character Theory
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
What are the group characters of the multiplicative group of a finite field $\mathbb{F}_q^\times$?
:::

::: solution
The group $\mathbb F_q^\times$ is cyclic of order $q-1$. Choose a generator $g$ and put
\[
\zeta=e^{2\pi i/(q-1)}.
\]
For each $k\in\mathbb Z/(q-1)\mathbb Z$, define
\[
\chi_k(g^m)=\zeta^{km}.
\]
This is well defined and multiplicative, hence a character
\[
\chi_k:\mathbb F_q^\times\to\mathbb C^\times.
\]
Conversely, any character is determined by its value on $g$, and that value must satisfy
\[
\chi(g)^{q-1}=\chi(g^{q-1})=1.
\]
Thus $\chi(g)$ is one of the $q-1$ roots $\zeta^k$, so every character is exactly one $\chi_k$.

Therefore
\[
\widehat{\mathbb F_q^\times}
=\operatorname{Hom}(\mathbb F_q^\times,\mathbb C^\times)
\cong C_{q-1}.
\]
For odd $q$, the unique character of order $2$ is the quadratic character.
:::
