---
schema: qual/card@1
id: P-AA27R
kind: problem
title: Irreducibility of $(x^p-1)/(x-1)$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Roots of Unity
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

::: {.problem}
Why is $\Phi_p(x) = \frac{x^p - 1}{x - 1} = x^{p-1} + x^{p-2} + \cdots + x + 1$ irreducible over $\mathbb{Q}$ for $p$ prime?
:::

::: {.solution}
Set
\[
g(y)=\Phi_p(y+1)=\frac{(y+1)^p-1}{y}
=\sum_{m=1}^p\binom pm y^{m-1}.
\]
Its leading coefficient is \(1\). For \(1\le m\le p-1\), the prime \(p\) divides \(\binom pm\), while the constant term is \(\binom p1=p\), which is not divisible by \(p^2\). Thus \(g(y)\) is Eisenstein at \(p\), hence irreducible over \(\mathbb Q\).

The substitution \(x\mapsto y+1\) is an automorphism of \(\mathbb Q[x]\), so reducibility of \(\Phi_p(x)\) would imply reducibility of \(\Phi_p(y+1)=g(y)\). Therefore
\[
\Phi_p(x)=1+x+\cdots+x^{p-1}
\]
is irreducible over \(\mathbb Q\).
:::
