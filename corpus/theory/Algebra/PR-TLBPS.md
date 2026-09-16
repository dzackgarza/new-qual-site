---
schema: qual/card@1
id: PR-TLBPS
kind: proposition
title: The derivative detects separability for irreducible polynomials
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Polynomials
  - Characteristic
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and let $f\in k[x]$ be nonzero.

(a) $f$ is [[D-ZT46D|separable]] if and only if $\gcd(f, f') = 1$.

(b) If $f$ is [[D-BVMTZ|irreducible]], then $f$ is separable if and only if $f'\neq 0$.

(c) If $\ch k = 0$, every irreducible $f$ is separable.

(d) If $\ch k = p>0$, an irreducible $f$ is inseparable if and only if $f(x) = g(x^p)$ for some $g\in k[x]$.
:::

::: {.proof}
(a) A root $\alpha$ of $f$ in a splitting field is repeated if and only if $f'(\alpha)=0$, so $f$ has a repeated root if and only if $f$ and $f'$ have a common root, if and only if $\gcd(f,f')\neq1$; the gcd does not change under field extension.

(b) If $f$ is irreducible, $\gcd(f,f')$ is $1$ or an associate of $f$, and it is an associate of $f$ if and only if $f\divides f'$, which, since $\deg f'<\deg f$, holds if and only if $f'=0$.

(c) If $\ch k=0$ and $\deg f\geq1$, then $f'$ has degree $\deg f-1$, so $f'\neq0$.

(d) Write $f=\sum_i a_ix^i$.
Then $f'=\sum_i ia_ix^{i-1}=0$ if and only if $p\divides i$ whenever $a_i\neq0$, that is, if and only if $f(x)=g(x^p)$ for some $g\in k[x]$.
:::

::: {.example}
Part (b) requires irreducibility: $f(x) = x^2(x-1)\in\QQ[x]$ has $f'=3x^2-2x\neq 0$ and the repeated root $0$.
:::
