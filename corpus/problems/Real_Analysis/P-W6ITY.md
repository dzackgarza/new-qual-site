---
schema: qual/card@1
id: P-W6ITY
kind: problem
title: Functions in $L^p(0,\infty)$ precisely for $a<p<b$, for $a\le p\le b$, and
  for $p=a$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $0 < a < b \leq \infty$, and find examples of functions $f \in L^p((0, \infty ))$ if and only if:

- $a < p < b$

- $a \leq p \leq b$

- $p = a$

*Hint: consider functions of the following form:*
\[
f(x) \definedas x^{- \alpha} \abs{ \log(x) }^{ \beta}
.\]
:::
::: {.solution}

::: pf

::: pf-step

Case (i) ($a < p < b$): define $f$ piecewise.

::: pf-proof

take, for fixed $\delta > 0$ (chosen below),
\[
f(x) \definedas \begin{cases}
x^{-1/b}\,(-\log x)^{-1} & 0 < x \le 1/2,\\
1 & 1/2 < x \le 2,\\
x^{-1/a}\,(\log x)^{-1} & x > 2 .
\end{cases}
\]

:::

:::

::: pf-step

$f \in L^p(0,\infty)$ iff $a < p < b$.

::: pf-proof

near $0$: $\int_0^{1/2} x^{-p/b}(-\log x)^{-p}\,dx$ converges iff $p/b < 1$, i.e. $p < b$ (the power of $x$ is integrable near $0$ exactly when its exponent is $> -1$; the log factor is irrelevant unless $p = b$, where $x^{-1}(-\log x)^{-1}$ is not integrable near $0$: substituting $u = -\log x$ gives $\int du/u = \infty$). Near $\infty$: $\int_2^\infty x^{-p/a}(\log x)^{-p}\,dx$ converges iff $p/a > 1$, i.e. $p > a$ (similarly, at $p = a$ the integrand is $x^{-1}(\log x)^{-1}$, not integrable). On $[1/2,2]$ the function is bounded. Hence $f \in L^p$ exactly when $a < p < b$.

:::

:::

::: pf-step

Case (ii) ($a \le p \le b$): use $\delta > 0$ with $(1+\delta)a > 1$ and
    \[
    f(x) \definedas \begin{cases}
    x^{-1/b}\,(-\log x)^{-1-\delta} & 0 < x \le 1/2,\\
    1 & 1/2 < x \le 2,\\
    x^{-1/a}\,(\log x)^{-1-\delta} & x > 2 .
    \end{cases}
    \]

:::

::: pf-step

$f \in L^p$ iff $a \le p \le b$.

::: pf-proof

near $0$: $\int_0^{1/2} x^{-p/b}(-\log x)^{-(1+\delta)p}\,dx$ converges iff $p/b \le 1$, i.e. $p \le b$: for $p < b$ the power of $x$ dominates, and at $p = b$ we get $\int_0^{1/2} x^{-1}(-\log x)^{-(1+\delta)b}\,dx < \infty$ since $(1+\delta)b > 1$ (substituting $u = -\log x$ gives $\int u^{-(1+\delta)b}\,du$). Near $\infty$: $\int_2^\infty x^{-p/a}(\log x)^{-(1+\delta)p}\,dx$ converges iff $p/a \ge 1$, i.e. $p \ge a$. Hence $f \in L^p$ exactly when $a \le p \le b$.

:::

:::

::: pf-step

Case (iii) ($p = a$): take $\delta > 0$ with $(1+\delta)a > 1$ and
    \[
    f(x) \definedas \begin{cases}
    x^{-1/a}\,(-\log x)^{-1-\delta} & 0 < x \le 1/2,\\
    1 & 1/2 < x \le 2,\\
    x^{-1/a}\,(\log x)^{-1-\delta} & x > 2 .
    \end{cases}
    \]

:::

::: pf-step

$f \in L^p$ iff $p = a$.

::: pf-proof

at $p = a$: near $0$, $\int_0^{1/2} x^{-1}(-\log x)^{-(1+\delta)a}\,dx < \infty$ (as $(1+\delta)a > 1$), and near $\infty$ similarly $\int_2^\infty x^{-1}(\log x)^{-(1+\delta)a}\,dx < \infty$, so $f \in L^a$. For $p > a$: near $0$, $\int_0^{1/2} x^{-p/a}\,(-\log x)^{-(1+\delta)p}\,dx = \infty$ since $p/a > 1$ makes the power of $x$ non-integrable. For $p < a$: near $\infty$, $\int_2^\infty x^{-p/a}(\log x)^{-(1+\delta)p}\,dx = \infty$ since $p/a < 1$. Hence $f \in L^p$ iff $p = a$.

:::

:::

:::

:::
