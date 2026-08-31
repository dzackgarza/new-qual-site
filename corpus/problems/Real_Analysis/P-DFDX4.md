---
schema: qual/card@1
id: P-DFDX4
kind: problem
title: Power series $\sum a_n x^n$ and $\sum b_n x^n$ with radii of convergence $R_1$
  and $R_2$
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
Let the power series series $\sum_{n=0}^\infty a_nx^n$ and $\sum_{n=0}^\infty b_nx^n$ have radii of convergence $R_1$ and $R_2$, respectively.
:::
::: {.solution}
**Honesty note:** the card as written is a fragment — it states the setup (two power series with radii $R_1, R_2$) without a question.
The standard companion questions are covered by the sibling cards P-E4WZN (radius of $\sum (a_n+b_n)x^n$) and P-FYGQ6 (radius of $\sum a_nb_nx^n$). This solution records the defining facts used there.

<1>1. Cauchy–Hadamard formula: the radius of convergence of $\sum a_n x^n$ is $R = 1/\limsup_{n \to \infty} |a_n|^{1/n}$ (with $1/0 = \infty$, $1/\infty = 0$).
::: {.proof}
the root test: $\limsup |a_n x^n|^{1/n} = |x| \limsup |a_n|^{1/n}$; the series converges absolutely when this is $< 1$, i.e. $|x| < R$, and diverges when $|x| > R$.
:::

<1>2. The series $\sum a_n x^n$ converges absolutely for $|x| < R_1$ and diverges for $|x| > R_1$; likewise for $\sum b_n x^n$ with $R_2$.
::: {.proof}
<1>1 applied to each series.
:::

<1>3. Standard consequence: if $R_1 \neq R_2$, the radius of $\sum (a_n + b_n) x^n$ is $\min\{R_1, R_2\}$; in general it is $\ge \min\{R_1, R_2\}$ (see P-E4WZN).

<1>4. Standard consequence: the radius of $\sum a_n b_n x^n$ satisfies $R \ge R_1 R_2$ (see P-FYGQ6).

<1>5. Q.E.D.
::: {.proof}
<1>1 is the definition one applies in <1>3 and <1>4.
:::
:::
