---
schema: qual/card@1
id: P-BKS16-3B
kind: problem
title: Lipschitz limit of $\sum(-1)^k/(k+\abs{x})$ and uniform convergence
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked the statement against Problem 3B in the vendored Berkeley Spring 2016 exam and independently reviewed the supplied solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the alternating-series estimates for pointwise convergence, the global Lipschitz bound through $\abs{x}$, and the uniform tail estimate.
---

::: {.problem}
Show that the series
$$
\sum_{k=1}^\infty \frac{(-1)^k}{k+\abs{x}}
$$
converges pointwise to a Lipschitz function $f(x)$.
Is the convergence uniform on $\RR$?
:::

::: {.solution}

For $u\geq0$, write
$$
F(u)\coloneqq\sum_{k=1}^\infty\frac{(-1)^k}{k+u}.
$$
Then the function in the problem is $f(x)=F(\abs{x})$.

::: pf

::: {.pf-step #s1-1}

The series defining $F(u)$ converges for every $u\geq0$.


::: pf-proof

For fixed $u\geq0$, the sequence
$$
\frac1{k+u}
$$
is positive, decreases in $k$, and tends to $0$. The alternating-series test therefore gives convergence.

:::

:::

::: {.pf-step #s1-2}

The function $F$ is $1$-Lipschitz on $[0,\infty)$.


::: pf-proof

Let $0\leq u<v$ and put $\varepsilon=v-u$. Subtracting the convergent series gives
$$
F(u)-F(v)
=
\sum_{k=1}^\infty
(-1)^k\frac{\varepsilon}{(k+u)(k+v)}.
$$
The positive magnitudes
$$
a_k\coloneqq\frac{\varepsilon}{(k+u)(k+v)}
$$
decrease to $0$. By the alternating-series remainder estimate,
$$
\abs{F(u)-F(v)}\leq a_1
=
\frac{v-u}{(1+u)(1+v)}
\leq v-u.
$$
Interchanging $u$ and $v$ gives the same estimate for arbitrary $u,v\geq0$.

:::

:::

::: {.pf-step #s1-3}

The pointwise limit $f$ is $1$-Lipschitz on $\RR$.


::: pf-proof

By step [](#s1-2){.pf-ref} and the reverse triangle inequality,
$$
\begin{aligned}
\abs{f(x)-f(y)}
&=\abs{F(\abs{x})-F(\abs{y})}\\
&\leq\abs{\abs{x}-\abs{y}}\\
&\leq\abs{x-y}.
\end{aligned}
$$
Thus $f$ is Lipschitz with constant $1$.

:::

:::

::: {.pf-step #s1-4}

The series converges uniformly on $\RR$; the answer to the second question is $\boxed{\text{yes}}$.


::: pf-proof

Let
$$
S_N(x)\coloneqq\sum_{k=1}^N\frac{(-1)^k}{k+\abs{x}}.
$$
For each fixed $x$, the alternating-series remainder estimate gives
$$
\abs{f(x)-S_N(x)}
\leq
\frac1{N+1+\abs{x}}
\leq
\frac1{N+1}.
$$
The last bound is independent of $x$ and tends to $0$, so
$$
\sup_{x\in\RR}\abs{f(x)-S_N(x)}\longrightarrow0.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} prove the pointwise convergence to a Lipschitz function, and step [](#s1-4){.pf-ref} proves uniform convergence.

:::

:::

:::
