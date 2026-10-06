---
schema: qual/card@1
id: P-UCLARA15F-02
kind: problem
title: Almost everywhere convergence of $\sum_n\int_n^{n+n^{-a}}|f(x+y)|\,dy$ for $f\in L^p$
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 2 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $f \in L^p(\mathbb{R})$, $1 < p < \infty$, and let $a \in \mathbb{R}$ be such that $a > 1 - \frac{1}{p}$. Show that the series
\[
\sum_{n=1}^{\infty} \int_n^{n+n^{-a}} |f(x+y)|\,dy
\]
converges for almost all $x \in \mathbb{R}$.
:::

::: {.solution}
Let
\[
q=\frac{p}{p-1}
\]
be the conjugate exponent, so
\[
\frac1p+\frac1q=1.
\]

Define the nonnegative measurable function
\[
G(x)
=
\sum_{n=1}^{\infty}
\int_n^{n+n^{-a}}
|f(x+y)|\,dy,
\]
allowing the value \(+\infty\).

It suffices to prove
\[
G(x)<\infty
\]
for almost every \(x\).

<1>1. For each \(n\),
\[
\boxed{
\int_n^{n+n^{-a}}
|f(x+y)|\,dy
=
n^{-a}
\int_0^1
|f(x+n+n^{-a}z)|\,dz}.
\]

::: {.proof}
Use the change of variables
\[
y=n+n^{-a}z,
\qquad
dy=n^{-a}\,dz.
\]
:::

For each \(n\), set
\[
B_n(x)
=
\int_0^1
|f(x+n+n^{-a}z)|\,dz.
\]
Then
\[
G(x)=\sum_{n=1}^{\infty}n^{-a}B_n(x).
\]

<1>2. Since
\[
a>\frac1q,
\]
one has
\[
\boxed{
\sum_{n=1}^{\infty}n^{-aq}<\infty}.
\]

::: {.proof}
The inequality \(a>1/q\) is equivalent to
\[
aq>1,
\]
so this is a convergent \(p\)-series.
:::

Let
\[
C=
\left(
\sum_{n=1}^{\infty}n^{-aq}
\right)^{1/q}.
\]

<1>3. For every \(M\ge1\),
\[
\sum_{n=1}^{M}n^{-a}B_n(x)
\le
C
\left(
\sum_{n=1}^{M}B_n(x)^p
\right)^{1/p}.
\]

::: {.proof}
Apply Hölder's inequality to the finite sum with exponents \(q\) and \(p\):
\[
\sum_{n=1}^{M}
n^{-a}B_n
\le
\left(
\sum_{n=1}^{M}n^{-aq}
\right)^{1/q}
\left(
\sum_{n=1}^{M}B_n^p
\right)^{1/p}.
\]
Bound the first factor by \(C\).
:::

<1>4. Letting \(M\to\infty\),
\[
\boxed{
G(x)^p
\le
C^p
\sum_{n=1}^{\infty}B_n(x)^p}.
\]

::: {.proof}
The partial sums on both sides increase with \(M\). Raise step <1>3 to the \(p\)th power and pass to the monotone limit, allowing \(+\infty\).
:::

<1>5. For each \(n\),
\[
\boxed{
B_n(x)^p
\le
\int_0^1
|f(x+n+n^{-a}z)|^p\,dz}.
\]

::: {.proof}
Apply Hölder's inequality on \([0,1]\):
\[
\left(
\int_0^1 h(z)\,dz
\right)^p
\le
\left(
\int_0^1 1^q\,dz
\right)^{p/q}
\int_0^1 h(z)^p\,dz
=
\int_0^1h(z)^p\,dz.
\]
Take
\[
h(z)=|f(x+n+n^{-a}z)|.
\]
:::

<1>6. Hence
\[
\boxed{
G(x)^p
\le
C^p
\sum_{n=1}^{\infty}
\int_0^1
|f(x+n+n^{-a}z)|^p\,dz}.
\]

::: {.proof}
Combine steps <1>4--<1>5.
:::

Now fix an integer \(N\).

<1>7. Tonelli's theorem gives
\[
\begin{aligned}
\int_N^{N+1}G(x)^p\,dx
\le
C^p
\int_0^1
\sum_{n=1}^{\infty}
\int_N^{N+1}
|f(x+n+n^{-a}z)|^p\,dx\,dz.
\end{aligned}
\]

