---
schema: qual/card@1
id: P-WESCA08-I2
kind: problem
title: 'Define local uniform convergence'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Theorems and Definitions, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $U\subset\CC$ be open, let $f_n:U\to\CC$, and let $f:U\to\CC$.
Define what it means for $(f_n)$ to converge normally (locally uniformly) to $f$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The sequence $(f_n)$ converges locally uniformly to $f$ on $U$ if
for every compact set
$$
K\subset U
$$
one has
$$
\boxed{
\sup_{z\in K}\abs{f_n(z)-f(z)}
\longrightarrow0}.
$$


::: pf-proof

This is the definition of uniform convergence on each compact subset of the
domain.

:::

:::

::: {.pf-step #s1-2}

Equivalently, for every compact $K\subset U$ and every
$$
\varepsilon>0,
$$
there exists
$$
N=N(K,\varepsilon)
$$
such that
$$
\boxed{
\abs{f_n(z)-f(z)}<\varepsilon}
$$
for every $z\in K$ and every $n\ge N$.


::: pf-proof

The statement
$$
\sup_{z\in K}\abs{f_n(z)-f(z)}\to0
$$
means exactly that eventually the supremum is $<\varepsilon$, which is
equivalent to the displayed pointwise inequality holding simultaneously for
all $z\in K$.

:::

:::

::: pf-step

The index $N$ may depend on the compact set $K$, so local uniform
convergence is weaker than uniform convergence on all of $U$.


::: pf-proof

Uniform convergence on $U$ would require one $N(\varepsilon)$ that works
for every point of the entire domain. The local version only requires such
uniform control separately on each compact subset.

:::

:::

::: pf-step

This mode of convergence is also called normal convergence in the
terminology used by the source.


::: pf-proof

This is the terminology requested in the problem statement.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the requested definition and its equivalent
$\varepsilon$-form.

:::

:::

:::
