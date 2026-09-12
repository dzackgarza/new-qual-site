---
schema: qual/card@1
id: P-5AMY7
kind: problem
title: Irreducible polynomials of degrees 7 and 14 over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
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
Can you have a degree 7 irreducible polynomial over $\mathbb{F}_p$? How about a degree 14 irreducible polynomial?
:::

::: solution
Yes in both degrees; in fact, over every finite field $\mathbb F_p$ there are irreducible polynomials of every positive degree.

For $n\ge1$, let $\mathbb F_{p^n}$ be the field with $p^n$ elements. Its multiplicative group is cyclic. If $\alpha$ generates $\mathbb F_{p^n}^{\times}$, then
\[
\mathbb F_p(\alpha)=\mathbb F_{p^n},
\]
because the left side is a subfield containing every nonzero power of $\alpha$, hence every element of $\mathbb F_{p^n}$. Therefore the minimal polynomial of $\alpha$ over $\mathbb F_p$ has degree
\[
[\mathbb F_p(\alpha):\mathbb F_p]=n.
\]
So irreducible polynomials of degrees $7$ and $14$ exist.

For completeness, the number $N_p(n)$ of monic irreducible polynomials of degree $n$ is
\[
N_p(n)=\frac1n\sum_{d\mid n}\mu(d)p^{n/d}.
\]
Hence
\[
N_p(7)=\frac{p^7-p}{7}>0
\]
and
\[
N_p(14)=\frac{p^{14}-p^7-p^2+p}{14}>0.
\]
:::
