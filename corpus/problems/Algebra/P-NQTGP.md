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
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source uses $a$ in part (a) without declaring it; the statement declares $a$ as an integer.
---

::: {.problem}
Let $\Phi_m(x)$ be the $m$th cyclotomic polynomial, with $m>1$.

(a) Prove that if $a$ is an integer and a prime $p$ divides $\Phi_m(a)$ and $\gcd(p,m)=1$, then $m\mid p-1$.

(b) Deduce that there are infinitely many primes congruent to $1\pmod m$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) If a prime $p\nmid m$ divides $\Phi_m(a)$, then $a$ has order exactly $m$ modulo $p$, so $m\mid p-1$.

::: pf-proof

Since $p\mid\Phi_m(a)$ and $p\nmid m$, the reduction of $x^m-1$ modulo $p$ is separable: its derivative is $mx^{m-1}$, which has no common root with $x^m-1$.

The factorization
$$
x^m-1=\prod_{d\mid m}\Phi_d(x)
$$
therefore remains a product of pairwise coprime factors modulo $p$. Thus a root of $\Phi_m$ modulo $p$ cannot be a root of $x^d-1$ for any proper divisor $d\mid m$. Hence the residue class of $a$ in $\FF_p^\times$ has multiplicative order exactly $m$.

By Lagrange's theorem, this order divides
$$
\abs{\FF_p^\times}=p-1,
$$
so $m\mid p-1$.

:::

:::

::: pf-step

(b) There are infinitely many primes $p\equiv1\pmod m$.

::: pf-proof

Suppose instead that the complete list is $p_1,\ldots,p_r$. Put
$$
N=mp_1\cdots p_r.
$$
Since $m>1$, the constant term of $\Phi_m$ is $1$, so
$$
\Phi_m(N)\equiv1\pmod N.
$$
Choose a prime $q$ dividing the integer $\Phi_m(N)$. Then $q\nmid N$, so in particular $q\nmid m$ and $q\ne p_i$ for every $i$.

By step [](#s1){.pf-ref} applied to $a=N$, we have
$$
m\mid q-1,
$$
so $q\equiv1\pmod m$. This gives a new prime of the required congruence class, contradicting completeness of the list.

:::

:::

:::

:::
