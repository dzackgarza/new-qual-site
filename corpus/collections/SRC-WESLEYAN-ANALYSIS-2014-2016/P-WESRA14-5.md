---
schema: qual/card@1
id: P-WESRA14-5
kind: problem
title: 'Convergence off sets of small measure: a.e. convergence, and the converse by Egorov''s theorem'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. The source uses the name “convergence in measure” for the displayed exceptional-set-uniform definition (usually called almost uniform convergence). The card preserves the source definition rather than silently replacing it with the standard one.
---

::: {.problem}
Say that measurable $f_n$ converge *in measure* to $f$ if for every $\varepsilon>0$ there are $N$ and a measurable $B$ with $\mu(B)<\varepsilon$ such that
$$
\abs{f_n(x)-f(x)}<\varepsilon
$$
for every $n\ge N$ and every $x\notin B$.

(a) Under this definition, prove that some subsequence converges to $f$ almost everywhere.

(b) If $\mu(X)<\infty$ and $f_n\to f$ almost everywhere, prove convergence in the sense just defined.
:::

::: {.solution}

::: pf

::: pf-step

(a) If $f_n\to f$ in the sense defined, then the whole sequence $f_n$ converges to $f$ almost everywhere, so every subsequence does.

::: pf-proof

::: {.pf-step #choose}

For each $k\ge1$ there are $N_k$ and a measurable $B_k$ with $\mu(B_k)<2^{-k}$ and $\abs{f_n(x)-f(x)}<2^{-k}$ for all $n\ge N_k$ and $x\notin B_k$.

::: pf-proof

Apply the definition with $\varepsilon=2^{-k}$.

:::

:::

::: {.pf-step #null}

The set $E\coloneqq\bigcap_{m\ge1}\bigcup_{k\ge m}B_k$ is null.

::: pf-proof

For each $m$, countable subadditivity and step [](#choose){.pf-ref} give $\mu(E)\le\mu\qty{\bigcup_{k\ge m}B_k}\le\sum_{k\ge m}2^{-k}=2^{1-m}$.

:::

:::

::: pf-step

$f_n(x)\to f(x)$ for every $x\notin E$.

::: pf-proof

If $x\notin E$, there is $m$ with $x\notin B_k$ for all $k\ge m$.
Given $\eta>0$, choose $k\ge m$ with $2^{-k}<\eta$; by step [](#choose){.pf-ref}, $\abs{f_n(x)-f(x)}<\eta$ for all $n\ge N_k$.
Since $E$ is null by step [](#null){.pf-ref}, this is convergence almost everywhere.

:::

:::

:::

:::

::: pf-step

(b) If $\mu(X)<\infty$ and $f_n\to f$ almost everywhere, then $f_n\to f$ in the sense defined.

::: pf-proof

Let $\varepsilon>0$.
By Egorov's theorem, which needs $\mu(X)<\infty$, there is a measurable $B$ with $\mu(B)<\varepsilon$ such that $f_n\to f$ uniformly on $X\setminus B$.
Uniform convergence gives $N$ with $\abs{f_n(x)-f(x)}<\varepsilon$ for all $n\ge N$ and $x\in X\setminus B$, which is the definition.

:::

:::

:::

:::

::: {.remark}
The displayed definition is almost uniform convergence, not the standard definition of convergence in measure; part (b) is Egorov's theorem in that language.
:::
