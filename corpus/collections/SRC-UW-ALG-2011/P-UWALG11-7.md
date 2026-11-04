---
schema: qual/card@1
id: P-UWALG11-7
kind: problem
title: 'For finitely generated $\ZZ$-modules, $M\otimes_\ZZ N=0$ if and only if $\operatorname{Ann}(M)+\operatorname{Ann}(N)=(1)$'
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Tensor Products
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $M,N$ be finitely generated modules over $\ZZ$.
Recall that $\operatorname{Ann}(M)$ is the ideal in $\ZZ$ defined as follows:
$$
\operatorname{Ann}(M)=\{a\in\ZZ\mid am=0\text{ for any }m\in M\}.
$$
Prove that $M\otimes_\ZZ N=0$ if and only if $\operatorname{Ann}(M)+\operatorname{Ann}(N)=(1)$.
:::

::: {.solution}
The ideals of $\ZZ$ are principal, so $\operatorname{Ann}(M)=(m)$ and $\operatorname{Ann}(N)=(n)$ for unique $m,n\ge0$, and $\operatorname{Ann}(M)+\operatorname{Ann}(N)=(\gcd(m,n))$; a module is annihilated by $0$ exactly when it has a nonzero free summand or is trivial.

::: pf

::: {.pf-step #sum-one-kills-tensor}
If $\operatorname{Ann}(M)+\operatorname{Ann}(N)=(1)$, then $M\otimes_\ZZ N=0$.

::: pf-proof
Write $1=a+b$ with $a\in\operatorname{Ann}(M)$ and $b\in\operatorname{Ann}(N)$, possible because the sum of the two ideals is the whole ring.
For $m\in M$ and $n\in N$ bilinearity gives
$$
m\otimes n=(a+b)(m\otimes n)=am\otimes n+m\otimes bn=0,
$$
and the pure tensors generate $M\otimes_\ZZ N$.
:::

:::

::: {.pf-step #nonzero-tensor}
If $M\otimes_\ZZ N=0$, then $\operatorname{Ann}(M)+\operatorname{Ann}(N)=(1)$.

::: pf-proof
We prove the contrapositive: assume $\operatorname{Ann}(M)+\operatorname{Ann}(N)=(d)$ with $d\ne1$.
Neither module is then zero, since the zero module has annihilator $(1)$, which would give $d=1$.
If $d=0$ then $\operatorname{Ann}(M)=\operatorname{Ann}(N)=(0)$: neither module is annihilated by a nonzero integer, so each has a nonzero free summand, and $\ZZ\otimes_\ZZ\ZZ\cong\ZZ$ is a direct summand of $M\otimes_\ZZ N$, which is therefore nonzero.
So let $d\ne0$ and choose a prime $p$ dividing $d=\gcd(m,n)$.
If $\operatorname{Ann}(M)=(0)$ then $M$ has a nonzero free summand, while $p\mid n\ne0$ makes $N$ finite with a summand $\ZZ/p^b\ZZ$, $b\ge1$, by the structure theorem; then $\ZZ\otimes_\ZZ\ZZ/p^b\ZZ\cong\ZZ/p^b\ZZ\ne0$ is a direct summand of $M\otimes_\ZZ N$.
Otherwise $m\ne0$, and $p\mid m$ makes $M$ finite with a summand $\ZZ/p^a\ZZ$, $a\ge1$; as $n\ne0$ and $p\mid n$, $N$ has a summand $\ZZ/p^b\ZZ$, $b\ge1$, and then
$$
\ZZ/p^{a}\ZZ\otimes_\ZZ\ZZ/p^{b}\ZZ\cong\ZZ/p^{\min(a,b)}\ZZ\ne0
$$
is a direct summand of $M\otimes_\ZZ N$.
:::

:::

:::

:::
