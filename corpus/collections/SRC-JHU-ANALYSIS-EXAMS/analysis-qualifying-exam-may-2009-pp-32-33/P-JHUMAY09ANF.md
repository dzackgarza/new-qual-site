---
schema: qual/card@1
id: P-JHUMAY09ANF
kind: problem
title: "Uniform convergence for an approximation to the identity on the circle"
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, May 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(K_n)$ be nonnegative integrable functions on $\mathbb R/\mathbb Z$ such that
\[
\int K_n=1
\]
and for every $0<\varepsilon<1/2$,
\[
\int_{\varepsilon\le |t|\le1/2}K_n(t)\,dt\longrightarrow0.
\]
For continuous $f$ on $\mathbb R/\mathbb Z$, prove that $f*K_n\to f$ uniformly.
:::

::: {.solution}
<1>1. The contribution from $|t|<\delta$ can be made uniformly small.
::: {.proof}
Fix $\eta>0$. Since $f$ is continuous on the compact circle, it is uniformly continuous. Choose $0<\delta<1/2$ so that
$$
|f(x-t)-f(x)|<\frac{\eta}{2}
\qquad(|t|<\delta)
$$
for every $x$. Since $K_n\ge0$ and $\int K_n=1$,
$$
\int_{|t|<\delta}|f(x-t)-f(x)|K_n(t)\,dt
\le\frac\eta2
$$
uniformly in $x$ and $n$.
:::

<1>2. The contribution from $\delta\le|t|\le1/2$ tends uniformly to zero.
::: {.proof}
For every $x$ and $t$,
$$
|f(x-t)-f(x)|\le2\|f\|_\infty.
$$
Therefore
$$
\int_{\delta\le|t|\le1/2}|f(x-t)-f(x)|K_n(t)\,dt
\le
2\|f\|_\infty
\int_{\delta\le|t|\le1/2}K_n(t)\,dt.
$$
The last integral tends to $0$ by hypothesis, and the bound is independent of $x$.
:::

<1>3. The convolutions converge uniformly to $f$.
::: {.proof}
Because $\int K_n=1$,
$$
(f*K_n)(x)-f(x)
=\int (f(x-t)-f(x))K_n(t)\,dt.
$$
By steps <1>1--<1>2, for all sufficiently large $n$ the absolute value of the right-hand side is $<\eta$ for every $x$. Hence
$$
\|f*K_n-f\|_\infty\longrightarrow0.
$$
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 is exactly the required uniform convergence.
:::
:::
