---
schema: qual/card@1
id: P-YFBGZ
kind: problem
title: Radical ideals in $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Nilpotence
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Classify all **radical ideals** in the ring of integers $\mathbb{Z}$.
:::

::: solution
**Goal:** Prove that the radical ideals in $\mathbb{Z}$ are precisely the principal ideals $(n) = n\mathbb{Z}$ where $n = 0$ or $n$ is a **square-free integer** (a product of distinct prime numbers).

<1>1. Definition of Radical Ideal in a Commutative Ring:
    *Proof:*
    <2>1. Let $R$ be a commutative ring and $I \subseteq R$ an ideal.
    <2>2. The **radical** of $I$, denoted $\sqrt{I}$ or $\operatorname{rad}(I)$, is defined as:
        $$\sqrt{I} \coloneqq \{x \in R \mid \exists k \in \mathbb{Z}_{\ge 1} \text{ such that } x^k \in I\}.$$
    <2>3. An ideal $I$ is called a **radical ideal** if $I = \sqrt{I}$.

<1>2. Principal Ideal Form in $\mathbb{Z}$:
    *Proof:*
    <2>1. Since $\mathbb{Z}$ is a Principal Ideal Domain, every ideal $I \subseteq \mathbb{Z}$ is of the form $I = (n) = n\mathbb{Z}$ for a unique non-negative integer $n \ge 0$.
    <2>2. **Case $n = 0$:**
        - $I = (0) = \{0\}$.
        - $x^k \in (0) \iff x^k = 0 \iff x = 0$ (since $\mathbb{Z}$ is an integral domain).
        - Thus $\sqrt{(0)} = (0)$, so $(0)$ is a radical ideal.

<1>3. Radical of $(n)$ for $n \ge 1$:
    *Proof:*
    <2>1. Let $n \ge 1$, and write its unique prime factorization as:
        $$n = p_1^{a_1} p_2^{a_2} \cdots p_r^{a_r}$$
        where $p_1, \dots, p_r$ are distinct prime numbers and $a_i \ge 1$.
    <2>2. Let $m = \operatorname{rad}(n) = p_1 p_2 \cdots p_r$ be the **square-free core** (radical) of $n$.
    <2>3. We determine $\sqrt{(n)}$:
        - If $x \in \sqrt{(n)}$, then $n \mid x^k$ for some $k \ge 1$.
        - For each prime factor $p_i \mid n$, we have $p_i \mid x^k \implies p_i \mid x$.
        - Since the primes $p_i$ are distinct and coprime, their product $m = p_1 \cdots p_r$ must divide $x$.
        - Thus $x \in (m)$.
        - Conversely, if $x \in (m)$, then $m \mid x$.
        - Letting $K = \max\{a_1, \dots, a_r\}$, we have $n = p_1^{a_1} \cdots p_r^{a_r} \mid (p_1 \cdots p_r)^K = m^K \mid x^K$.
        - Thus $x^K \in (n)$, so $x \in \sqrt{(n)}$.
    <2>4. Therefore:
        $$\sqrt{(n)} = (p_1 p_2 \cdots p_r) = (m).$$

<1>4. Characterization of Radical Ideals:
    *Proof:*
    <2>1. $(n)$ is a radical ideal $\iff (n) = \sqrt{(n)} = (m) \iff n = m$.
    <2>2. $n = m \iff a_1 = a_2 = \cdots = a_r = 1$.
    <2>3. This is precisely the condition that $n$ is **square-free** (or $n = 1$, where $(1) = \mathbb{Z}$).

<1>5. Conclusion:
    The radical ideals in $\mathbb{Z}$ are $(0)$ and $(p_1 p_2 \cdots p_r)$ where $p_1, \dots, p_r$ are distinct primes (including the empty product $n = 1$, giving $(1) = \mathbb{Z}$). Q.E.D.
:::
