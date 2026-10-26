---
schema: qual/card@1
id: P-UCLARA11F-06
kind: problem
title: Upper semicontinuity of measure under weak-star convergence
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(X,d)$ be a compact metric space.
Let $(\mu_n)$ be positive Borel measures on $X$ converging weak-* to a finite positive Borel measure $\mu$, meaning
\[
\int_X f\,d\mu_n\to\int_X f\,d\mu
\qquad\text{for every }f\in C(X).
\]
Show that
\[
\mu(K)\ge \limsup_{n\to\infty}\mu_n(K)
\]
for every compact set $K\subseteq X$.
:::

Let
\[
K\subseteq X
\]
be compact. Since \(X\) is metric, \(K\) is closed.

For \(\delta>0\), define
\[
\boxed{
\varphi_\delta(x)
=
\max\left\{
1-\frac{d(x,K)}{\delta},
0
\right\}}.
\]

::: pf

::: pf-step

The function \(\varphi_\delta\) is continuous on \(X\).


::: pf-proof

The distance function
\[
x\mapsto d(x,K)
\]
is \(1\)-Lipschitz, hence continuous. Composing with
\[
t\mapsto \max\{1-t/\delta,0\}
\]
preserves continuity.

:::

:::

::: pf-step

One has
\[
\boxed{
0\le\varphi_\delta\le1}.
\]


::: pf-proof

This is immediate from the defining maximum.

:::

:::

::: pf-step

For every \(x\in K\),
\[
\boxed{\varphi_\delta(x)=1}.
\]


::: pf-proof

If \(x\in K\), then
\[
d(x,K)=0.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\mathbf 1_K\le\varphi_\delta}.
\]


::: pf-proof

On \(K\), both sides equal \(1\) by step <1>3. Outside \(K\), the left side is \(0\) and the right side is nonnegative by step <1>2.

:::

:::

::: pf-step

For every \(n\),
\[
\boxed{
\mu_n(K)
\le
\int_X\varphi_\delta\,d\mu_n}.
\]


::: pf-proof

Since \(\mu_n\) is positive,
\[
\mu_n(K)
=
\int_X\mathbf 1_K\,d\mu_n
\le
\int_X\varphi_\delta\,d\mu_n
\]
by step <1>4.

:::

:::

::: pf-step

Taking \(\limsup\),
\[
\limsup_{n\to\infty}\mu_n(K)
\le
\lim_{n\to\infty}
\int_X\varphi_\delta\,d\mu_n.
\]


::: pf-proof

The pointwise inequality in step <1>5 holds for every \(n\), so the limsup of the left side is bounded by the limsup of the right side. The latter sequence actually converges by weak-* convergence.

:::

:::

::: pf-step

By weak-* convergence,
\[
\boxed{
\lim_{n\to\infty}
\int_X\varphi_\delta\,d\mu_n
=
\int_X\varphi_\delta\,d\mu}.
\]


::: pf-proof

The test function \(\varphi_\delta\) is continuous by step <1>1.

:::

:::

::: pf-step

Hence
\[
\boxed{
\limsup_{n\to\infty}\mu_n(K)
\le
\int_X\varphi_\delta\,d\mu}
\]
for every \(\delta>0\).


::: pf-proof

Combine steps <1>6--<1>7.

:::

:::

::: pf-step

For every \(x\notin K\),
\[
d(x,K)>0.
\]


::: pf-proof

The set \(K\) is closed. If \(d(x,K)=0\), then \(x\) belongs to the closure of \(K\), hence to \(K\), contradiction.

:::

:::

::: pf-step

Therefore, for every \(x\in X\),
\[
\boxed{
\varphi_\delta(x)\to\mathbf 1_K(x)}
\]
as \(\delta\downarrow0\).


::: pf-proof

If \(x\in K\), step <1>3 gives \(\varphi_\delta(x)=1\) for every \(\delta\).

If \(x\notin K\), let
\[
r=d(x,K)>0
\]
by step <1>9. For every \(0<\delta<r\),
\[
1-\frac r\delta<0,
\]
so
\[
\varphi_\delta(x)=0.
\]
Thus the limit is \(0=\mathbf 1_K(x)\).

:::

:::

::: pf-step

Since
\[
0\le\varphi_\delta\le1
\]
and \(\mu\) is finite, dominated convergence gives
\[
\boxed{
\int_X\varphi_\delta\,d\mu
\longrightarrow
\mu(K)}
\]
as \(\delta\downarrow0\).


::: pf-proof

Use step <1>10 for pointwise convergence and step <1>2 for domination by the integrable constant function \(1\), whose integral is \(\mu(X)<\infty\).

:::

:::

::: pf-step

Letting \(\delta\downarrow0\) in step <1>8,
\[
\boxed{
\limsup_{n\to\infty}\mu_n(K)
\le
\mu(K)}.
\]


::: pf-proof

The left-hand side is independent of \(\delta\), while the right-hand side converges to \(\mu(K)\) by step <1>11.

:::

:::

::: pf-step

Equivalently,
\[
\boxed{
\mu(K)
\ge
\limsup_{n\to\infty}\mu_n(K)}.
\]


::: pf-proof

This is step <1>12 rewritten.

:::

:::

::: pf-qed

Step <1>13 is the required conclusion.

:::

:::
