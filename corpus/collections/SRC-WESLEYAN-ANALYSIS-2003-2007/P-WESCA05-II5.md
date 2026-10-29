---
schema: qual/card@1
id: P-WESCA05-II5
kind: problem
title: "A Schwarz–Pick bound in terms of $f(0)$"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 2, problem 5 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Suppose $f$ is analytic in the open unit disk $D$ and $|f(z)|<1$ for all $z\in D$.
Let $a=f(0)$ and define
$$
g(z)=\frac{f(z)-a}{1-\overline a\,f(z)}.
$$
Using $g$ and the fact that $g$ maps $D$ to $D$, prove that
$$
|f(z)|\le\frac{|f(0)|+|z|}{1-|f(0)||z|}
\qquad(z\in D).
$$
:::

::: {.solution}

Write $a=f(0)$.

::: pf

::: {.pf-step #s1-1}

The function
$$
g(z)=\frac{f(z)-a}{1-\overline a\,f(z)}
$$
satisfies
$$
g(0)=0.
$$


::: pf-proof

Since $f(0)=a$,
$$
g(0)
=
\frac{a-a}{1-\overline a\,a}
=0.
$$
The denominator is nonzero because $|a|<1$.

:::

:::

::: {.pf-step #s1-2}

For every $z\in D$,
$$
|g(z)|\le|z|.
$$


::: pf-proof

By hypothesis, $g$ is an analytic self-map of the unit disk. Step [](#s1-1){.pf-ref} gives $g(0)=0$. Schwarz's lemma therefore yields
$$
|g(z)|\le|z|
$$
for every $z\in D$.

:::

:::

::: {.pf-step #s1-3}

Solving the defining equation for $f$ gives
$$
f(z)=\frac{a+g(z)}{1+\overline a\,g(z)}.
$$


::: pf-proof

Starting with
$$
g(1-\overline a f)=f-a,
$$
collect the terms containing $f$:
$$
a+g=f+\overline a\,gf
=f(1+\overline a\,g).
$$
Since $|a|<1$ and $|g(z)|<1$, one has
$$
|\overline a\,g(z)|<1,
$$
so $1+\overline a\,g(z)\ne0$. Division gives the displayed formula.

:::

:::

::: {.pf-step #s1-4}

For every $z\in D$,
$$
|f(z)|
\le
\frac{|a|+|g(z)|}{1-|a||g(z)|}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref} and the triangle inequalities,
$$
|a+g(z)|\le|a|+|g(z)|
$$
and
$$
|1+\overline a\,g(z)|
\ge
1-|a||g(z)|.
$$
The latter denominator is positive because $|a|,|g(z)|<1$. Dividing gives the claim.

:::

:::

::: {.pf-step #s1-5}

For every $z\in D$,
$$
\boxed{
|f(z)|
\le
\frac{|f(0)|+|z|}{1-|f(0)||z|}.}
$$


::: pf-proof

Set
$$
r=|z|.
$$
By step [](#s1-2){.pf-ref},
$$
|g(z)|\le r.
$$
Hence the numerator in step [](#s1-4){.pf-ref} satisfies
$$
|a|+|g(z)|\le|a|+r,
$$
while
$$
1-|a||g(z)|
\ge
1-|a|r>0.
$$
Therefore
$$
|f(z)|
\le
\frac{|a|+|g(z)|}{1-|a||g(z)|}
\le
\frac{|a|+r}{1-|a|r}.
$$
Since $a=f(0)$, this is exactly the stated inequality.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required bound.

:::

:::

:::
