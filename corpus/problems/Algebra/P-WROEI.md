---
schema: qual/card@1
id: P-WROEI
kind: problem
title: Galois group of $x^7-3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
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
Compute the Galois group of $p(x) = x^7 - 3$ over $\QQ$.
:::

::: {.solution}
Let
$$
\alpha=3^{1/7},\qquad \zeta=\zeta_7.
$$
The polynomial $x^7-3$ is Eisenstein at $3$, so
$$
[\QQ(\alpha):\QQ]=7.
$$
Its splitting field is
$$
K=\QQ(\alpha,\zeta).
$$
Since
$$
[\QQ(\zeta):\QQ]=6
$$
and the two degrees are coprime, the intersection of $\QQ(\alpha)$ and $\QQ(\zeta)$ is $\QQ$. Hence
$$
[K:\QQ]=42.
$$

Since $[K:\QQ(\zeta)]=7$, the polynomial $x^7-3$ is irreducible over $\QQ(\zeta)$, and since $[K:\QQ(\alpha)]=6$, the polynomial $\Phi_7$ is irreducible over $\QQ(\alpha)$. Hence there are automorphisms of $K$ defined by
$$
\sigma(\alpha)=\zeta\alpha,
\qquad \sigma(\zeta)=\zeta;
$$
then $\sigma$ has order $7$. Choose $3$ as a generator of $(\ZZ/7\ZZ)^\times$ and define
$$
\tau(\alpha)=\alpha,
\qquad \tau(\zeta)=\zeta^3;
$$
then $\tau$ has order $6$. They satisfy
$$
\tau\sigma\tau^{-1}=\sigma^3.
$$
Thus
$$
\Gal(K/\QQ)
\cong C_7\rtimes C_6,
$$
where $C_6\cong(\ZZ/7\ZZ)^\times$ acts faithfully on $C_7$. Equivalently,
$$
\boxed{\Gal(K/\QQ)\cong\operatorname{AGL}_1(\FF_7)},
$$
the Frobenius group of order $42$.
:::
