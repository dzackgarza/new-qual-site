---
schema: qual/card@1
id: P-PRELIM82S-09
kind: problem
title: Absolute convergence of all derivatives of $\sum z^n/n^{\log n}$
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
    The nth root of 1/n^{log n} tends to 1, so the original series has
    radius 1 and diverges for |z|>1. For the mth derivative, the
    coefficient is at most n^m/n^{log n}. On |z|=1 this is eventually
    at most n^{-2}, and for |z|<1 the geometric factor gives absolute
    convergence. Thus every derivative converges absolutely exactly on
    the closed unit disk.
---

::: {.problem}
Determine all $z\in\mathbb C$ for which the power series
\[
\sum_{n=1}^{\infty}\frac{z^n}{n^{\log n}}
\]
and every term-by-term derivative of this series converge absolutely.
:::

::: {.solution}
For an integer $m\geq0$, let $S_m(z)$ denote the series obtained by
differentiating term by term $m$ times. Thus
$$
S_m(z)
=
\sum_{n=\max\{1,m\}}^{\infty}
\frac{n(n-1)\cdots(n-m+1)}{n^{\log n}}z^{n-m},
$$
where for $m=0$ the numerator is understood to be $1$.

::: pf

::: {.pf-step #s1}

One has
$$
\lim_{n\to\infty}
\left(\frac{1}{n^{\log n}}\right)^{1/n}
=1.
$$

::: pf-proof

Since
$$
n^{\log n}
=
e^{(\log n)^2},
$$
we have
$$
\left(\frac{1}{n^{\log n}}\right)^{1/n}
=
e^{-(\log n)^2/n}.
$$
Because
$$
\frac{(\log n)^2}{n}\longrightarrow0,
$$
the displayed quantity tends to $1$.

:::

:::

::: {.pf-step #s2}

If $\abs{z}>1$, then the original series does not converge.

::: pf-proof

For its $n$th term,
$$
u_n=\frac{z^n}{n^{\log n}},
$$
step [](#s1){.pf-ref} gives
$$
\abs{u_n}^{1/n}
=
\abs{z}
\left(\frac{1}{n^{\log n}}\right)^{1/n}
\longrightarrow
\abs{z}>1.
$$
Hence $\abs{u_n}$ does not tend to zero, so the series cannot converge.

:::

:::

::: {.pf-step #s3}

Fix $m\geq0$. For all $n\geq\max\{1,m\}$,
$$
n(n-1)\cdots(n-m+1)\leq n^m.
$$

::: pf-proof

Each of the $m$ factors on the left is at most $n$.

:::

:::

::: {.pf-step #s4}

If $\abs{z}<1$, then $S_m(z)$ converges absolutely for every
$m\geq0$.

::: pf-proof

Fix $m\geq0$ and put $r=\abs{z}<1$. By step [](#s3){.pf-ref},
$$
\left|
\frac{n(n-1)\cdots(n-m+1)}{n^{\log n}}z^{n-m}
\right|
\leq
n^m r^{n-m},
$$
because $n^{\log n}\geq1$ for $n\geq1$. The series
$$
\sum_{n=\max\{1,m\}}^{\infty}n^m r^{n-m}
$$
converges by the ratio test, since the ratio of consecutive terms tends
to $r<1$. Therefore $S_m(z)$ converges absolutely.

:::

:::

::: {.pf-step #s5}

If $\abs{z}=1$, then $S_m(z)$ converges absolutely for every
$m\geq0$.

::: pf-proof

Fix $m\geq0$. By step [](#s3){.pf-ref} and $\abs{z}=1$,
$$
\left|
\frac{n(n-1)\cdots(n-m+1)}{n^{\log n}}z^{n-m}
\right|
\leq
n^{m-\log n}.
$$
Since $\log n\to\infty$, there exists $N$ such that
$$
\log n\geq m+2
$$
for every $n\geq N$. Hence for $n\geq N$,
$$
n^{m-\log n}\leq n^{-2}.
$$
The tail is therefore dominated by the convergent series
$$
\sum_{n=N}^{\infty}\frac1{n^2},
$$
so $S_m(z)$ converges absolutely.

:::

:::

::: {.pf-step #s6}

The required set is
$$
\boxed{\{z\in\CC:\abs{z}\leq1\}}.
$$

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} show that the original series and every
term-by-term derivative converge absolutely whenever $\abs{z}\leq1$.
Step [](#s2){.pf-ref} excludes every $z$ with $\abs{z}>1$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives exactly the requested set of complex numbers.

:::

:::

:::
