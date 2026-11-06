---
schema: qual/card@1
id: P-WESRA03-I4
kind: problem
title: State the Lebesgue dominated convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Read against the Wesleyan Preliminary Examination, Analysis, August 4, 2003,
    section I, item 4 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item is "State the Lebesgue Dominated Convergence
    Theorem." The card states it with a.e. convergence, a dominating L^1
    function, and the conclusion in both the L^1 and the integral form, so no
    repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The statement is
    the answer; the proof block records the deduction of the integral form from
    the L^1 form and the failure of the conclusion when the domination is
    dropped, which delineates the statement rather than replacing it.
---

::: {.problem}
State the Lebesgue Dominated Convergence Theorem.
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space, $f_n$ measurable with $f_n\to f$
$\mu$-almost everywhere, and suppose there is $g\in L^1(\mu)$ with
$\abs{f_n}\le g$ $\mu$-almost everywhere for every $n$. Then $f\in L^1(\mu)$,
$\norm{f_n-f}_1\to0$, and in particular
$$
\boxed{\int_Xf_n\,d\mu\longrightarrow\int_Xf\,d\mu.}
$$

::: pf

::: {.pf-step #integralform}

If $f_n,f\in L^1(\mu)$ and $\norm{f_n-f}_1\to0$, then
$\int_Xf_n\,d\mu\to\int_Xf\,d\mu$.

::: pf-proof

$\left|\int f_n-\int
f\right|=\left|\int(f_n-f)\right|\le\int\abs{f_n-f}=\norm{f_n-f}_1$, by the
triangle inequality for the integral applied to the real and imaginary parts,
and the right side tends to $0$. This is the deduction by which the theorem is
applied, and it is all that is needed when only the integrals are in question.

:::

:::

::: {.pf-step #sharpness}

The domination cannot be dropped: with Lebesgue measure on $\RR$,
$f_n=\mathbf1_{[n,n+1]}$ converges pointwise to $0$ while $\int f_n=1$ for
every $n$.

::: pf-proof

For each $x$ there is at most one $n$ with $x\in[n,n+1)$ and none for large
$n$, so $f_n(x)\to0$; each $f_n$ has integral $1$ over its interval of length
one. No integrable dominating function exists, since $\sup_nf_n=1$ is
integrable but $\abs{f_n}\le g$ with $\int g<\infty$ would force
$\sum_n\int_{[n,n+1]}g<\infty$ to dominate an infinite sum of $1$s; the
conclusion fails, which shows that the hypothesis $\abs{f_n}\le g$ with $g\in
L^1$ is essential.

:::

:::

:::


:::
