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
Suppose $f$ is analytic in the open unit disk $D$ and $\abs{f(z)}<1$ for all $z\in D$.
Let $a=f(0)$ and define
$$
g(z)=\frac{f(z)-a}{1-\overline a\,f(z)}.
$$
Using $g$ and the fact that $g$ maps $D$ to $D$, prove that
$$
\abs{f(z)}\le\frac{\abs{f(0)}+\abs{z}}{1-\abs{f(0)}\abs{z}}
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
The denominator is nonzero because $\abs{a}<1$.

:::

:::

::: {.pf-step #s1-2}

For every $z\in D$,
$$
\abs{g(z)}\le\abs{z}.
$$


::: pf-proof

By hypothesis, $g$ is an analytic self-map of the unit disk. Step [](#s1-1){.pf-ref} gives $g(0)=0$. Schwarz's lemma therefore yields
$$
\abs{g(z)}\le\abs{z}
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
Since $\abs{a}<1$ and $\abs{g(z)}<1$, one has
$$
\abs{\overline a\,g(z)}<1,
$$
so $1+\overline a\,g(z)\ne0$. Division gives the displayed formula.

:::

:::

::: {.pf-step #s1-4}

For every $z\in D$,
$$
\abs{f(z)}
\le
\frac{\abs{a}+\abs{g(z)}}{1-\abs{a}\abs{g(z)}}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref} and the triangle inequalities,
$$
\abs{a+g(z)}\le\abs{a}+\abs{g(z)}
$$
and
$$
\abs{1+\overline a\,g(z)}
\ge
1-\abs{a}\abs{g(z)}.
$$
The latter denominator is positive because $\abs{a},\abs{g(z)}<1$. Dividing gives the claim.

:::

:::

::: {.pf-step #s1-5}

For every $z\in D$,
$$
\boxed{
\abs{f(z)}
\le
\frac{\abs{f(0)}+\abs{z}}{1-\abs{f(0)}\abs{z}}.}
$$


::: pf-proof

Set
$$
r=\abs{z}.
$$
By step [](#s1-2){.pf-ref},
$$
\abs{g(z)}\le r.
$$
Hence the numerator in step [](#s1-4){.pf-ref} satisfies
$$
\abs{a}+\abs{g(z)}\le\abs{a}+r,
$$
while
$$
1-\abs{a}\abs{g(z)}
\ge
1-\abs{a}r>0.
$$
Therefore
$$
\abs{f(z)}
\le
\frac{\abs{a}+\abs{g(z)}}{1-\abs{a}\abs{g(z)}}
\le
\frac{\abs{a}+r}{1-\abs{a}r}.
$$
Since $a=f(0)$, this is exactly the stated inequality.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required bound.

:::

:::

:::
