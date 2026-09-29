---
schema: qual/card@1
id: P-BKS00-7
kind: problem
title: A positive decreasing $C^2$ function with bounded second derivative has derivative tending to zero
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Positivity and f'<=0 give a finite limit for f. Bounded f'' makes
    f' Lipschitz; any derivative value bounded away from zero on the
    negative side would therefore force a fixed drop of f over a
    fixed-length interval, contradicting convergence of f.
---

::: {.problem}
Let $f$ be a positive $C^2$ function on $(0,\infty)$ such that $f'\le0$ and $f''$ is bounded. Prove that
\[
\lim_{t\to\infty}f'(t)=0.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The limit
$$
L=\lim_{t\to\infty}f(t)
$$
exists and is finite.

::: pf-proof

Since $f'\leq0$, the function $f$ is nonincreasing. Since $f$ is
positive, it is bounded below by $0$. Hence the monotone convergence
theorem for real-valued functions gives a finite limit $L\geq0$.

:::

:::

::: {.pf-step #s2}

There is a constant $M>0$ such that
$$
\abs{f'(s)-f'(t)}
\leq
M\abs{s-t}
$$
for all $s,t>0$.

::: pf-proof

Choose $M>0$ with
$$
\abs{f''(u)}\leq M
$$
for every $u>0$. By the mean value theorem applied to $f'$,
$$
\abs{f'(s)-f'(t)}
\leq
M\abs{s-t}.
$$

:::

:::

::: {.pf-step #s3}

For every $\varepsilon>0$, there exists $T>0$ such that
$$
t\geq T
\quad\Longrightarrow\quad
f'(t)>-\varepsilon.
$$

::: pf-proof

Suppose not. Then for some $\varepsilon>0$ there are arbitrarily large
$t$ such that
$$
f'(t)\leq-\varepsilon.
$$
Set
$$
\delta=\frac{\varepsilon}{2M}>0.
$$
For every $s\in[t,t+\delta]$, step [](#s2){.pf-ref} gives
$$
f'(s)
\leq
f'(t)+M(s-t)
\leq
-\varepsilon+M\delta
=
-\frac{\varepsilon}{2}.
$$
Therefore
$$
\begin{aligned}
f(t)-f(t+\delta)
&=
-\int_t^{t+\delta}f'(s)\,ds\\
&\geq
\frac{\varepsilon\delta}{2}.
\end{aligned}
$$
The right-hand side is a fixed positive number, independent of $t$.
But step [](#s1){.pf-ref} gives
$$
f(t)-f(t+\delta)\longrightarrow L-L=0
$$
as $t\to\infty$, a contradiction.

:::

:::

::: {.pf-step #s4}

The derivative satisfies
$$
\boxed{\lim_{t\to\infty}f'(t)=0}.
$$

::: pf-proof

By hypothesis, $f'(t)\leq0$ for every $t$. Step [](#s3){.pf-ref} says that for
every $\varepsilon>0$, all sufficiently large $t$ satisfy
$$
-\varepsilon<f'(t)\leq0.
$$
This is exactly $f'(t)\to0$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the desired conclusion.

:::

:::

:::
