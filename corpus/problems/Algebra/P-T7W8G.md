---
schema: qual/card@1
id: P-T7W8G
kind: problem
title: Irreducible polynomials over a field in which every element has a $p$th root are separable
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.problem}
Let $F$ be a field of characteristic $p>0$ such that every element of $F$ has a $p$th root in $F$. Show that every irreducible polynomial in $F[x]$ is separable.
:::

::: {.solution}
Let $f\in F[x]$ be irreducible. Suppose, for contradiction, that $f$ is inseparable. Since $f$ is irreducible, inseparability implies
\[
\gcd(f,f')=f.
\]
But $\deg f'<\deg f$, so this forces
\[
f'=0.
\]

In characteristic $p$, the derivative vanishes exactly when every exponent occurring in $f$ is divisible by $p$. Hence
\[
f(x)=\sum_i a_i x^{pi}
\]
for coefficients $a_i\in F$.

By hypothesis, each $a_i$ is a $p$th power, say
\[
a_i=b_i^p
\]
with $b_i\in F$. Therefore, using the Frobenius identity in characteristic $p$,
\[
f(x)=\sum_i b_i^p x^{pi}
=\left(\sum_i b_i x^i\right)^p.
\]
Since $f$ is nonconstant, the polynomial inside the parentheses is nonconstant. Thus $f$ is a nontrivial $p$th power in $F[x]$, contradicting irreducibility.

Hence every irreducible polynomial over $F$ is separable.
:::
