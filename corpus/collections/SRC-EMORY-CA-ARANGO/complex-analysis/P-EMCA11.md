---
schema: qual/card@1
id: P-EMCA11
kind: problem
title: "Meromorphic function with limit infinity is rational"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $f$ be a meromorphic function in the plane such that $\lim_{|z| \to \infty} |f(z)| = \infty$.

(a) Show that $f$ has only finitely many poles.

(b) Show that $f$ is a rational function.
:::

::: {.solution}
**Part (a).**

<1>1. Since $|f(z)| \to \infty$ as $|z| \to \infty$, there is $R$ such that $|f(z)| > 1$ for all $|z| > R$.
Proof: definition of the limit.

<1>2. Hence $f$ has no poles in $|z| > R$.
Proof: a pole is a point where $|f(z)| \to \infty$ locally, but $f$ is bounded below by $1$ (in modulus) and finite on $|z| > R$; more precisely, $f$ is holomorphic on $|z| > R$ (no poles there, since $|f|$ is finite and $> 1$).

<1>3. The poles of $f$ all lie in the compact disk $|z| \le R$.
Proof: <1>2.

<1>4. A meromorphic function has isolated poles, so a compact set contains only finitely many of them.
Proof: the poles form a discrete set, and a discrete subset of a compact set is finite.

<1>5. Hence $f$ has only finitely many poles.
Proof: <1>3 and <1>4.

**Part (b).**

<1>1. Let $a_1, \ldots, a_k$ be the (finitely many) poles of $f$, with principal parts $P_1, \ldots, P_k$.
Proof: <1>5 of part (a).

<1>2. $g(z) = f(z) - \sum_{j=1}^k P_j(z)$ is entire.
Proof: subtracting the principal parts removes all the poles.

<1>3. $|g(z)| \to \infty$ as $|z| \to \infty$.
Proof: each $P_j(z) \to 0$ as $|z| \to \infty$ (principal parts are polynomials in $1/(z-a_j)$), and $|f(z)| \to \infty$.

<1>4. An entire function with $|g(z)| \to \infty$ as $|z| \to \infty$ is a polynomial.
Proof: $g$ has a pole (not an essential singularity) at $\infty$, so its Laurent expansion at $\infty$ has finitely many terms.

<1>5. Hence $f = g + \sum_j P_j$ is a sum of a polynomial and rational functions, so $f$ is rational.
Proof: <1>2 and <1>4.

<1>6. Q.E.D.
Proof: <1>5 (a) and <1>5 (b).
:::
