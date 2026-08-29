---
schema: qual/card@1
id: P-F2YIN
kind: problem
title: Factorisation in $R[x_1,\ldots,x_n]$
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Talk about factorisation and primes in a polynomial ring.
What is irreducibility?
For what rings $R$ is it true that $R[x_1, \dots , x_n]$ is a unique factorisation domain?
What is wrong with unique factorisation if we don't have a domain?
Now, PIDs are Noetherian, but are there UFDs which are not?
:::

::: solution
**Goal:** Address definitions of irreducibility and primality, Gauss's theorem for polynomial rings, factorization in non-domains, and non-Noetherian UFDs.

<1>1. Definitions: Irreducibility vs. Primality:
    *Proof:*
    <2>1. Let $R$ be an integral domain. A non-zero element $p \in R \setminus R^\times$ is:
        - **Irreducible:** if whenever $p = ab$ with $a, b \in R$, either $a \in R^\times$ or $b \in R^\times$.
        - **Prime:** if $(p)$ is a prime ideal, i.e., whenever $p \mid ab$, either $p \mid a$ or $p \mid b$.
    <2>2. In any integral domain, prime $\implies$ irreducible. In a UFD (and only in a UFD among ACCP domains), irreducible $\implies$ prime.

<1>2. Condition for $R[x_1, \dots, x_n]$ to be a UFD (Gauss's Theorem):
    *Proof:*
    <2>1. **Theorem (Gauss):** If $R$ is a UFD, then the polynomial ring $R[x]$ is a UFD.
    <2>2. By induction on $n$, $R[x_1, \dots, x_n] = (R[x_1, \dots, x_{n-1}])[x_n]$ is a UFD if and only if $R$ is a UFD.
    <2>3. Conversely, if $R[x_1, \dots, x_n]$ is a UFD, then $R$ is a UFD (since $R \cong R[x_1, \dots, x_n] / (x_1, \dots, x_n)$ and retracts of UFDs onto subrings of constants preserve unique factorization).

<1>3. Unique factorization in non-domains:
    *Proof:*
    <2>1. In rings with zero divisors, unique factorization breaks down completely:
        - Zero divisors allow non-unique factorizations of $0$: $0 = 0 \cdot a = 0 \cdot b$.
        - Idempotents $e^2 = e \implies e(1-e) = 0$ give multiple factorizations of elements into non-units.
        - For example, in $\mathbb{Z}/6\mathbb{Z}$: $0 = 2 \cdot 3 = 0 \cdot 0$, and elements can have factorizations into products of differing lengths with no meaningful uniqueness up to associates.

<1>4. Non-Noetherian UFDs:
    *Proof:*
    <2>1. Yes, there exist UFDs that are not Noetherian.
    <2>2. **Canonical example:** A polynomial ring in infinitely many variables over a field:
        $$R = k[x_1, x_2, x_3, \dots].$$
    <2>3. **Why it is a UFD:** Any polynomial $f \in R$ involves only finitely many variables $\{x_1, \dots, x_m\}$, hence factors uniquely in the UFD $k[x_1, \dots, x_m]$.
    <2>4. **Why it is not Noetherian:** The ascending chain of ideals:
        $$(x_1) \subsetneq (x_1, x_2) \subsetneq (x_1, x_2, x_3) \subsetneq \cdots$$
        never stabilizes. Equivalently, the ideal $\mathfrak{m} = (x_1, x_2, x_3, \dots)$ is not finitely generated.

<1>5. Conclusion:
    $R[x_1, \dots, x_n]$ is a UFD iff $R$ is a UFD; non-domains suffer from zero-divisor and idempotent ambiguities; $k[x_1, x_2, \dots]$ is a non-Noetherian UFD. Q.E.D.
:::
