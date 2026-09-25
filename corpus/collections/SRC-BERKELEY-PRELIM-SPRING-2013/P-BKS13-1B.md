---
schema: qual/card@1
id: P-BKS13-1B
kind: problem
title: Evaluation of $\int_0^1\arctan x\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 3 of the retained Spring 2013 solution PDF and independently reviewed the integration-by-parts computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the antiderivative reduction and endpoint values.
---

::: {.problem}
Find $\textstyle \int _ { 0 } ^ { 1 }$ arctan(x)dx.
:::

::: {.solution}
<1>1. Integration by parts gives
$$
\int_0^1\arctan x\,dx
=
\frac{\pi}{4}
-
\int_0^1\frac{x}{1+x^2}\,dx.
$$

::: {.proof}
Take
$$
u=\arctan x,
\qquad
dv=dx.
$$
Then
$$
du=\frac{dx}{1+x^2},
\qquad
v=x.
$$
Therefore
$$
\begin{aligned}
\int_0^1\arctan x\,dx
&=
\left[x\arctan x\right]_0^1
-
\int_0^1\frac{x}{1+x^2}\,dx\\
&=
\frac{\pi}{4}
-
\int_0^1\frac{x}{1+x^2}\,dx.
\end{aligned}
$$
:::

<1>2. One has
$$
\int_0^1\frac{x}{1+x^2}\,dx
=
\frac12\log2.
$$

::: {.proof}
With
$$
u=1+x^2,
\qquad
du=2x\,dx,
$$
one obtains
$$
\int_0^1\frac{x}{1+x^2}\,dx
=
\frac12
\left[
\log(1+x^2)
\right]_0^1
=
\frac12\log2.
$$
:::

<1>3. Hence
$$
\boxed{
\int_0^1\arctan x\,dx
=
\frac{\pi}{4}
-
\frac{\log2}{2}
}.
$$

::: {.proof}
Substitute step <1>2 into step <1>1.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required value.
:::
:::
