---
schema: qual/card@1
id: E-AMD-73ABFI2F
kind: exercise
title: $x^{p^d}-x$ divides $x^{p^n}-x$ iff $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - finite-fields
  - polynomials
  - factorization
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that $x^{p^d} - x \divides x^{p^n} - x \iff d \divides n$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $p$ be a prime and $d, n \ge 1$ be positive integers.
In the polynomial ring $\mathbb{F}_p[x]$, prove that $(x^{p^d} - x) \mid (x^{p^n} - x)$ if and only if $d \mid n$.

<1>1. Elementary algebraic divisibility lemmas: <2>1. For any integers $a \ge 2$ and $k, m \ge 1$, $(a^k - 1) \mid (a^m - 1)$ if and only if $k \mid m$.
<3>1. Direction $\impliedby$: If $k \mid m$, write $m = k q$.
Then $a^m - 1 = (a^k)^q - 1 = (a^k - 1)((a^k)^{q-1} + \dots + a^k + 1)$, so $(a^k - 1) \mid (a^m - 1)$.
Proof: Polynomial identity $y^q - 1 = (y-1)(y^{q-1} + \dots + 1)$ with $y = a^k$.
<3>2. Direction $\implies$: If $(a^k - 1) \mid (a^m - 1)$, write $m = k q + r$ with $0 \le r < k$.
Then $a^m - 1 = a^r (a^{kq} - 1) + (a^r - 1)$.
Since $(a^k - 1) \mid (a^{kq} - 1)$, we have $(a^k - 1) \mid (a^r - 1)$.
If $r > 0$, then $0 < a^r - 1 < a^k - 1$, which is impossible for divisibility of positive integers.
Thus $r = 0$, meaning $k \mid m$.
Proof: Euclidean division and standard divisibility properties.
<3>3. Q.E.D. Proof: Follows from <3>1 and <3>2. <2>2. For any non-constant polynomial $g(x) \in \mathbb{F}_p[x]$ and $A, B \ge 1$, $(x^A - 1) \mid (x^B - 1)$ in $\mathbb{F}_p[x]$ if and only if $A \mid B$.
Proof: Identical Euclidean division argument in polynomial rings: $x^B - 1 = x^r(x^{Aq} - 1) + (x^r - 1)$ where $B = Aq + r$ with $0 \le r < A$.
Divisibility requires the remainder $x^r - 1 = 0$, so $r = 0$ and $A \mid B$.

<1>2. Equivalence between $(x^{p^d} - x) \mid (x^{p^n} - x)$ and $(x^{p^d-1} - 1) \mid (x^{p^n-1} - 1)$: <2>1. Factoring out $x$, we have $x^{p^d} - x = x(x^{p^d - 1} - 1)$ and $x^{p^n} - x = x(x^{p^n - 1} - 1)$.
Proof: Direct factorization in $\mathbb{F}_p[x]$.
<2>2. Since $\gcd(x, x^{p^d - 1} - 1) = 1$ and $\gcd(x, x^{p^n - 1} - 1) = 1$, $(x^{p^d} - x) \mid (x^{p^n} - x)$ if and only if $(x^{p^d - 1} - 1) \mid (x^{p^n - 1} - 1)$.
Proof: In any UFD, $a b \mid a c$ is equivalent to $b \mid c$ when $a \neq 0$.
Here $a = x \neq 0$.

<1>3. Direction 1 ($\implies$): If $(x^{p^d} - x) \mid (x^{p^n} - x)$, then $d \mid n$.
<2>1. Assume $(x^{p^d} - x) \mid (x^{p^n} - x)$.
Proof: Hypothesis.
<2>2. By <1>2.<2>2, $(x^{p^d - 1} - 1) \mid (x^{p^n - 1} - 1)$.
Proof: Canceling $x$.
<2>3. By <1>1.<2>2 with $A = p^d - 1$ and $B = p^n - 1$, $(p^d - 1) \mid (p^n - 1)$.
Proof: Divisibility of $x^A - 1 \mid x^B - 1$ implies $A \mid B$.
<2>4. By <1>1.<2>1 with $a = p \ge 2$, $(p^d - 1) \mid (p^n - 1)$ implies $d \mid n$.
Proof: Divisibility $(a^d - 1) \mid (a^n - 1)$ implies $d \mid n$.
<2>5. Q.E.D. Proof: Follows from <2>1 through <2>4.

<1>4. Direction 2 ($\impliedby$): If $d \mid n$, then $(x^{p^d} - x) \mid (x^{p^n} - x)$.
<2>1. Assume $d \mid n$.
Proof: Hypothesis.
<2>2. By <1>1.<2>1, $(p^d - 1) \mid (p^n - 1)$.
Proof: Since $d \mid n$ and $p \ge 2$, $(p^d - 1)$ divides $(p^n - 1)$.
<2>3. By <1>1.<2>2 with $A = p^d - 1$ and $B = p^n - 1$, $(x^{p^d - 1} - 1) \mid (x^{p^n - 1} - 1)$ in $\mathbb{F}_p[x]$.
Proof: Since $A \mid B$, $(x^A - 1) \mid (x^B - 1)$.
<2>4. Multiplying both sides by $x$ gives $(x^{p^d} - x) \mid (x^{p^n} - x)$.
Proof: If $u(x) \mid v(x)$, then $x u(x) \mid x v(x)$.
<2>5. Q.E.D. Proof: Follows from <2>1 through <2>4.

<1>5. Conclusion: $(x^{p^d} - x) \mid (x^{p^n} - x)$ in $\mathbb{F}_p[x]$ if and only if $d \mid n$.
Proof: By <1>3 and <1>4.
:::
