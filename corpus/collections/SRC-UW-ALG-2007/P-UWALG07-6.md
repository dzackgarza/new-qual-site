---
schema: qual/card@1
id: P-UWALG07-6
kind: problem
title: If $A^7=\operatorname{id}$ on a $\QQ$-vector space and $1$ is not an eigenvalue, then $6\mid\dim V$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $V$ be a finite dimensional vector space over $\QQ$ and $A:V\to V$ a linear map such that $A^7=\operatorname{id}$, the identity map.
Suppose that $1$ is not an eigenvalue of $A$.
Prove that $\dim V$ is divisible by $6$.
:::

::: {.solution}
Let $T\colon V\to V$ denote $A$, so that $T^7=1$ and $T-1$ is injective; the polynomial ring $\QQ[x]$ is a principal ideal domain, and $V$ is a finitely generated torsion $\QQ[x]$-module through $T$.

::: pf

::: {.pf-step #eigenvalue-one-absent}
$(x-1)$ is not an elementary divisor of $V$.

::: pf-proof
The element $1$ is an eigenvalue of $T$ exactly when some nonzero $v\in V$ satisfies $Tv=v$, that is exactly when $x-1$ divides an elementary divisor of $V$.
By hypothesis no such $v$ exists, so $(x-1)$ divides no elementary divisor.
:::

:::

::: {.pf-step #elementary-divisors}
Every elementary divisor of $V$ is $\Phi_7(x)=x^6+x^5+x^4+x^3+x^2+x+1$.

::: pf-proof
Since $T^7=1$, the polynomial $x^7-1=(x-1)\Phi_7$ annihilates $V$, so the minimal polynomial divides $x^7-1$ and every elementary divisor is a power of an irreducible factor of $x^7-1$.
Those irreducible factors are $x-1$ and $\Phi_7$: the cyclotomic polynomial $\Phi_7$ is irreducible over $\QQ$ because $7$ is prime, its roots being the primitive seventh roots of unity and its degree being $\varphi(7)=6$.
By step [](#eigenvalue-one-absent){.pf-ref} the factor $x-1$ occurs in no elementary divisor, so only $\Phi_7$ occurs.
:::

:::

::: {.pf-step #divisibility}
$6$ divides $\dim_\QQ V$.

::: pf-proof
By the structure theorem for finitely generated torsion modules over the principal ideal domain $\QQ[x]$, the module $V$ is a direct sum of pieces $\QQ[x]/(\Phi_7^{e_i})$ with $e_i\ge1$, by step [](#elementary-divisors){.pf-ref}.
Each piece is a $\QQ$-vector space of dimension $\deg\Phi_7^{e_i}=6e_i$, and dimensions add over direct sums, so $\dim_\QQ V=6\sum_ie_i$ is a multiple of $6$.
:::

:::

:::

:::
