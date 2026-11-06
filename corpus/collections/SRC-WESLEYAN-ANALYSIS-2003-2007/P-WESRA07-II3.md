---
schema: qual/card@1
id: P-WESRA07-II3
kind: problem
title: A measurable set contains subsets of every smaller prescribed measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md. Flash misrecognizes the measure symbol in m(B)=t, but the same statement defines m(A)>0 and asks for a subset of prescribed measure; the card normalizes that concrete extraction defect.
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
    2007, Part II problem 3 (assets/attachments/analysis_2003-2007.pdf, PDF page
    1), from the checked-in MinerU extraction and a 300 dpi render of the page.
    The printed problem takes a Lebesgue measurable A in R^2 with m(A) > 0 and
    asks, for each t in (0, m(A)), for a subset B of A with m(B) = t; the
    extraction writes the condition as "A(B) = t", which the render shows to be
    m(B) = t. The card states the problem as printed, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination; the proof is
    derived here, using continuity from below to reduce to a bounded set and
    dominated convergence to get a continuous distribution function, then the
    intermediate value theorem.
---

::: {.problem}
Let $A\subset\RR^2$ be Lebesgue measurable with $m(A)>0$.
Prove that for every
$$
0<t<m(A)
$$
there is a measurable subset $B\subset A$ with $m(B)=t$.
:::

::: {.solution}

Let $A\subset\RR^2$ be Lebesgue measurable with $m(A)>0$, where $m$ is planar
Lebesgue measure, and fix $0<t<m(A)$.

::: pf

::: {.pf-step #bounded}

There is $N$ such that $E=A\cap[-N,N]^2$ satisfies $m(E)>t$.

::: pf-proof

The sets $A\cap[-N,N]^2$ are measurable and increase with $N$, and their union
is $A$, since every point of the plane lies in some square $[-N,N]^2$.
Continuity from below for $m$, which holds because the sets are increasing
(and needs no finiteness), gives $m(A)=\lim_Nm(A\cap[-N,N]^2)$; as the limit
exceeds $t$, some term does.

:::

:::

::: {.pf-step #continuous}

$F(s)=m\bigl(E\cap((-\infty,s]\times\RR)\bigr)$ is continuous, with $F(s)=0$
for $s<-N$ and $F(s)=m(E)$ for $s\ge N$.

::: pf-proof

For $s<-N$ the set is empty because $E\subseteq[-N,N]^2$; for $s\ge N$ it is
all of $E$. For continuity, if $s_j\to s$ then $\mathbf
1_{E\cap((-\infty,s_j]\times\RR)}\to\mathbf 1_{E\cap((-\infty,s]\times\RR)}$
at every point whose first coordinate is not $s$, since membership depends
only on the first coordinate; the exceptional set $\{s\}\times\RR$ is a line,
hence of planar measure zero. The indicators are dominated by the integrable
function $\mathbf 1_E$, so dominated convergence gives $F(s_j)\to F(s)$, which
is sequential continuity, hence continuity.

:::

:::

::: {.pf-step #level}

There is a measurable $B\subseteq A$ with $m(B)=t$, namely
$B=E\cap((-\infty,s_0]\times\RR)$ for a point $s_0$ where $F(s_0)=t$.

::: pf-proof

$F$ is continuous by step [](#continuous){.pf-ref}, $F(-N)=0<t$ and
$F(N)=m(E)>t$ by step [](#bounded){.pf-ref} and the choice of $E$, so the
intermediate value theorem gives $s_0\in[-N,N]$ with $F(s_0)=t$. Then
$B=E\cap((-\infty,s_0]\times\RR)$ is measurable as an intersection of
measurable sets, is contained in $E\subseteq A$, and $m(B)=F(s_0)=t$. So every
value between $0$ and $m(A)$ is attained by a measurable subset of $A$.

:::

:::

:::


:::
