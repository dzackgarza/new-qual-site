---
schema: qual/card@1
id: P-UCLARA16F-09
kind: problem
title: Fourier--Laplace transforms of probability measures on $[0,1]$ with polynomial growth
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $\mu$ be a positive Borel measure on $[0,1]$ with $\mu([0,1])=1$.

(a) Show that the function
\[
f(z)=\int_{[0,1]}e^{izt}\,d\mu(t)
\]
is holomorphic on $\mathbb C$.

(b) Suppose that there exists $n\in\mathbb N$ such that
\[
\limsup_{|z|\to\infty}\frac{|f(z)|}{|z|^n}<\infty.
\]
Show that then $\mu$ is equal to the Dirac measure $\delta_0$ at $0$.
:::

## Part (a)

For every \(k\ge0\), define the moment
\[
m_k
=
\int_{[0,1]}t^k\,d\mu(t).
\]

::: pf

::: pf-step

One has
\[
\boxed{0\le m_k\le1}.
\]


::: pf-proof

Since \(0\le t\le1\),
\[
0\le t^k\le1.
\]
Integrating against the probability measure \(\mu\) gives
\[
0\le m_k\le\mu([0,1])=1.
\]

:::

:::

::: pf-step

For fixed \(z\in\mathbb C\),
\[
e^{izt}
=
\sum_{k=0}^{\infty}
\frac{(izt)^k}{k!}
\]
uniformly for \(t\in[0,1]\).


::: pf-proof

For \(t\in[0,1]\),
\[
\left|
\frac{(izt)^k}{k!}
\right|
\le
\frac{|z|^k}{k!},
\]
and
\[
\sum_{k=0}^{\infty}
\frac{|z|^k}{k!}
=
e^{|z|}<\infty.
\]
Apply the Weierstrass \(M\)-test.

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(z)
=
\sum_{k=0}^{\infty}
\frac{i^k m_k}{k!}z^k}.
\]


::: pf-proof

Integrate the uniformly convergent series from step <1>2 term by term:
\[
\begin{aligned}
f(z)
&=
\int
\sum_{k=0}^{\infty}
\frac{(izt)^k}{k!}\,d\mu(t)\\
&=
\sum_{k=0}^{\infty}
\frac{(iz)^k}{k!}
\int t^k\,d\mu(t).
\end{aligned}
\]

:::

:::

::: pf-step

The series in step <1>3 has infinite radius of convergence.


::: pf-proof

By step <1>1,
\[
\left|
\frac{i^k m_k}{k!}z^k
\right|
\le
\frac{|z|^k}{k!},
\]
and the exponential series converges for every \(z\in\mathbb C\).

:::

:::

::: pf-step

Hence
\[
\boxed{
f\text{ is entire}.}
\]


::: pf-proof

Step <1>3 represents \(f\) by a power series with infinite radius of convergence.

:::

:::

::: pf-step

There exist constants \(C>0\) and \(R_0>0\) such that
\[
\boxed{
|f(z)|
\le
C|z|^n}
\]
whenever \(|z|\ge R_0\).


::: pf-proof

This is the definition of finiteness of the stated limsup.

:::

:::

::: pf-step

There is a constant \(C_1>0\) such that for every \(R\ge1\),
\[
\boxed{
\max_{|z|=R}|f(z)|
\le
C_1R^n}.
\]


::: pf-proof

For \(R\ge R_0\), use step <1>6. For \(1\le R\le R_0\), continuity of \(f\) on the compact disk \(|z|\le R_0\) gives a finite maximum; enlarge \(C_1\) to absorb this bounded range.

:::

:::

::: pf-step

For every integer \(m>n\), Cauchy's estimate gives
\[
|f^{(m)}(0)|
\le
\frac{m!}{R^m}
\max_{|z|=R}|f(z)|.
\]


::: pf-proof

Apply Cauchy's estimate to the entire function \(f\) on the circle \(|z|=R\).

:::

:::

::: pf-step

Therefore
\[
|f^{(m)}(0)|
\le
m!C_1R^{n-m}
\]
for every \(R\ge1\).


::: pf-proof

Substitute step <1>7 into step <1>8.

:::

:::

::: pf-step

Letting \(R\to\infty\),
\[
\boxed{
f^{(m)}(0)=0}
\]
for every \(m>n\).


::: pf-proof

Since \(m>n\),
\[
R^{n-m}\to0.
\]
The left-hand side of step <1>9 is independent of \(R\), so it must vanish.

:::

:::

::: pf-step

Hence \(f\) is a polynomial of degree at most \(n\).


::: pf-proof

All Taylor coefficients of degree \(>n\) vanish by step <1>10, and \(f\) is entire.

:::

:::

::: pf-step

For every real \(x\),
\[
\boxed{|f(x)|\le1}.
\]


::: pf-proof

Since \(|e^{ixt}|=1\),
\[
\begin{aligned}
|f(x)|
&=
\left|
\int e^{ixt}\,d\mu(t)
\right|\\
&\le
\int |e^{ixt}|\,d\mu(t)\\
&=
\mu([0,1])\\
&=
1.
\end{aligned}
\]

:::

:::

::: pf-step

Therefore \(f\) is constant.


::: pf-proof

A nonconstant polynomial is unbounded on the real axis as \(|x|\to\infty\). Step <1>12 says \(f\) is bounded on \(\mathbb R\).

:::

:::

::: pf-step

Since
\[
f(0)=1,
\]
one has
\[
\boxed{f\equiv1}.
\]


::: pf-proof

\[
f(0)
=
\int 1\,d\mu
=
\mu([0,1])
=
1.
\]
Combine with step <1>13.

:::

:::

::: pf-step

Differentiating the power series at \(0\),
\[
\boxed{
f'(0)
=
i\int_{[0,1]}t\,d\mu(t)}.
\]


::: pf-proof

From step <1>3, the coefficient of \(z\) is
\[
im_1
=
i\int t\,d\mu.
\]

:::

:::

::: pf-step

Since \(f\equiv1\),
\[
\boxed{
\int_{[0,1]}t\,d\mu(t)=0}.
\]


::: pf-proof

Step <1>14 gives
\[
f'(0)=0.
\]
Use step <1>15 and divide by \(i\).

:::

:::

::: pf-step

For every \(\varepsilon>0\),
\[
\boxed{
\mu([\varepsilon,1])=0}.
\]


::: pf-proof

Since \(t\ge\varepsilon\) on \([\varepsilon,1]\),
\[
0
=
\int_0^1 t\,d\mu(t)
\ge
\int_{[\varepsilon,1]}t\,d\mu(t)
\ge
\varepsilon\,\mu([\varepsilon,1]).
\]
Thus the measure must vanish there.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\mu((0,1])=0}.
\]


::: pf-proof

Since
\[
(0,1]
=
\bigcup_{m=1}^{\infty}
[1/m,1],
\]
and each set in the union has measure zero by step <1>17, countable subadditivity gives zero measure to the union.

:::

:::

::: pf-step

Since \(\mu([0,1])=1\),
\[
\boxed{
\mu(\{0\})=1}.
\]


::: pf-proof

The complement of \(\{0\}\) in \([0,1]\) is \((0,1]\), which has measure zero by step <1>18.

:::

:::

::: pf-step

Hence
\[
\boxed{
\mu=\delta_0}.
\]


::: pf-proof

A probability measure concentrated entirely at \(0\) is the Dirac measure at \(0\).

:::

:::

::: pf-qed

Step <1>5 proves part (a), and step <1>20 proves part (b).

:::

:::
