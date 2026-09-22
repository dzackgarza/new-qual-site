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

<1>1. The function
$$
h(t)\coloneqq\log f(t)
$$
is differentiable at $x$, with
$$
h'(x)=\frac{f'(x)}{f(x)}.
$$

::: {.proof}
The hypothesis gives $f(x)>0$, and $f$ is differentiable at $x$.
Therefore the chain rule applies to $\log\circ f$ and yields the displayed
derivative.
:::

<1>2. One has
$$
\lim_{\delta\to0}
\frac{
\log f(x+\delta x)-\log f(x)
}{\delta}
=
\frac{x f'(x)}{f(x)}.
$$

::: {.proof}
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
the derivative. Apply step <1>1.
:::

<1>3. For every sufficiently small nonzero $\delta$,
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

::: {.proof}
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

<1>4. Therefore
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

::: {.proof}
By step <1>3, the expression is the exponential of the quotient in
step <1>2. Since the exponential function is continuous, step <1>2 gives
the displayed limit.
:::

<1>5. The limit in step <1>4 is finite and nonzero.

::: {.proof}
The number
$$
\frac{x f'(x)}{f(x)}
$$
is finite because $f$ is differentiable and $f(x)>0$. Its exponential
is therefore a finite positive real number.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>4 and <1>5 prove the required existence, finiteness, and
nonvanishing.
:::
:::
