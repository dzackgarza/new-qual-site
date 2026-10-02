---
schema: qual/card@1
id: FD-YYLYR
kind: definition
title: Perfect field
prompts:
- What is a perfect field, and which characteristics give one for free?
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

::: {.definition}
A [[D-UI6CU|field]] $k$ is \dfn{perfect} if every irreducible polynomial in $k[x]$ is [[D-ZT46D|separable]].
:::

::: {.proposition}
A field $k$ is perfect if and only if either $\ch k=0$, or $\ch k=p>0$ and the Frobenius map $F\colon k\to k$, $F(a)=a^p$, is surjective, hence an automorphism.
In particular, every field of characteristic zero and every finite field is perfect.
:::

::: {.proof}
An irreducible $f\in k[x]$ has a repeated root if and only if $\gcd(f,f')\ne1$, and since $f$ is irreducible and $\deg f'<\deg f$, this happens if and only if $f'=0$.

If $\ch k=0$, then $f'\ne0$ for every nonconstant $f$, so $k$ is perfect.

Let $\ch k=p>0$.
Then $f'=0$ if and only if $f(x)=\sum_i a_ix^{pi}$ for some $a_i\in k$.
If $F$ is surjective, choose $b_i\in k$ with $b_i^p=a_i$; then $f=\qty{\sum_ib_ix^i}^p$ is reducible, so no irreducible polynomial has $f'=0$, and $k$ is perfect.
If $F$ is not surjective, choose $a\in k$ that is not a $p$th power, and let $\beta$ be a root of $x^p-a$ in a splitting field, so $x^p-a=(x-\beta)^p$.
A monic factor of $x^p-a$ in $k[x]$ of degree $j$ with $0<j<p$ is $(x-\beta)^j$, whose coefficient of $x^{j-1}$ is $-j\beta$; since $j$ is a unit in $k$, this would give $\beta\in k$ and $a=\beta^p$.
So $x^p-a$ is irreducible and not separable, and $k$ is not perfect.

The Frobenius map is an injective ring homomorphism, so on a finite field it is surjective.
:::
