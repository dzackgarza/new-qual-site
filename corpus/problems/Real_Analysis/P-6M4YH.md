---
schema: qual/card@1
id: P-6M4YH
kind: problem
title: '$e^{-1/x^2}$ is smooth with all derivatives zero at $0$, has no power series there, and gives a bump function'
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Taylor Series
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-30
  note: 'Split from P-4FH62, where it was part (k).'
---

::: {.problem}
Define a function $f$ on $\RR$ by
$$
f(x) = \begin{cases} e^{-1/x^2} & \text{if } x > 0 \\ 0 & \text{if } x \leq 0. \end{cases}
$$

1. Check whether $f$ is infinitely differentiable at $0$, and, if so, find $f^{(n)}(0)$, $n = 1, 2, 3, \ldots$. Show details.

2. Does $f$ have a power series expansion at $0$?

3. Let $g(x) = f(x)f(1-x)$. Show that $g$ is a nontrivial infinitely differentiable function on $\RR$ which vanishes outside $(0,1)$.
:::

::: {.solution}

::: pf

::: pf-step

$f$ is $C^\infty$ with $f^{(n)}(0)=\boxed{0}$ for every $n$, $f$ has no power series expansion at $0$, and $g(x)=f(x)f(1-x)$ is smooth, positive on $(0,1)$ and zero elsewhere.

::: pf-proof

Induction on $n$ gives $f^{(n)}(x)=P_n(1/x)e^{-1/x^2}$ for $x>0$ and a polynomial $P_n$. Since $t^m e^{-t^2}\to0$ as $t\to\infty$ for every $m$, the right difference quotient $f^{(n)}(x)/x = (1/x)P_n(1/x)e^{-1/x^2}$ tends to $0$ as $x \to 0^+$, and the left difference quotient is $0$. So by induction $f^{(n+1)}(0)$ exists and equals $0$ for every $n$, and $f\in C^\infty$. A power series expansion at $0$ would be the Taylor series, which is identically zero, but $f(x) > 0$ for $x>0$. Finally $g$ is a product of smooth functions, it is positive on $(0,1)$, and one factor vanishes outside $(0,1)$.

:::

:::

:::

:::
