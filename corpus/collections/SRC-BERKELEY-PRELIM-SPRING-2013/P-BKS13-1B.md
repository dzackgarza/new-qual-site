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
Find $\int_0^1 \arctan(x)\,dx$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Integration by parts gives
$$
\int_0^1\arctan x\,dx
=
\frac{\pi}{4}
-
\int_0^1\frac{x}{1+x^2}\,dx.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

One has
$$
\int_0^1\frac{x}{1+x^2}\,dx
=
\frac12\log2.
$$

::: pf-proof

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

:::

::: {.pf-step #s3}

Hence
$$
\boxed{
\int_0^1\arctan x\,dx
=
\frac{\pi}{4}
-
\frac{\log2}{2}
}.
$$

::: pf-proof

Substitute step [](#s2){.pf-ref} into step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required value.

:::

:::

:::
