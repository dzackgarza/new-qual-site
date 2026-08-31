---
schema: qual/card@1
id: P-VGN3T
kind: problem
title: '$\ZZ[\sqrt{-5}]$ is not a PID: units $\pm 1$, and $3$ irreducible but not
  prime'
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Integral Domains
  - Principal Ideal Domains
relations: []
review: draft
---

::: problem
For a commutative ring $R$, let $U(R) = R^\times$ denote the group of units in $R$. Recall that in an integral domain $R$, a non-zero, non-unit element $r \in R$ is called *irreducible* if whenever $r = x y$ with $x, y \in R$, then either $x \in U(R)$ or $y \in U(R)$. A non-zero, non-unit element $r \in R$ is called *prime* in $R$ if $r \mid a b \implies r \mid a \text{ or } r \mid b$.

Consider the ring $R = \mathbb{Z}[\sqrt{-5}] = \{a + b \sqrt{-5} \mid a, b \in \mathbb{Z}\} \subset \mathbb{C}$.

(a) Prove that $R$ is an integral domain.

(b) Show that $U(R) = \{\pm 1\}$.

(c) Show that $3$, $2 + \sqrt{-5}$, and $2 - \sqrt{-5}$ are irreducible in $R$.

(d) Show that $3$ is not prime in $R$.

(e) Conclude that $R$ is not a principal ideal domain (PID).
:::

::: solution
**Goal:** Prove properties of the ring $\mathbb{Z}[\sqrt{-5}]$ using the field norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$, deduce that $3$ is irreducible but not prime, and conclude $R$ is not a PID.

<1>1. Part (a): $R$ is an integral domain.
::: {.proof}
    <2>1. $R = \mathbb{Z}[\sqrt{-5}]$ is a subring of the field of complex numbers $\mathbb{C}$:
        - $1 = 1 + 0\sqrt{-5} \in R$.
        - For $\alpha = a + b\sqrt{-5}$ and $\beta = c + d\sqrt{-5} \in R$:
          $$\alpha - \beta = (a - c) + (b - d)\sqrt{-5} \in R,$$
          $$\alpha \beta = (a c - 5 b d) + (a d + b c)\sqrt{-5} \in R.$$
    <2>2. Since $\mathbb{C}$ is a field, $\mathbb{C}$ has no non-zero zero-divisors.
    <2>3. Any subring of a field is an integral domain. Thus $R$ is an integral domain.

:::

<1>2. Part (b): $U(R) = \{\pm 1\}$.
::: {.proof}
    <2>1. Define the algebraic norm $N: R \to \mathbb{Z}_{\ge 0}$ by
    $$N(a + b\sqrt{-5}) = |a + b\sqrt{-5}|^2 = a^2 + 5b^2.$$
    <2>2. The norm is multiplicative: $N(\alpha \beta) = N(\alpha) N(\beta)$ for all $\alpha, \beta \in R$.
    <2>3. If $u \in U(R)$, then there exists $v \in R$ such that $u v = 1$.
    <2>4. Taking norms gives $N(u) N(v) = N(1) = 1$ in $\mathbb{Z}_{\ge 0}$, which forces $N(u) = 1$.
    <2>5. Write $u = a + b\sqrt{-5}$ with $a, b \in \mathbb{Z}$. Then $a^2 + 5b^2 = 1$.
    <2>6. Since $a, b \in \mathbb{Z}$, if $b \ne 0$, then $a^2 + 5b^2 \ge 5 > 1$. Thus $b = 0$, which leaves $a^2 = 1 \implies a = \pm 1$.
    <2>7. Conversely, $(\pm 1)(\pm 1) = 1$, so $\pm 1 \in U(R)$.
    <2>8. Therefore $U(R) = \{\pm 1\}$.

:::

