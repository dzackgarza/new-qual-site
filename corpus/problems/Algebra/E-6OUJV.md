---
schema: qual/card@1
id: E-6OUJV
kind: problem
title: Irreducible polynomials in characteristic $p$ are $g(x^{p^k})$ for unique separable
  $g$
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
If $f\in k[x]^{\irr}$ with $\ch k = p$, then there is a unique separable $g\in k[x]^{\irr}$ such that $f(x) = g(x^{p^e})$ for some unique $e \ge 0$.
:::

::: solution
**Goal:** Prove that every irreducible polynomial $f(x) \in k[x]$ over a field $k$ of characteristic $p > 0$ can be written uniquely as $f(x) = g(x^{p^e})$ for a unique integer $e \ge 0$ and a unique irreducible separable polynomial $g(x) \in k[x]$.

<1>1. Separability criterion for irreducible polynomials: An irreducible polynomial $h(x) \in k[x]$ is inseparable if and only if $h'(x) = 0$, which occurs if and only if $h(x) = h_1(x^p)$ for some polynomial $h_1(x) \in k[x]$.
*Proof:* <2>1. An irreducible polynomial is separable if and only if $\gcd(h, h') = 1$, which is equivalent to $h'(x) \neq 0$ since $h$ is irreducible and $\deg(h') < \deg(h)$.
<2>2. Write $h(x) = \sum_{j=0}^m c_j x^j$.
Its formal derivative is $h'(x) = \sum_{j=1}^m j c_j x^{j-1}$.
<2>3. In characteristic $p$, $j c_j = 0$ for all $j \ge 1$ if and only if $c_j = 0$ whenever $p \nmid j$.
<2>4. Hence $h'(x) = 0$ if and only if all non-zero terms have powers that are multiples of $p$, i.e. $h(x) = \sum_{r=0}^{\lfloor m/p \rfloor} c_{pr} (x^p)^r = h_1(x^p)$.
<2>5. Furthermore, if $h$ is irreducible, then $h_1$ is irreducible (since a non-trivial factorization $h_1(y) = a(y)b(y)$ gives $h(x) = a(x^p)b(x^p)$).

<1>2. Existence of $e$ and separable irreducible $g$: *Proof:* <2>1. Consider the set $S = \{n \in \mathbb{N} \mid f(x) = h_n(x^{p^n}) \text{ for some } h_n \in k[x]\}$.
<2>2. $S$ is non-empty because $0 \in S$ (with $h_0 = f$). <2>3. For any $n \in S$, $\deg(f) = p^n \deg(h_n) \ge p^n$, so $S$ is bounded above by $\log_p(\deg f)$.
<2>4. Let $e = \max S$, and set $g(x) = h_e(x) \in k[x]$, so $f(x) = g(x^{p^e})$.
<2>5. The polynomial $g$ is irreducible because any factorization $g(y) = a(y)b(y)$ would yield a factorization $f(x) = a(x^{p^e})b(x^{p^e})$.
<2>6. If $g$ were inseparable, then by <1>1, $g(y) = g_1(y^p)$, so $f(x) = g_1((x^{p^e})^p) = g_1(x^{p^{e+1}})$, which would imply $e+1 \in S$, contradicting the maximality of $e$.
<2>7. Thus $g$ is separable and irreducible.

<1>3. Uniqueness of $e$ and $g$: *Proof:* <2>1. Suppose $f(x) = g_1(x^{p^{e_1}}) = g_2(x^{p^{e_2}})$ with $g_1, g_2 \in k[x]$ irreducible and separable.
<2>2. Without loss of generality, assume $e_1 \le e_2$.
<2>3. Substituting $y = x^{p^{e_1}}$, we obtain $g_1(y) = g_2(y^{p^{e_2 - e_1}})$.
<2>4. If $e_2 > e_1$, then $e_2 - e_1 \ge 1$, so $g_1(y) = \tilde{g}(y^p)$ where $\tilde{g}(y) = g_2(y^{p^{e_2 - e_1 - 1}})$.
<2>5. By <1>1, this implies $g_1'(y) = 0$, contradicting the separability of $g_1$.
<2>6. Therefore $e_2 = e_1$, which immediately forces $g_1(y) = g_2(y)$.

<1>4. Conclusion: The integer $e \ge 0$ and the separable irreducible polynomial $g \in k[x]$ are unique.
Q.E.D.
:::
