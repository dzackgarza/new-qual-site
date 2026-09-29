---
schema: qual/card@1
id: E-SS1.EX-20
kind: problem
title: Power-series expansion and coefficient asymptotics of $(1-z)^{-m}$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Let $m$ be a fixed positive integer. Expand $(1-z)^{-m}$ in powers of $z$. Also, if
\[
(1-z)^{-m}=\sum_{n=0}^{\infty}a_nz^n,
\]
show that
\[
a_n\sim\frac{1}{(m-1)!}n^{m-1}
\qquad\text{as }n\to\infty.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $|z|<1$,
\[
\frac1{1-z}=\sum_{k=0}^{\infty}z^k.
\]

::: pf-proof

This is the geometric-series identity.

:::

:::

::: {.pf-step #s2}

Differentiating the identity in step [](#s1){.pf-ref} exactly $m-1$ times gives
\[
\frac{(m-1)!}{(1-z)^m}
=
\sum_{k=m-1}^{\infty}\frac{k!}{(k-m+1)!}z^{k-m+1}.
\]

::: pf-proof

A power series may be differentiated term-by-term inside its radius of convergence. The $(m-1)$st derivative of $(1-z)^{-1}$ is $(m-1)!(1-z)^{-m}$, while
\[
\frac{d^{m-1}}{dz^{m-1}}z^k
=
\frac{k!}{(k-m+1)!}z^{k-m+1}
\]
for $k\ge m-1$; lower-degree terms differentiate to zero.

:::

:::

::: {.pf-step #s3}

Hence, for $|z|<1$,
\[
(1-z)^{-m}
=
\sum_{n=0}^{\infty}\binom{n+m-1}{m-1}z^n.
\]

::: pf-proof

Set $n=k-m+1$ in step [](#s2){.pf-ref} and divide by $(m-1)!$. The coefficient becomes
\[
\frac{(n+m-1)!}{n!(m-1)!}
=\binom{n+m-1}{m-1}.
\]

:::

:::

::: {.pf-step #s4}

Therefore
\[
a_n=\binom{n+m-1}{m-1}
=
\frac{(n+1)(n+2)\cdots(n+m-1)}{(m-1)!}.
\]

::: pf-proof

The first equality is coefficient comparison in step [](#s3){.pf-ref}. The second is the factorial formula for the binomial coefficient; when $m=1$, the numerator is the empty product and equals $1$.

:::

:::

::: {.pf-step #s5}

One has
\[
\frac{a_n}{n^{m-1}/(m-1)!}
=
\prod_{j=1}^{m-1}\left(1+\frac jn\right)
\longrightarrow1.
\]

::: pf-proof

Divide the product expression in step [](#s4){.pf-ref} by $n^{m-1}/(m-1)!$. There are finitely many factors, and each tends to $1$ as $n\to\infty$.

:::

:::

::: pf-step

Thus
\[
a_n\sim\frac{n^{m-1}}{(m-1)!}.
\]

::: pf-proof

This is exactly the ratio limit established in step [](#s5){.pf-ref}.

:::

:::

:::

:::
