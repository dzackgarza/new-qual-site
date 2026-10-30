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

(i) $a < p < b$;

(ii) $a \leq p \leq b$;

(iii) $p = a$.

:::

::: {.hint}

Consider functions of the form
$$
f(x) \coloneqq x^{- \alpha} \abs{ \log(x) }^{ \beta}.
$$

:::

::: {.solution}

Each example is $1$ on $(1/2, 2]$, so only the behaviour on $(0, 1/2]$ and on $(2, \infty)$ decides membership in $L^p$. Two facts decide it. For $\gamma > 0$ and $\beta \in \RR$, $\int_0^{1/2} x^{-\gamma}(-\log x)^{\beta}\dx$ is finite iff $\gamma < 1$, or $\gamma = 1$ and $\beta < -1$; and $\int_2^\infty x^{-\gamma}(\log x)^{\beta}\dx$ is finite iff $\gamma > 1$, or $\gamma = 1$ and $\beta < -1$. When $\gamma = 1$ both follow from the substitution $u = \abs{\log x}$, which turns each integral into $\int^\infty u^{\beta}\,du$.

::: pf

::: pf-step

(i) Let
$$
f(x) \coloneqq \begin{cases}
x^{-1/b}\,(-\log x)^{-1/b} & 0 < x \le 1/2 \text{ if } b < \infty, \\
-\log x & 0 < x \le 1/2 \text{ if } b = \infty, \\
1 & 1/2 < x \le 2,\\
x^{-1/a}\,(\log x)^{-1/a} & x > 2 .
\end{cases}
$$
Then $f \in L^p(0,\infty)$ iff $a < p < b$.

::: pf-proof

Near $0$ with $b < \infty$, $f^p = x^{-p/b}(-\log x)^{-p/b}$ is integrable iff $p < b$: at $p = b$ it is $x^{-1}(-\log x)^{-1}$. For $p = \infty$, $f$ is unbounded near $0$. With $b = \infty$, $(-\log x)^p$ is integrable on $(0, 1/2]$ for every finite $p$, and $f$ is unbounded, so $f \notin L^\infty$.
Near $\infty$, $f^p = x^{-p/a}(\log x)^{-p/a}$ is integrable iff $p > a$: at $p = a$ it is $x^{-1}(\log x)^{-1}$.

:::

:::

::: pf-step

(ii) Fix $\delta > 0$ with $(1+\delta)a > 1$, and let
$$
f(x) \coloneqq \begin{cases}
x^{-1/b}\,(-\log x)^{-1-\delta} & 0 < x \le 1/2,\\
1 & 1/2 < x \le 2,\\
x^{-1/a}\,(\log x)^{-1-\delta} & x > 2 ,
\end{cases}
$$
with $x^{-1/b} = 1$ when $b = \infty$. Then $f \in L^p$ iff $a \le p \le b$.

::: pf-proof

Near $0$, $f^p = x^{-p/b}(-\log x)^{-(1+\delta)p}$ is integrable iff $p \le b$: at $p = b < \infty$ the exponent of the logarithm is $-(1+\delta)b < -1$ because $b > a$. For $p = \infty$, $f$ is bounded near $0$ iff $b = \infty$.
Near $\infty$, $f^p = x^{-p/a}(\log x)^{-(1+\delta)p}$ is integrable iff $p \ge a$: at $p = a$ the exponent of the logarithm is $-(1+\delta)a < -1$. Also $f$ is bounded on $(2, \infty)$.

:::

:::

::: pf-step

(iii) Fix $\delta > 0$ with $(1+\delta)a > 1$, and let
$$
f(x) \coloneqq \begin{cases}
x^{-1/a}\,(-\log x)^{-1-\delta} & 0 < x \le 1/2,\\
1 & 1/2 < x \le 2,\\
x^{-1/a}\,(\log x)^{-1-\delta} & x > 2 .
\end{cases}
$$
Then $f \in L^p$ iff $p = a$.

::: pf-proof

At $p = a$, both $\int_0^{1/2} x^{-1}(-\log x)^{-(1+\delta)a}\dx$ and $\int_2^\infty x^{-1}(\log x)^{-(1+\delta)a}\dx$ are finite because $(1+\delta)a > 1$. For $a < p \le \infty$, $f \notin L^p$: for finite $p$ the power $x^{-p/a}$ is not integrable near $0$, and $f$ is unbounded near $0$. For $p < a$, the power $x^{-p/a}$ makes $\int_2^\infty f^p = \infty$.

:::

:::

:::

:::
