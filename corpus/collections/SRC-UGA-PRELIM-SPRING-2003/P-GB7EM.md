---
schema: qual/card@1
id: P-GB7EM
kind: problem
title: Differentiability in $\mathbb{R}^n$, and $xy/(x^2+y^2)$ is not differentiable
  at the origin
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
a. Let $f$ be a real-valued function defined on $\mathbb{R}^n$.
Define differentiability of $f$ at a point $p$.
b. Show that the function $f: \mathbb{R}^2 \to \mathbb{R}$ defined by $$f(x,y) = \frac{xy}{x^2+y^2} \text{ for } (x,y) \neq (0,0), \text{ and } f(0,0) = 0$$ is not differentiable at $(0,0)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a): Definition of differentiability:

::: pf-proof

::: pf-step

A function $f: \mathbb{R}^n \to \mathbb{R}$ is differentiable at a point $p \in \mathbb{R}^n$ if there exists a linear transformation $L: \mathbb{R}^n \to \mathbb{R}$ (or equivalently a gradient vector $\nabla f(p) \in \mathbb{R}^n$ such that $L(h) = \langle \nabla f(p), h \rangle$) satisfying:
\[
\lim_{h \to 0} \frac{|f(p + h) - f(p) - L(h)|}{\|h\|} = 0.
\]
Equivalently, $f(p + h) = f(p) + L(h) + o(\|h\|)$ as $\|h\| \to 0$.

::: pf-proof

standard definition of Fréchet differentiability on $\mathbb{R}^n$.

:::

:::

:::

:::

::: {.pf-step #s2}

Part (b): Non-differentiability of $f(x, y)$ at $(0, 0)$:

::: pf-proof

::: {.pf-step #s2-1}

If a function $f$ is differentiable at $p$, then $f$ is continuous at $p$.

::: pf-proof

$|f(p+h) - f(p)| \le |L(h)| + o(\|h\|) \le \|L\| \|h\| + o(\|h\|) \to 0$ as $h \to 0$.

:::

:::

::: pf-step

We evaluate the limit of $f(x, y) = \frac{xy}{x^2 + y^2}$ as $(x, y) \to (0, 0)$ along lines $y = mx$:
For $x \neq 0$:
\[
f(x, mx) = \frac{x(mx)}{x^2 + (mx)^2} = \frac{m x^2}{x^2(1 + m^2)} = \frac{m}{1 + m^2}.
\]

::: pf-proof

algebraic substitution $y = mx$.

:::

:::

::: pf-step

Along the line $y = 0$ ($m = 0$), $\lim_{x \to 0} f(x, 0) = 0$.
Along the line $y = x$ ($m = 1$), $\lim_{x \to 0} f(x, x) = \frac{1}{1 + 1^2} = \frac{1}{2} \neq f(0, 0)$.
Since the limit depends on the path of approach, $\lim_{(x, y) \to (0, 0)} f(x, y)$ does not exist.
Thus $f$ is discontinuous at $(0, 0)$.

::: pf-proof

non-uniqueness of directional limits.

:::

:::

::: pf-step

Since $f$ is not continuous at $(0, 0)$, by step [](#s2-1){.pf-ref} $f$ cannot be differentiable at $(0, 0)$.

::: pf-proof

contrapositive of differentiability implies continuity.

:::

:::

:::

:::

::: pf-step

Conclusion:
$f$ is defined to be differentiable if its linear approximation error is $o(\|h\|)$, and $f(x, y) = \frac{xy}{x^2+y^2}$ is not differentiable at $(0, 0)$ due to discontinuity. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
