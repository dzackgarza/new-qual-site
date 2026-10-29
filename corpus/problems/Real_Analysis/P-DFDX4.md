---
schema: qual/card@1
id: P-DFDX4
kind: problem
title: Radii of convergence of $\sum (a_n+b_n)x^n$ and $\sum a_nb_nx^n$ in terms of
  those of $\sum a_n x^n$ and $\sum b_n x^n$
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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The statement held only the source's opening sentence; parts (a) and (b) are restored from the source, and the convention 0 times infinity equals 0 is fixed so that R_1 R_2 is defined when one radius is 0 and the other infinite.
---

::: {.problem}
Let the power series $\sum_{n=0}^\infty a_nx^n$ and $\sum_{n=0}^\infty b_nx^n$ have radii of convergence $R_1$ and $R_2$, respectively.

(a) If $R_1 \neq R_2$, prove that the radius of convergence, $R$, of the power series $\sum_{n=0}^\infty (a_n+b_n)x^n$ is $\min\{R_1, R_2\}$.
What can be said about $R$ when $R_1 = R_2$?

(b) Prove that the radius of convergence, $R$, of $\sum_{n=0}^\infty a_nb_nx^n$ satisfies $R \geq R_1R_2$, with $0 \cdot \infty = 0$.
Show by means of example that this inequality can be strict.
:::

::: {.solution}

::: pf

::: {.pf-step #a}

(a) If $R_1 \neq R_2$, then $R = \min\{R_1, R_2\}$; if $R_1 = R_2$, then $R \ge R_1$, and both $R = R_1$ and $R > R_1$ occur.

::: pf-proof

::: {.pf-step #a1}

$R \ge \min\{R_1, R_2\}$.

::: pf-proof

For $|x| < \min\{R_1, R_2\}$ both $\sum a_n x^n$ and $\sum b_n x^n$ converge absolutely, and $\abs{(a_n + b_n)x^n} \le \abs{a_nx^n} + \abs{b_nx^n}$.

:::

:::

::: {.pf-step #a2}

If $R_1 < R_2$, then $R \le R_1$.

::: pf-proof

Let $R_1 < |x| < R_2$. Then $\sum a_n x^n$ diverges and $\sum b_n x^n$ converges. If $\sum (a_n + b_n)x^n$ converged, then $\sum a_n x^n$ would converge as the difference of two convergent series. So $\sum (a_n + b_n)x^n$ diverges at points with $|x| > R_1$ arbitrarily close to $R_1$, and $R \le R_1$.

:::

:::

::: {.pf-step #a3}

If $R_1 = R_2$, then $R \ge R_1$, and both $R = R_1$ and $R > R_1$ occur.

::: pf-proof

The inequality is step [](#a1){.pf-ref}. With $b_n = a_n$, the coefficients $2a_n$ give $R = R_1$. With $b_n = -a_n$, the series is $0$ and $R = \infty$, which exceeds $R_1$ whenever $R_1 < \infty$.

:::

:::

::: pf-qed

If $R_1 \neq R_2$, steps [](#a1){.pf-ref} and [](#a2){.pf-ref}, with the roles of the series exchanged if $R_2 < R_1$, give $R = \min\{R_1, R_2\}$. Step [](#a3){.pf-ref} is the case $R_1 = R_2$.

:::

:::

:::

::: {.pf-step #b}

(b) $R \ge R_1R_2$, and the inequality can be strict.

::: pf-proof

::: {.pf-step #b1}

For $|x| < R_1 R_2$, $\sum a_n b_n x^n$ converges absolutely.

::: pf-proof

::: {.pf-step #b1-1}

There are $u < R_1$ and $v < R_2$ with $|x| < uv$.

::: pf-proof

The set $\theset{uv : 0 \le u < R_1,\ 0 \le v < R_2}$ is the interval $[0, R_1R_2)$, with $R_1R_2 = \infty$ if either radius is infinite and the other positive.

:::

:::

::: {.pf-step #b1-2}

$\abs{a_n}u^n \le 1$ and $\abs{b_n}v^n \le 1$ for all large $n$.

::: pf-proof

$\sum a_n u^n$ and $\sum b_n v^n$ converge, since $u < R_1$ and $v < R_2$, so their terms tend to $0$.

:::

:::

::: pf-qed

By step [](#b1-2){.pf-ref}, $\abs{a_n b_n x^n} = (\abs{a_n}u^n)(\abs{b_n}v^n)\abs{\frac{x}{uv}}^n \le \abs{\frac{x}{uv}}^n$ for large $n$, and $\sum_n \abs{x/(uv)}^n$ is a convergent geometric series by step [](#b1-1){.pf-ref}.

:::

:::

:::

::: {.pf-step #b2}

For $a_n = 1$ ($n$ even), $a_n = 0$ ($n$ odd), $b_n = 0$ ($n$ even), $b_n = 1$ ($n$ odd), $R_1 = R_2 = 1$ and $R = \infty$.

::: pf-proof

$\limsup \abs{a_n}^{1/n} = 1$ along the even indices and $\limsup\abs{b_n}^{1/n} = 1$ along the odd indices, so the Cauchy--Hadamard formula gives $R_1 = R_2 = 1$. Every $a_nb_n = 0$, so $\sum a_nb_nx^n$ is the zero series and $R = \infty > 1 = R_1R_2$.

:::

:::

::: pf-qed

By step [](#b1){.pf-ref}, the series converges at every $x$ with $|x| < R_1R_2$, so $R \ge R_1R_2$; step [](#b2){.pf-ref} gives coefficients with $R > R_1R_2$.

:::

:::

:::

::: pf-qed

Steps [](#a){.pf-ref} and [](#b){.pf-ref} answer parts (a) and (b).

:::

:::

:::
