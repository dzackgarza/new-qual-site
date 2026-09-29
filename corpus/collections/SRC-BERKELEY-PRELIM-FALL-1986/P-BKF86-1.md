---
schema: qual/card@1
id: P-BKF86-1
kind: problem
title: Sequences showing each Arzelà–Ascoli hypothesis is needed
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
---

::: {.problem}
The Arzelà–Ascoli theorem asserts that a sequence $\{f_n\}$ of continuous real-valued functions on a metric space $\Omega$ is precompact (i.e., has a uniformly convergent subsequence) if

(i) $\Omega$ is compact,

(ii) $\sup_n\|f_n\|<\infty$, where $\|f_n\|=\sup\{|f_n(x)| : x\in\Omega\}$,

(iii) the sequence is equicontinuous.

Give examples of sequences which are not precompact such that: (i) and (ii) hold but (iii) fails; (i) and (iii) hold but (ii) fails; (ii) and (iii) hold but (i) fails.
Take $\Omega$ to be a subset of the real line.
Sketch the graph of a typical member of the sequence in each case.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Conditions (i) and (ii) can hold while (iii) fails, without precompactness.

::: pf-proof

Take
$$
\Omega=[0,1],
\qquad
f_n(x)=x^n.
$$
The space $\Omega$ is compact, and
$$
\norm{f_n}_\infty=1
$$
for every $n$, so (i) and (ii) hold.

The family is not equicontinuous at $x=1$. Indeed, if equicontinuity held there, then for $\varepsilon=1/2$ there would be $\delta>0$ such that
$$
\abs{x-1}<\delta
\quad\Longrightarrow\quad
\abs{x^n-1}<\frac12
$$
for every $n$. Choose any
$$
x\in\bigl(\max\{0,1-\delta\},1\bigr).
$$
Then $x\in[0,1)$ and $\abs{x-1}<\delta$. Since $x^n\to0$, the displayed inequality fails for all sufficiently large $n$.

Moreover, every subsequence $(f_{n_k})$ has the same pointwise limit
$$
f(x)=
\begin{cases}
0,&0\leq x<1,\\
1,&x=1.
\end{cases}
$$
This limit is discontinuous. A uniformly convergent subsequence of continuous functions would have a continuous pointwise limit, so no such subsequence exists.

The graph of $f_n$ runs from $(0,0)$ to $(1,1)$ and, as $n$ grows, stays increasingly close to the $x$-axis until very near $x=1$.

:::

:::

::: {.pf-step #s2}

Conditions (i) and (iii) can hold while (ii) fails, without precompactness.

::: pf-proof

Again take
$$
\Omega=[0,1],
$$
but now let
$$
f_n(x)=n
$$
for every $x\in[0,1]$.
The domain is compact. The sequence is equicontinuous because
$$
\abs{f_n(x)-f_n(y)}=0
$$
for all $x,y$ and all $n$.

On the other hand,
$$
\norm{f_n}_\infty=n,
$$
so (ii) fails. If a subsequence converged uniformly, then it would be uniformly Cauchy. But for distinct indices $m,n$,
$$
\norm{f_n-f_m}_\infty
=
\abs{n-m}
\geq1.
$$
Hence no subsequence is uniformly Cauchy.

The graph of $f_n$ is the horizontal line of height $n$.

:::

:::

::: {.pf-step #s3}

Conditions (ii) and (iii) can hold while (i) fails, without precompactness.

::: pf-proof

Take
$$
\Omega=\RR
$$
and define
$$
\phi(t)=\max\{1-2\abs{t},0\},
\qquad
f_n(x)=\phi(x-n).
$$
The domain $\RR$ is not compact. Each $f_n$ satisfies
$$
0\leq f_n(x)\leq1,
\qquad
\norm{f_n}_\infty=1,
$$
so (ii) holds.

The function $\phi$ is $2$-Lipschitz, hence for every $n$,
$$
\abs{f_n(x)-f_n(y)}
\leq
2\abs{x-y}.
$$
Thus the family is equicontinuous.

If $m\neq n$ are positive integers, then
$$
f_n(n)=1
$$
whereas
$$
f_m(n)=0,
$$
because $\abs{n-m}\geq1$ and $\phi$ vanishes outside $[-1/2,1/2]$. Consequently
$$
\norm{f_n-f_m}_\infty\geq1.
$$
No subsequence is uniformly Cauchy, hence no subsequence converges uniformly.

The graph of $f_n$ is a triangular bump of height $1$ centered at $x=n$, supported on
$$
\left[n-\frac12,n+\frac12\right],
$$
and zero elsewhere.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} give the three requested examples and describe their typical graphs.

:::

:::

:::
