---
schema: qual/card@1
id: P-5KZDX
kind: problem
title: A field is perfect if every irreducible polynomial is separable
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Finite Fields
relations: []
review: draft
---

::: problem
Define a perfect field. Prove that every finite field is perfect.
:::

::: {.solution}
A field $F$ is **perfect** if every irreducible polynomial in $F[x]$ is separable.

Every finite field is perfect. Let $F=\FF_q$ have characteristic $p>0$ and let
\[
\operatorname{Fr}:F\to F,\qquad a\mapsto a^p
\]
be Frobenius. Since $F$ is finite and Frobenius is injective, it is surjective.
Hence every $a\in F$ has a $p$th root in $F$.

Now let $f\in F[x]$ be irreducible. If $f$ were inseparable, then $f'=0$, so every exponent occurring in $f$ would be divisible by $p$ and
\[
f(x)=\sum_i a_i x^{pi}.
\]
Choose $b_i\in F$ with $b_i^p=a_i$. In characteristic $p$,
\[
f(x)=\left(\sum_i b_i x^i\right)^p,
\]
which is reducible unless $f$ is linear. Thus every nonconstant irreducible polynomial over $F$ is separable, so $F$ is perfect.
:::
