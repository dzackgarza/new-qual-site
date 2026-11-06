---
schema: qual/card@1
id: P-WESRA04-P6
kind: problem
title: Completeness of $L^\infty$
classification:
  areas: [real-analysis]
  topics: [Function Spaces, Banach Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.3, problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the Wesleyan Preliminary Examination, Analysis, August 2, 2004,
    Real Analysis section 2.3 problem 6 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 35, printed page 3), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed problem is "Prove that
    L^infinity(X,B,mu) is complete in the L^infinity norm." The card states
    exactly this, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The proof is
    derived here, by extracting a rapidly Cauchy subsequence that is uniformly
    Cauchy off a null set, then passing to the full sequence.
---

::: {.problem}
Prove that $L^\infty(X,\mathcal B,\mu)$ is complete in the $L^\infty$ norm.
:::

::: {.solution}

Let $(f_n)$ be a Cauchy sequence in $L^\infty(X,\mathcal B,\mu)$ with respect
to $\norm{\cdot}_\infty$, the essential supremum norm, and recall that
$\abs{g}\le\norm{g}_\infty$ holds $\mu$-almost everywhere.

::: pf

::: {.pf-step #subsequence}

There is a subsequence $(f_{n_k})$ and a null set $N$ such that
$\abs{f_{n_{k+1}}(x)-f_{n_k}(x)}\le2^{-k}$ for all $k$ and all $x\notin N$.

::: pf-proof

Being Cauchy, the sequence has a subsequence with
$\norm{f_{n_{k+1}}-f_{n_k}}_\infty<2^{-k}$: choose $n_k$ inductively so that
$\norm{f_p-f_q}_\infty<2^{-k}$ for all $p,q\ge n_k$. For each $k$ the set
$N_k=\{\abs{f_{n_{k+1}}-f_{n_k}}>2^{-k}\}$ is null, because $2^{-k}$ exceeds
the essential supremum of the difference. Let $N=\bigcup_kN_k$, a countable
union of null sets, hence null; off $N$ all the displayed inequalities hold.

:::

:::

::: {.pf-step #limit}

There is $f\in L^\infty$ with $\norm{f-f_{n_k}}_\infty\to0$, and $f$ is
measurable.

::: pf-proof

For $x\notin N$ and $m>k$,
$\abs{f_{n_m}(x)-f_{n_k}(x)}\le\sum_{j=k}^{m-1}2^{-j}\le2^{1-k}$, so
$(f_{n_k}(x))$ is Cauchy in $\RR$; define $f(x)=\lim_kf_{n_k}(x)$ off $N$ and
$f=0$ on $N$. Then $f$ is measurable, being an a.e. pointwise limit of
measurable functions. Letting $m\to\infty$ in the displayed inequality gives
$\abs{f(x)-f_{n_k}(x)}\le2^{1-k}$ off $N$, so
$\norm{f-f_{n_k}}_\infty\le2^{1-k}\to0$; in particular $f$ is a bounded a.e.
limit of an $L^\infty$ function, hence lies in $L^\infty$.

:::

:::

::: {.pf-step #completeness}

$f_n\to f$ in $L^\infty$, so $L^\infty$ is complete.

::: pf-proof

Given $\varepsilon>0$, Cauchyness gives $N_0$ with
$\norm{f_m-f_n}_\infty<\varepsilon/2$ for $m,n\ge N_0$. Choose $k$ with
$n_k\ge N_0$ and $\norm{f_{n_k}-f}_\infty<\varepsilon/2$, possible by step
[](#limit){.pf-ref}. Then for $n\ge N_0$ the triangle inequality for the
essential supremum norm gives
$\norm{f_n-f}_\infty\le\norm{f_n-f_{n_k}}_\infty+\norm{f_{n_k}-f}_\infty<\varepsilon$.
So the Cauchy sequence converges in $L^\infty$, which is the completeness
asserted.

:::

:::

:::


:::
