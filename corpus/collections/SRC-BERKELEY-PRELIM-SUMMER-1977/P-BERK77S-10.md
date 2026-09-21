---
schema: qual/card@1
id: P-BERK77S-10
kind: problem
title: Convergence of a symmetric-difference Taylor remainder series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Taylor's theorem at zero through second order makes the constant and
    quadratic terms cancel in the symmetric difference. Boundedness of the
    continuous third derivative gives an O(n^-2) bound on the resulting
    summand, so comparison with the p-series proves absolute convergence.
---

::: {.problem}
Suppose $f$ is defined on $[-1,1]$ and $f'''$ is continuous. Show that
\[
\sum_{n=1}^\infty
\left(
n\left(f\left(\frac1n\right)-f\left(-\frac1n\right)\right)-2f'(0)
\right)
\]
converges.
:::

::: {.solution}
Let
$$
M=\max_{x\in[-1,1]}\abs{f'''(x)}.
$$
This number is finite because $f'''$ is continuous on the compact interval
$[-1,1]$.

<1>1. For every integer $n\geq1$, there are points
$$
\xi_n^+\in(0,1/n)
\qquad\text{and}\qquad
\xi_n^-\in(-1/n,0)
$$
such that
$$
f(1/n)
=
f(0)
+
\frac{f'(0)}n
+
\frac{f''(0)}{2n^2}
+
\frac{f'''(\xi_n^+)}{6n^3}
$$
and
$$
f(-1/n)
=
f(0)
-
\frac{f'(0)}n
+
\frac{f''(0)}{2n^2}
-
\frac{f'''(\xi_n^-)}{6n^3}.
$$

::: {.proof}
Apply Taylor's theorem with Lagrange remainder of order three at the center
$0$, once to $x=1/n$ and once to $x=-1/n$.
:::

<1>2. The $n$th summand of the given series equals
$$
\frac{
f'''(\xi_n^+)+f'''(\xi_n^-)
}{6n^2}.
$$

::: {.proof}
Subtract the two Taylor expansions in step <1>1. The constant and quadratic
terms cancel, giving
$$
f(1/n)-f(-1/n)
=
\frac{2f'(0)}n
+
\frac{
f'''(\xi_n^+)+f'''(\xi_n^-)
}{6n^3}.
$$
Multiplying by $n$ and subtracting $2f'(0)$ gives the displayed formula.
:::

<1>3. The absolute value of the $n$th summand is at most
$$
\frac{M}{3n^2}.
$$

::: {.proof}
By the definition of $M$,
$$
\abs{f'''(\xi_n^+)}
\leq M,
\qquad
\abs{f'''(\xi_n^-)}
\leq M.
$$
Therefore step <1>2 and the triangle inequality give
$$
\abs{
\frac{
f'''(\xi_n^+)+f'''(\xi_n^-)
}{6n^2}
}
\leq
\frac{2M}{6n^2}
=
\frac{M}{3n^2}.
$$
:::

<1>4. The given series converges absolutely.

::: {.proof}
By step <1>3, its terms are dominated in absolute value by the convergent
series
$$
\frac{M}{3}\sum_{n=1}^{\infty}\frac1{n^2}.
$$
The comparison test therefore gives absolute convergence.
:::

<1>5. Q.E.D.

::: {.proof}
Absolute convergence in step <1>4 implies the required convergence.
:::
:::
