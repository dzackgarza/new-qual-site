---
schema: qual/card@1
id: P-WESRA07-I4
kind: problem
title: State Egorov's theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Read against the Wesleyan analysis qualifier, Real Analysis section, Summer
    2007, Part I item 4 (assets/attachments/analysis_2003-2007.pdf, PDF page 1),
    from the checked-in MinerU extraction and a 300 dpi render of the page. The
    printed item is "Egorov's theorem", under "Give precise statements of the
    following". The card's statement is Egorov's theorem with the finiteness of
    the measure stated as a hypothesis, which the printed item leaves implicit
    because the whole section is about finite-measure spaces; the card's form is
    correct as it stands, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The theorem is
    proved here rather than only stated, so that the card carries a proof of the
    assertion it is asked to state.
---

::: {.problem}
Give a precise statement of Egorov's theorem.
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space with $\mu(X)<\infty$, let $f_n,f$
be measurable and suppose $f_n\to f$ $\mu$-almost everywhere. Egorov's theorem
asserts that $f_n\to f$ almost uniformly: for every $\varepsilon>0$ there is
$E\in\mathcal A$ with $\mu(E)<\varepsilon$ such that $f_n\to f$ uniformly on
$X\setminus E$.

::: pf

::: {.pf-step #negligible}

Let $N$ be a null set off which $f_n\to f$ pointwise, and for $k,j\ge1$ put
$$
A_{k,j}=\bigcup_{n\ge j}\left\{x\in X\setminus N:\abs{f_n(x)-f(x)}>\tfrac1k\right\}.
$$
Then each $A_{k,j}$ is measurable, $A_{k,j+1}\subseteq A_{k,j}$, and
$\bigcap_jA_{k,j}=\emptyset$.

::: pf-proof

Each set in the union is measurable because $f_n-f$ is measurable and
$(1/k,\infty)$ is open; a countable union of measurable sets is measurable.
The sets are nested because the union defining $A_{k,j+1}$ has fewer terms. If
$x\in\bigcap_jA_{k,j}$ with $x\notin N$, then for every $j$ there is $n\ge j$
with $\abs{f_n(x)-f(x)}>1/k$, which contradicts $f_n(x)\to f(x)$; points of
$N$ are excluded by the definition. So the intersection is empty.

:::

:::

::: {.pf-step #measure}

For each $k$ there is $j_k$ with $\mu(A_{k,j_k})<\varepsilon/2^{k+1}$.

::: pf-proof

$\mu(A_{k,1})\le\mu(X)<\infty$, so continuity of $\mu$ from above on a
decreasing sequence of finite-measure sets gives
$\mu(A_{k,j})\to\mu(\bigcap_jA_{k,j})=\mu(\emptyset)=0$; hence some $j_k$ has
$\mu(A_{k,j_k})<\varepsilon/2^{k+1}$. This is the only place where
$\mu(X)<\infty$ is used, and without it the theorem fails.

:::

:::

::: {.pf-step #uniform}

$E=\bigcup_kA_{k,j_k}$ has $\mu(E)<\varepsilon$, and $f_n\to f$ uniformly on
$X\setminus E$.

::: pf-proof

$\mu(E)\le\sum_k\mu(A_{k,j_k})<\sum_k\varepsilon/2^{k+1}=\varepsilon$. If
$x\in X\setminus E$ then $x\notin A_{k,j_k}$ for every $k$, so for every $n\ge
j_k$ one has $\abs{f_n(x)-f(x)}\le1/k$; given $\delta>0$ choose $k>1/\delta$
and then $N=j_k$, and for all $n\ge N$ and all such $x$ simultaneously
$\abs{f_n(x)-f(x)}\le1/k<\delta$. That is uniform convergence on $X\setminus
E$, and $E$ is measurable as a countable union of measurable sets.

:::

:::

:::


:::