::: {.proof}
Integrate step <1>6 over \([N,N+1]\). All terms are nonnegative, so Tonelli permits interchange of the integral and the infinite sum.
:::

<1>8. For fixed \(n,z\), the change of variables
\[
u=x+n+n^{-a}z
\]
gives
\[
\boxed{
\int_N^{N+1}
|f(x+n+n^{-a}z)|^p\,dx
=
\int_{N+n+n^{-a}z}^{N+1+n+n^{-a}z}
|f(u)|^p\,du}.
\]

::: {.proof}
The change of variables is a translation, so \(du=dx\).
:::

<1>9. Since
\[
a>1-\frac1p>0,
\]
one has
\[
\boxed{
0<n^{-a}\le1}
\]
for every \(n\ge1\).

::: {.proof}
The exponent \(a\) is positive, and \(n\ge1\).
:::

<1>10. Therefore, for \(0\le z\le1\),
\[
\boxed{
[N+n+n^{-a}z,\,
N+1+n+n^{-a}z]
\subseteq
[N+n,\,
N+n+2]}.
\]

::: {.proof}
The left endpoint is at least \(N+n\), and by step <1>9,
\[
1+n^{-a}z\le2.
\]
:::

<1>11. Hence
\[
\int_N^{N+1}
|f(x+n+n^{-a}z)|^p\,dx
\le
\int_{N+n}^{N+n+2}
|f(u)|^p\,du.
\]

::: {.proof}
Use steps <1>8--<1>10 and nonnegativity of the integrand.
:::

<1>12. The intervals
\[
[N+n,N+n+2],
\qquad
n=1,2,\dots,
\]
have overlap multiplicity at most \(2\) almost everywhere.

::: {.proof}
A point \(u\) belongs to such an interval exactly when
\[
u-N-2\le n\le u-N.
\]
This interval of possible integers has length \(2\), so except at endpoints it contains at most two integers. Endpoint coincidences form a null set and do not affect the integral estimate.
:::

<1>13. Consequently,
\[
\boxed{
\sum_{n=1}^{\infty}
\int_{N+n}^{N+n+2}
|f(u)|^p\,du
\le
2\|f\|_{L^p(\mathbb R)}^p}.
\]

::: {.proof}
By Tonelli,
\[
\sum_n
\int_{N+n}^{N+n+2}|f(u)|^p\,du
=
\int_{\mathbb R}
|f(u)|^p
\left(
\sum_n
\mathbf1_{[N+n,N+n+2]}(u)
\right)
du.
\]
The multiplicity factor is at most \(2\) almost everywhere by step <1>12.
:::

<1>14. Combining steps <1>7, <1>11, and <1>13,
\[
\boxed{
\int_N^{N+1}G(x)^p\,dx
\le
2C^p\|f\|_p^p
<
\infty}.
\]

::: {.proof}
The bound in step <1>13 is independent of \(z\), and
\[
\int_0^1dz=1.
\]
:::

<1>15. Therefore
\[
\boxed{
G(x)<\infty
\text{ for almost every }x\in[N,N+1]}.
\]

::: {.proof}
If a nonnegative measurable function has finite \(p\)th power integral on a finite interval, it is finite almost everywhere there.
:::

<1>16. Since
\[
\mathbb R
=
\bigcup_{N\in\mathbb Z}[N,N+1],
\]
one has
\[
\boxed{
G(x)<\infty
\text{ for almost every }x\in\mathbb R}.
\]

::: {.proof}
For each integer \(N\), the exceptional set in \([N,N+1]\) has measure zero by step <1>15. A countable union of null sets is null.
:::

<1>17. Hence, for almost every \(x\),
\[
\boxed{
\sum_{n=1}^{\infty}
\int_n^{n+n^{-a}}
|f(x+y)|\,dy
\text{ converges}.}
\]

::: {.proof}
The series has nonnegative terms, so convergence is equivalent to finiteness of its sum \(G(x)\). Apply step <1>16.
:::

<1>18. Q.E.D.

::: {.proof}
Step <1>17 is the required conclusion.
:::
:::
