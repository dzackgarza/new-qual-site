---
schema: qual/card@1
id: P-WESRA07-I1
kind: problem
title: State the dominated convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    2007, Part I item 1 (assets/attachments/analysis_2003-2007.pdf, PDF page 1),
    from the checked-in MinerU extraction and a 300 dpi render of the page. The
    printed item is "The dominated convergence theorem" under the instruction
    "Give precise statements of the following"; the card asks for exactly that,
    so no repair was needed. The card's statement is the standard one: a.e.
    convergence, a dominating L^1 function, and the conclusion that the
    integrals converge, with the L^1 convergence of f_n to f included.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination, so the proof is
    derived here. It proves the theorem from Fatou's lemma rather than quoting
    it, so that the statement stands as something proved and not only asserted.
---

::: {.problem}
Give a precise statement of the dominated convergence theorem.
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space and $(f_n)$ measurable
complex-valued functions with $f_n\to f$ $\mu$-almost everywhere. Suppose
there is $g\in L^1(\mu)$ with $\abs{f_n}\le g$ $\mu$-almost everywhere for
every $n$. Then $f\in L^1(\mu)$ and
$$
\lim_{n\to\infty}\int_X\abs{f_n-f}\,d\mu=0,
\qquad\text{in particular}\qquad
\boxed{\lim_{n\to\infty}\int_X f_n\,d\mu=\int_X f\,d\mu.}
$$

::: pf

::: {.pf-step #fatou}

If $h_n\ge0$ are measurable then $\displaystyle\int_X\liminf_n
h_n\,d\mu\le\liminf_n\int_X h_n\,d\mu$.

::: pf-proof

This is Fatou's lemma, which precedes the dominated convergence theorem. Put
$h=\liminf h_n$ and $k_j=\inf_{n\ge j}h_n$, so $k_j\uparrow h$ and $\int
k_j\to\int h$ by monotone convergence; and $k_j\le h_n$ for every $n\ge j$, so
$\int k_j\le\inf_{n\ge j}\int h_n$, whence $\int h\le\liminf_n\int h_n$.

:::

:::

::: {.pf-step #integral}

$f\in L^1(\mu)$ and $\displaystyle\int_X f_n\,d\mu\longrightarrow\int_X
f\,d\mu$.

::: pf-proof

$\abs{f_n}\to\abs f$ almost everywhere and $\abs{f_n}\le g$, so $\abs f\le g$
almost everywhere and $f\in L^1(\mu)$. Now $g+f_n\ge0$ and $g-f_n\ge0$ almost
everywhere, with $g+f_n\to g+f$ and $g-f_n\to g-f$ almost everywhere. Applying
step [](#fatou){.pf-ref} to each: first, $\int(g+f)\le\liminf\int(g+f_n)=\int
g+\liminf\int f_n$, which gives $\int f\le\liminf\int f_n$ since $\int g$ is
finite; second, $\int(g-f)\le\liminf\int(g-f_n)=\int g-\limsup\int f_n$, which
gives $\limsup\int f_n\le\int f$. Hence $\int f\le\liminf\int
f_n\le\limsup\int f_n\le\int f$ and the limit exists and equals $\int f$.

:::

:::

::: {.pf-step #l1}

$\displaystyle\lim_{n\to\infty}\int_X\abs{f_n-f}\,d\mu=0$.

::: pf-proof

The functions $h_n=\abs{f_n-f}$ are measurable and nonnegative, $h_n\to0$
almost everywhere, and $h_n\le\abs{f_n}+\abs f\le2g$ almost everywhere with
$2g\in L^1$. Applying step [](#integral){.pf-ref} to the sequence $(h_n)$ in
place of $(f_n)$, whose limit function is $0$, gives $\int h_n\to\int0=0$.
Hence $\int\abs{f_n-f}\to0$, and then $\left|\int f_n-\int
f\right|=\left|\int(f_n-f)\right|\le\int\abs{f_n-f}\to0$, which is the stated
consequence.

:::

:::

:::


:::
