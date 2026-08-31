---
schema: qual/card@1
id: E-SS7.EX-2
kind: exercise
title: "The following links the multiplication of Dirichlet series with the divisibility"
classification:
  areas:
  - complex-analysis
  topics: ['Zeta Function', 'Prime Number Theorem', 'Dirichlet Series']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: exercise
2. The following links the multiplication of Dirichlet series with the divisibility properties of their coeficients.

(a) Show that if $\{ a _ { m } \}$ and $\{ b _ { k } \}$ are two bounded sequences of complex numbers, then

$$
\left(\sum_ {m = 1} ^ {\infty} \frac {a _ {m}}{m ^ {s}}\right) \left(\sum_ {k = 1} ^ {\infty} \frac {b _ {k}}{k ^ {s}}\right) = \sum_ {n = 1} ^ {\infty} \frac {c _ {n}}{n ^ {s}} \quad \text { where } c _ {n} = \sum_ {m k = n} a _ {m} b _ {k}.
$$

The above series converge absolutely when $\operatorname { R e } ( s ) > 1$

(b) Prove as a consequence that one has

$$
(\zeta (s)) ^ {2} = \sum_ {n = 1} ^ {\infty} \frac {d (n)}{n ^ {s}} \quad \text { and } \quad \zeta (s) \zeta (s - a) = \sum_ {n = 1} ^ {\infty} \frac {\sigma_ {a} (n)}{n ^ {s}}
$$

for $\operatorname { R e } ( s ) > 1$ and $\operatorname { R e } ( s - a ) > 1$ , respectively.
Here $d ( n )$ equals the number of divisors of $n _ { \mathrm { : } }$ , and $\sigma _ { a } ( n )$ is the sum of the $a ^ { \mathrm { t h } }$ powers of divisors of $n$ . In particular, one has $\sigma _ { 0 } ( n ) = d ( n )$
:::

::: {.solution}
**Part (a).**

<1>1. For $\operatorname{Re}(s) > 1$, both series $\sum_m \frac{a_m}{m^s}$ and $\sum_k \frac{b_k}{k^s}$ converge absolutely.
::: {.proof}
$|a_m|, |b_k|$ are bounded, and $\sum \frac{1}{n^{\operatorname{Re} s}}$ converges for $\operatorname{Re} s > 1$.
:::

<1>2. Hence their product is the Cauchy product:
$$\left(\sum_m \frac{a_m}{m^s}\right)\left(\sum_k \frac{b_k}{k^s}\right) = \sum_{m,k} \frac{a_m b_k}{(mk)^s} = \sum_{n=1}^{\infty} \frac{c_n}{n^s},$$
where $c_n = \sum_{mk = n} a_m b_k$.
::: {.proof}
absolute convergence justifies rearranging the double sum by grouping terms with $mk = n$.
:::

**Part (b).**

<1>1. $\zeta(s)^2 = \left(\sum_m \frac{1}{m^s}\right)\left(\sum_k \frac{1}{k^s}\right) = \sum_n \frac{d(n)}{n^s}$.
::: {.proof}
by part (a) with $a_m = b_k = 1$, we get $c_n = \sum_{mk = n} 1 = d(n)$ (the number of divisors of $n$).
:::

<1>2. $\zeta(s)\zeta(s-a) = \left(\sum_m \frac{1}{m^s}\right)\left(\sum_k \frac{k^a}{k^s}\right) = \sum_n \frac{\sigma_a(n)}{n^s}$.
::: {.proof}
by part (a) with $a_m = 1$ and $b_k = k^a$, we get $c_n = \sum_{mk = n} k^a = \sigma_a(n)$ (the sum of the $a$-th powers of the divisors of $n$).
:::

<1>3. Q.E.D.
::: {.proof}
<1>2 (a) and <1>1–<1>2 (b).
:::
:::
