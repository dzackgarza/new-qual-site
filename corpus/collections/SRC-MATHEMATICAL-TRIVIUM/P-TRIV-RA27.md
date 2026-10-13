---
schema: qual/card@1
id: P-TRIV-RA27
kind: problem
title: Convergence of $\int_0^1 x^{-\alpha}\,dx$ and $\int_1^\infty x^{-\alpha}\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 27, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
For what values of α the following integrals are convergent?
(a) $\int _ { 0 } ^ { 1 } { \frac { d x } { x ^ { \alpha } } } .$ (b) $\int _ { 1 } ^ { \infty } { \frac { d x } { x ^ { \alpha } } } .$
:::

::: {.solution}
<1>1. For $\alpha\neq1$,
$$
\int x^{-\alpha}\,dx
=
\frac{x^{1-\alpha}}{1-\alpha}+C.
$$

::: {.proof}
Differentiate the right-hand side.
:::

<1>2. For $0<\varepsilon<1$ and $\alpha\neq1$,
$$
\int_\varepsilon^1 x^{-\alpha}\,dx
=
\frac{1-\varepsilon^{1-\alpha}}{1-\alpha}.
$$

::: {.proof}
Evaluate the antiderivative from step <1>1 at the endpoints.
:::

<1>3. If $\alpha<1$, then
$$
\int_0^1 x^{-\alpha}\,dx
$$
converges and equals
$$
\frac1{1-\alpha}.
$$

::: {.proof}
When $\alpha<1$, one has $1-\alpha>0$, so
$$
\varepsilon^{1-\alpha}\to0
$$
as $\varepsilon\to0^+$. Apply step <1>2.
:::

<1>4. If $\alpha>1$, then
$$
\int_0^1 x^{-\alpha}\,dx
$$
diverges.

::: {.proof}
Now $1-\alpha<0$, so
$$
\varepsilon^{1-\alpha}\to\infty
$$
as $\varepsilon\to0^+$. The expression in step <1>2 therefore has no finite
limit.
:::

<1>5. If $\alpha=1$, then
$$
\int_0^1\frac{dx}{x}
$$
diverges.

::: {.proof}
For $0<\varepsilon<1$,
$$
\int_\varepsilon^1\frac{dx}{x}
=
-\log\varepsilon
\longrightarrow\infty.
$$
:::

<1>6. Therefore
$$
\boxed{
\int_0^1 x^{-\alpha}\,dx
\text{ converges iff }\alpha<1.
}
$$

::: {.proof}
Combine steps <1>3--<1>5.
:::

<1>7. For $R>1$ and $\alpha\neq1$,
$$
\int_1^R x^{-\alpha}\,dx
=
\frac{R^{1-\alpha}-1}{1-\alpha}.
$$

::: {.proof}
Evaluate the antiderivative from step <1>1 between $1$ and $R$.
:::

<1>8. If $\alpha>1$, then
$$
\int_1^\infty x^{-\alpha}\,dx
$$
converges and equals
$$
\frac1{\alpha-1}.
$$

::: {.proof}
Now $1-\alpha<0$, so
$$
R^{1-\alpha}\to0
$$
as $R\to\infty$. Step <1>7 therefore tends to
$$
\frac{-1}{1-\alpha}
=
\frac1{\alpha-1}.
$$
:::

<1>9. If $\alpha<1$, then
$$
\int_1^\infty x^{-\alpha}\,dx
$$
diverges.

::: {.proof}
Then $1-\alpha>0$, so $R^{1-\alpha}\to\infty$ in step <1>7.
:::

<1>10. If $\alpha=1$, then
$$
\int_1^\infty\frac{dx}{x}
$$
diverges.

::: {.proof}
For $R>1$,
$$
\int_1^R\frac{dx}{x}
=
\log R
\longrightarrow\infty.
$$
:::

<1>11. Therefore
$$
\boxed{
\int_1^\infty x^{-\alpha}\,dx
\text{ converges iff }\alpha>1.
}
$$

::: {.proof}
Combine steps <1>8--<1>10.
:::

<1>12. Q.E.D.

::: {.proof}
Steps <1>6 and <1>11 answer parts (a) and (b), respectively.
:::
:::
