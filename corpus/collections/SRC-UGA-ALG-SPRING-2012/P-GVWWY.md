---
schema: qual/card@1
id: P-GVWWY
kind: problem
title: Minimal and characteristic polynomials; Cayley-Hamilton
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---
::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $k$ and $T:V\to V$ a linear transformation.

a. Provide a definition for the *minimal polynomial* in $k[x]$ for $T$.

b. Define the *characteristic polynomial* for $T$.

c. Prove the Cayley-Hamilton theorem: the linear transformation $T$ satisfies its characteristic polynomial.
:::

::: {.solution}
Write $n=\dim_kV$.

::: pf

::: {.pf-step #s1}

The minimal polynomial $m_T\in k[x]$ is the unique monic generator of the ideal $\{p\in k[x]:p(T)=0\}$.

::: pf-proof

Evaluation at $T$ is a ring homomorphism $k[x]\to\operatorname{End}_k(V)$. Its kernel is an ideal and is nonzero: finite dimensionality of $\operatorname{End}_k(V)$ forces a linear dependence among $I,T,T^2,\ldots$. Since $k[x]$ is a PID, this nonzero ideal has a unique monic generator. When $V=0$, the ideal is the whole ring and the minimal polynomial is $1$.

:::

:::

::: {.pf-step #s2}

The characteristic polynomial is $p_T(x)=\det(xI_n-A)$ for any matrix $A$ representing $T$.

::: pf-proof

If $A'=PAP^{-1}$ represents $T$ in another basis, then $xI_n-A'=P(xI_n-A)P^{-1}$. Multiplicativity of the determinant implies $\det(xI_n-A')=\det(xI_n-A)$, so this definition is basis independent.

:::

:::

::: {.pf-step #s3}

The Cayley–Hamilton identity
$$
\boxed{p_T(T)=0}
$$
holds.

::: pf-proof

For $n=0$ the characteristic polynomial is $1$ and the endomorphism ring of the zero space is the zero ring, so the statement holds. Assume $n>0$. Set $C(x)=\operatorname{adj}(xI_n-A)=\sum_{j=0}^{n-1}C_jx^j$ and $p_T(x)=\sum_{j=0}^na_jx^j$. The adjugate identity gives
$$
C(x)(xI_n-A)=p_T(x)I_n.
$$
Equating coefficients gives $-C_0A=a_0I_n$, $C_{j-1}-C_jA=a_jI_n$ for $1\leq j<n$, and $C_{n-1}=a_nI_n$. Multiplying the $j$-th coefficient equation on the right by $A^j$ and summing yields
$$
\sum_{j=0}^na_jA^j=-C_0A+\sum_{j=1}^{n-1}(C_{j-1}A^j-C_jA^{j+1})+C_{n-1}A^n=0
$$
by telescoping. Thus $p_T(A)=0$, and therefore $p_T(T)=0$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} supply the requested definitions, and step [](#s3){.pf-ref} proves Cayley–Hamilton.

:::

:::

:::
