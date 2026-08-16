---
schema: qual/card@1
id: P-3T5VY
kind: problem
title: Find the number of zeroes, counting multiplicities, of the polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - holomorphic-functions
  - polynomials
  - rouche
relations: []
review: draft
---

::: problem
Find the number of zeroes, counting multiplicities, of the polynomial

$f(z) = 2z^5 - 6z^2 - z + 1 = 0$

in the annulus $1 \leq |z| \leq 2$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Determine the number of zeros of $f(z) = 2z^5 - 6z^2 - z + 1$, counted with multiplicity, in the closed annulus $A = \{z \in \mathbb{C} : 1 \leq |z| \leq 2\}$.

---

### Step 1: Count Zeros in the Open Disk $|z| < 2$

<1>1. **$f(z)$ has 5 zeros in $|z| < 2$.**
  <2>1. Decompose $f(z) = F_1(z) + G_1(z)$ on the circle $|z| = 2$, where $F_1(z) = 2z^5$ and $G_1(z) = -6z^2 - z + 1$.
    *Proof:* Algebraic splitting of terms.
  <2>2. On $|z| = 2$, $|F_1(z)| = 2 |z|^5 = 2 \cdot 2^5 = 64$.
    *Proof:* Direct evaluation on $|z|=2$.
  <2>3. On $|z| = 2$, by the triangle inequality:
  $$|G_1(z)| = |-6z^2 - z + 1| \leq 6|z|^2 + |z| + 1 = 6(4) + 2 + 1 = 27.$$
    *Proof:* Triangle inequality $|a+b+c| \leq |a|+|b|+|c|$.
  <2>4. Since $|G_1(z)| \leq 27 < 64 = |F_1(z)|$ on $|z| = 2$, the strict inequality $|G_1(z)| < |F_1(z)|$ holds everywhere on the circle $|z| = 2$.
    *Proof:* $27 < 64$.
  <2>5. By Rouché's Theorem, $f(z) = F_1(z) + G_1(z)$ and $F_1(z) = 2z^5$ have the same number of zeros inside $|z| < 2$.
    *Proof:* Hypotheses of Rouché's Theorem are satisfied on the simple closed curve $|z|=2$.
  <2>6. The polynomial $F_1(z) = 2z^5$ has a zero of multiplicity 5 at $z = 0 \in D(0, 2)$, and no other zeros.
    *Proof:* $2z^5 = 0 \iff z = 0$.
  <2>7. Thus, $f(z)$ has exactly 5 zeros in $|z| < 2$. Moreover, since $|f(z)| \geq |F_1(z)| - |G_1(z)| \geq 64 - 27 = 37 > 0$ on $|z|=2$, $f(z)$ has no zeros on the circle $|z|=2$.
    *Proof:* Reverse triangle inequality.
  <2>8. Q.E.D.

---

### Step 2: Count Zeros in the Open Disk $|z| < 1$

<1>2. **$f(z)$ has 2 zeros in $|z| < 1$.**
  <2>1. Decompose $f(z) = F_2(z) + G_2(z)$ on the circle $|z| = 1$, where $F_2(z) = -6z^2$ and $G_2(z) = 2z^5 - z + 1$.
    *Proof:* Algebraic splitting of terms.
  <2>2. On $|z| = 1$, $|F_2(z)| = 6 |z|^2 = 6$.
    *Proof:* Direct evaluation on $|z|=1$.
  <2>3. On $|z| = 1$, by the triangle inequality:
  $$|G_2(z)| = |2z^5 - z + 1| \leq 2|z|^5 + |z| + 1 = 2(1) + 1 + 1 = 4.$$
    *Proof:* Triangle inequality.
  <2>4. Since $|G_2(z)| \leq 4 < 6 = |F_2(z)|$ on $|z| = 1$, the strict inequality $|G_2(z)| < |F_2(z)|$ holds everywhere on the circle $|z| = 1$.
    *Proof:* $4 < 6$.
  <2>5. By Rouché's Theorem, $f(z) = F_2(z) + G_2(z)$ and $F_2(z) = -6z^2$ have the same number of zeros inside $|z| < 1$.
    *Proof:* Hypotheses of Rouché's Theorem are satisfied on the simple closed curve $|z|=1$.
  <2>6. The polynomial $F_2(z) = -6z^2$ has a zero of multiplicity 2 at $z = 0 \in D(0, 1)$, and no other zeros.
    *Proof:* $-6z^2 = 0 \iff z = 0$.
  <2>7. Thus, $f(z)$ has exactly 2 zeros in $|z| < 1$. Furthermore, on $|z|=1$, $|f(z)| \geq |F_2(z)| - |G_2(z)| \geq 6 - 4 = 2 > 0$, so $f(z)$ has no zeros on the boundary circle $|z|=1$.
    *Proof:* Reverse triangle inequality.
  <2>8. Q.E.D.

---

### Step 3: Count Zeros in the Annulus $1 \leq |z| \leq 2$

<1>3. **$f(z)$ has exactly $5 - 2 = 3$ zeros in the annulus $1 \leq |z| \leq 2$.**
  <2>1. The closed disk $\overline{D}(0, 2) = \{|z| \leq 2\}$ is the disjoint union of the open disk $D(0, 1) = \{|z| < 1\}$, the closed annulus $A = \{1 \leq |z| \leq 2\}$, and the boundary circles $|z|=1, |z|=2$.
    *Proof:* Partition of the closed disk.
  <2>2. By <1>1.<2>7 and <1>2.<2>7, $f$ has no zeros on $|z|=1$ or on $|z|=2$.
    *Proof:* Direct consequence of the non-vanishing bounds $|f(z)| \geq 2 > 0$ on $|z|=1$ and $|f(z)| \geq 37 > 0$ on $|z|=2$.
  <2>3. Therefore, all zeros of $f$ in $|z| \leq 2$ lie either in $|z| < 1$ or in the interior of the annulus $1 < |z| < 2$.
    *Proof:* Disjoint union of zero sets.
  <2>4. Number of zeros in $A$ = (Number of zeros in $|z| < 2$) - (Number of zeros in $|z| < 1$) = $5 - 2 = 3$.
    *Proof:* Subtraction of counts from <1>1 and <1>2.
  <2>5. Q.E.D.
:::
