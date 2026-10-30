---
schema: qual/card@1
id: P-BKS16-5B
kind: problem
title: Hadamard product of power series holomorphic near the closed disk
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked the statement against Problem 5B in the vendored Berkeley Spring 2016 exam and independently reviewed the supplied solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the common radius greater than one, the coefficient decay at an interior radius, and absolute convergence of the Hadamard product on a larger disk.
---

::: {.problem}
Let
$$
f(z)=\sum f_n z^n\qquad\text{and}\qquad g(z)=\sum g_n z^n
$$
define holomorphic functions on a neighborhood of the closed unit disk $D=\{z:\abs{z}\le 1\}$.
Prove that
$$
h(z)=\sum f_n g_n z^n
$$
also defines a holomorphic function on a neighborhood of $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There exists a number $\rho>1$ such that both power series for $f$ and $g$ converge on the disk $\abs{z}<\rho$.


::: pf-proof

By hypothesis, both functions are holomorphic on an open neighborhood of the compact set
$$
D=\{z:\abs{z}\leq1\}.
$$
Hence there is some $R>1$ such that the closed disk $\abs{z}\leq R$ is still contained in that neighborhood. The power series centered at $0$ therefore have radii of convergence at least $R$. Choose any $\rho$ with
$$
1<\rho<R.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
f_n\rho^n\longrightarrow0,
\qquad
g_n\rho^n\longrightarrow0.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the series
$$
\sum_{n=0}^\infty f_n\rho^n
\qquad\text{and}\qquad
\sum_{n=0}^\infty g_n\rho^n
$$
converge. Therefore their terms tend to $0$.

:::

:::

::: {.pf-step #s1-3}

The series
$$
\sum_{n=0}^\infty f_ng_nz^n
$$
converges absolutely for every $\abs{z}<\rho^2$.


::: pf-proof

By step [](#s1-2){.pf-ref}, the sequences $(f_n\rho^n)$ and $(g_n\rho^n)$ are bounded. Choose $M,N>0$ such that
$$
\abs{f_n}\rho^n\leq M,
\qquad
\abs{g_n}\rho^n\leq N
$$
for every $n$. Then, for $\abs{z}<\rho^2$,
$$
\abs{f_ng_nz^n}
\leq
MN\left(\frac{\abs{z}}{\rho^2}\right)^n.
$$
The geometric series on the right converges, so the comparison test gives absolute convergence.

:::

:::

::: {.pf-step #s1-4}

The function $h$ is holomorphic on a neighborhood of $D$.


::: pf-proof

By step [](#s1-3){.pf-ref}, the power series for $h$ has radius of convergence at least $\rho^2$. Since $\rho^2>1$, the disk $\abs{z}<\rho^2$ is an open neighborhood of $D$, and every power series is holomorphic on the interior of its disk of convergence.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
