---
schema: qual/card@1
id: P-FYGQ6
kind: problem
title: Radius of $\sum a_n b_n x^n$ at least the product of the radii of $\sum a_n
  x^n$ and $\sum b_n x^n$, strictly in an example
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Prove that the radius of convergence, $R$, of $\sum_{n=0}^\infty a_nb_nx^n$ satisfies $R \geq R_1R_2$.
Show by means of example that this inequality can be strict.
:::
::: {.solution}
<1>1. Claim: for $|x| < R_1 R_2$, the series $\sum a_n b_n x^n$ converges absolutely.
<2>1. Since $|x| < R_1 R_2$, choose $\lambda$ with $|x| < \lambda < R_1 R_2$, and set $u = R_1\sqrt{\lambda/(R_1 R_2)}$, $v = R_2\sqrt{\lambda/(R_1 R_2)}$; then $u < R_1$, $v < R_2$, and $uv = \lambda > |x|$.
::: {.proof}
$\sqrt{\lambda/(R_1R_2)} < 1$ by choice of $\lambda$; the product is $\lambda$.
:::
<2>2. $\sum |a_n| u^n < \infty$ and $\sum |b_n| v^n < \infty$.
::: {.proof}
$u < R_1$ and $v < R_2$, and a power series converges absolutely strictly inside its radius of convergence.
:::
<2>3. Hence $|a_n|u^n \to 0$ and $|b_n|v^n \to 0$ (terms of convergent series).
::: {.proof}
a necessary condition for convergence.
:::
<2>4. Write $|a_n b_n x^n| = (|a_n|u^n)(|b_n|v^n)\left|\frac{x}{uv}\right|^n$.
For large $n$, $|a_n|u^n \le 1$ and $|b_n|v^n \le 1$ (they tend to $0$), so $|a_n b_n x^n| \le \left|\frac{x}{\lambda}\right|^n$ for large $n$, and $\sum \left|\frac{x}{\lambda}\right|^n < \infty$ since $|x| < \lambda$.
::: {.proof}
<2>3 and the geometric series test.
:::

<1>2. $R \ge R_1 R_2$.
::: {.proof}
<1>1 shows absolute convergence for every $|x| < R_1 R_2$, so the radius of $\sum a_nb_nx^n$ is at least $R_1R_2$.
:::

<1>3. The inequality can be strict.
<2>1. Take $a_n = 1$ for $n$ even and $a_n = 0$ for $n$ odd; take $b_n = 0$ for $n$ even and $b_n = 1$ for $n$ odd.
::: {.proof}
explicit sequences.
:::
<2>2. $R_1 = 1$ and $R_2 = 1$.
::: {.proof}
$|a_n|^{1/n} = 1$ along even indices (limsup $= 1$) and $0$ along odd; so $\limsup |a_n|^{1/n} = 1$, giving $R_1 = 1$ by Cauchy–Hadamard; likewise $R_2 = 1$ (the ones now sit on the odd indices).
:::
<2>3. $a_n b_n = 0$ for every $n$, so the product series is identically $0$ and has radius $R = \infty$.
::: {.proof}
for each $n$, exactly one of $a_n, b_n$ is zero (they are supported on complementary index sets).
:::
<2>4. $R = \infty > 1 = R_1 R_2$.
::: {.proof}
<2>2 and <2>3.
:::

<1>4. Q.E.D.
::: {.proof}
<1>2 gives $R \ge R_1R_2$; <1>3 exhibits strict inequality.
:::
:::
