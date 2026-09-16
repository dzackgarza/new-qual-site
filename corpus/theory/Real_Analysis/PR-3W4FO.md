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
$$
\frac1p+\frac1q=1.
$$
If $f\in L^p(\RR^d)$ and $g\in L^q(\RR^d)$, then the [[D-TS42Y|convolution]]
$$
(f*g)(x)\coloneqq\int_{\RR^d}f(x-y)g(y)\,dy
$$
converges absolutely for every $x\in\RR^d$, satisfies
$$
\sup_{x\in\RR^d}\abs{(f*g)(x)}\le \norm{f}_p\norm{g}_q,
$$
and is [[D-HHVPT|uniformly continuous]] on $\RR^d$.
:::

::: {.proof}
For every $x\in\RR^d$, the function $y\mapsto f(x-y)$ is measurable with $\norm{f(x-\cdot)}_p=\norm{f}_p$ by invariance of Lebesgue measure under $y\mapsto x-y$.
Hölder's inequality gives
$$
\int_{\RR^d}\abs{f(x-y)g(y)}\,dy \le \norm{f(x-\cdot)}_p\norm{g}_q=\norm{f}_p\norm{g}_q,
$$
so the integral converges absolutely and $\abs{(f*g)(x)}\le\norm{f}_p\norm{g}_q$.

Suppose first that $p<\infty$.
For $h\in\RR^d$ and every $x$, Hölder's inequality and the same invariance give
$$
\abs{(f*g)(x+h)-(f*g)(x)}
\le \norm{f(\,\cdot+h)-f}_p\,\norm{g}_q .
$$
Translation is continuous in $L^p(\RR^d)$ for $1\le p<\infty$, so the right-hand side, which does not depend on $x$, tends to $0$ as $h\to0$.
Hence $f*g$ is uniformly continuous.

If $p=\infty$, then $q=1$.
The substitution $y\mapsto x-y$ gives
$$
(f*g)(x)=\int_{\RR^d}f(y)g(x-y)\,dy,
$$
so
$$
\abs{(f*g)(x+h)-(f*g)(x)}
\le \norm{f}_\infty\,\norm{g(\,\cdot+h)-g}_1
$$
for every $x$, and $\norm{g(\,\cdot+h)-g}_1\to0$ as $h\to0$ by [[FR-EM6AL|continuity of translation in $L^1$]].
Hence $f*g$ is uniformly continuous in this case as well.
:::
