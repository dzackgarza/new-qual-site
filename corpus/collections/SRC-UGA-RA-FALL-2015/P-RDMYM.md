---
schema: qual/card@1
id: P-RDMYM
kind: problem
title: Borel measurability of $f(x-y)g(y)$ and Young's inequality $\|f*g\|_1\le\|f\|_1\|g\|_1$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 5 of the UGA Fall 2015 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced an incorrect linear map in the measurability argument and removed a circular use of Fubini-Tonelli.
---

::: {.problem}
Let $f, g \in L^1(\RR)$ be Borel measurable.

- Show that 
  - The function $$F(x, y) \definedas f(x-y) g(y)$$ is Borel measurable on $\RR^2$, and
  - For almost every $x\in \RR$, the function $f(x-y)g(y)$ is integrable with respect to $y$ on $\RR$.

- Show that $f\ast g \in L^1(\RR)$ and
\[
\|f * g\|_{1} \leq \|f\|_{1} \|g\|_{1}
\]
:::

::: {.solution}
<1>1. Prove measurability on $\mathbb R^2$.
::: {.proof}
The maps
\[
S:\mathbb R^2\to\mathbb R,
\qquad S(x,y)=x-y,
\]
and
\[
\pi_2:\mathbb R^2\to\mathbb R,
\qquad \pi_2(x,y)=y,
\]
are continuous. Since $f$ and $g$ are Borel measurable, so are
\[
(x,y)\mapsto f(x-y)=f\circ S(x,y)
\]
and
\[
(x,y)\mapsto g(y)=g\circ\pi_2(x,y).
\]
Their product
\[
F(x,y)=f(x-y)g(y)
\]
is therefore Borel measurable on $\mathbb R^2$.
:::

<1>2. Show that the absolute-value kernel is integrable on $\mathbb R^2$.
::: {.proof}
The function
\[
(x,y)\mapsto |f(x-y)|\,|g(y)|
\]
is nonnegative and measurable. Tonelli's theorem therefore applies without any prior integrability assumption and gives
\[
\begin{aligned}
\int_{\mathbb R^2}|f(x-y)|\,|g(y)|\,dx\,dy
&=\int_{\mathbb R}|g(y)|
   \left(\int_{\mathbb R}|f(x-y)|\,dx\right)dy\\
&=\int_{\mathbb R}|g(y)|\,\|f\|_1\,dy\\
&=\|f\|_1\|g\|_1<\infty,
\end{aligned}
\]
where translation invariance of Lebesgue measure gives
\[
\int_{\mathbb R}|f(x-y)|\,dx=\|f\|_1.
\]
Thus $F\in L^1(\mathbb R^2)$.
:::

<1>3. Obtain almost-everywhere existence of the convolution slices.
::: {.proof}
Since $|F|\in L^1(\mathbb R^2)$, Fubini's theorem implies that for almost every $x\in\mathbb R$,
\[
\int_{\mathbb R}|f(x-y)g(y)|\,dy<\infty.
\]
Hence for almost every $x$ the convolution integral
\[
(f*g)(x)=\int_{\mathbb R}f(x-y)g(y)\,dy
\]
is absolutely convergent.
:::

<1>4. Prove Young's $L^1$ inequality.
::: {.proof}
For every $x$ for which the convolution integral exists,
\[
|(f*g)(x)|
\le \int_{\mathbb R}|f(x-y)|\,|g(y)|\,dy.
\]
Integrating in $x$ and using Tonelli together with Step 2,
\[
\begin{aligned}
\|f*g\|_1
&\le \int_{\mathbb R}\int_{\mathbb R}
|f(x-y)|\,|g(y)|\,dy\,dx\\
&=\|f\|_1\|g\|_1.
\end{aligned}
\]
Therefore $f*g\in L^1(\mathbb R)$ and
\[
\boxed{\|f*g\|_1\le \|f\|_1\|g\|_1.}
\]
:::
:::
