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
For what values of $\alpha$ the following integrals are convergent?

(a) $\int_0^1 \frac{dx}{x^\alpha}$, (b) $\int_1^{\infty} \frac{dx}{x^\alpha}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $\alpha\neq1$,
$$
\int x^{-\alpha}\,dx
=
\frac{x^{1-\alpha}}{1-\alpha}+C.
$$


::: pf-proof

Differentiate the right-hand side.

:::

:::

::: {.pf-step #s1-2}

For $0<\varepsilon<1$ and $\alpha\neq1$,
$$
\int_\varepsilon^1 x^{-\alpha}\,dx
=
\frac{1-\varepsilon^{1-\alpha}}{1-\alpha}.
$$


::: pf-proof

Evaluate the antiderivative from step [](#s1-1){.pf-ref} at the endpoints.

:::

:::

::: {.pf-step #s1-3}

If $\alpha<1$, then
$$
\int_0^1 x^{-\alpha}\,dx
$$
converges and equals
$$
\frac1{1-\alpha}.
$$


::: pf-proof

When $\alpha<1$, one has $1-\alpha>0$, so
$$
\varepsilon^{1-\alpha}\to0
$$
as $\varepsilon\to0^+$. Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

If $\alpha>1$, then
$$
\int_0^1 x^{-\alpha}\,dx
$$
diverges.


::: pf-proof

Now $1-\alpha<0$, so
$$
\varepsilon^{1-\alpha}\to\infty
$$
as $\varepsilon\to0^+$. The expression in step [](#s1-2){.pf-ref} therefore has no finite
limit.

:::

:::

::: {.pf-step #s1-5}

If $\alpha=1$, then
$$
\int_0^1\frac{dx}{x}
$$
diverges.


::: pf-proof

For $0<\varepsilon<1$,
$$
\int_\varepsilon^1\frac{dx}{x}
=
-\log\varepsilon
\longrightarrow\infty.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\int_0^1 x^{-\alpha}\,dx
\text{ converges iff }\alpha<1.
}
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For $R>1$ and $\alpha\neq1$,
$$
\int_1^R x^{-\alpha}\,dx
=
\frac{R^{1-\alpha}-1}{1-\alpha}.
$$


::: pf-proof

Evaluate the antiderivative from step [](#s1-1){.pf-ref} between $1$ and $R$.

:::

:::

::: {.pf-step #s1-8}

If $\alpha>1$, then
$$
\int_1^\infty x^{-\alpha}\,dx
$$
converges and equals
$$
\frac1{\alpha-1}.
$$


::: pf-proof

Now $1-\alpha<0$, so
$$
R^{1-\alpha}\to0
$$
as $R\to\infty$. Step [](#s1-7){.pf-ref} therefore tends to
$$
\frac{-1}{1-\alpha}
=
\frac1{\alpha-1}.
$$

:::

:::

::: {.pf-step #s1-9}

If $\alpha<1$, then
$$
\int_1^\infty x^{-\alpha}\,dx
$$
diverges.


::: pf-proof

Then $1-\alpha>0$, so $R^{1-\alpha}\to\infty$ in step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

If $\alpha=1$, then
$$
\int_1^\infty\frac{dx}{x}
$$
diverges.


::: pf-proof

For $R>1$,
$$
\int_1^R\frac{dx}{x}
=
\log R
\longrightarrow\infty.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
\int_1^\infty x^{-\alpha}\,dx
\text{ converges iff }\alpha>1.
}
$$


::: pf-proof

Combine steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref} and [](#s1-11){.pf-ref} answer parts (a) and (b), respectively.

:::

:::

:::
