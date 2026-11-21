---
schema: qual/card@1
id: P-RASP13B
kind: problem
title: '$t\,\mu\{\abs{f}\geq t\}\to0$ for $f\in L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Distribution Functions
  - Chebyshev Inequality
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's proof into numbered steps and removed the nested proof div, keeping the
    argument identical. Checked: the pointwise inequality on E_t, the monotone decrease of E_t to
    the empty set up to a null set, the domination by |f|, and the squeeze. Not checked against a
    printed source: the UCSD real analysis examinations are not retained in tmp/sources and the
    card records no page.
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space and $f \in L^1(\mu)$.
Prove that
$$
\lim_{t \to \infty} t \, \mu\{x \in X : \abs{f(x)} \geq t\} = 0.
$$
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $(X,\mathcal{M},\mu)$ is a measure space and $f\in L^{1}(\mu)$; $E_t=\theset{x\in X\mid\abs{f(x)}\geq t}$, and the criterion used is the dominated convergence theorem.

::: pf

::: {.pf-step #markov}

$t\,\mu(E_t)\leq\int_{E_t}\abs{f}\,d\mu$.

::: pf-proof

On $E_t$ one has $t\leq\abs{f(x)}$ pointwise, so $t\,\mu(E_t)=\int_{E_t}t\,d\mu\leq\int_{E_t}\abs{f}\,d\mu$.

:::

:::

::: {.pf-step #dct}

$\int_{E_t}\abs{f}\,d\mu\to0$ as $t\to\infty$.

::: pf-proof

The functions $\abs{f}\mathbf{1}_{E_t}$ are dominated by the integrable $\abs{f}$ and tend to $0$ pointwise at every $x$ with $\abs{f(x)}<\infty$, since $x\notin E_t$ once $t>\abs{f(x)}$; and $\abs{f}<\infty$ almost everywhere because $f\in L^{1}$. The dominated convergence theorem gives the limit $\int_X0\,d\mu=0$.

:::

:::

::: {.pf-step #done}

$\lim_{t\to\infty}t\,\mu\theset{x\in X\mid\abs{f(x)}\geq t}=0$.

::: pf-proof

Step [](#markov){.pf-ref} bounds $t\,\mu(E_t)$ between $0$ and the quantity of step [](#dct){.pf-ref}, which tends to $0$.

:::

:::

:::

:::
