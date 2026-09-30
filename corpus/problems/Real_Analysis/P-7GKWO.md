---
schema: qual/card@1
id: P-7GKWO
kind: problem
title: Continuity of $d(x,F)$ and finiteness of $\int\delta(y)/|x-y|^2\,dy$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Matched SRC-MATH8100-ASSIGNMENT-5/P-M81A5-E2; the source assumes F is closed.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: {.problem}
Suppose $F \subseteq \RR$ is closed with $m(F^c) < \infty$ and let \( \delta(x) \definedas d(x, F) \) and
\[
I_F(x) \definedas \int_\RR { \delta(y) \over \abs{x-y}^2 } \dy
.\]

a. Show that \( \delta \) is continuous.

b. Show that if $x\in F^c$ then $I_F(x) = \infty$.

c. Show that $I_F(x) < \infty$ for almost every $x\in F$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $\delta(x)=d(x,F)$ is $1$-Lipschitz, hence continuous.

::: pf-proof

For $x,x'\in\RR$ and every $z\in F$, the triangle inequality gives
\[
d(x,z)\le |x-x'|+d(x',z).
\]
Taking the infimum over $z\in F$ yields
\[
\delta(x)\le |x-x'|+\delta(x').
\]
Interchanging $x$ and $x'$ gives
\[
|\delta(x)-\delta(x')|\le |x-x'|.
\]

:::

:::

::: pf-step

If $x\in F^c$, then $I_F(x)=\infty$.

::: pf-proof

Because $F$ is closed, $F^c$ is open, so
\[
r\definedas\delta(x)=d(x,F)>0.
\]
By step [](#s1){.pf-ref}, whenever $|y-x|<r/2$,
\[
\delta(y)\ge \delta(x)-|x-y|>r/2.
\]
Therefore
\[
I_F(x)
\ge {r\over2}\int_{x-r/2}^{x+r/2}{dy\over|x-y|^2}
=\infty.
\]

:::

:::

::: {.pf-step #s3}

For every $y\in F^c$,
\[
\int_F {dx\over|x-y|^2}\le {2\over\delta(y)}.
\]

::: pf-proof

If $y\in F^c$, then $\delta(y)>0$ because $F$ is closed. By the definition of distance,
\[
|x-y|\ge\delta(y)
\qquad\text{for every }x\in F.
\]
Hence, after translating by $y$,
\[
\int_F {dx\over|x-y|^2}
\le \int_{|t|\ge\delta(y)}{dt\over t^2}
={2\over\delta(y)}.
\]

:::

:::

::: {.pf-step #s4}

The function $I_F$ is integrable over $F$ and
\[
\int_F I_F(x)\,dx\le 2m(F^c).
\]

::: pf-proof

Define the value on the diagonal $x=y$ to be $0$; this changes no integral. The integrand is then nonnegative and measurable, so Tonelli's theorem gives
\[
\begin{aligned}
\int_F I_F(x)\,dx
&=\int_F\int_\RR {\delta(y)\over|x-y|^2}\,dy\,dx\\
&=\int_\RR\left(\int_F{\delta(y)\over|x-y|^2}\,dx\right)dy.
\end{aligned}
\]
For $y\in F$, the inner integrand is $0$ almost everywhere in $x$, so its integral is $0$. For $y\in F^c$, step [](#s3){.pf-ref} gives
\[
\int_F{\delta(y)\over|x-y|^2}\,dx
=\delta(y)\int_F{dx\over|x-y|^2}\le2.
\]
Thus
\[
\int_F I_F(x)\,dx
\le\int_{F^c}2\,dy
=2m(F^c)<\infty.
\]

:::

:::

::: pf-step

$I_F(x)<\infty$ for almost every $x\in F$.

::: pf-proof

By step [](#s4){.pf-ref}, the nonnegative measurable function $I_F|_F$ has finite integral. Therefore it is finite almost everywhere on $F$.

:::

:::

:::

:::
