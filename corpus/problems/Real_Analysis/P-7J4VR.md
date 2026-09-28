---
schema: qual/card@1
id: P-7J4VR
kind: problem
title: Limit interchange for derivatives and integrals; closed subsets of metric spaces
  are complete
classification:
  areas:
  - real-analysis
  topics:
  - Counterexamples
  - Convergence of Functions
  - Differentiation
  - Completeness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- If $f$ is continuous, is it necessarily the case that $f'$ is continuous?

- If $f_n \to f$, is it necessarily the case that $f_n'$ converges to $f'$ (or at all)?

- Is it true that the sum of differentiable functions is differentiable?

- Is it true that the limit of integrals equals the integral of the limit?

- Is it true that a limit of continuous functions is continuous?

- Show that a subset of a metric space is closed iff it is complete.

- Show that if $m(E) < \infty$ and $f_n\to f$ uniformly, then $\lim \int_E f_n = \int_E f$.
:::

::: {.solution}
<1>1. $f(x) = x^2\sin(1/x)$, $f(0) = 0$, is differentiable on $\RR$ and $f'$ is discontinuous at $0$.

::: {.proof}
$\frac{f(h) - f(0)}{h} = h\sin(1/h) \to 0$, so $f'(0) = 0$. For $x \ne 0$, $f'(x) = 2x\sin(1/x) - \cos(1/x)$, and $f'(1/(2k\pi)) = -1$ for every $k \geq 1$.
:::

<1>2. $f_n(x) = \frac{\sin(nx)}{n} \to 0$ uniformly, while $f_n'(x) = \cos(nx)$ satisfies $f_n'(0) = 1$ for all $n$ and $f_n'(\pi) = (-1)^n$.

::: {.proof}
$|f_n| \le 1/n$. So $f_n'(0) \to 1 \neq 0$, the derivative of the limit, and $f_n'(\pi)$ does not converge.
:::

<1>3. If $f$ and $g$ are differentiable at $x$, so is $f + g$, with $(f + g)'(x) = f'(x) + g'(x)$.

::: {.proof}
The difference quotient of $f + g$ is the sum of the difference quotients of $f$ and $g$.
:::

<1>4. $f_n = n\chi_{(0, 1/n)}$ on $[0,1]$ satisfies $f_n \to 0$ pointwise and $\int f_n = 1$ for all $n$.

::: {.proof}
For each $x \in [0,1]$, $f_n(x) = 0$ once $1/n \le x$ or if $x = 0$, and $\int f_n = n \cdot \frac1n$.
:::

<1>5. $f_n(x) = x^n$ on $[0,1]$ are continuous and converge pointwise to $\chi_{\theset{1}}$, which is discontinuous at $1$.

::: {.proof}
$x^n \to 0$ for $0 \le x < 1$ and $1^n = 1$. By the uniform limit theorem the convergence is not uniform.
:::

<1>6. Let $A$ be a subset of a metric space $X$. If $A$ is complete, then $A$ is closed. If $X$ is complete and $A$ is closed, then $A$ is complete.

::: {.proof}
If $A$ is complete and $x_k \in A$ with $x_k \to x \in X$, then $(x_k)$ is Cauchy, so it converges in $A$, and by uniqueness of limits $x \in A$. If $X$ is complete and $A$ is closed, a Cauchy sequence in $A$ converges to some $x \in X$, and $x \in A$ because $A$ is closed.
:::

<1>7. If $m(E) < \infty$ and $f_n \to f$ uniformly on $E$, then $\lim_n \int_E f_n = \int_E f$.

::: {.proof}
$\left|\int_E f_n - \int_E f\right| \le \int_E |f_n - f| \le m(E)\sup_E|f_n - f| \to 0$.
:::
:::

::: {.remark}
The closed-iff-complete statement needs the ambient space to be complete: $(0,1]$ is closed in the metric space $(0,1]$ but is not complete, since $1/n$ is Cauchy with no limit in it. Complete subsets are closed in every metric space.
:::
