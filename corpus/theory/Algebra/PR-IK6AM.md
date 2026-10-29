---
schema: qual/card@1
id: PR-IK6AM
kind: proposition
title: Frobenius criterion for perfect fields
slogan: 'Perfect means characteristic zero, or Frobenius-surjective in positive characteristic.'
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Characteristic
relations: []
review: draft
---

::: {.proposition}
A field $k$ is [[D-KQFIV|perfect]] if and only if either

- $\ch k = 0$, or

- $\ch k = p > 0$ and $k^p = k$.
:::

::: {.proof}
If $\ch k=0$ and $f\in k[x]$ is a nonconstant irreducible polynomial, then $f'\neq0$ and $\deg f'<\deg f$. Hence $\gcd(f,f')=1$, so $f$ is separable by [[PR-TLBPS]]. Thus $k$ is perfect.

Now let $\ch k=p>0$. Suppose first that $k^p=k$. If an irreducible $f\in k[x]$ were inseparable, then [[PR-TLBPS]] would give $\gcd(f,f')\neq1$. Irreducibility and $\deg f'<\deg f$ force $f'=0$. Thus
$$
f(x)=\sum_i a_i x^{pi}.
$$
Surjectivity of Frobenius gives $a_i=b_i^p$ for some $b_i\in k$, so
$$
f(x)=\left(\sum_i b_i x^i\right)^p,
$$
contradicting irreducibility. Hence $k$ is perfect.

Conversely, suppose $k^p\neq k$, and choose $a\in k\setminus k^p$. Let $\beta$ satisfy $\beta^p=a$ in a splitting field. Then
$$
x^p-a=(x-\beta)^p.
$$
If $x^p-a$ had a monic factor over $k$ of degree $j$ with $0<j<p$, then over the splitting field that factor would be $(x-\beta)^j$. Its coefficient of $x^{j-1}$ is $-j\beta$; since $j$ is nonzero in $k$, this would imply $\beta\in k$, contradicting $a\notin k^p$. Thus $x^p-a$ is irreducible. Its derivative is zero, so it is inseparable, and $k$ is not perfect.
:::
