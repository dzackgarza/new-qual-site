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
Let $f$ be Lebesgue integrable on $\mathbb R$.
For each $n\in\mathbb N$, define
\[
E_n=\{x\in\mathbb R:|f(x)|\ge n\}.
\]
Show that
\[
\lim_{n\to\infty} n\,m(E_n)=0.
\]
:::

::: {.solution}
For
\[
E_n=\{x\in\mathbb R:|f(x)|\ge n\},
\]
define
\[
g_n(x)=|f(x)|\,\mathbf 1_{E_n}(x).
\]

<1>1. For every \(x\in E_n\),
\[
\boxed{|f(x)|\ge n}.
\]

::: {.proof}
This is the definition of \(E_n\).
:::

<1>2. Therefore
\[
\boxed{
n\,\mathbf 1_{E_n}(x)
\le
|f(x)|\,\mathbf 1_{E_n}(x)}
\]
for every \(x\in\mathbb R\).

::: {.proof}
If \(x\in E_n\), this is step <1>1. If \(x\notin E_n\), both sides are zero
except possibly the factor \(|f(x)|\), which is multiplied by
\(\mathbf 1_{E_n}(x)=0\).
:::

<1>3. Integrating step <1>2,
\[
\boxed{
n\,m(E_n)
\le
\int_{E_n}|f|\,dm}.
\]

::: {.proof}
Integrate both sides over \(\mathbb R\):
\[
n\int\mathbf 1_{E_n}\,dm
\le
\int |f|\mathbf 1_{E_n}\,dm.
\]
The left side is
\[
n\,m(E_n),
\]
and the right side is
\[
\int_{E_n}|f|\,dm.
\]
:::

<1>4. Since \(f\) is Lebesgue integrable,
\[
\boxed{|f(x)|<\infty}
\]
for almost every \(x\in\mathbb R\).

::: {.proof}
If \(|f|=\infty\) on a set of positive measure, then
\[
\int_{\mathbb R}|f|\,dm
=
\infty,
\]
contradicting integrability.
:::

<1>5. For almost every \(x\),
\[
\boxed{
\mathbf 1_{E_n}(x)\longrightarrow0}.
\]

::: {.proof}
Fix \(x\) with \(|f(x)|<\infty\). For every integer
\[
n>|f(x)|,
\]
one has
\[
x\notin E_n.
\]
Thus \(\mathbf 1_{E_n}(x)=0\) eventually.
:::

<1>6. Hence
\[
\boxed{
g_n(x)
=
|f(x)|\mathbf 1_{E_n}(x)
\longrightarrow0}
\]
for almost every \(x\).

::: {.proof}
Combine the definition of \(g_n\) with step <1>5.
:::

<1>7. For every \(n\),
\[
\boxed{
0\le g_n(x)\le|f(x)|}.
\]

::: {.proof}
The indicator satisfies
\[
0\le\mathbf 1_{E_n}\le1.
\]
Multiply by \(|f(x)|\ge0\).
:::

<1>8. By the dominated convergence theorem,
\[
\boxed{
\int_{\mathbb R}g_n\,dm
\longrightarrow0}.
\]

::: {.proof}
By step <1>6, \(g_n\to0\) almost everywhere. By step <1>7, the functions are
dominated by the integrable function \(|f|\). Therefore
\[
\int g_n\,dm
\to
\int0\,dm
=
0.
\]
:::

<1>9. Equivalently,
\[
\boxed{
\int_{E_n}|f|\,dm
\longrightarrow0}.
\]

::: {.proof}
By definition,
\[
\int_{\mathbb R}g_n\,dm
=
\int_{\mathbb R}|f|\mathbf 1_{E_n}\,dm
=
\int_{E_n}|f|\,dm.
\]
Apply step <1>8.
:::

<1>10. Since
\[
0\le n\,m(E_n)
\le
\int_{E_n}|f|\,dm,
\]
one has
\[
\boxed{
n\,m(E_n)\longrightarrow0}.
\]

::: {.proof}
The upper bound tends to \(0\) by step <1>9. Apply the squeeze theorem.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required limit.
:::
:::
