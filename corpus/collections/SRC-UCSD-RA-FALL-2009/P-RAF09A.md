---
schema: qual/card@1
id: P-RAF09A
kind: problem
title: "True/false on convergence, Fubini, measurability, and weak compactness"
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
  note: Checked against Problem 1 of the official UCSD Fall 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample (or prove your assertion in another way, if you prefer).

(a) Let $(X, \mathcal{M}, \mu)$ be a complete measure space.
If $f_n, g_n, g, f \in L^1$, $f_n \to f$ and $g_n \to g$ a.e., $|f_n| \leq g_n$ and $\int g_n\,d\mu = A < \infty$ for some $A > 0$, then $\int f_n\,d\mu \to \int f\,d\mu$.

(b) The iterated integrals
$$
\int_{-1}^{1} \left[\int_{-1}^{1} \frac{xy}{(x^2+y^2)^2}\,dx\right]dy = \int_{-1}^{1} \left[\int_{-1}^{1} \frac{xy}{(x^2+y^2)^2}\,dy\right]dx.
$$
Hence by the Fubini-Tonelli theorem $\frac{xy}{(x^2+y^2)^2}$ is (Lebesgue) integrable on $[-1,1] \times [-1,1]$.

(c) Assume that $f$ is a continuous real-valued function on $\mathbb{R}$ and $g$ is Lebesgue measurable, then $f > g$ is Lebesgue measurable.

(d) Let $X$ be an infinite-dimensional Banach space.
Then every nonempty weak*-open set in $X^*$ is unbounded with respect to the induced norm.

(e) A bounded sequence in a Hilbert space contains a weakly convergent subsequence.
:::

::: solution
<1>1. Part (a) is false.
::: proof
Take $X=\mathbb R$ with Lebesgue measure and let
\[
g_n=f_n=\mathbf1_{[n,n+1]}.
\]
Then $f_n,g_n\in L^1$, $|f_n|\le g_n$, and
\[
\int_{\mathbb R}g_n\,dx=1
\]
for every $n$. Moreover, for every fixed $x\in\mathbb R$,
\[
f_n(x)=g_n(x)\longrightarrow0,
\]
so $f=g=0$ almost everywhere. However
\[
\int f_n\,dx=1\not\longrightarrow0=\int f\,dx.
\]
Thus the assertion is false.
:::

<1>2. Part (b) is false.
::: proof
Let
\[
F(x,y)=\frac{xy}{(x^2+y^2)^2}
\]
away from the origin and define $F(0,0)=0$. For each fixed $y\ne0$, the function $x\mapsto F(x,y)$ is integrable on $[-1,1]$ and odd, so
\[
\int_{-1}^1F(x,y)\,dx=0.
\]
The same holds with $x$ and $y$ interchanged. Hence both iterated integrals exist and equal $0$.

Nevertheless $F$ is not integrable on the square. In polar coordinates near the origin,
\[
|F(r\cos\theta,r\sin\theta)|
=\frac{|\cos\theta\sin\theta|}{r^2}.
\]
Thus on any angular sector on which $|\cos\theta\sin\theta|$ is bounded below by a positive constant,
\[
\iint |F|\,dx\,dy
\gtrsim \int_0^\varepsilon \frac1{r^2}r\,dr
=\int_0^\varepsilon\frac{dr}{r}
=\infty.
\]
So equality of the two iterated integrals does not justify an application of Fubini--Tonelli here.
:::

<1>3. Part (c) is true.
::: proof
The function $f$ is continuous, hence Lebesgue measurable. Since $g$ is measurable, $f-g$ is measurable. Therefore
\[
\{x:f(x)>g(x)\}
=\{x:(f-g)(x)>0\}
\]
is Lebesgue measurable.
:::

<1>4. Part (d) is true.
::: proof
Let $U\subset X^*$ be a nonempty weak*-open set and choose $\phi_0\in U$. There exist $x_1,\dots,x_N\in X$ and $\varepsilon>0$ such that
\[
V:=\{\phi\in X^*:|\phi(x_j)-\phi_0(x_j)|<\varepsilon\text{ for }1\le j\le N\}
\subset U.
\]
Put
\[
M=\operatorname{span}\{x_1,\dots,x_N\}.
\]
Since $X$ is infinite dimensional, $M\ne X$. By Hahn--Banach there is a nonzero functional $\psi\in X^*$ such that
\[
\psi|_M=0.
\]
Hence for every scalar $t$,
\[
(\phi_0+t\psi)(x_j)=\phi_0(x_j),
\]
so $\phi_0+t\psi\in V\subset U$. But
\[
\|\phi_0+t\psi\|\ge |t|\,\|\psi\|-\|\phi_0\|\longrightarrow\infty
\]
as $|t|\to\infty$. Thus every nonempty weak*-open subset of $X^*$ is norm-unbounded.
:::

<1>5. Part (e) is true.
::: proof
Hilbert spaces are reflexive. Hence every closed bounded ball is weakly compact. By the Eberlein--Smulian theorem, weak compactness in a Banach space is equivalent to weak sequential compactness. Therefore every bounded sequence in a Hilbert space has a weakly convergent subsequence.
:::
:::
