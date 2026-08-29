---
schema: qual/card@1
id: P-ALGS04J
kind: problem
title: "Representing numbers as sums of two squares using Gaussian integer norms"
classification:
  areas:
  - algebra
  topics:
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
In the ring of Gaussian integers $\mathbb{Z}[i]$, the field norm $N(a + bi) = a^2 + b^2$ is used to analyze representations of integers as sums of two squares.
Use this technique to determine the number of integer pairs $(a, b) \in \mathbb{Z}^2$ such that $a^2 + b^2 = N$ for:
(1) $N = 3^4 = 81$, and
(2) $M = 5^4 = 625$.
*(Also determine the number of essentially distinct representations up to sign changes and order).*
:::

::: solution
**Goal:** Count the number of representations of $3^4$ and $5^4$ as sums of two squares $a^2 + b^2$ using unique factorization in the Gaussian integers $\mathbb{Z}[i]$.

<1>1. Gaussian Integer Arithmetic and Sums of Two Squares:
    *Proof:*
    <2>1. An integer representation $a^2 + b^2 = n$ corresponds bijectively to finding a Gaussian integer $\alpha = a + bi \in \mathbb{Z}[i]$ whose norm is:
        $$N(\alpha) = a^2 + b^2 = n.$$
    <2>2. The ring of Gaussian integers $\mathbb{Z}[i]$ is a Euclidean Domain, hence a **Unique Factorization Domain (UFD)**.
    <2>3. The group of units in $\mathbb{Z}[i]$ has order 4:
        $$\mathbb{Z}[i]^\times = \{1, -1, i, -i\}.$$
    <2>4. If $\alpha = a + bi$ has norm $n$, multiplying by units $\{\pm 1, \pm i\}$ produces the four associate elements:
        $$\pm (a + bi), \quad \pm (-b + ai)$$
        which correspond to the ordered pairs $(\pm a, \pm b)$ and $(\pm b, \mp a)$.

<1>2. Factorization of $N = 3^4 = 81$ in $\mathbb{Z}[i]$:
    *Proof:*
    <2>1. The rational prime $p = 3$ satisfies $3 \equiv 3 \pmod 4$, so $3$ is an **inert prime** in $\mathbb{Z}[i]$.
    <2>2. Thus the unique prime factorization of $81$ in $\mathbb{Z}[i]$ is:
        $$81 = 3^4.$$
    <2>3. Any divisor $\alpha \in \mathbb{Z}[i]$ with $N(\alpha) = 81 = 3^4$ must have the prime factorization:
        $$\alpha = u \cdot 3^k$$
        for some unit $u \in \mathbb{Z}[i]^\times$ and integer $k \ge 0$.
    <2>4. Taking norms: $N(\alpha) = N(u) N(3)^k = 1 \cdot (3^2)^k = 3^{2k} = 9^k$.
    <2>5. Setting $9^k = 81 = 9^2$ forces $k = 2$.
    <2>6. Thus the only elements of norm $81$ are:
        $$\alpha = u \cdot 3^2 = 9u \quad \text{for } u \in \{1, -1, i, -i\}.$$
    <2>7. Explicitly, $\alpha \in \{9, -9, 9i, -9i\}$.
    <2>8. In terms of pairs $(a, b) \in \mathbb{Z}^2$:
        $$(a, b) \in \{ (9, 0), (-9, 0), (0, 9), (0, -9) \}.$$
    <2>9. Total ordered representations: **$r_2(3^4) = 4$**.
    <2>10. Essentially distinct sum of squares: $81 = 9^2 + 0^2$ (**1 distinct representation**).

<1>3. Factorization of $M = 5^4 = 625$ in $\mathbb{Z}[i]$:
    *Proof:*
    <2>1. The rational prime $p = 5$ satisfies $5 \equiv 1 \pmod 4$, so $5$ **splits** into non-associate conjugate Gaussian primes:
        $$5 = (2 + i)(2 - i) = \pi \bar{\pi}.$$
    <2>2. Thus $M = 5^4 = \pi^4 \bar{\pi}^4$ in $\mathbb{Z}[i]$.
    <2>3. Any Gaussian integer $\alpha$ with $N(\alpha) = 5^4$ must have the form:
        $$\alpha = u \cdot \pi^k \bar{\pi}^{4-k}$$
        for some unit $u \in \mathbb{Z}[i]^\times$ and integer $0 \le k \le 4$.
    <2>4. There are $5$ possible choices for $k \in \{0, 1, 2, 3, 4\}$, and for each choice of $k$, there are $4$ choices for the unit $u$.
    <2>5. Since $\pi$ and $\bar{\pi}$ are not associates ($\pi / \bar{\pi} = \frac{3+4i}{5} \notin \mathbb{Z}[i]$), all $4 \times 5 = 20$ elements are distinct!
    <2>6. Total ordered representations:
        $$r_2(5^4) = 4 \cdot (4 + 1) = 20.$$
    <2>7. We list the 5 ideal classes / values of $\alpha$ up to units:
        - $k = 4$: $\alpha = (2+i)^4 = -7 + 24i \implies (\pm 7, \pm 24), (\pm 24, \pm 7)$ ($7^2 + 24^2 = 49 + 576 = 625$, 8 pairs).
        - $k = 3$: $\alpha = (2+i)^3(2-i) = 5(2+i)^2 = 5(3+4i) = 15 + 20i \implies (\pm 15, \pm 20), (\pm 20, \pm 15)$ ($15^2 + 20^2 = 225 + 400 = 625$, 8 pairs).
        - $k = 2$: $\alpha = (2+i)^2(2-i)^2 = 5^2 = 25 \implies (\pm 25, 0), (0, \pm 25)$ ($25^2 + 0^2 = 625$, 4 pairs).
        - $k = 1$: $\alpha = (2+i)(2-i)^3 = \bar{\alpha}_{k=3} = 15 - 20i$ (same pairs as $k=3$).
        - $k = 0$: $\alpha = (2-i)^4 = \bar{\alpha}_{k=4} = -7 - 24i$ (same pairs as $k=4$).
    <2>8. Summing the pairs: $8 + 8 + 4 = 20$ ordered pairs.
    <2>9. Essentially distinct sums of squares:
        $$625 = 25^2 + 0^2 = 24^2 + 7^2 = 20^2 + 15^2$$
        (**3 distinct representations**).

<1>4. Conclusion:
    - For $N = 3^4 = 81$: $4$ integer pairs $(a, b)$, corresponding to $81 = 9^2 + 0^2$.
    - For $M = 5^4 = 625$: $20$ integer pairs $(a, b)$, corresponding to $625 = 25^2 + 0^2 = 24^2 + 7^2 = 20^2 + 15^2$.
    Q.E.D.
:::
