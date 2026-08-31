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

::: problem
- If $f$ is continuous, is it necessarily the case that $f'$ is continuous?

- If $f_n \to f$, is it necessarily the case that $f_n'$ converges to $f'$ (or at all)?

- Is it true that the sum of differentiable functions is differentiable?

- Is it true that the limit of integrals equals the integral of the limit?

- Is it true that a limit of continuous functions is continuous?

- Show that a subset of a metric space is closed iff it is complete.

- Show that if $m(E) < \infty$ and $f_n\to f$ uniformly, then $\lim \int_E f_n = \int_E f$.
:::

::: {.solution}
<1>1. If $f$ is continuous, is $f'$ necessarily continuous?
No: $f(x) = x^2\sin(1/x)$ (with $f(0) = 0$) is differentiable everywhere but $f'$ is discontinuous at $0$.
::: {.proof}
$f'(0) = 0$ (difference quotient $h\sin(1/h) \to 0$), while for $x \ne 0$, $f'(x) = 2x\sin(1/x) - \cos(1/x)$ has no limit as $x \to 0$.
:::

<1>2. If $f_n \to f$, does $f_n'$ converge to $f'$ (or at all)?
No: $f_n(x) = \frac{\sin(nx)}{n} \to 0$ uniformly, but $f_n'(x) = \cos(nx)$ fails to converge pointwise (e.g. $f_n'(0) = 1 \to 1 \ne 0$; for $x \ne 0$ the limit does not exist).
::: {.proof}
standard counterexample; differentiability is not preserved by limits without extra hypotheses (e.g. uniform convergence of the derivatives).
:::

<1>3. Is the sum of differentiable functions differentiable?
Yes: $(f + g)' = f' + g'$.
::: {.proof}
linearity of the derivative — the difference quotient of $f + g$ is the sum of the difference quotients.
:::

<1>4. Is the limit of integrals equal to the integral of the limit?
No: $f_n = n\chi_{(0, 1/n)}$ on $[0,1]$ has $f_n \to 0$ pointwise but $\int f_n = 1 \not\to 0 = \int 0$.
::: {.proof}
convergence theorems need hypotheses (domination, monotonicity, uniformity).
:::

<1>5. Is a limit of continuous functions continuous?
Only if the convergence is uniform (or suitably strengthened): $f_n(x) = x^n$ on $[0,1]$ converges pointwise to the discontinuous $\chi_{\{1\}}$-type limit.
::: {.proof}
the uniform limit theorem gives continuity under uniform convergence; pointwise convergence alone fails.
:::

<1>6. A subset of a metric space is closed iff it is complete.
<2>1. Complete subsets are closed.
::: {.proof}
if $x_k \in A$ with $x_k \to x$, then $(x_k)$ is Cauchy, and completeness of $A$ gives $x \in A$.
:::
<2>2. Closed subsets of complete spaces are complete.
::: {.proof}
a Cauchy sequence in $A$ is Cauchy in $X$, converges to some $x \in X$ (completeness), and closedness of $A$ gives $x \in A$.
:::
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2 (the second direction needs $X$ complete; the first does not).
:::

<1>7. If $m(E) < \infty$ and $f_n \to f$ uniformly, then $\lim_n \int_E f_n = \int_E f$.
<2>1. $\left|\int_E f_n - \int_E f\right| \le \int_E |f_n - f| \le \|f_n - f\|_\infty\, m(E) \to 0$.
::: {.proof}
triangle inequality and uniform convergence.
:::
<2>2. Q.E.D.
::: {.proof}
<2>1.
:::
:::
