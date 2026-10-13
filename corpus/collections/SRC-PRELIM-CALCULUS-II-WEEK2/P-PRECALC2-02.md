---
schema: qual/card@1
id: P-PRECALC2-02
kind: problem
title: Integral of $\frac{1}{x\log x}$ over $[e^{-3},e^{-2}]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute $\int _ { e ^ { - 3 } } ^ { e ^ { - 2 } } \frac { d x } { x \log ( x ) } .$
:::

::: {.solution}
<1>1. Set
\[
\boxed{u=\log x}.
\]

::: {.proof}
This substitution is natural because the integrand contains the factor
\[
\frac{dx}{x}.
\]
:::

<1>2. Then
\[
\boxed{du=\frac{dx}{x}}.
\]

::: {.proof}
Differentiate
\[
u=\log x.
\]
:::

<1>3. The lower bound transforms as
\[
x=e^{-3}
\quad\Longrightarrow\quad
\boxed{u=-3}.
\]

::: {.proof}
\[
\log(e^{-3})=-3.
\]
:::

<1>4. The upper bound transforms as
\[
x=e^{-2}
\quad\Longrightarrow\quad
\boxed{u=-2}.
\]

::: {.proof}
\[
\log(e^{-2})=-2.
\]
:::

<1>5. Therefore
\[
\int_{e^{-3}}^{e^{-2}}
\frac{dx}{x\log x}
=
\int_{-3}^{-2}
\frac{du}{u}.
\]

::: {.proof}
Substitute steps <1>1--<1>4 into the original integral.
:::

<1>6. An antiderivative of \(1/u\) on the interval \([-3,-2]\) is
\[
\boxed{\log|u|}.
\]

::: {.proof}
Since the interval does not contain \(0\),
\[
\frac{d}{du}\log|u|
=
\frac1u.
\]
:::

<1>7. Hence
\[
\begin{aligned}
\int_{-3}^{-2}\frac{du}{u}
&=
\log|-2|-\log|-3|\\
&=
\log2-\log3.
\end{aligned}
\]

::: {.proof}
Apply the fundamental theorem of calculus using step <1>6.
:::

<1>8. Therefore
\[
\boxed{
\int_{e^{-3}}^{e^{-2}}
\frac{dx}{x\log x}
=
\log\frac23}.
\]

::: {.proof}
Use the logarithm identity
\[
\log2-\log3
=
\log\left(\frac23\right).
\]
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested value.
:::
:::
