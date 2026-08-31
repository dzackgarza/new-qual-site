---
schema: qual/card@1
id: P-PGDJ2
kind: problem
title: "Zeros of a polynomial in the annulus from one to three"
classification:
  areas:
  - real-analysis
  topics:
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

1. How many zeros does the polynomial

$$
z^9 + z^6 + 30 z^5 - 3z + 2
$$

have in the annulus $\{ 1 \leq | z | \leq 3 \}$ . Justify your answer.

::: solution
**Goal:** Determine the number of zeros of the polynomial $P(z) = z^9 + z^6 + 30z^5 - 3z + 2$ in the closed annulus $A = \{z \in \mathbb{C} : 1 \le |z| \le 3\}$ counted with multiplicity.

<1>1. Number of zeros inside the open disk $D_3 = \{z \in \mathbb{C} : |z| < 3\}$:
    *Proof:*
    <2>1. On the boundary circle $C_3 = \{z \in \mathbb{C} : |z| = 3\}$, let $f(z) = z^9$ and $g(z) = z^6 + 30z^5 - 3z + 2$, so $P(z) = f(z) + g(z)$.
    <2>2. For $|z| = 3$, $|f(z)| = |z|^9 = 3^9 = 19683$.
    <2>3. By the triangle inequality on $C_3$:
    $$|g(z)| \le |z|^6 + 30|z|^5 + 3|z| + 2 = 3^6 + 30(3^5) + 3(3) + 2 = 729 + 30(243) + 9 + 2 = 8030.$$
    <2>4. Since $|g(z)| = 8030 < 19683 = |f(z)|$ for all $z \in C_3$, Rouché's Theorem implies that $P(z) = f(z) + g(z)$ and $f(z) = z^9$ have the exact same number of zeros inside $|z| < 3$.
    <2>5. The function $f(z) = z^9$ has a single zero of multiplicity 9 at $z = 0$, so $P(z)$ has exactly 9 zeros in $|z| < 3$.
    <2>6. Furthermore, since $|P(z)| \ge |f(z)| - |g(z)| = 19683 - 8030 = 11653 > 0$ on $C_3$, $P(z)$ has no zeros on the circle $|z| = 3$.

<1>2. Number of zeros inside the open disk $D_1 = \{z \in \mathbb{C} : |z| < 1\}$:
    *Proof:*
    <2>1. On the boundary circle $C_1 = \{z \in \mathbb{C} : |z| = 1\}$, let $F(z) = 30z^5$ and $G(z) = z^9 + z^6 - 3z + 2$, so $P(z) = F(z) + G(z)$.
    <2>2. For $|z| = 1$, $|F(z)| = 30|z|^5 = 30(1)^5 = 30$.
    <2>3. By the triangle inequality on $C_1$:
    $$|G(z)| \le |z|^9 + |z|^6 + 3|z| + 2 = 1 + 1 + 3(1) + 2 = 7.$$
    <2>4. Since $|G(z)| = 7 < 30 = |F(z)|$ for all $z \in C_1$, Rouché's Theorem implies that $P(z)$ and $F(z) = 30z^5$ have the exact same number of zeros inside $|z| < 1$.
    <2>5. The function $F(z) = 30z^5$ has a single zero of multiplicity 5 at $z = 0$, so $P(z)$ has exactly 5 zeros in $|z| < 1$.
    <2>6. Since $|P(z)| \ge |F(z)| - |G(z)| = 30 - 7 = 23 > 0$ on $C_1$, $P(z)$ has no zeros on the boundary circle $|z| = 1$.

<1>3. Counting zeros in the annulus $\{1 \le |z| \le 3\}$:
    *Proof:*
    <2>1. By steps 1.6 and 2.6, $P(z)$ has no zeros on the boundary circles $|z| = 1$ and $|z| = 3$.
    <2>2. The number of zeros of $P(z)$ in the annulus $\{1 \le |z| \le 3\}$ is the difference between the number of zeros in $|z| < 3$ and $|z| < 1$:
    $$N_{\text{annulus}} = N(|z| < 3) - N(|z| < 1) = 9 - 5 = 4.$$

<1>4. Conclusion:
    *Proof:*
    The polynomial has exactly 4 zeros in the annulus $\{1 \le |z| \le 3\}$.
:::
