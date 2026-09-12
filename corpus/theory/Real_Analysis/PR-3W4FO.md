---
schema: qual/card@1
id: PR-3W4FO
kind: proposition
title: Convolution of Hölder-conjugate $L^p$ functions is bounded and uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - Lp Spaces
relations: []
review: draft
---

::: {.proposition}
Let $1\le p,q\le\infty$ satisfy
\[
\frac1p+\frac1q=1.
\]
If $f\in L^p(\mathbb R^d)$ and $g\in L^q(\mathbb R^d)$, then
\[
(f*g)(x):=\int_{\mathbb R^d}f(x-y)g(y)\,dy
\]
is defined for every $x$ after choosing measurable representatives, satisfies
\[
\|f*g\|_\infty\le \|f\|_p\|g\|_q,
\]
and has a bounded uniformly continuous representative.
:::

::: {.proof}
For every $x\in\mathbb R^d$, Hölder's inequality and translation invariance give
\[
\begin{aligned}
|(f*g)(x)|
&\le \|f(x-\cdot)\|_p\|g\|_q\\
&=\|f\|_p\|g\|_q.
\end{aligned}
\]
Thus the convolution is absolutely defined for every $x$ for any fixed representatives for which the translated functions are measurable, and
\[
\|f*g\|_\infty\le\|f\|_p\|g\|_q.
\]

Suppose first that $p<\infty$. For $h\in\mathbb R^d$,
\[
\begin{aligned}
|(f*g)(x+h)-(f*g)(x)|
&\le \|f(\,\cdot+h)-f\|_p\,\|g\|_q,
\end{aligned}
\]
uniformly in $x$. Translation is continuous in $L^p(\mathbb R^d)$ for $1\le p<\infty$, so the right-hand side tends to $0$ as $h\to0$. Hence $f*g$ is uniformly continuous.

If $p=\infty$, then $q=1$. Rewriting the convolution as
\[
(f*g)(x)=\int_{\mathbb R^d}f(y)g(x-y)\,dy
\]
gives instead
\[
|(f*g)(x+h)-(f*g)(x)|
\le \|f\|_\infty\,\|g(\,\cdot+h)-g\|_1,
\]
again uniformly in $x$, and the $L^1$ translation norm tends to $0$.

Therefore $f*g$ is bounded and uniformly continuous in all conjugate-exponent cases.
:::
