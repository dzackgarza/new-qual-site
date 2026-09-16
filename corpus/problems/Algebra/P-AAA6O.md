---
schema: qual/card@1
id: P-AAA6O
kind: problem
title: Rational roots of polynomials in $\QQ[x]$ are integers
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Factorization
  - Number Theory
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

::: {.problem}
Show that if \(p(x)\in\mathbb Z[x]\) is monic and \(r\in\mathbb Q\) is a root of \(p\), then \(r\in\mathbb Z\).
:::

::: {.solution}
Write
\[
p(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_0
\]
and suppose \(r=a/b\) in lowest terms with \(b>0\). From \(p(a/b)=0\), multiplying by \(b^n\) gives
\[
a^n+b(a_{n-1}a^{n-1}+a_{n-2}a^{n-2}b+\cdots+a_0b^{n-1})=0.
\]
Hence \(b\mid a^n\). Since \(\gcd(a,b)=1\), also \(\gcd(a^n,b)=1\), so \(b=1\). Therefore \(r=a\in\mathbb Z\).
:::
