---
schema: qual/card@1
id: P-2XYZ3
kind: problem
title: Finite division rings are fields, and an infinite noncommutative example
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Rings
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Prove that any finite division ring is a field (that is, prove commutativity).
Give an example of a (necessarily infinite) division ring which is NOT a field.
:::

::: {.solution}
Let $D$ be a finite division ring with center $Z$, a finite field of order $q\ge2$, and let $n=\dim_ZD$, so $|D|=q^n$.

::: pf

::: {.pf-step #s1}

For $x\in D^\times$ noncentral, $|C_D(x)|=q^d$ with $d\mid n$ and $d<n$.

::: pf-proof

$C_D(x)=\{y:yx=xy\}$ is a division subring containing $Z$, so $|C_D(x)|=q^d$ with $d=\dim_ZC_D(x)$.
$D$ is a vector space over $C_D(x)$, so $q^n=(q^d)^m$ for some $m$, and $d\mid n$; $d<n$ because $x$ is not central.

:::

:::

::: {.pf-step #s2}

$q-1=(q^n-1)-\sum_{i=1}^m\frac{q^n-1}{q^{d_i}-1}$ for proper divisors $d_i$ of $n$.

::: pf-proof

This is the class equation of $D^\times$: $|D^\times|=q^n-1$, $|Z(D^\times)|=|Z^\times|=q-1$, and the class of a noncentral $x_i$ has size $[D^\times:C_D(x_i)^\times]=\frac{q^n-1}{q^{d_i}-1}$ with $d_i$ as in step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

$\Phi_n(q)\mid q-1$, where $\Phi_n$ is the $n$th cyclotomic polynomial.

::: pf-proof

In $\ZZ[x]$, $x^n-1=\prod_{c\mid n}\Phi_c(x)$ and $x^{d}-1=\prod_{c\mid d}\Phi_c(x)$.
For a proper divisor $d$ of $n$, $\Phi_n$ does not occur in the second product, so $\Phi_n(x)$ divides $\frac{x^n-1}{x^d-1}$ in $\ZZ[x]$.
Evaluating at $q$, $\Phi_n(q)$ divides $q^n-1$ and every $\frac{q^n-1}{q^{d_i}-1}$, hence $q-1$ by step [](#s2){.pf-ref}.

:::

:::

::: pf-step

$n=1$, so $D=Z$ is a field.

::: pf-proof

Suppose $n>1$.
For a primitive $n$th root of unity $\zeta\neq1$, $\operatorname{Re}\zeta<1$, so
$$|q-\zeta|^2=q^2-2q\operatorname{Re}\zeta+1>(q-1)^2 .$$
Hence $|\Phi_n(q)|=\prod_\zeta|q-\zeta|>(q-1)^{\varphi(n)}\ge q-1$, contradicting step [](#s3){.pf-ref} since $q-1>0$.

:::

:::

::: pf-step

The real quaternions $\mathbb H=\{a+bi+cj+dk:a,b,c,d\in\RR\}$, with $i^2=j^2=k^2=ijk=-1$, form a division ring that is not a field.

::: pf-proof

For $z=a+bi+cj+dk\neq0$, put $\bar z=a-bi-cj-dk$; then $z\bar z=\bar zz=a^2+b^2+c^2+d^2>0$, so $z^{-1}=\bar z/(a^2+b^2+c^2+d^2)$.
Since $ij=k\neq-k=ji$, $\mathbb H$ is not commutative.

:::

:::

:::

:::
