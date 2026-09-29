---
schema: qual/card@1
id: P-JHUFA11ANE
kind: problem
title: 'An $L^2$-bounded sequence in $L^2$ of the line without convergent subsequences'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, September 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Give a sequence $(f_j)$ in $L^2(\RR)$ such that $\norm{f_j}_2=1$ for every $j$, but $(f_j)$ has no norm-convergent subsequence.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $j\ge1$, define
$$
f_j=\mathbf1_{[j,j+1]}.
$$
Then $\norm{f_j}_2=1$ for every $j$.

::: pf-proof

Indeed,
$$
\norm{f_j}_2^2=\int_j^{j+1}1\,dx=1.
$$

:::

:::

::: {.pf-step #s2}

Distinct terms satisfy
$$
\norm{f_j-f_k}_2=\sqrt2.
$$

::: pf-proof

If $j\ne k$, the supports are disjoint, so
$$
\norm{f_j-f_k}_2^2
=\norm{f_j}_2^2+\norm{f_k}_2^2
=2.
$$

:::

:::

::: {.pf-step #s3}

The sequence has no norm-convergent subsequence.

::: pf-proof

By step [](#s2){.pf-ref}, distinct terms are always distance $\sqrt2$ apart. Hence no subsequence is Cauchy in $L^2(\RR)$, so no subsequence converges in norm.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s3){.pf-ref} give the required sequence and its noncompactness property.

:::

:::

:::