<1>3. Part (c): $3$, $2 + \sqrt{-5}$, and $2 - \sqrt{-5}$ are irreducible in $R$.
::: {.proof}
    <2>1. Compute the norms:
        $$N(3) = 3^2 + 5(0)^2 = 9,$$
        $$N(2 + \sqrt{-5}) = 2^2 + 5(1)^2 = 4 + 5 = 9,$$
        $$N(2 - \sqrt{-5}) = 2^2 + 5(-1)^2 = 4 + 5 = 9.$$
    <2>2. Suppose $\alpha \in \{3, 2 + \sqrt{-5}, 2 - \sqrt{-5}\}$ factors as $\alpha = x y$ for some $x, y \in R$.
    <2>3. Taking norms gives $N(x) N(y) = N(\alpha) = 9$.
    <2>4. In $\mathbb{Z}_{\ge 0}$, the divisors of 9 are 1, 3, and 9.
    <2>5. If $N(x) = 3$, write $x = a + b\sqrt{-5}$ with $a, b \in \mathbb{Z}$. Then $a^2 + 5b^2 = 3$.
        - If $|b| \ge 1$, then $a^2 + 5b^2 \ge 5 > 3$.
        - If $b = 0$, then $a^2 = 3$, which has no integer solutions since 3 is not a square in $\mathbb{Z}$.
        - Thus no element in $R$ has norm 3.
    <2>6. Therefore, the only possibilities for $(N(x), N(y))$ are $(1, 9)$ or $(9, 1)$.
    <2>7. By Part (b), an element of norm 1 is a unit ($\pm 1$). Thus either $x \in U(R)$ or $y \in U(R)$.
    <2>8. Since $N(\alpha) = 9 > 1$, $\alpha$ is not a unit. Hence $3$, $2 + \sqrt{-5}$, and $2 - \sqrt{-5}$ are irreducible in $R$.

:::

<1>4. Part (d): $3$ is not prime in $R$.
::: {.proof}
    <2>1. Consider the factorization:
    $$(2 + \sqrt{-5})(2 - \sqrt{-5}) = 2^2 - (-5) = 4 + 5 = 9 = 3 \cdot 3.$$
    <2>2. Thus $3 \mid (2 + \sqrt{-5})(2 - \sqrt{-5})$ in $R$.
    <2>3. Suppose for contradiction that $3 \mid (2 + \sqrt{-5})$.
        - Then $2 + \sqrt{-5} = 3(a + b\sqrt{-5}) = 3a + 3b\sqrt{-5}$ for some $a, b \in \mathbb{Z}$.
        - Equating real parts gives $3a = 2$, so $a = 2/3 \notin \mathbb{Z}$, a contradiction.
    <2>4. Similarly, suppose $3 \mid (2 - \sqrt{-5})$.
        - Then $2 - \sqrt{-5} = 3(c + d\sqrt{-5})$ implies $3c = 2$, again impossible in $\mathbb{Z}$.
    <2>5. Thus $3 \nmid (2 + \sqrt{-5})$ and $3 \nmid (2 - \sqrt{-5})$.
    <2>6. Therefore $3$ is not a prime element in $R$.

:::

<1>5. Part (e): $R$ is not a PID.
::: {.proof}
    <2>1. In any principal ideal domain $D$, every irreducible element is prime:
        - Let $p \in D$ be irreducible. If $p \mid a b$ and $p \nmid a$, then $\gcd(p, a) = 1$.
        - In a PID, Bézout's identity gives $x p + y a = 1$ for some $x, y \in D$.
        - Multiplying by $b$ gives $x p b + y a b = b$.
        - Since $p \mid (x p b)$ and $p \mid (y a b)$, $p \mid b$.
    <2>2. In $R = \mathbb{Z}[\sqrt{-5}]$, the element $3$ is irreducible (by Part (c)) but is not prime (by Part (d)).
    <2>3. By contraposition, $R$ cannot be a principal ideal domain.

:::

<1>6. Conclusion:
::: {.proof}
    $R = \mathbb{Z}[\sqrt{-5}]$ is an integral domain with units $\{\pm 1\}$, has $3$ as an irreducible non-prime element, and is not a PID.
:::
:::

