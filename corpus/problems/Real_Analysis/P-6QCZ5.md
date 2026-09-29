---
schema: qual/card@1
id: P-6QCZ5
kind: problem
title: Measurability of $f(x)$ and $f(x-y)g(y)$ on $\RR^n\times\RR^n$, and $\|f*g\|_p\le\|g\|_1\|f\|_p$
  for $p=1,2,\infty$ when $f\in L^1\cap L^\infty$ and $g\in L^1$
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
a. Prove that if $f, g: \RR^n\to \CC$ is both measurable then $F(x, y) \definedas f(x)$ and $h(x, y)\definedas f(x-y) g(y)$ is measurable on $\RR^n\cross \RR^n$.

b. Show that if $f\in L^1(\RR^n) \intersect L^\infty(\RR^n)$ and $g\in L^1(\RR^n)$, then $f\ast g \in L^1(\RR^n) \intersect L^\infty(\RR^n)$ is well defined, and carefully show that it satisfies the following properties:
\[
\norm{f\ast g}_\infty &\leq \norm{g}_1 \norm{f}_\infty
\norm{f\ast g}_1      &\leq \norm{g}_1 \norm{f}_1
\norm{f\ast g}_2      &\leq \norm{g}_1 \norm{f}_2
.\]

> Hint: first show $\abs{f\ast g}^2 \leq \norm{g}_1 \qty{ \abs{f}^2 \ast \abs{g}}$.
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

For $f \in L^1 \cap L^\infty$ and $g \in L^1$, $f\ast g(x) = \int f(x-y)g(y)\,dy$ is defined for every $x$, and $\|f \ast g\|_\infty \le \|g\|_1\|f\|_\infty$.

::: pf-proof

$\int|f(x-y)||g(y)|\,dy \le \|f\|_\infty\|g\|_1 < \infty$ for every $x$.

:::

:::

::: {.pf-step #s4}

$\|f \ast g\|_1 \le \|g\|_1\|f\|_1$.

::: pf-proof

By step [](#s2){.pf-ref} and Tonelli's theorem, $\int|f\ast g(x)|\,dx \le \iint |f(x-y)||g(y)|\,dy\,dx = \int|g(y)|\int|f(x-y)|\,dx\,dy = \|f\|_1\|g\|_1$, using translation invariance of the inner integral.

:::

:::

::: {.pf-step #s5}

$|f \ast g(x)|^2 \le \|g\|_1\,(|f|^2 \ast |g|)(x)$.

::: pf-proof

Write $|f(x-y)g(y)| = |f(x-y)|\,|g(y)|^{1/2}\cdot|g(y)|^{1/2}$. The Cauchy--Schwarz inequality in $y$ gives $|f\ast g(x)|^2 \le \left(\int|f(x-y)|^2|g(y)|\,dy\right)\left(\int|g(y)|\,dy\right)$.

:::

:::

::: {.pf-step #s6}

$\|f \ast g\|_2 \le \|g\|_1\|f\|_2$.

::: pf-proof

$|f|^2 \le \|f\|_\infty|f|$, so $|f|^2 \in L^1$ with $\||f|^2\|_1 = \|f\|_2^2$. Integrating step [](#s5){.pf-ref} and applying step [](#s4){.pf-ref} to $|f|^2$ and $|g|$ gives $\|f \ast g\|_2^2 \le \|g\|_1\,\||f|^2 \ast |g|\|_1 \le \|g\|_1^2\|f\|_2^2$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are part (a). Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s6){.pf-ref} give $f\ast g \in L^1 \cap L^\infty$ and the three inequalities of part (b).

:::

:::

:::
