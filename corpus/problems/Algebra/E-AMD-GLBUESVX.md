---
schema: qual/card@1
id: E-AMD-GLBUESVX
kind: problem
title: $x^{p^n}-x$ is the product of monic irreducibles in $\FF_p[x]$ of degree dividing
  $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove that $x^{p^n}-x$ is the product of all monic irreducible polynomials in $\mathbb{F}_p[x]$ with degree dividing $n$.
:::

::: {.solution}
Let
\[
P(x)=x^{p^n}-x\in\FF_p[x].
\]
Its derivative is
\[
P'(x)=p^n x^{p^n-1}-1=-1,
\]
so $P$ is squarefree.

Let $f\in\FF_p[x]$ be monic irreducible of degree $d$, and let $\alpha$ be a root. Then
\[
\FF_p(\alpha)\cong\FF_{p^d}.
\]
Now
\[
f\mid P
\iff \alpha^{p^n}=\alpha
\iff \alpha\in\FF_{p^n}
\iff \FF_{p^d}\subseteq\FF_{p^n}
\iff d\mid n.
\]
Thus the irreducible factors of $P$ are exactly the monic irreducibles whose degrees divide $n$. Since $P$ is monic and squarefree,
\[
\boxed{x^{p^n}-x=\prod_{d\mid n}\ \prod_{\substack{f\text{ monic irreducible}\\ \deg f=d}} f(x).}
\]
:::
