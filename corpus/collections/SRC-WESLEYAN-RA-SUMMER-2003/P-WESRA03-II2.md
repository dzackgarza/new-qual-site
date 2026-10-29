---
schema: qual/card@1
id: P-WESRA03-II2
kind: problem
title: Tail measure decay for an integrable function
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 2 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf; Flash drops the arrow in the displayed limit, while the surrounding text and indexed limit expression determine the statement.
---

::: {.problem}
Let $f$ be Lebesgue integrable on $\RR$.
For each $n\in\NN$, define
$$
E_n=\{x\in\RR:|f(x)|\ge n\}.
$$
Show that
$$
\lim_{n\to\infty} n\,m(E_n)=0.
$$
:::

::: {.solution}

For
$$
E_n=\{x\in\RR:|f(x)|\ge n\},
$$
define
$$
g_n(x)=|f(x)|\,\mathbf 1_{E_n}(x).
$$

::: pf

::: {.pf-step #s1-1}

For every $x\in E_n$,
$$
\boxed{|f(x)|\ge n}.
$$


::: pf-proof

This is the definition of $E_n$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{
n\,\mathbf 1_{E_n}(x)
\le
|f(x)|\,\mathbf 1_{E_n}(x)}
$$
for every $x\in\RR$.


::: pf-proof

If $x\in E_n$, this is step [](#s1-1){.pf-ref}. If $x\notin E_n$, both sides are zero
except possibly the factor $|f(x)|$, which is multiplied by
$\mathbf 1_{E_n}(x)=0$.

:::

:::

::: pf-step

Integrating step [](#s1-2){.pf-ref},
$$
\boxed{
n\,m(E_n)
\le
\int_{E_n}|f|\,dm}.
$$


::: pf-proof

Integrate both sides over $\RR$:
$$
n\int\mathbf 1_{E_n}\,dm
\le
\int |f|\mathbf 1_{E_n}\,dm.
$$
The left side is
$$
n\,m(E_n),
$$
and the right side is
$$
\int_{E_n}|f|\,dm.
$$

:::

:::

::: pf-step

Since $f$ is Lebesgue integrable,
$$
\boxed{|f(x)|<\infty}
$$
for almost every $x\in\RR$.


::: pf-proof

If $|f|=\infty$ on a set of positive measure, then
$$
\int_{\RR}|f|\,dm
=
\infty,
$$
contradicting integrability.

:::

:::

::: {.pf-step #s1-5}

For almost every $x$,
$$
\boxed{
\mathbf 1_{E_n}(x)\longrightarrow0}.
$$


::: pf-proof

Fix $x$ with $|f(x)|<\infty$. For every integer
$$
n>|f(x)|,
$$
one has
$$
x\notin E_n.
$$
Thus $\mathbf 1_{E_n}(x)=0$ eventually.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
g_n(x)
=
|f(x)|\mathbf 1_{E_n}(x)
\longrightarrow0}
$$
for almost every $x$.


::: pf-proof

Combine the definition of $g_n$ with step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For every $n$,
$$
\boxed{
0\le g_n(x)\le|f(x)|}.
$$


::: pf-proof

The indicator satisfies
$$
0\le\mathbf 1_{E_n}\le1.
$$
Multiply by $|f(x)|\ge0$.

:::

:::

::: {.pf-step #s1-8}

By the dominated convergence theorem,
$$
\boxed{
\int_{\RR}g_n\,dm
\longrightarrow0}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, $g_n\to0$ almost everywhere. By step [](#s1-7){.pf-ref}, the functions are
dominated by the integrable function $|f|$. Therefore
$$
\int g_n\,dm
\to
\int0\,dm
=
0.
$$

:::

:::

::: {.pf-step #s1-9}

Equivalently,
$$
\boxed{
\int_{E_n}|f|\,dm
\longrightarrow0}.
$$


::: pf-proof

By definition,
$$
\int_{\RR}g_n\,dm
=
\int_{\RR}|f|\mathbf 1_{E_n}\,dm
=
\int_{E_n}|f|\,dm.
$$
Apply step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Since
$$
0\le n\,m(E_n)
\le
\int_{E_n}|f|\,dm,
$$
one has
$$
\boxed{
n\,m(E_n)\longrightarrow0}.
$$


::: pf-proof

The upper bound tends to $0$ by step [](#s1-9){.pf-ref}. Apply the squeeze theorem.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required limit.

:::

:::

:::
