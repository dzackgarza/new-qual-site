---
schema: qual/card@1
id: E-SS6.EX-4
kind: problem
title: "SS 6.4: Asymptotics of binomial coefficients via Gamma"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Added the necessary exclusion of nonpositive integral alpha and handled that exceptional polynomial case separately.
---

::: {.exercise}
4. Prove that if we take

$$
f (z) = \frac {1}{(1 - z) ^ {\alpha}}, \quad \mathrm{for} | z | <   1
$$

(defined in terms of the principal branch of the logarithm), where $\alpha$ is a fixed complex number not in $\{0,-1,-2,\ldots\}$, then

$$
f (z) = \sum_ {n = 0} ^ {\infty} a _ {n} (\alpha) z ^ {n}
$$

with

$$
a _ {n} (\alpha) \sim \frac {1}{\Gamma (\alpha)} n ^ {\alpha - 1} \quad \text { as } n \to \infty .
$$

If $\alpha$ is a nonpositive integer, describe separately what happens to the coefficients.

$$
$$
:::

::: {.solution}
The generalized binomial theorem gives
\[
(1-z)^{-\alpha}=\sum_{n=0}^\infty \frac{(\alpha)_n}{n!}z^n,
\qquad |z|<1,
\]
where
\[
(\alpha)_n=\alpha(\alpha+1)\cdots(\alpha+n-1)
=\frac{\Gamma(n+\alpha)}{\Gamma(\alpha)}.
\]
Hence
\[
a_n(\alpha)=\frac{\Gamma(n+\alpha)}{\Gamma(\alpha)\Gamma(n+1)}.
\]
For fixed $\alpha\notin\{0,-1,-2,\ldots\}$, the gamma-ratio asymptotic
\[
\frac{\Gamma(n+\alpha)}{\Gamma(n+1)}\sim n^{\alpha-1}
\]
gives
\[
\boxed{a_n(\alpha)\sim \frac{n^{\alpha-1}}{\Gamma(\alpha)}}.
\]

If $\alpha=-m$ with $m\in\mathbb Z_{\ge0}$, then
\[
(1-z)^{-\alpha}=(1-z)^m
\]
is a polynomial of degree $m$, so $a_n(-m)=0$ for every $n>m$. This is why the asymptotic statement requires excluding the nonpositive integers.
:::
