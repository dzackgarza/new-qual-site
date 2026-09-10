---
schema: qual/card@1
id: P-NQTGP
kind: problem
title: Infinitely many primes congruent to $1\bmod m$ via cyclotomic polynomials
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Number Theory
  - Finite Fields
relations: []
review: draft
---

::: problem
Let $\Phi_m(x)$ be the $m$th cyclotomic polynomial, with $m>1$.

1. Prove that if a prime $p$ divides $\Phi_m(a)$ and $\gcd(p,m)=1$, then $m\mid p-1$.
2. Deduce that there are infinitely many primes congruent to $1\pmod m$.
:::

::: {.solution}
<1>1. A prime divisor of $\Phi_m(a)$ has $a$ of order $m$ modulo $p$.
::: {.proof}
Since $p\mid\Phi_m(a)$ and $p\nmid m$, the reduction of $x^m-1$ modulo $p$ is separable: its derivative is $mx^{m-1}$, which has no common root with $x^m-1$.

The factorization
\[
x^m-1=\prod_{d\mid m}\Phi_d(x)
\]
therefore remains a product of pairwise coprime factors modulo $p$. Thus a root of $\Phi_m$ modulo $p$ cannot be a root of $x^d-1$ for any proper divisor $d\mid m$. Hence the residue class of $a$ in $\FF_p^\times$ has multiplicative order exactly $m$.

By Lagrange's theorem, this order divides
\[
|\FF_p^\times|=p-1,
\]
so $m\mid p-1$.
:::

<1>2. There are infinitely many primes $p\equiv1\pmod m$.
::: {.proof}
Suppose instead that the complete list is $p_1,\ldots,p_r$. Put
\[
N=mp_1\cdots p_r.
\]
Since $m>1$, the constant term of $\Phi_m$ is $1$, so
\[
\Phi_m(N)\equiv1\pmod N.
\]
Choose a prime $q$ dividing the integer $\Phi_m(N)$. Then $q\nmid N$, so in particular $q\nmid m$ and $q\ne p_i$ for every $i$.

By <1>1 applied to $a=N$, we have
\[
m\mid q-1,
\]
so $q\equiv1\pmod m$. This gives a new prime of the required congruence class, contradicting completeness of the list.
:::
:::
