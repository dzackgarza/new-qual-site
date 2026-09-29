---
schema: qual/card@1
id: P-JHUSP07ANF
kind: problem
title: '$L^4$ functions with vanishing $L^1$ norm converge weakly'
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, Spring 2007, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_n)$ be a sequence in $L^4([0,1])$ such that
\[
\int_0^1|f_n|^4\le1
\qquad\text{for all }n,
\]
and
\[
\int_0^1|f_n|\longrightarrow0.
\]
Show that $f_n\rightharpoonup0$ weakly in $L^4([0,1])$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The part of the pairing where $g$ is bounded tends to zero.

::: pf-proof

Let $g\in L^{4/3}([0,1])$ and fix $\varepsilon>0$. Since
$$
|g|^{4/3}\in L^1([0,1]),
$$
choose $M>0$ so large that
$$
\|g\mathbf 1_{\{|g|>M\}}\|_{4/3}<\frac\varepsilon2.
$$
This is possible by the [[T-IJQQG|dominated convergence theorem]] applied as $M\to\infty$.

Split
$$
\int_0^1 f_n g
=
\int_{\{|g|\le M\}}f_ng
+
\int_{\{|g|>M\}}f_ng.
$$
For the bounded part,
$$
\left|\int_{\{|g|\le M\}}f_ng\right|
\le M\|f_n\|_1\longrightarrow0.
$$

:::

:::

::: {.pf-step #s2}

The tail of the pairing is uniformly small.

::: pf-proof

The [[PR-7BGSE|Hölder inequality]] and the uniform $L^4$ bound give
$$
\left|\int_{\{|g|>M\}}f_ng\right|
\le \|f_n\|_4\,\|g\mathbf 1_{\{|g|>M\}}\|_{4/3}
\le \frac\varepsilon2.
$$

:::

:::

::: {.pf-step #s3}

The sequence converges weakly to zero.

::: pf-proof

Hence for all sufficiently large $n$,
$$
\left|\int_0^1 f_n g\right|<\varepsilon.
$$
Since $g\in L^{4/3}$ was arbitrary, the [[T-5BFVS|duality of $L^p$ spaces]] shows that this is exactly
$$
f_n\rightharpoonup0\quad\text{in }L^4([0,1]).
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove convergence against every element of the dual space $L^{4/3}([0,1])$.

:::

:::

:::
