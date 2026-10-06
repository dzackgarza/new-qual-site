---
schema: qual/card@1
id: P-PRECALC1-18
kind: problem
title: Derivative of $g\circ g$ at $0$ for $g(x)=e^{2x+1}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $g ( x ) = e ^ { 2 x + 1 }$ . Compute $\operatorname* { l i m } _ { x \to 0 } { \frac { g ( g ( x ) ) - g ( e ) } { x } }$
:::

::: {.solution}
Let
\[
h(x)=g(g(x)).
\]

<1>1. One has
\[
\boxed{
g(0)=e}.
\]

::: {.proof}
\[
g(0)
=
e^{2\cdot0+1}
=
e.
\]
:::

<1>2. Therefore
\[
\boxed{
h(0)=g(e)}.
\]

::: {.proof}
By definition,
\[
h(0)=g(g(0)).
\]
Apply step <1>1.
:::

<1>3. The given limit is
\[
\boxed{
\lim_{x\to0}
\frac{h(x)-h(0)}{x}
=
h'(0)}.
\]

::: {.proof}
Step <1>2 identifies the numerator as the standard difference quotient for
\(h\) at \(0\).
:::

<1>4. The derivative of \(g\) is
\[
\boxed{
g'(x)=2e^{2x+1}}.
\]

::: {.proof}
Apply the chain rule to
\[
g(x)=e^{2x+1}.
\]
:::

<1>5. Hence
\[
\boxed{
g'(0)=2e}.
\]

::: {.proof}
Substitute \(x=0\) into step <1>4.
:::

<1>6. Also,
\[
\boxed{
g'(e)=2e^{2e+1}}.
\]

::: {.proof}
Substitute \(x=e\) into step <1>4.
:::

<1>7. By the chain rule,
\[
h'(0)
=
g'(g(0))\,g'(0).
\]

::: {.proof}
Since
\[
h=g\circ g,
\]
the chain rule gives
\[
h'(x)=g'(g(x))g'(x).
\]
Set \(x=0\).
:::

<1>8. Therefore
\[
h'(0)
=
\left(
2e^{2e+1}
\right)
(2e).
\]

::: {.proof}
Use steps <1>1, <1>5, <1>6, and <1>7.
:::

<1>9. Simplifying,
\[
\boxed{
h'(0)
=
4e^{2e+2}}.
\]

::: {.proof}
\[
2e^{2e+1}\cdot2e
=
4e^{2e+1+1}
=
4e^{2e+2}.
\]
:::

<1>10. Hence
\[
\boxed{
\lim_{x\to0}
\frac{g(g(x))-g(e)}{x}
=
4e^{2e+2}}.
\]

::: {.proof}
Combine steps <1>3 and <1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the requested limit.
:::
:::
