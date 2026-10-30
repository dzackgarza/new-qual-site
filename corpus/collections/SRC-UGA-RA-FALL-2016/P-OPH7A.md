---
schema: qual/card@1
id: P-OPH7A
kind: problem
title: 'Equal integrals of measurable functions: equality a.e. or a strict inequality
  on a subset'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UGA August 2016 real-analysis qualifying exam. The source assumes only measurability and equality of the displayed integrals; with extended-valued integrals this is false. The card is corrected to the natural L1 formulation.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $f,g\in L^1([a,b])$ be real-valued with
$$
\int_{a}^{b} f(x) ~d x=\int_{a}^{b} g(x) ~d x.
$$
Show that either

(a) $f(x) = g(x)$ almost everywhere, or

(b) There exists a measurable set $E \subseteq [a, b]$ such that
$$
\int _{E} f(x) \, dx > \int _{E} g(x) \, dx .
$$
:::

::: {.concept}
\envlist
- Monotonicity of the Lebesgue integral: $f\leq g$ on $A$ $\implies \int_A f \leq \int_A g$

:::

::: {.strategy}
Take the assumption and the negation of (1) and show (2).
The obvious move: define the set $A$ where they differ.
The non-obvious move: split $A$ itself up to get a strict inequality.

:::

::: {.solution}
Let $h\coloneqq f-g$, so $h\in L^1([a,b])$ and $\int_a^b h\,dx=0$.
Put $E_+\coloneqq\theset{h>0}$ and $E_-\coloneqq\theset{h<0}$.

::: pf

::: {.pf-step #positive-integral}

If $u\geq0$ is measurable and $m(\theset{u>0})>0$, then $\int u\,dx>0$.

::: pf-proof

Since $\theset{u>0}=\bigcup_{k\geq1}\theset{u\geq 1/k}$, countable subadditivity gives some $k$ with $m(\theset{u\ge1/k})>0$, and then
$$
\int u\,dx\ge \frac1k\,m(\theset{u\ge1/k})>0 .
$$

:::

:::

::: {.pf-step #both-null}

If $m(E_+)=m(E_-)=0$, then $f=g$ almost everywhere.

::: pf-proof

Then $h=0$ off the null set $E_+\cup E_-$.

:::

:::

::: {.pf-step #plus-positive}

If $m(E_+)+m(E_-)>0$, then $m(E_+)>0$.

::: pf-proof

Suppose $m(E_+)=0$. Then $m(E_-)>0$ and $h^+=0$ almost everywhere, so by step [](#positive-integral){.pf-ref} applied to $u=h^-$,
$$
\int_a^b h\,dx=-\int_a^b h^-\,dx<0,
$$
contradicting $\int_a^b h\,dx=0$.

:::

:::

::: {.pf-step #integral-on-plus}

If $m(E_+)>0$, then $\int_{E_+}f\,dx>\int_{E_+}g\,dx$.

::: pf-proof

Apply step [](#positive-integral){.pf-ref} to $u=h\chi_{E_+}\ge0$, which is positive exactly on $E_+$:
$$
\int_{E_+} f\,dx-\int_{E_+} g\,dx=\int_{E_+} h\,dx>0 .
$$

:::

:::

::: pf-qed

If $f=g$ almost everywhere fails, then $m(E_+)+m(E_-)>0$ by step [](#both-null){.pf-ref}, so $m(E_+)>0$ by step [](#plus-positive){.pf-ref}, and $E\coloneqq E_+$ satisfies alternative 2 by step [](#integral-on-plus){.pf-ref}.

:::

:::

:::
