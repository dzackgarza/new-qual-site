---
schema: qual/card@1
id: P-RAF22B
kind: problem
title: "For $f_n\\to f$ a.e. on a finite measure space, $\\norm{f_n-f}_p\\to0$ iff $\\norm{f_n}_p\\to\\norm{f}_p$"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Pointwise Convergence
  - Vitali Convergence Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Let $1 \leq p < \infty$, let $f, f_n \in L^p(X, \mu)$ for $n \in \NN$, and assume that $f_n \to f$ pointwise $\mu$-almost-everywhere.
Prove that $\norm{f_n - f}_p \to 0$ if and only if $\norm{f_n}_p \to \norm{f}_p$.

(Note: You are not allowed to use the generalized Dominated Convergence Theorem unless you prove it.)
:::

::: {.solution}

::: pf

::: pf-step

If $\norm{f_n-f}_p\to0$, then $\norm{f_n}_p\to\norm{f}_p$.

::: pf-proof

If
$$
\norm{f_n-f}_p\to0,
$$
then the reverse triangle inequality gives
$$
\abs{\norm{f_n}_p-\norm{f}_p}
\le\norm{f_n-f}_p\to0.
$$
Hence
$$
\norm{f_n}_p\to\norm{f}_p.
$$

:::

:::

::: {.pf-step #s2}

If $\norm{f_n}_p\to\norm{f}_p$, then $\abs{f_n}^p\to\abs{f}^p$ in $L^1$.

::: pf-proof

Assume now that
$$
\norm{f_n}_p\to\norm{f}_p.
$$
Set
$$
g_n:=\abs{f_n}^p,
\qquad
g:=\abs{f}^p.
$$
Then $g_n\to g$ almost everywhere and
$$
\int_Xg_n\,d\mu=\norm{f_n}_p^p
\longrightarrow
\norm{f}_p^p=\int_Xg\,d\mu.
$$

Moreover,
$$
\min(g_n,g)\to g
$$
almost everywhere and $0\le\min(g_n,g)\le g\in L^1$. By the ordinary dominated convergence theorem,
$$
\int_X\min(g_n,g)\,d\mu\to\int_Xg\,d\mu.
$$
Since
$$
\abs{g_n-g}=g_n+g-2\min(g_n,g),
$$
we obtain
$$
\boxed{\norm{g_n-g}_1\to0.}
$$

:::

:::

::: pf-step

Under the hypothesis of step [](#s2){.pf-ref}, the functions $h_n\coloneqq\abs{f_n-f}^p$ are uniformly integrable.

::: pf-proof

Convergence $g_n\to g$ in $L^1$ implies that the family $\{g_n:n\ge1\}$ is uniformly integrable. Indeed, given $\varepsilon>0$, first choose $N$ so that
$$
\norm{g_n-g}_1<\varepsilon/4
$$
for $n\ge N$. By absolute continuity of the integrals of $g,g_1,\ldots,g_{N-1}$, there exists $\delta>0$ such that $\mu(E)<\delta$ implies
$$
\int_E g<\varepsilon/4
$$
and
$$
\int_E g_n<\varepsilon/2
\qquad(n<N).
$$
For $n\ge N$,
$$
\int_Eg_n
\le\norm{g_n-g}_1+\int_Eg
<\varepsilon/2.
$$

Now put
$$
h_n:=\abs{f_n-f}^p.
$$
The elementary inequality
$$
h_n\le2^{p-1}(g_n+g)
$$
shows that $(h_n)$ is uniformly integrable as well.

:::

:::

::: pf-step

Under the hypothesis of step [](#s2){.pf-ref}, $\norm{f_n-f}_p\to0$.

::: pf-proof

We have $h_n\to0$ almost everywhere. Fix $\varepsilon>0$. By uniform integrability, choose $\delta>0$ such that
$$
\mu(E)<\delta
\quad\Longrightarrow\quad
\sup_n\int_Eh_n\,d\mu<\frac\varepsilon2.
$$
Because $\mu(X)<\infty$, Egorov's theorem gives a measurable $E\subset X$ with $\mu(E)<\delta$ such that $h_n\to0$ uniformly on $X\setminus E$. Hence, for all sufficiently large $n$,
$$
\int_{X\setminus E}h_n\,d\mu
\le \mu(X)\sup_{X\setminus E}h_n
<\frac\varepsilon2.
$$
Therefore
$$
\int_X\abs{f_n-f}^p\,d\mu
=\int_Xh_n\,d\mu
<\varepsilon
$$
for all sufficiently large $n$. Thus
$$
\boxed{\norm{f_n-f}_p\to0.}
$$

:::

:::

:::

:::
