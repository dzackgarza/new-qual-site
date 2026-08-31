---
schema: qual/card@1
id: P-4RGCT
kind: problem
title: Fundamental Theorem of Algebra via Rouché's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomials
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra:

If
$$
P_n(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + a_nz^n\quad  (a_n \neq 0)
$$
is a polynomial of degree $n$, then it has $n$ zeros in $\mathbb{C}$.
:::

::: {.solution}
**Goal:** Apply Rouch\'e's theorem to prove the Fundamental Theorem of Algebra: a polynomial $P_n(z) = a_0 + a_1 z + \cdots + a_{n-1}z^{n-1} + a_n z^n$ with $a_n \ne 0$ has exactly $n$ zeros in $\CC$ counting multiplicity.

<1>1. Setup: compare $P_n$ with its leading term $a_n z^n$ on a large circle.
::: {.proof}
write $P_n(z) = a_n z^n + Q(z)$ with $Q(z) = a_0 + \cdots + a_{n-1}z^{n-1}$ a polynomial of degree $\le n-1$.
:::

<1>2. For sufficiently large $R$, $|Q(z)| < |a_n z^n|$ on $|z| = R$.
::: {.proof}
on $|z| = R$, $|a_n z^n| = |a_n|R^n$ and $|Q(z)| \le \sum_{k=0}^{n-1}|a_k|R^k \le C R^{n-1}$ for $R \ge 1$; choose $R$ with $C R^{n-1} < |a_n| R^n$, i.e. $R > C/|a_n|$.
:::

<1>3. $P_n$ has exactly $n$ zeros in $|z| < R$ counting multiplicity.
::: {.proof}
Rouch\'e's theorem on $|z| = R$ with $f = a_n z^n$ and $g = Q$: by <1>2, $|Q| < |a_n z^n|$, so $P_n = f + g$ has the same number of zeros in $|z| < R$ as $a_n z^n$, which has exactly $n$ (all at $0$, with multiplicity $n$).
:::

<1>4. $P_n$ has exactly $n$ zeros in $\CC$ counting multiplicity.
::: {.proof}
by <1>3, $P_n$ has $n$ zeros (counting multiplicity) in $|z| < R$; since $R$ can be chosen arbitrarily large and a degree-$n$ polynomial has at most $n$ zeros counting multiplicity, these are all of them.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1–<1>4 prove the Fundamental Theorem of Algebra via Rouch\'e's theorem.
:::
:::
