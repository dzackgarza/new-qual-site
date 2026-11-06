---
schema: qual/card@1
id: P-WESRA07-II4
kind: problem
title: A finite measure invariant under a nonzero translation is zero
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, item 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    2007, Part II problem 4 (assets/attachments/analysis_2003-2007.pdf, PDF page
    1), from the checked-in MinerU extraction and a 300 dpi render of the page.
    The printed problem takes a finite Borel measure on R with mu(A + t) = mu(A)
    for all Borel A and some t > 0, and asks for a proof that mu is zero. The
    card states exactly this, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination; the proof is
    derived here, from the disjoint translates of a half-open interval of length
    t, finite additivity, and inner regularity of a finite Borel measure.
---

::: {.problem}
Let $\mu$ be a finite Borel measure on $\RR$.
Suppose there is $t>0$ such that
$$
\mu(A+t)=\mu(A)
$$
for every Borel set $A\subset\RR$.
Prove that $\mu$ is the zero measure.
:::

::: {.solution}

Let $\mu$ be a finite Borel measure on $\RR$ and $t>0$ with $\mu(A+t)=\mu(A)$
for every Borel $A$.

::: pf

::: {.pf-step #interval}

$\mu([0,t))=0$.

::: pf-proof

The translates $[kt,(k+1)t)=[0,t)+kt$, $k\in\ZZ$, are pairwise disjoint, and
by translation invariance each has measure $\mu([0,t))$. Finite additivity
over the disjoint union of the first $N$ of them, together with monotonicity,
gives $\mu(\RR)\ge\sum_{k=0}^{N-1}\mu([0,t)+kt)=N\mu([0,t))$ for every $N$. If
$\mu([0,t))>0$ the right side exceeds the finite number $\mu(\RR)$ for large
$N$; hence $\mu([0,t))=0$.

:::

:::

::: {.pf-step #intervals}

$\mu(J)=0$ for every bounded interval $J=[a,b]$, and then $\mu(B)=0$ for every
Borel set $B$.

::: pf-proof

Choose $k$ with $a-kt\in[0,t)$. Each translate $[a-kt,a-kt+t)+jt$ has measure
$\mu([a-kt,a-kt+t))\le\mu([0,t))+\mu([t,2t))=0$, using step
[](#interval){.pf-ref} and $[t,2t)=[0,t)+t$, and the $M+1$ of them with
$j=0,\dots,M=\lfloor(b-a)/t\rfloor$ cover $J$; so $\mu(J)=0$ by subadditivity
and positivity. A finite Borel measure on $\RR$ is inner regular, so for Borel
$B$ and $\varepsilon>0$ there is compact $K\subseteq B$ with
$\mu(B)<\mu(K)+\varepsilon$; $K$ is bounded, hence inside a bounded interval
of measure $0$, so $\mu(K)=0$ and $\mu(B)<\varepsilon$ for every
$\varepsilon>0$, giving $\mu(B)=0$.

:::

:::

::: {.pf-step #zero}

$\mu$ is the zero measure.

::: pf-proof

$\RR=\bigcup_n[-n,n]$ with the intervals bounded and increasing, so
$\mu(\RR)=\lim_n\mu([-n,n])=0$ by step [](#intervals){.pf-ref}; and a positive
measure vanishing on $\RR$ vanishes on every measurable set. So no nonzero
finite Borel measure on the line is invariant under a nonzero translation,
which is the assertion.

:::

:::

:::


:::
