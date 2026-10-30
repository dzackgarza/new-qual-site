---
schema: qual/card@1
id: P-6QCZ5
kind: problem
title: Measurability of $f(x)$ and $f(x-y)g(y)$ on $\RR^n\times\RR^n$, and $\norm{f*g}_p\le\norm{g}_1\norm{f}_p$ for $p=1,2,\infty$ when $f\in L^1\cap L^\infty$ and $g\in L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
(a) Prove that if $f, g: \RR^n\to \CC$ are both measurable then $F(x, y) \coloneqq f(x)$ and $h(x, y)\coloneqq f(x-y) g(y)$ are measurable on $\RR^n\cross \RR^n$.

(b) Show that if $f\in L^1(\RR^n) \intersect L^\infty(\RR^n)$ and $g\in L^1(\RR^n)$, then $f\ast g \in L^1(\RR^n) \intersect L^\infty(\RR^n)$ is well defined, and carefully show that it satisfies the following properties:
$$
\begin{aligned}
\norm{f\ast g}_\infty &\leq \norm{g}_1 \norm{f}_\infty, \\
\norm{f\ast g}_1      &\leq \norm{g}_1 \norm{f}_1, \\
\norm{f\ast g}_2      &\leq \norm{g}_1 \norm{f}_2.
\end{aligned}
$$
:::

::: {.hint}
First show $\abs{f\ast g}^2 \leq \norm{g}_1 \qty{ \abs{f}^2 \ast \abs{g}}$.
:::

::: {.solution}
Measurability means Lebesgue measurability; $m$ denotes Lebesgue measure.

::: pf

::: {.pf-step #s1}

$F(x,y) = f(x)$ and $G(x,y) = g(y)$ are measurable on $\RR^n \times \RR^n$.

::: pf-proof

For open $W \subseteq \CC$, $F^{-1}(W) = f^{-1}(W) \times \RR^n$. Write $f^{-1}(W) = V \setminus Z$ with $V$ a $G_\delta$ set and $Z$ null. Then $V \times \RR^n$ is a $G_\delta$ set and $Z \times \RR^n$ is null, so $F^{-1}(W)$ is measurable. The same argument applies to $G$. See [[E-JJ746]].

:::

:::

::: {.pf-step #s2}

$h(x,y) = f(x - y)g(y)$ is measurable.

::: pf-proof

Let $T(x,y) = (x - y, y)$, an invertible linear map of $\RR^{2n}$ with determinant $1$. Then $h = (F \circ T)\cdot G$. For open $W$, $(F\circ T)^{-1}(W) = T^{-1}(F^{-1}(W))$. $T^{-1}$ is a homeomorphism, so it maps $G_\delta$ sets to $G_\delta$ sets, and $m(T^{-1}(A)) = m(A)$ for measurable $A$, so it maps null sets to null sets. Writing $F^{-1}(W)$ as a $G_\delta$ set minus a null set, as in step [](#s1){.pf-ref}, shows $(F\circ T)^{-1}(W)$ is measurable. A product of measurable functions is measurable.

:::

:::

::: {.pf-step #s3}

For $f \in L^1 \cap L^\infty$ and $g \in L^1$, $f\ast g(x) = \int f(x-y)g(y)\,dy$ is defined for every $x$, and $\norm{f \ast g}_\infty \le \norm{g}_1\norm{f}_\infty$.

::: pf-proof

$\int\abs{f(x-y)}\abs{g(y)}\,dy \le \norm{f}_\infty\norm{g}_1 < \infty$ for every $x$.

:::

:::

::: {.pf-step #s4}

$\norm{f \ast g}_1 \le \norm{g}_1\norm{f}_1$.

::: pf-proof

By step [](#s2){.pf-ref} and Tonelli's theorem, $\int\abs{f\ast g(x)}\,dx \le \iint \abs{f(x-y)}\abs{g(y)}\,dy\,dx = \int\abs{g(y)}\int\abs{f(x-y)}\,dx\,dy = \norm{f}_1\norm{g}_1$, using translation invariance of the inner integral.

:::

:::

::: {.pf-step #s5}

$\abs{f \ast g(x)}^2 \le \norm{g}_1\,(\abs{f}^2 \ast \abs{g})(x)$.

::: pf-proof

Write $\abs{f(x-y)g(y)} = \abs{f(x-y)}\,\abs{g(y)}^{1/2}\cdot\abs{g(y)}^{1/2}$. The Cauchy--Schwarz inequality in $y$ gives $\abs{f\ast g(x)}^2 \le \left(\int\abs{f(x-y)}^2\abs{g(y)}\,dy\right)\left(\int\abs{g(y)}\,dy\right)$.

:::

:::

::: {.pf-step #s6}

$\norm{f \ast g}_2 \le \norm{g}_1\norm{f}_2$.

::: pf-proof

$\abs{f}^2 \le \norm{f}_\infty\abs{f}$, so $\abs{f}^2 \in L^1$ with $\norm{\abs{f}^2}_1 = \norm{f}_2^2$. Integrating step [](#s5){.pf-ref} and applying step [](#s4){.pf-ref} to $\abs{f}^2$ and $\abs{g}$ gives $\norm{f \ast g}_2^2 \le \norm{g}_1\,\norm{\abs{f}^2 \ast \abs{g}}_1 \le \norm{g}_1^2\norm{f}_2^2$.

:::

:::

:::

:::
