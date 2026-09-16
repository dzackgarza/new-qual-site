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
<1>1. For $|z|<1$,
\[
\frac1{1-z}=\sum_{k=0}^{\infty}z^k.
\]
::: {.proof}
This is the geometric-series identity.
:::

<1>2. Differentiating the identity in <1>1 exactly $m-1$ times gives
\[
\frac{(m-1)!}{(1-z)^m}
=
\sum_{k=m-1}^{\infty}\frac{k!}{(k-m+1)!}z^{k-m+1}.
\]
::: {.proof}
A power series may be differentiated term-by-term inside its radius of convergence. The $(m-1)$st derivative of $(1-z)^{-1}$ is $(m-1)!(1-z)^{-m}$, while
\[
\frac{d^{m-1}}{dz^{m-1}}z^k
=
\frac{k!}{(k-m+1)!}z^{k-m+1}
\]
for $k\ge m-1$; lower-degree terms differentiate to zero.
:::

<1>3. Hence, for $|z|<1$,
\[
(1-z)^{-m}
=
\sum_{n=0}^{\infty}\binom{n+m-1}{m-1}z^n.
\]
::: {.proof}
Set $n=k-m+1$ in <1>2 and divide by $(m-1)!$. The coefficient becomes
\[
\frac{(n+m-1)!}{n!(m-1)!}
=\binom{n+m-1}{m-1}.
\]
:::

<1>4. Therefore
\[
a_n=\binom{n+m-1}{m-1}
=
\frac{(n+1)(n+2)\cdots(n+m-1)}{(m-1)!}.
\]
::: {.proof}
The first equality is coefficient comparison in <1>3. The second is the factorial formula for the binomial coefficient; when $m=1$, the numerator is the empty product and equals $1$.
:::

<1>5. One has
\[
\frac{a_n}{n^{m-1}/(m-1)!}
=
\prod_{j=1}^{m-1}\left(1+\frac jn\right)
\longrightarrow1.
\]
::: {.proof}
Divide the product expression in <1>4 by $n^{m-1}/(m-1)!$. There are finitely many factors, and each tends to $1$ as $n\to\infty$.
:::

<1>6. Thus
\[
a_n\sim\frac{n^{m-1}}{(m-1)!}.
\]
::: {.proof}
This is exactly the ratio limit established in <1>5.
:::
:::
