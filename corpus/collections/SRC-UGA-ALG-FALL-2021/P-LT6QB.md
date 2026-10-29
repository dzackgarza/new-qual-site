---
schema: qual/card@1
id: P-LT6QB
kind: problem
title: 'Cyclotomic fields $\QQ(\zeta_n)$: degree, Galois group, and quadratic subfields
  of $\QQ(\zeta_{2021})$'
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---
::: {.problem}
Recall that for a positive integer $n$, the cyclotomic field $\QQ(\zeta_n)$ is generated over $\QQ$ by a primitive $n$-th root of unity $\zeta_n$.

(a) What is the degree $[\QQ(\zeta_n) : \QQ]$?

(b) Define what it means for a finite field extension $L/K$ to be **Galois**, and prove that the cyclotomic field $\QQ(\zeta_n)$ is Galois over $\QQ$.

(c) What is the Galois group $\operatorname{Gal}(\QQ(\zeta_n)/\QQ)$?

(d) How many subfields of $\QQ(\zeta_{2021})$ have degree 2 over $\QQ$? *(Note that $2021 = 43 \cdot 47$).*
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The degree of the $n$-th cyclotomic field is
\[
\boxed{[\QQ(\zeta_n):\QQ]=\varphi(n)}.
\]

::: pf-proof

The minimal polynomial of a primitive $n$-th root of unity is the cyclotomic polynomial $\Phi_n(x)$, irreducible over $\QQ$. Its roots are precisely the $\varphi(n)$ primitive $n$-th roots, so its degree is $\varphi(n)$.

:::

:::

::: {.pf-step #s2}

The extension $\QQ(\zeta_n)/\QQ$ is Galois.

::: pf-proof

A finite extension is Galois if and only if it is normal and separable. The cyclotomic field is the splitting field over $\QQ$ of $x^n-1$, because every root is a power of $\zeta_n$. This polynomial is separable in characteristic zero, so the extension is normal and separable.

:::

:::

::: {.pf-step #s3}

Its Galois group is
\[
\boxed{\operatorname{Gal}(\QQ(\zeta_n)/\QQ)\cong(\ZZ/n\ZZ)^\times}.
\]

::: pf-proof

An automorphism of $\QQ(\zeta_n)$ is determined by the image of $\zeta_n$, necessarily a primitive $n$-th root $\zeta_n^a$ with $a$ invertible modulo $n$. The assignment $\sigma\mapsto a\bmod n$ is an injective homomorphism into $(\ZZ/n\ZZ)^\times$, since composition corresponds to multiplication of exponents. By step [](#s1){.pf-ref}, both groups have cardinality $\varphi(n)$, so the map is an isomorphism.

:::

:::

::: {.pf-step #s4}

The field $\QQ(\zeta_{2021})$ has exactly
\[
\boxed{3}
\]
quadratic subfields.

::: pf-proof

Since $2021=43\cdot47$, the Chinese remainder theorem and step [](#s3){.pf-ref} give
\[
G\cong(\ZZ/43\ZZ)^\times\times(\ZZ/47\ZZ)^\times
\cong C_{42}\times C_{46}.
\]
Each factor is cyclic of even order, with exactly one nontrivial homomorphism to $C_2$. Hence $\operatorname{Hom}(G,C_2)\cong C_2^2$ has exactly three nontrivial homomorphisms. Each is surjective and has an index-two kernel; conversely every index-two subgroup arises uniquely in this way. By the Galois correspondence, these three subgroups correspond to the quadratic intermediate fields.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a)--(d), respectively.

:::

:::

:::
