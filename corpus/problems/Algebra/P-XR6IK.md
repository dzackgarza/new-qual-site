---
schema: qual/card@1
id: P-XR6IK
kind: problem
title: An irreducible polynomial of degree $p$ over $\FF_p$ for each prime $p$
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
For each prime $p$, give an explicit polynomial of degree $p$ that is irreducible over the finite field $\mathbb{F}_p$, constructed in a uniform way across all primes $p$.
Prove that your polynomial is irreducible over $\mathbb{F}_p$.
:::

::: solution
For every prime $p$, take
\[
f(x)=x^p-x-1\in\mathbb F_p[x].
\]
Let $\alpha$ be a root in an algebraic closure. Then
\[
\alpha^p=\alpha+1.
\]
Iterating Frobenius gives
\[
\alpha^{p^m}=\alpha+m
\]
for every integer $m\ge0$, where $m$ is read in $\mathbb F_p$.

The degree of the minimal polynomial of $\alpha$ over $\mathbb F_p$ is the size of its Frobenius orbit. The first positive $m$ for which
\[
\alpha^{p^m}=\alpha
\]
is therefore the first positive $m$ with $m=0$ in $\mathbb F_p$, namely $m=p$. Hence
\[
[\mathbb F_p(\alpha):\mathbb F_p]=p.
\]
Since $f$ has degree $p$ and vanishes at $\alpha$, it is the minimal polynomial of $\alpha$. Thus
\[
\boxed{x^p-x-1\text{ is irreducible over }\mathbb F_p}
\]
for every prime $p$.
:::
