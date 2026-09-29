---
schema: qual/card@1
id: P-BERK86S-04
kind: problem
title: Limit of a multiplicative difference quotient for a positive differentiable function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Took logarithms and recognized the exponent as x times the difference
    quotient for log f at x, obtaining exp(x f'(x)/f(x)).
---

::: {.problem}
Let $f:(0,\infty)\to(0,\infty)$ be differentiable. Prove that for every $x>0$ the finite nonzero limit
\[
\lim_{\delta\to0}
\left(\frac{f(x+\delta x)}{f(x)}\right)^{1/\delta}
\]
exists.
:::

::: {.solution}
Fix $x>0$.

::: pf

::: {.pf-step #log-f-derivative}
The function
$$
h(t)\coloneqq\log f(t)
$$
is differentiable at $x$, with
$$
h'(x)=\frac{f'(x)}{f(x)}.
$$

::: pf-proof
The hypothesis gives $f(x)>0$, and $f$ is differentiable at $x$.
Therefore the chain rule applies to $\log\circ f$ and yields the displayed
derivative.
:::

:::

::: {.pf-step #quotient-limit}
One has
$$
\lim_{\delta\to0}
\frac{
\log f(x+\delta x)-\log f(x)
}{\delta}
=
\frac{x f'(x)}{f(x)}.
$$

::: pf-proof
For $\delta\neq0$ sufficiently close to $0$, the point
$x+\delta x=x(1+\delta)$ remains positive. Rewrite the quotient as
$$
x\,
\frac{
h(x+\delta x)-h(x)
}{
\delta x
}.
$$
As $\delta\to0$, the second factor tends to $h'(x)$ by the definition of
the derivative. Apply step [](#log-f-derivative){.pf-ref}.
:::

:::

::: {.pf-step #exponential-identity}
For every sufficiently small nonzero $\delta$,
$$
\left(
\frac{f(x+\delta x)}{f(x)}
\right)^{1/\delta}
=
\exp\left(
\frac{
\log f(x+\delta x)-\log f(x)
}{\delta}
\right).
$$

::: pf-proof
Both numerator and denominator inside the ratio are positive, so the real
logarithm is defined. For every $u>0$ and real $r$,
$$
u^r=e^{r\log u}.
$$
Apply this with
$$
u=\frac{f(x+\delta x)}{f(x)}
\qquad\text{and}\qquad
r=\frac1\delta.
$$
:::

:::

::: {.pf-step #limit-boxed}
Therefore
$$
\boxed{
\lim_{\delta\to0}
\left(
\frac{f(x+\delta x)}{f(x)}
\right)^{1/\delta}
=
\exp\left(\frac{x f'(x)}{f(x)}\right)
}.
$$

::: pf-proof
By step [](#exponential-identity){.pf-ref}, the expression is the exponential of the quotient in
step [](#quotient-limit){.pf-ref}. Since the exponential function is continuous, step [](#quotient-limit){.pf-ref} gives
the displayed limit.
:::

:::

::: {.pf-step #finite-nonzero}
The limit in step [](#limit-boxed){.pf-ref} is finite and nonzero.

::: pf-proof
The number
$$
\frac{x f'(x)}{f(x)}
$$
is finite because $f$ is differentiable and $f(x)>0$. Its exponential
is therefore a finite positive real number.
:::

:::

::: pf-qed
Steps [](#limit-boxed){.pf-ref} and [](#finite-nonzero){.pf-ref} prove the required existence, finiteness, and
nonvanishing.
:::

:::
:::
