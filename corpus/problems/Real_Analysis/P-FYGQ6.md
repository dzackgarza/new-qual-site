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

::: {.problem}
Prove that the radius of convergence, $R$, of $\sum_{n=0}^\infty a_nb_nx^n$ satisfies $R \geq R_1R_2$.
Show by means of example that this inequality can be strict.
:::
::: {.solution}
Here $R_1$ and $R_2$ are the radii of convergence of $\sum a_n x^n$ and $\sum b_n x^n$.

<1>1. For $|x| < R_1 R_2$, $\sum a_n b_n x^n$ converges absolutely.

<2>1. There are $u < R_1$ and $v < R_2$ with $|x| < uv$.

::: {.proof}
The set $\theset{uv : 0 \le u < R_1,\ 0 \le v < R_2}$ is the interval $[0, R_1R_2)$, with $R_1R_2 = \infty$ if either radius is infinite and the other positive.
:::

<2>2. $|a_n|u^n \le 1$ and $|b_n|v^n \le 1$ for all large $n$.

::: {.proof}
$\sum a_n u^n$ and $\sum b_n v^n$ converge, since $u < R_1$ and $v < R_2$, so their terms tend to $0$.
:::

<2>3. Q.E.D.

::: {.proof}
By step <2>2, $|a_n b_n x^n| = (|a_n|u^n)(|b_n|v^n)\left|\frac{x}{uv}\right|^n \le \left|\frac{x}{uv}\right|^n$ for large $n$, and $\sum_n |x/(uv)|^n$ is a convergent geometric series by step <2>1.
:::

<1>2. $R \ge R_1 R_2$.

::: {.proof}
Step <1>1.
:::

<1>3. For $a_n = 1$ ($n$ even), $a_n = 0$ ($n$ odd), $b_n = 0$ ($n$ even), $b_n = 1$ ($n$ odd), $R_1 = R_2 = 1$ and $R = \infty$.

::: {.proof}
$\limsup |a_n|^{1/n} = 1$ along the even indices and $\limsup|b_n|^{1/n} = 1$ along the odd indices, so the Cauchy--Hadamard formula gives $R_1 = R_2 = 1$. Every $a_nb_n = 0$, so $\sum a_nb_nx^n$ is the zero series and $R = \infty > 1 = R_1R_2$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 is the inequality and step <1>3 shows that it can be strict.
:::
:::
