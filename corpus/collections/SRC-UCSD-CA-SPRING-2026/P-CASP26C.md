---
schema: qual/card@1
id: P-CASP26C
kind: problem
title: "The polynomial 1 + z + az^n has a root in |z| <= 2 for all a and n >= 2"
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomial Roots
  - Rouche Theorem
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Prove that, for any $a \in \mathbb{C}$ and any integer $n \geq 2$, the polynomial $1 + z + az^n$ has at least one root in the disk $\{|z| \leq 2\}$.

Hint: The constant term in a monic polynomial is the product of its zeros (up to sign).
:::

::: {.solution}
<1>1. Suppose for contradiction that all roots of $1 + z + az^n$ have modulus $> 2$.
Proof: assume the contrary.

<1>2. Write $1 + z + az^n = a\prod_{i=1}^n (z - r_i)$, where $r_1, \ldots, r_n$ are the roots.
Proof: factor the polynomial (assuming $a \neq 0$; if $a = 0$, the polynomial is $1 + z$ with root $-1$, which has modulus $1 \le 2$, done).

<1>3. The constant term is $1 = a(-1)^n \prod_i r_i$, so $\prod_i |r_i| = 1/|a|$.
Proof: the constant term is $a(-1)^n \prod_i r_i = 1$.

<1>4. If all $|r_i| > 2$, then $\prod_i |r_i| > 2^n$, so by <1>3, $1/|a| > 2^n$, i.e. $|a| < 2^{-n}$.
Proof: <1>3 and the assumption $|r_i| > 2$.

<1>5. On $|z| = 2$, $|az^n| = |a| \cdot 2^n < 1$, and $|1 + z| \ge |z| - 1 = 1$.
Proof: <1>4 and the reverse triangle inequality.

<1>6. Hence on $|z| = 2$, $|az^n| < 1 \le |1 + z|$, so by Rouché's theorem, $1 + z + az^n$ and $1 + z$ have the same number of zeros in $|z| < 2$.
Proof: Rouché's theorem.

<1>7. $1 + z$ has exactly one zero in $|z| < 2$ (at $z = -1$).
Proof: $1 + z = 0$ iff $z = -1$, which has modulus $1 < 2$.

<1>8. Hence $1 + z + az^n$ has a root in $|z| < 2$, contradicting the assumption that all roots have modulus $> 2$.
Proof: <1>6 and <1>7.

<1>9. Therefore $1 + z + az^n$ has at least one root in $|z| \le 2$.
Proof: <1>1–<1>8.

<1>10. Q.E.D.
Proof: <1>9.
:::
