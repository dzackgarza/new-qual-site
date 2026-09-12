---
schema: qual/card@1
id: P-RAF05F
kind: problem
title: "Distribution function convergence and integral representation for monotone limits"
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Distribution Functions
  - Monotone Convergence
  - Layer Cake Representation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2005 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a finite measure space, and $0 \leq f_1 \leq f_2 \leq \cdots \leq f$ be nonnegative measurable functions on $X$ with $\lim f_j(x) = f(x)$ for almost every $x \in X$.

(a) Prove that $\mu(f_j^{-1}((r, \infty])) \to \mu(f^{-1}((r, \infty)))$ as $j \to \infty$ for every $r \geq 0$, $r \in \mathbb{R}$.

(b) Prove that $\int_X f \, d\mu = \int_0^\infty \mu(f^{-1}((r, \infty))) \, dr$.
:::

::: solution
<1>1. Prove convergence of the distribution functions.
::: proof
Fix $r\ge0$ and set
\[
E_j:=\{x\in X:f_j(x)>r\},
\qquad
E:=\{x\in X:f(x)>r\}.
\]
Since $f_j\le f_{j+1}$, the sets $E_j$ are increasing. Also $E_j\subseteq E$ because $f_j\le f$.

Let
\[
N:=\{x:f_j(x)\not\to f(x)\}.
\]
Then $\mu(N)=0$. If $x\in E\setminus N$, then $f(x)>r$ and $f_j(x)\to f(x)$, so $f_j(x)>r$ for all sufficiently large $j$. Hence
\[
E\setminus N\subseteq\bigcup_{j=1}^\infty E_j\subseteq E.
\]
Therefore
\[
\mu\!\left(\bigcup_{j=1}^\infty E_j\right)=\mu(E).
\]
By continuity from below,
\[
\mu(E_j)\longrightarrow\mu(E),
\]
that is,
\[
\boxed{
\mu(f_j^{-1}((r,\infty]))
\longrightarrow
\mu(f^{-1}((r,\infty])).}
\]
:::

<1>2. Write $f$ as an integral of its superlevel indicators.
::: proof
For every $x\in X$,
\[
f(x)=\int_0^\infty \mathbf1_{\{r<f(x)\}}\,dr.
\]
Indeed, if $f(x)=a<\infty$, the integrand is the indicator of $(0,a)$; if $f(x)=\infty$, the integral is infinite.
:::

<1>3. Apply Tonelli's theorem.
::: proof
The function
\[
(x,r)\longmapsto \mathbf1_{\{r<f(x)\}}
\]
is nonnegative and measurable on $X\times[0,\infty)$. Therefore Tonelli's theorem gives
\[
\begin{aligned}
\int_X f(x)\,d\mu(x)
&=\int_X\int_0^\infty \mathbf1_{\{r<f(x)\}}\,dr\,d\mu(x)\\
&=\int_0^\infty\int_X \mathbf1_{\{f(x)>r\}}\,d\mu(x)\,dr\\
&=\int_0^\infty \mu(f^{-1}((r,\infty]))\,dr.
\end{aligned}
\]
Thus
\[
\boxed{
\int_X f\,d\mu
=\int_0^\infty \mu(f^{-1}((r,\infty]))\,dr.}
\]
:::
:::
