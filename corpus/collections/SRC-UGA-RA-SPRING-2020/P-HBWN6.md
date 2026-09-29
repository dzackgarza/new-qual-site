---
schema: qual/card@1
id: P-HBWN6
kind: problem
title: $f(y)g(x-y)\in L^1(\RR^2)$ and $\|f*g\|_1\le\|f\|_1\|g\|_1$ for $f,g\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Fubini-Tonelli
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 3 of the UGA Spring 2020 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Reordered the argument so measurability and Tonelli are established before any iterated-integral computation.
---

::: {.problem}
Let $f, g\in L^1(\RR)$. 
Argue that $H(x, y) \definedas f(y) g(x-y)$ defines a function in $L^1(\RR^2)$ and deduce from this fact that
\[
(f\ast g)(x) \definedas \int_\RR f(y) g(x-y) \,dy
\]
defines a function in $L^1(\RR)$ that satisfies 
\[
\norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1
.\]
:::

::: {.strategy}
Tonelli's theorem applied to the nonnegative measurable function $\abs{H}$ gives $\norm{H}_{L^1(\RR^2)}=\norm{f}_1\norm{g}_1$.
Fubini's theorem applied to $H$ then shows that $f\ast g$ is defined almost everywhere and bounds its $L^1$ norm.
:::

::: {.concept}
\envlist
- Tonelli: non-negative and measurable yields measurability of slices and equality of iterated integrals
- Fubini: $f(x, y) \in L^1$ yields *integrable* slices and equality of iterated integrals
- F/T: apply Tonelli to $\abs{f}$; if finite, $f\in L^1$ and apply Fubini to $f$ [@Fol13, Theorem 2.37].
:::

::: {.solution}

::: pf

::: {.pf-step #h-measurable}
Prove that $H$ is measurable.

::: pf-proof
The maps
\[
(x,y)\mapsto y
\qquad\text{and}\qquad
(x,y)\mapsto x-y
\]
are continuous. Since $f$ and $g$ are measurable, the functions
\[
(x,y)\mapsto f(y)
\qquad\text{and}\qquad
(x,y)\mapsto g(x-y)
\]
are measurable. Their product
\[
H(x,y)=f(y)g(x-y)
\]
is therefore measurable on $\mathbb R^2$.
:::

:::

::: {.pf-step #h-in-l1}
Prove that $H\in L^1(\mathbb R^2)$.

::: pf-proof
Since $|H|$ is nonnegative and measurable, Tonelli's theorem applies directly:
\[
\begin{aligned}
\int_{\mathbb R^2}|H(x,y)|\,dx\,dy
&=\int_{\mathbb R}|f(y)|
  \left(\int_{\mathbb R}|g(x-y)|\,dx\right)dy\\
&=\int_{\mathbb R}|f(y)|\,\|g\|_1\,dy\\
&=\|f\|_1\|g\|_1<\infty.
\end{aligned}
\]
Hence $H\in L^1(\mathbb R^2)$.
:::

:::

::: {.pf-step #convolution-bound}
Deduce the $L^1$ convolution bound.

::: pf-proof
By Fubini's theorem, for almost every $x$ the slice $y\mapsto H(x,y)$ is integrable, so
\[
(f*g)(x)=\int_{\mathbb R}H(x,y)\,dy
\]
is defined for almost every $x$. Moreover,
\[
|(f*g)(x)|
\le \int_{\mathbb R}|H(x,y)|\,dy.
\]
Integrating in $x$ and using Tonelli,
\[
\begin{aligned}
\|f*g\|_1
&\le \int_{\mathbb R}\int_{\mathbb R}|H(x,y)|\,dy\,dx\\
&=\|f\|_1\|g\|_1.
\end{aligned}
\]
Thus
\[
\boxed{f*g\in L^1(\mathbb R),\qquad
\|f*g\|_1\le\|f\|_1\|g\|_1.}
\]
:::

:::

::: pf-qed
Steps [](#h-measurable){.pf-ref} and [](#h-in-l1){.pf-ref} show $H\in L^1(\mathbb R^2)$, and step [](#convolution-bound){.pf-ref} deduces that $f*g\in L^1(\mathbb R)$ with $\|f*g\|_1\le\|f\|_1\|g\|_1$.
:::

:::

:::

