---
schema: qual/card@1
id: P-UCLAB06W-02
kind: problem
title: Left continuity of an alternating power series at its endpoint
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $(a_n)_{n\geq 1}$ be a decreasing sequence of positive numbers such that
$$
\sum_{n=1}^{\infty}a_n=\infty.
$$
Under what condition(s) is the function
$$
f(x)=\sum_{n=1}^{\infty}(-1)^n a_nx^n
$$
well-defined and left-continuous at $x=1$?
Carefully prove your assertion.
:::

::: {.solution}

The necessary and sufficient condition is
$$
\boxed{a_n\longrightarrow0}.
$$
Under this condition, define $f$ on $[0,1]$ by the displayed series.

::: pf

::: {.pf-step #s1-1}

For every $x\in[0,1)$, the series
$$
\sum_{n=1}^{\infty}(-1)^n a_nx^n
$$
converges absolutely.


::: pf-proof

Because $(a_n)$ is decreasing and positive,
$$
0<a_n\le a_1
$$
for every $n$. Hence for $0\le x<1$,
$$
\sum_{n=1}^{\infty}\abs{(-1)^na_nx^n}
=
\sum_{n=1}^{\infty}a_nx^n
\le
 a_1\sum_{n=1}^{\infty}x^n<\infty.
$$

:::

:::

::: {.pf-step #s1-2}

If the series is well defined at $x=1$, then necessarily $a_n\to0$.


::: pf-proof

At $x=1$ the series is
$$
\sum_{n=1}^{\infty}(-1)^na_n.
$$
Convergence of any series forces its terms to tend to zero. Therefore
$$
(-1)^na_n\to0,
$$
which is equivalent to $a_n\to0$ because $a_n>0$.

:::

:::

::: {.pf-step #s1-3}

If $a_n\to0$, then the series converges at $x=1$.


::: pf-proof

The sequence $(a_n)$ is positive, decreasing, and tends to zero. The alternating-series test therefore gives convergence of
$$
\sum_{n=1}^{\infty}(-1)^na_n.
$$
Thus $f(1)$ is well defined.

:::

:::

::: {.pf-step #s1-4}

Assume $a_n\to0$. For every $x\in[0,1]$ and every $N\ge1$, the tail satisfies
$$
\abs{
\sum_{n=N+1}^{\infty}(-1)^na_nx^n
}
\le a_{N+1}.
$$


::: pf-proof

Fix $x\in[0,1]$. The sequence
$$
b_n=a_nx^n
$$
is nonnegative and decreasing, because both $(a_n)$ and $(x^n)$ are nonincreasing. Moreover,
$$
0\le b_n\le a_n\to0.
$$
The alternating-series remainder estimate therefore gives
$$
\abs{
\sum_{n=N+1}^{\infty}(-1)^nb_n
}
\le b_{N+1}
=a_{N+1}x^{N+1}
\le a_{N+1}.
$$

:::

:::

::: {.pf-step #s1-5}

If $a_n\to0$, the partial sums
$$
f_N(x)=\sum_{n=1}^N(-1)^na_nx^n
$$
converge uniformly to $f$ on $[0,1]$.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\sup_{x\in[0,1]}\abs{f(x)-f_N(x)}
\le a_{N+1}.
$$
Since $a_{N+1}\to0$, the convergence is uniform.

:::

:::

::: {.pf-step #s1-6}

If $a_n\to0$, then $f$ is continuous on $[0,1]$, in particular left-continuous at $x=1$.


::: pf-proof

Each $f_N$ is a polynomial and hence continuous on $[0,1]$. By step [](#s1-5){.pf-ref}, $f_N\to f$ uniformly on $[0,1]$. A uniform limit of continuous functions is continuous. Therefore
$$
\lim_{x\to1^-}f(x)=f(1).
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves necessity of $a_n\to0$. Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} show that this condition makes the series well defined on $[0,1]$, and step [](#s1-6){.pf-ref} proves left-continuity at $1$.

:::

:::

:::
