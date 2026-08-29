---
schema: qual/card@1
id: P-6T7VU
kind: problem
title: Invariant factors of $R/(r)\oplus R/(s)$ over a PID
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $R$ be a Principal Ideal Domain (PID), and let $r, s \in R \setminus \{0\}$ be non-zero elements.
Determine the **invariant factors** of the $R$-module:
$$M = R/(r) \oplus R/(s).$$
:::

::: solution
**Goal:** Prove that the invariant factors of $R/(r) \oplus R/(s)$ are $d_1 = \gcd(r, s)$ and $d_2 = \operatorname{lcm}(r, s)$ with $d_1 \mid d_2$.

<1>1. Elementary Divisors via Prime Factorization:
    *Proof:*
    <2>1. Since $R$ is a PID, it is a Unique Factorization Domain (UFD).
    <2>2. Let $\{p_1, p_2, \dots, p_k\}$ be the set of all distinct irreducible elements (primes up to units) dividing $r$ or $s$.
    <2>3. Write the prime factorizations (up to units):
        $$r = u \prod_{i=1}^k p_i^{a_i}, \qquad s = v \prod_{i=1}^k p_i^{b_i}$$
        where $u, v \in R^\times$ are units and $a_i, b_i \ge 0$ are non-negative integers.
    <2>4. By the **Chinese Remainder Theorem for PIDs**, each cyclic module decomposes into primary cyclic components:
        $$R/(r) \cong \bigoplus_{i=1}^k R/(p_i^{a_i}), \qquad R/(s) \cong \bigoplus_{i=1}^k R/(p_i^{b_i}).$$
    <2>5. Taking the direct sum, the module $M$ decomposes into its primary components:
        $$M = R/(r) \oplus R/(s) \cong \bigoplus_{i=1}^k \left( R/(p_i^{a_i}) \oplus R/(p_i^{b_i}) \right).$$
    <2>6. Thus the **elementary divisors** of $M$ are the prime powers $\{p_i^{a_i}, p_i^{b_i} \mid a_i > 0 \text{ or } b_i > 0\}$.

<1>2. Assembling Invariant Factors from Elementary Divisors:
    *Proof:*
    <2>1. By the Structure Theorem for finitely generated torsion modules over a PID, the invariant factors $d_1 \mid d_2 \mid \cdots \mid d_m$ are reconstructed from the elementary divisors by grouping the prime power factors:
        - The largest invariant factor $d_{\max} = d_2$ takes the **highest power** of each prime appearing among the primary components:
          $$d_2 \coloneqq \prod_{i=1}^k p_i^{\max(a_i, b_i)} = \operatorname{lcm}(r, s).$$
        - The remaining powers for each prime are allocated to the second invariant factor $d_1$:
          $$d_1 \coloneqq \prod_{i=1}^k p_i^{\min(a_i, b_i)} = \gcd(r, s).$$
    <2>2. Since $\min(a_i, b_i) \le \max(a_i, b_i)$ for every $i \in \{1, \dots, k\}$, the divisibility condition holds:
        $$d_1 \mid d_2 \quad (\gcd(r, s) \mid \operatorname{lcm}(r, s)).$$
    <2>3. By the Chinese Remainder Theorem:
        $$R/(d_1) \cong \bigoplus_{i=1}^k R/(p_i^{\min(a_i, b_i)}), \qquad R/(d_2) \cong \bigoplus_{i=1}^k R/(p_i^{\max(a_i, b_i)}).$$
    <2>4. Thus:
        $$M \cong R/(d_1) \oplus R/(d_2) = R/(\gcd(r, s)) \oplus R/(\operatorname{lcm}(r, s)).$$

<1>3. Alternative Presentation Matrix Method (Smith Normal Form):
    *Proof:*
    <2>1. The module $M = R/(r) \oplus R/(s)$ has presentation matrix $A = \begin{bmatrix} r & 0 \\ 0 & s \end{bmatrix}$.
    <2>2. The determinantal divisors of $A$ are:
        - $\Delta_1 = \gcd(r, 0, 0, s) = \gcd(r, s)$.
        - $\Delta_2 = \det(A) = rs = u \cdot \gcd(r, s) \cdot \operatorname{lcm}(r, s)$.
    <2>3. The invariant factors from the determinantal divisors are:
        - $d_1 = \Delta_1 = \gcd(r, s)$.
        - $d_2 = \Delta_2 / \Delta_1 = \operatorname{lcm}(r, s)$.

<1>4. Conclusion:
    The invariant factors of $R/(r) \oplus R/(s)$ are $d_1 = \gcd(r, s)$ and $d_2 = \operatorname{lcm}(r, s)$. Q.E.D.
:::
