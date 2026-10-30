---
schema: qual/card@1
id: P-GB7EM
kind: problem
title: Differentiability in $\RR^n$, and $xy/(x^2+y^2)$ is not differentiable
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
a. Let $f$ be a real-valued function defined on $\RR^n$.
Define differentiability of $f$ at a point $p$.
b. Show that the function $f: \RR^2 \to \RR$ defined by $$f(x,y) = \frac{xy}{x^2+y^2} \text{ for } (x,y) \neq (0,0), \text{ and } f(0,0) = 0$$ is not differentiable at $(0,0)$.
:::

::: {.solution}

::: pf

::: pf-step

(a) The function $f$ is differentiable at $p$ if there is a linear map $L\colon \RR^n \to \RR$ such that
$$
\lim_{h \to 0} \frac{\abs{f(p + h) - f(p) - L(h)}}{\norm{h}} = 0.
$$

::: pf-proof

This is the definition of (Fréchet) differentiability. The map $L$ is then unique, and $L(h) = \langle \nabla f(p), h \rangle$.

:::

:::

::: pf-step

(b) The function $f$ is not differentiable at $(0,0)$.

::: pf-proof

::: {.pf-step #diff-cont}

A function $g\colon \RR^n \to \RR$ that is differentiable at $p$ is continuous at $p$.

::: pf-proof

Let $L$ be as in the definition, and let $r(h) = g(p+h) - g(p) - L(h)$, so that $\abs{r(h)}/\norm{h} \to 0$ as $h \to 0$.
A linear map on $\RR^n$ is bounded, so there is $C$ with $\abs{L(h)} \le C\norm{h}$.
Then $\abs{g(p+h) - g(p)} \le C\norm{h} + \abs{r(h)} \to 0$ as $h \to 0$.

:::

:::

::: {.pf-step #discont}

The function $f$ is not continuous at $(0,0)$.

::: pf-proof

For $x \neq 0$,
$$
f(x, x) = \frac{x^2}{2x^2} = \frac12.
$$
Thus $f(x,x) \to \frac12$ as $x \to 0$, but $f(0,0) = 0$.

:::

:::

::: pf-qed

By step [](#discont){.pf-ref}, $f$ is not continuous at $(0,0)$, so by step [](#diff-cont){.pf-ref} it is not differentiable there.

:::

:::

:::

:::

:::
