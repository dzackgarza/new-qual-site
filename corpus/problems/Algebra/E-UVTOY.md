---
schema: qual/card@1
id: E-UVTOY
kind: problem
title: $K$-automorphisms permute the roots of polynomials in $K[x]$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
3. For a polynomial $f \in K[x]$, prove that if $r \in F$ is a root of $f$ then for any $\sigma\in\operatorname{Aut}_K(F)$, $\sigma(r)$ is also a root of $f$.
:::

::: {.solution}

::: pf

::: {.pf-step #automorphism-fixes-coefficients}
A $K$-automorphism fixes every coefficient of $f$.

::: pf-proof
Write
\[
f(x)=a_0+a_1x+\cdots+a_nx^n
\]
with $a_i\in K$. If $\sigma\in\operatorname{Aut}_K(F)$, then by definition $\sigma(a_i)=a_i$ for every $i$.
:::

:::

::: {.pf-step #root-preserved}
If $r\in F$ satisfies $f(r)=0$, then $f(\sigma(r))=0$.

::: pf-proof
Using step [](#automorphism-fixes-coefficients){.pf-ref} and the fact that $\sigma$ is a field homomorphism,
\[
\begin{aligned}
f(\sigma(r))
&=\sum_{i=0}^n a_i\sigma(r)^i\\
&=\sum_{i=0}^n \sigma(a_i)\sigma(r^i)\\
&=\sigma\left(\sum_{i=0}^n a_ir^i\right)\\
&=\sigma(f(r))\\
&=\sigma(0)=0.
\end{aligned}
\]
Thus $\sigma(r)$ is again a root of $f$.
:::

:::

::: pf-step
Hence $K$-automorphisms of $F$ permute the roots in $F$ of every polynomial in $K[x]$.

::: pf-proof
By step [](#root-preserved){.pf-ref}, each automorphism sends the set of roots in $F$ into itself. Since $\sigma$ is bijective and $\sigma^{-1}$ has the same property, the induced map on that root set is a permutation.
:::

:::

:::

:::
