---
schema: qual/card@1
id: P-O6JP3
kind: problem
title: Polynomial rings over integral domains are integral domains
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Polynomials
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
- Prove that if $R$ is an integral domain, then $R[t]$ is again an integral domain.
:::

::: {.solution}
Let
\[
f(t)=a_nt^n+\cdots+a_0,\qquad g(t)=b_mt^m+\cdots+b_0
\]
be nonzero polynomials in $R[t]$, with $a_n,b_m\neq0$. The coefficient of $t^{n+m}$ in $fg$ is $a_nb_m$. Since $R$ is an integral domain, $a_nb_m\neq0$. Hence $fg\neq0$.

Therefore $R[t]$ has no nonzero zero divisors, so it is an integral domain. In particular,
\[
\deg(fg)=\deg f+\deg g
\]
for nonzero $f,g\in R[t]$.
:::
