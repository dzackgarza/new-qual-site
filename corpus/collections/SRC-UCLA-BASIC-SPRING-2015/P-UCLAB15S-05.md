---
schema: qual/card@1
id: P-UCLAB15S-05
kind: problem
title: Convergence of the integral-sum discrepancy for a decreasing function
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:[1,\infty)\to[0,\infty)$ be bounded and monotonically decreasing with $\lim_{x\to\infty}f(x)=0$.
Show that
$$
\int_1^{N+1}f(x)\,dx-\sum_{n=1}^N f(n)
$$
converges to a finite limit as $N\to\infty$.
:::

::: {.solution}

Define
$$
D_N
=
\int_1^{N+1}f(x)\,dx
-
\sum_{n=1}^Nf(n).
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
D_N
=
-
\sum_{n=1}^N
\left(
f(n)-\int_n^{n+1}f(x)\,dx
\right).
$$


::: pf-proof

Split the integral into unit intervals:
$$
\int_1^{N+1}f(x)\,dx
=
\sum_{n=1}^N
\int_n^{n+1}f(x)\,dx.
$$
Subtract
$$
\sum_{n=1}^Nf(n)
$$
and collect the terms.

:::

:::

::: {.pf-step #s1-2}

For every $n\ge1$,
$$
0
\le
f(n)-\int_n^{n+1}f(x)\,dx.
$$


::: pf-proof

Because $f$ is decreasing,
$$
f(x)\le f(n)
$$
for
$$
n\le x\le n+1.
$$
Therefore
$$
\int_n^{n+1}f(x)\,dx
\le
f(n).
$$

:::

:::

::: {.pf-step #s1-3}

For every $n\ge1$,
$$
f(n)-\int_n^{n+1}f(x)\,dx
\le
f(n)-f(n+1).
$$


::: pf-proof

Because $f$ is decreasing,
$$
f(x)\ge f(n+1)
$$
on
$$
[n,n+1].
$$
Hence
$$
\int_n^{n+1}f(x)\,dx
\ge
f(n+1).
$$
Subtract from $f(n)$.

:::

:::

::: {.pf-step #s1-4}

The partial sums
$$
S_N
=
\sum_{n=1}^N
\left(
f(n)-\int_n^{n+1}f(x)\,dx
\right)
$$
form an increasing sequence.


::: pf-proof

Every summand is nonnegative by step [](#s1-2){.pf-ref}.
Therefore
$$
S_{N+1}\ge S_N.
$$

:::

:::

::: {.pf-step #s1-5}

The sequence $(S_N)$ is bounded above by $f(1)$.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\begin{aligned}
S_N
&\le
\sum_{n=1}^N
\bigl(f(n)-f(n+1)\bigr)\\
&=
f(1)-f(N+1)\\
&\le
f(1),
\end{aligned}
$$
because
$$
f(N+1)\ge0.
$$

:::

:::

::: {.pf-step #s1-6}

Hence $(S_N)$ converges to a finite limit
$$
S.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $(S_N)$ is increasing.
By step [](#s1-5){.pf-ref}, it is bounded above.
The monotone convergence theorem for real sequences therefore gives a finite limit.

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{
D_N\to -S
}
$$
as
$$
N\to\infty.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
D_N=-S_N.
$$
Take the limit from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\int_1^{N+1}f(x)\,dx
-
\sum_{n=1}^Nf(n)
}
$$
converges to a finite limit.


::: pf-proof

This is exactly step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
