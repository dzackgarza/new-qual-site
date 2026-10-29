---
schema: qual/card@1
id: P-WESRA13J-II4
kind: problem
title: 'Level sets and support of a nonnegative integrable function'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $(X,\mathcal B,\mu)$ be a measure space and let $f\ge0$ be integrable.

(a) Prove that for every $a>0$,
$$
\mu\{x:f(x)\ge a\}<\infty.
$$

(b) Prove that $\{x:f(x)>0\}$ is a countable union of sets of finite measure.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $a>0$,
$$
a\,\mu\{x:f(x)\geq a\}
\leq
\int_X f\,d\mu.
$$


::: pf-proof

Let
$$
E_a=\{x:f(x)\geq a\}.
$$
Since $f\geq0$, one has pointwise
$$
a\mathbf1_{E_a}\leq f.
$$
Integrating gives
$$
a\mu(E_a)
\leq\int_Xf\,d\mu.
$$

:::

:::

::: {.pf-step #s1-2}

For every $a>0$,
$$
\boxed{\mu\{x:f(x)\geq a\}<\infty}.
$$


::: pf-proof

Because $f$ is integrable,
$$
\int_Xf\,d\mu<\infty.
$$
Dividing the inequality in step [](#s1-1){.pf-ref} by $a>0$ yields
$$
\mu\{f\geq a\}
\leq\frac1a\int_Xf\,d\mu<\infty.
$$
This proves part (a).

:::

:::

::: {.pf-step #s1-3}

One has
$$
\{x:f(x)>0\}
=\bigcup_{n=1}^\infty\left\{x:f(x)\geq\frac1n\right\}.
$$


::: pf-proof

If $f(x)\geq1/n$ for some $n$, then $f(x)>0$. Conversely, if $f(x)>0$, choose $n$ so large that $1/n\leq f(x)$. Then $x$ belongs to the $n$-th set in the union.

:::

:::

::: {.pf-step #s1-4}

The set $\{x:f(x)>0\}$ is a countable union of sets of finite measure.


::: pf-proof

By step [](#s1-3){.pf-ref} it is the countable union of the measurable sets
$$
E_n=\left\{x:f(x)\geq\frac1n\right\}.
$$
Step [](#s1-2){.pf-ref} with $a=1/n$ gives $\mu(E_n)<\infty$ for every $n$. This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-4){.pf-ref} proves part (b).

:::

:::

:::
