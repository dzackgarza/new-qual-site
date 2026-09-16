---
schema: qual/card@1
id: PR-OMKPN
kind: proposition
title: An irreducible polynomial is inseparable if and only if its derivative is zero
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and let $f\in k[x]$ be [[D-BVMTZ|irreducible]].
Then $f$ has a repeated root in a splitting field, that is, $f$ is not [[D-ZT46D|separable]], if and only if $f'=0$ in $k[x]$.
:::

::: {.proof}
A root $\alpha$ of $f$ in a splitting field is repeated if and only if $f'(\alpha)=0$, so $f$ has a repeated root if and only if $\gcd(f,f')$ is nonconstant; this gcd is the same whether computed in $k[x]$ or over the splitting field.
Since $f$ is irreducible, $\gcd(f,f')$ is $1$ or an associate of $f$, so $f$ has a repeated root if and only if $f\mid f'$.
As $\deg f'<\deg f$, this holds if and only if $f'=0$.
:::
