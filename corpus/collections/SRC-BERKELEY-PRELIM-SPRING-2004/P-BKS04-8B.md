---
schema: qual/card@1
id: P-BKS04-8B
kind: problem
title: Limit of $n((1+x/n)^n-e^x)$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Transcribed from the retained solution sheet — Berkeley preliminary examination, Spring
    2004, solutions, assets/attachments/s04solution.pdf, Problem 8B on PDF p. 8 — and
    restructured into steps; the card's prose was already that sheet's argument verbatim. Every
    step was checked: the series for log(1+u) and for e^y - 1 are applied at u = x/n and y =
    O(1/n), and the big-O constant's dependence on x but not on n is the sheet's own remark and
    is kept. An independent check with sympy confirms the limit -x^2 e^x / 2.
---

::: {.problem}
For each real number $x$, compute

$$
\lim_{n\to\infty}n\left(\left(1+\frac xn\right)^n-e^x\right).
$$
:::

::: {.solution}
The argument is the retained solution sheet's: **Berkeley preliminary examination, Spring 2004, solutions** (`assets/attachments/s04solution.pdf`), Problem 8B, PDF p. 8. Throughout $x$ is a fixed real number, $n$ tends to infinity, and $O(n^{-k})$ denotes a quantity bounded by $C_{x}n^{-k}$ for large $n$ with a constant that depends on $x$ but not on $n$.

::: pf

::: {.pf-step #exp}
For $n > \abs{x}$, $\bigl(1 + \frac{x}{n}\bigr)^{n} = e^{n\log(1+x/n)}$.

::: pf-proof
$1 + \frac{x}{n} > 0$ for $n > \abs{x}$, so the real logarithm of the left side is defined and $n\log(1+x/n)$ is its logarithm.

:::

:::

::: {.pf-step #log}
$\log\bigl(1+\frac{x}{n}\bigr) = \frac{x}{n} - \frac{x^{2}}{2n^{2}} + O(n^{-3})$, hence $n\log\bigl(1+\frac{x}{n}\bigr) = x - \frac{x^{2}}{2n} + O(n^{-2})$.

::: pf-proof
Taylor's theorem for $\log(1+u)$ at $u = 0$ gives $\log(1+u) = u - \frac{u^{2}}{2} + O(u^{3})$ for small $\abs{u}$, with the implicit constant absolute; substituting $u = \frac{x}{n}$ gives the first display for $n$ large enough that $\abs{x/n}$ is in that range, and the second display follows by multiplying by $n$. The constant depends on $x$ through the threshold on $n$ and the size of $x^{3}$, and not otherwise on $n$.

:::

:::

::: {.pf-step #reduce}
$n\Bigl(\bigl(1+\frac{x}{n}\bigr)^{n} - e^{x}\Bigr) = ne^{x}\Bigl(e^{-x^{2}/(2n) + O(n^{-2})} - 1\Bigr)$.

::: pf-proof
Factor out $e^{x}$ from the difference and use steps [](#exp){.pf-ref} and [](#log){.pf-ref}: $e^{n\log(1+x/n)} - e^{x} = e^{x}\bigl(e^{\,n\log(1+x/n) - x} - 1\bigr)$, and the exponent is $-\frac{x^{2}}{2n} + O(n^{-2})$.

:::

:::

::: {.pf-step #linearise}
$e^{y} - 1 = y + O(y^{2})$ for $y \to 0$, so the bracket equals $-\frac{x^{2}}{2n} + O(n^{-2})$.

::: pf-proof
Applying the expansion with $y = -\frac{x^{2}}{2n} + O(n^{-2})$, which tends to $0$, gives $e^{y} - 1 = y + O(y^{2})$; and $y^{2} = O(n^{-2})$, so the quadratic term is absorbed into $O(n^{-2})$.

:::

:::

::: {.pf-step #limit}
$n\Bigl(\bigl(1+\frac{x}{n}\bigr)^{n} - e^{x}\Bigr) = -\frac{x^{2}e^{x}}{2} + O(n^{-1}) \to -\frac{x^{2}e^{x}}{2}$.

::: pf-proof
Multiply the bracket of step [](#linearise){.pf-ref} by $ne^{x}$: the leading term $ne^{x}\bigl(-\frac{x^{2}}{2n}\bigr)$ is $-\frac{x^{2}e^{x}}{2}$, and $ne^{x}O(n^{-2}) = O(n^{-1})$ tends to $0$.

:::

:::

::: pf-step
For every real $x$, $\displaystyle\lim_{n\to\infty} n\Bigl(\bigl(1+\frac{x}{n}\bigr)^{n} - e^{x}\Bigr) = \boxed{-\frac{x^{2}e^{x}}{2}}$.

::: pf-proof
Step [](#limit){.pf-ref} computes the limit for the fixed $x$; taking $x = 0$ the formula gives $0$, which is also the value of $n(1^{n} - 1)$.

:::

:::

:::
:::
