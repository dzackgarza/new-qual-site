---
schema: qual/card@1
id: T-6XDRA
kind: theorem
title: Fundamental theorem of algebra
slogan: 'A complex polynomial of degree $n$ has $n$ zeros counted with multiplicity.'
prompts:
- State the fundamental theorem of algebra.
- How many zeros does a polynomial of degree $n$ have?
classification:
  areas:
  - complex-analysis
  topics:
  - Fundamental Theorem of Algebra
  - Polynomials
  - Zeros of Polynomials
relations: []
review: draft
---

::: {.theorem}
Let $P(z) = a_nz^n+\cdots+a_0\in\CC[z]$ with $a_n\neq0$ and $n\geq1$.
Then $P$ has exactly $n$ zeros in $\CC$, counted with multiplicity, and
$$
P(z) = a_n\prod_{k=1}^{n}(z-z_k)
$$
for its zeros $z_1,\ldots,z_n$ listed with multiplicity [@SS03, Corollary 4.7 (p. 51)].
:::

::: {.remark}
It is enough to prove that a nonconstant polynomial has one zero: dividing by $z-z_0$ and iterating gives the count.
The proofs that run through Liouville's theorem, Rouché's theorem, the argument principle, and the open mapping theorem are collected on [[complex-analysis/appendices/appendix-fta-proofs|Proofs of the fundamental theorem of algebra]].
:::
