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

::: problem
Prove that any finite division ring is a field (that is, prove commutativity).
Give an example of a (necessarily infinite) division ring which is NOT a field.
:::

::: solution
**Goal:** Prove Wedderburn's Little Theorem (that every finite division ring is a field) and provide an example of an infinite non-commutative division ring.

<1>1. Setup of the finite division ring and its center:
    *Proof:*
    <2>1. Let $D$ be a finite division ring. The center of $D$ is
    $$Z = Z(D) = \{z \in D : zx = xz \text{ for all } x \in D\}.$$
    <2>2. $Z$ is a finite field of order $q = p^r$ for some prime $p$ and integer $r \ge 1$.
    <2>3. $D$ is a finite-dimensional vector space over its subfield $Z$. Let $n = \dim_Z D \ge 1$.
    <2>4. The cardinality of $D$ is $|D| = q^n$. The goal is to show $n = 1$.

<1>2. The class equation for the multiplicative group $D^\times$:
    *Proof:*
    <2>1. The multiplicative group $D^\times = D \setminus \{0\}$ has order $q^n - 1$, and its center is $Z^\times = Z \setminus \{0\}$ of order $q - 1$.
    <2>2. For any $x \in D^\times$, the centralizer of $x$ in $D$ is $C_D(x) = \{y \in D : yx = xy\}$.
    <2>3. Since $C_D(x)$ is a division subring containing $Z$, it is a $Z$-vector subspace of dimension $d = d(x)$, so $|C_D(x)| = q^d$.
    <2>4. Since $D$ is a vector space over $C_D(x)$, $d$ must divide $n$ ($d \mid n$).
    <2>5. The conjugacy class of $x \in D^\times$ in $D^\times$ has size $[D^\times : C_D(x)^\times] = \frac{q^n - 1}{q^d - 1}$.
    <2>6. Partitioning $D^\times$ into conjugacy classes gives the class equation:
    $$|D^\times| = |Z^\times| + \sum_{i=1}^m \frac{|D^\times|}{|C_D(x_i)^\times|},$$
    which translates to
    $$q^n - 1 = (q - 1) + \sum_{i=1}^m \frac{q^n - 1}{q^{d_i} - 1},$$
    where the sum runs over representatives $x_1, \dots, x_m$ of the distinct non-central conjugacy classes, so each $d_i \mid n$ with $d_i < n$.

<1>3. Divisibility by the $n$-th cyclotomic polynomial $\Phi_n(q)$:
    *Proof:*
    <2>1. In $\mathbb{Z}[x]$, the polynomial $x^n - 1$ factors as $x^n - 1 = \prod_{d \mid n} \Phi_d(x)$, where $\Phi_d(x)$ is the $d$-th cyclotomic polynomial.
    <2>2. For any proper divisor $d_i$ of $n$ ($d_i \mid n, d_i < n$), $x^{d_i} - 1 = \prod_{c \mid d_i} \Phi_c(x)$.
    <2>3. Because $d_i < n$, the factor $\Phi_n(x)$ does not appear in $x^{d_i} - 1$. Therefore $\Phi_n(x)$ divides $\frac{x^n - 1}{x^{d_i} - 1}$ in $\mathbb{Z}[x]$.
    <2>4. Evaluating at the integer $q \ge 2$, $\Phi_n(q)$ divides $\frac{q^n - 1}{q^{d_i} - 1}$ for each $i \in \{1, \dots, m\}$.
    <2>5. Furthermore, $\Phi_n(q)$ divides $q^n - 1$.
    <2>6. Rewriting the class equation as
    $$q - 1 = (q^n - 1) - \sum_{i=1}^m \frac{q^n - 1}{q^{d_i} - 1},$$
    it follows that $\Phi_n(q)$ divides $q - 1$ in $\mathbb{Z}$.
    <2>7. Since $q - 1 > 0$, this implies the inequality $|\Phi_n(q)| \le q - 1$.

<1>4. Geometric bound on $|\Phi_n(q)|$ and contradiction:
    *Proof:*
    <2>1. By definition, $\Phi_n(q) = \prod_{\substack{1 \le k \le n \\ \gcd(k, n) = 1}} (q - \zeta_n^k)$, where $\zeta_n = e^{2\pi i / n}$.
    <2>2. Suppose for contradiction that $n > 1$. Then for each primitive root $\zeta_n^k \neq 1$, the complex number $\zeta_n^k$ lies on the unit circle with $\operatorname{Re}(\zeta_n^k) < 1$.
    <2>3. For real $q \ge 2$, the Euclidean distance from $q$ to $\zeta_n^k$ strictly exceeds $q - 1$:
    $$|q - \zeta_n^k| = \sqrt{(q - \cos(2\pi k/n))^2 + \sin^2(2\pi k/n)} = \sqrt{q^2 - 2q\cos(2\pi k/n) + 1} > \sqrt{q^2 - 2q + 1} = q - 1.$$
    <2>4. Taking the product over all $\varphi(n) \ge 1$ primitive roots gives
    $$|\Phi_n(q)| = \prod_{\gcd(k,n)=1} |q - \zeta_n^k| > \prod_{\gcd(k,n)=1} (q - 1) \ge q - 1.$$
    <2>5. This strictly contradicts step 3.7 ($|\Phi_n(q)| \le q - 1$).
    <2>6. Thus $n = 1$, which means $D = Z(D)$, so $D$ is commutative. Hence $D$ is a field.

<1>5. Example of an infinite non-commutative division ring:
    *Proof:*
    <2>1. Consider the real quaternions $\mathbb{H} = \{a + bi + cj + dk : a, b, c, d \in \mathbb{R}\}$, with basis elements satisfying $i^2 = j^2 = k^2 = ijk = -1$.
    <2>2. For any non-zero element $z = a + bi + cj + dk \neq 0$, its conjugate is $\bar{z} = a - bi - cj - dk$, and $z \bar{z} = \bar{z} z = a^2 + b^2 + c^2 + d^2 > 0$.
    <2>3. The multiplicative inverse is $z^{-1} = \frac{\bar{z}}{a^2 + b^2 + c^2 + d^2} \in \mathbb{H}$, so every non-zero element is invertible, making $\mathbb{H}$ a division ring.
    <2>4. Since $ij = k \neq -k = ji$, multiplication in $\mathbb{H}$ is non-commutative, so $\mathbb{H}$ is not a field.
:::
