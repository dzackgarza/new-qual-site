---
schema: qual/card@1
id: P-ZOTXG
kind: problem
title: $L^1$ convolution with a bounded measurable function is bounded and uniformly
  continuous, and $(f*g)'=f*g'$ when $g'$ is bounded
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Spring 2015 Problem 6 in the preserved UGA real-analysis source extraction.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the sign in the translation identity used for uniform continuity.
---

::: problem
Let $f \in L^1(\RR)$ and $g$ be a bounded measurable function on $\RR$.

1. Show that the convolution $f\ast g$ is well-defined, bounded, and uniformly continuous on $\RR$.

2. Prove that one further assumes that $g \in C^1(\RR)$ with bounded derivative, then $f\ast g \in C^1(\RR)$ and
\[
\frac{d}{d x}(f * g)=f *\left(\frac{d}{d x} g\right)
\]
:::
::: solution
<1>1. The convolution is well defined and bounded.
::: proof
Let $M:=\|g\|_\infty$. For every $x\in\mathbb R$,
\[
\int_{\mathbb R}|f(y)g(x-y)|\,dy
\le M\|f\|_1<\infty.
\]
Thus $(f*g)(x)$ is absolutely convergent and
\[
\|f*g\|_\infty\le M\|f\|_1.
\]
:::

<1>2. The convolution is uniformly continuous.
::: proof
For $h\in\mathbb R$, a change of variables gives
\[
(f*g)(x+h)
=\int_{\mathbb R} f(y+h)g(x-y)\,dy.
\]
Hence
\[
(f*g)(x+h)-(f*g)(x)
=\int_{\mathbb R}\bigl(f(y+h)-f(y)\bigr)g(x-y)\,dy,
\]
and therefore
\[
|(f*g)(x+h)-(f*g)(x)|
\le M\|\tau_{-h}f-f\|_1.
\]
Translations are strongly continuous on $L^1(\mathbb R)$, so the right-hand side tends to $0$ as $h\to0$, independently of $x$. Thus $f*g$ is uniformly continuous.
:::

<1>3. Differentiate when $g\in C^1$ and $g'$ is bounded.
::: proof
For $h\ne0$,
\[
\frac{(f*g)(x+h)-(f*g)(x)}h
=\int_{\mathbb R}f(y)
\frac{g(x+h-y)-g(x-y)}h\,dy.
\]
For each fixed $y$, the difference quotient converges to $g'(x-y)$. By the mean value theorem it is bounded in absolute value by $\|g'\|_\infty$. Since $f\in L^1$, dominated convergence yields
\[
\frac d{dx}(f*g)(x)
=\int_{\mathbb R}f(y)g'(x-y)\,dy
=(f*g')(x).
\]
Finally, $g'$ is bounded and measurable, so Step 2 applied to $(f,g')$ shows that $f*g'$ is uniformly continuous. Hence $f*g\in C^1(\mathbb R)$ and
\[
\boxed{(f*g)'=f*g'.}
\]
:::
:::
