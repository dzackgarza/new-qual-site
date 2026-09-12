---
schema: qual/card@1
id: P-RASP15A
kind: problem
title: "True/false on weak convergence, Fubini, L^p membership, and limit of integrals"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if the statements below are True or False.

(a) (10 points) In an infinite-dimensional Hilbert space $H$, for any weakly convergent sequence $\{x_n\}$, there exists a subsequence that is convergent with respect to the norm.

(b) (10 points) Since two iterated integrals exist and
$$
\int_{(0,1)} \int_{(0,1)} \frac{x^2 - y^2}{(x^2 + y^2)^2}\,dm(x)\,dm(y) = \int_{(0,1)} \int_{(0,1)} \frac{x^2 - y^2}{(x^2 + y^2)^2}\,dm(y)\,dm(x)
$$
we can conclude, via the Tonelli-Fubini theorem, that the double integral exists.

(c) (10 points) There exists a function $f \geq 0$ on $(0, \infty)$ such that $f \in L^p((0, \infty))$ if and only if $p = 1$.

(d) (10 points)
$$
\lim_{n \to \infty} \int_0^\infty \frac{\sin(x/n)}{(1 + x/n)^n}\,dm(x) = 0.
$$
:::

::: solution
<1>1. Part (a) is false.
::: proof
Let $H$ be an infinite-dimensional Hilbert space and choose an orthonormal sequence $(e_n)$. Then
\[
e_n\rightharpoonup0
\]
weakly: for every $x\in H$, Bessel's inequality implies
\[
\sum_n|\langle x,e_n\rangle|^2<\infty,
\]
so $\langle x,e_n\rangle\to0$.

However, for $m\ne n$,
\[
\|e_n-e_m\|^2=2.
\]
Thus no subsequence is even norm-Cauchy, hence no subsequence converges in norm.
:::

<1>2. Part (b) is false.
::: proof
Let
\[
F(x,y)=\frac{x^2-y^2}{(x^2+y^2)^2}.
\]
For fixed $y>0$,
\[
F(x,y)=-\frac{d}{dx}\left(\frac{x}{x^2+y^2}\right),
\]
so
\[
\int_0^1F(x,y)\,dx=-\frac1{1+y^2}.
\]
Hence
\[
\int_0^1\int_0^1F(x,y)\,dx\,dy
=-\int_0^1\frac{dy}{1+y^2}
=-\frac\pi4.
\]

For fixed $x>0$,
\[
F(x,y)=\frac{d}{dy}\left(\frac{y}{x^2+y^2}\right),
\]
so
\[
\int_0^1F(x,y)\,dy=\frac1{1+x^2}
\]
and therefore
\[
\int_0^1\int_0^1F(x,y)\,dy\,dx
=\frac\pi4.
\]
Thus the two iterated integrals are not equal. In particular the asserted Tonelli--Fubini conclusion is false; indeed $F$ is not absolutely integrable near $(0,0)$.
:::

<1>3. Part (c) is true.
::: proof
Define
\[
f(x)=
\begin{cases}
\dfrac1{x(\log(1/x))^2},&0<x<e^{-1},\\[6pt]
\dfrac1{x(\log x)^2},&x>e,\\[6pt]
0,&e^{-1}\le x\le e.
\end{cases}
\]
Then $f\ge0$. With the substitutions $u=\log(1/x)$ near $0$ and $u=\log x$ near infinity,
\[
\int_0^{e^{-1}}f(x)\,dx
=\int_1^\infty\frac{du}{u^2}<\infty,
\qquad
\int_e^\infty f(x)\,dx
=\int_1^\infty\frac{du}{u^2}<\infty.
\]
Thus $f\in L^1(0,\infty)$.

If $p>1$, then near $0$ the factor $x^{-p}$ makes
\[
\int_0^{e^{-1}}f(x)^p\,dx=\infty.
\]
If $0<p<1$, then at infinity
\[
\int_e^\infty f(x)^p\,dx=\infty
\]
because the power $x^{-p}$ is not integrable there. Also $f$ is unbounded, so $f\notin L^\infty$. Hence among all $0<p\le\infty$, the function belongs to $L^p$ exactly when $p=1$.
:::

<1>4. Part (d) is true.
::: proof
Using $|\sin t|\le t$ for $t\ge0$, for $n>2$ we obtain
\[
\begin{aligned}
\left|\int_0^\infty\frac{\sin(x/n)}{(1+x/n)^n}\,dx\right|
&\le \frac1n\int_0^\infty\frac{x}{(1+x/n)^n}\,dx\\
&=n\int_0^\infty\frac{t}{(1+t)^n}\,dt.
\end{aligned}
\]
The last integral equals
\[
\int_0^\infty\frac{t}{(1+t)^n}\,dt
=\frac1{(n-1)(n-2)}.
\]
Therefore
\[
\left|\int_0^\infty\frac{\sin(x/n)}{(1+x/n)^n}\,dx\right|
\le\frac{n}{(n-1)(n-2)}\longrightarrow0.
\]
Hence the stated limit is $0$.
:::
:::
