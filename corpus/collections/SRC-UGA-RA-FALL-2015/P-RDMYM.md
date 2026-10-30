---
schema: qual/card@1
id: P-RDMYM
kind: problem
title: Borel measurability of $f(x-y)g(y)$ and Young's inequality $\norm{f*g}_1\le\norm{f}_1\norm{g}_1$
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

(a) Show that the function
$$
F(x, y) \coloneqq f(x-y) g(y)
$$
is Borel measurable on $\RR^2$, and that for almost every $x\in \RR$ the function $y\mapsto f(x-y)g(y)$ is integrable on $\RR$.

(b) Define $(f\ast g)(x)=\int_\RR f(x-y)g(y)\,dy$. Show that $f\ast g \in L^1(\RR)$ and
$$
\norm{f * g}_{1} \leq \norm{f}_{1} \norm{g}_{1}.
$$
:::

::: {.solution}

::: pf

::: pf-step

Prove measurability on $\RR^2$.

::: pf-proof

The maps
$$
S:\RR^2\to\RR,
\qquad S(x,y)=x-y,
$$
and
$$
\pi_2:\RR^2\to\RR,
\qquad \pi_2(x,y)=y,
$$
are continuous. Since $f$ and $g$ are Borel measurable, so are
$$
(x,y)\mapsto f(x-y)=f\circ S(x,y)
$$
and
$$
(x,y)\mapsto g(y)=g\circ\pi_2(x,y).
$$
Their product
$$
F(x,y)=f(x-y)g(y)
$$
is therefore Borel measurable on $\RR^2$.

:::

:::

::: pf-step

Show that the absolute-value kernel is integrable on $\RR^2$.

::: pf-proof

The function
$$
(x,y)\mapsto \abs{f(x-y)}\,\abs{g(y)}
$$
is nonnegative and measurable. Tonelli's theorem therefore applies without any prior integrability assumption and gives
$$
\begin{aligned}
\int_{\RR^2}\abs{f(x-y)}\,\abs{g(y)}\,dx\,dy
&=\int_{\RR}\abs{g(y)}
   \left(\int_{\RR}\abs{f(x-y)}\,dx\right)dy\\
&=\int_{\RR}\abs{g(y)}\,\norm{f}_1\,dy\\
&=\norm{f}_1\norm{g}_1<\infty,
\end{aligned}
$$
where translation invariance of Lebesgue measure gives
$$
\int_{\RR}\abs{f(x-y)}\,dx=\norm{f}_1.
$$
Thus $F\in L^1(\RR^2)$.

:::

:::

::: pf-step

Obtain almost-everywhere existence of the convolution slices.

::: pf-proof

Since $\abs{F}\in L^1(\RR^2)$, Fubini's theorem implies that for almost every $x\in\RR$,
$$
\int_{\RR}\abs{f(x-y)g(y)}\,dy<\infty.
$$
Hence for almost every $x$ the convolution integral
$$
(f*g)(x)=\int_{\RR}f(x-y)g(y)\,dy
$$
is absolutely convergent.

:::

:::

::: pf-step

Prove Young's $L^1$ inequality.

::: pf-proof

For every $x$ for which the convolution integral exists,
$$
\abs{(f*g)(x)}
\le \int_{\RR}\abs{f(x-y)}\,\abs{g(y)}\,dy.
$$
Integrating in $x$ and using Tonelli together with Step 2,
$$
\begin{aligned}
\norm{f*g}_1
&\le \int_{\RR}\int_{\RR}
\abs{f(x-y)}\,\abs{g(y)}\,dy\,dx\\
&=\norm{f}_1\norm{g}_1.
\end{aligned}
$$
Therefore $f*g\in L^1(\RR)$ and
$$
\boxed{\norm{f*g}_1\le \norm{f}_1\norm{g}_1.}
$$

:::

:::

:::

:::
