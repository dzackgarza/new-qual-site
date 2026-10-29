---
schema: qual/card@1
id: P-WESCA08-II3
kind: problem
title: 'An analytic function attaining a positive minimum modulus is constant'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $f$ be analytic on a domain $D$, and suppose there is $z_0\in D$ such that
$$
|f(z)|\ge |f(z_0)|>0\qquad(z\in D).
$$
Show that $f$ is constant on $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f$ has no zeros in $D$.


::: pf-proof

For every $z\in D$,
$$
|f(z)|
\ge
|f(z_0)|
>
0.
$$
Hence
$$
f(z)\ne0.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
g(z)=\frac1{f(z)}
$$
is analytic on $D$.


::: pf-proof

The reciprocal of a nonvanishing analytic function is analytic.
Explicitly,
$$
g'(z)
=
-\frac{f'(z)}{f(z)^2}.
$$
Step [](#s1-1){.pf-ref} guarantees that the denominator never vanishes.

:::

:::

::: {.pf-step #s1-3}

For every $z\in D$,
$$
\boxed{
|g(z)|
\le
|g(z_0)|}.
$$


::: pf-proof

The hypothesis gives
$$
|f(z)|
\ge
|f(z_0)|
>
0.
$$
Taking reciprocals reverses the inequality:
$$
\frac1{|f(z)|}
\le
\frac1{|f(z_0)|}.
$$
These are exactly $|g(z)|$ and $|g(z_0)|$.

:::

:::

::: {.pf-step #s1-4}

Thus $|g|$ attains its maximum on $D$ at the interior point
$z_0$.


::: pf-proof

Step [](#s1-3){.pf-ref} shows that no value of $|g|$ exceeds $|g(z_0)|$, and
$z_0\in D$.

:::

:::

::: pf-step

The maximum modulus principle implies that
$$
\boxed{g\text{ is constant on }D}.
$$


::: pf-proof

The domain $D$ is connected, $g$ is analytic by step [](#s1-2){.pf-ref}, and
$|g|$ attains a maximum at an interior point by step [](#s1-4){.pf-ref}. The strong
maximum modulus principle therefore forces $g$ to be constant.

:::

:::

::: {.pf-step #s1-6}

Hence $f$ is constant on $D$.


::: pf-proof

If
$$
g(z)=c
$$
for all $z\in D$, then $c\ne0$ because
$$
g=\frac1f.
$$
Therefore
$$
f(z)=\frac1c
$$
for all $z\in D$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
