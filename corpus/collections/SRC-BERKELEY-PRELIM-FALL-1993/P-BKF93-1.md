---
schema: qual/card@1
id: P-BKF93-1
kind: problem
title: A convergent sequence together with its limit is compact
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used convergence to place the tail of the sequence in one member of an
    arbitrary open cover and covered the remaining finite initial segment by
    finitely many further members.
---

::: {.problem}
Let $X$ be a metric space and let $(x_n)$ converge to $x_0\in X$. Prove that
\[
C=\{x_0,x_1,x_2,\ldots\}
\]
is compact.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\mathcal U$ be an arbitrary open cover of $C$. There are
$U_0\in\mathcal U$ and an integer $N\geq2$ such that
$$
x_0\in U_0
\qquad\text{and}\qquad
x_n\in U_0\quad\text{for every }n\geq N.
$$

::: pf-proof

Because $\mathcal U$ covers $C$, there is $U_0\in\mathcal U$ with
$x_0\in U_0$. Since $U_0$ is open, there is $\varepsilon>0$ such that
$$
B(x_0,\varepsilon)\subseteq U_0.
$$
The convergence $x_n\to x_0$ gives an integer $N\geq2$ such that
$$
n\geq N
\quad\Longrightarrow\quad
d(x_n,x_0)<\varepsilon.
$$
Hence every $x_n$ with $n\geq N$ lies in $U_0$.

:::

:::

::: {.pf-step #s2}

The finite set
$$
\{x_1,\ldots,x_{N-1}\}
$$
is covered by finitely many members of $\mathcal U$.

::: pf-proof

For each integer $n$ with $1\leq n<N$, choose
$U_n\in\mathcal U$ such that $x_n\in U_n$. There are only finitely many
such indices.

:::

:::

::: {.pf-step #s3}

The family
$$
\{U_0,U_1,\ldots,U_{N-1}\}
$$
is a finite subcover of $C$.

::: pf-proof

The point $x_0$ and every $x_n$ with $n\geq N$ lie in $U_0$ by step [](#s1){.pf-ref}.
Every $x_n$ with $1\leq n<N$ lies in $U_n$ by step [](#s2){.pf-ref}. Thus the displayed
finite family covers every point of $C$.

:::

:::

::: pf-qed

The open cover $\mathcal U$ was arbitrary, and step [](#s3){.pf-ref} gives it a finite
subcover. Therefore $C$ is compact.

:::

:::

:::
