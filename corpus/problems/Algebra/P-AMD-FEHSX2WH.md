---
schema: qual/card@1
id: P-AMD-FEHSX2WH
kind: problem
title: The nilradical is contained in the Jacobson radical
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Nilpotence
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
The nilradical is contained in the Jacobson radical, i.e.
\[
\nilrad{R} \subseteq J(R)
.\]
:::

::: {.solution}
Let \(x\in\operatorname{nil}(R)\), so \(x^n=0\) for some \(n\). For every prime ideal \(\mathfrak p\), primality gives \(x\in\mathfrak p\) from \(x^n\in\mathfrak p\). Every maximal ideal is prime in a commutative ring with identity, hence \(x\) lies in every maximal ideal. Therefore
\[
\operatorname{nil}(R)\subseteq\bigcap_{\mathfrak m\in\operatorname{mSpec}R}\mathfrak m=J(R).
\]
:::
