---
schema: qual/card@1
id: P-WESRA07-II6
kind: problem
title: The printed integral functional is not a norm on $C([0,1])$
classification:
  areas: [real-analysis]
  topics: [Function Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, item 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md. Flash explicitly prints the functional as integral f dm without absolute values; the card preserves and diagnoses that printed defect.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
The source defines, for $f\in C([0,1],\mathbb R)$,
\[
\|f\|:=\int_0^1 f\,dm
\]
and asks:

1. Explain why this defines a norm on $C([0,1])$.

2. Is $C([0,1])$ complete with respect to this norm?

Is the printed claim valid?
If not, identify the defect.
For comparison, also answer the completeness question for the likely corrected formula
\[
\|f\|_1:=\int_0^1|f|\,dm.
\]
:::

::: solution
<1>1. The printed formula does not define a norm.
::: proof
A norm must be nonnegative.
For the continuous function $f\equiv-1$,
\[
\int_0^1 f\,dm=-1<0.
\]
It also fails positive definiteness: for
\[
f(x)=x-\frac12,
\]
we have $f\not\equiv0$ but
\[
\int_0^1f(x)\,dx=0.
\]
Hence
\[
\boxed{f\longmapsto\int_0^1f\,dm\text{ is not a norm on }C([0,1]).}
\]
Therefore part 2 of the source, literally interpreted as completeness with respect to "this norm," is not well posed.
:::

<1>2. With the absolute value inserted, the formula is a norm but $C([0,1])$ is not complete.
::: proof
The functional
\[
\|f\|_1=\int_0^1|f(x)|\,dx
\]
is a norm on $C([0,1])$: homogeneity and the triangle inequality are immediate, and if $\|f\|_1=0$, then $|f|=0$ almost everywhere.
Since $f$ is continuous, this forces $f\equiv0$.

To see incompleteness, let
\[
h=\mathbf1_{[1/2,1]}.
\]
Choose continuous functions $h_n$ such that
\[
h_n(x)=0\quad(x\le 1/2-1/n),
\qquad
h_n(x)=1\quad(x\ge1/2+1/n),
\]
and interpolate linearly on the interval between these two points.
Then
\[
\|h_n-h\|_1\le\frac2n\longrightarrow0.
\]
Thus $(h_n)$ is Cauchy in the $L^1$ norm.

If it converged in that norm to some $g\in C([0,1])$, uniqueness of $L^1$ limits would give $g=h$ almost everywhere.
Continuity would then force $g=0$ on $(0,1/2)$ and $g=1$ on $(1/2,1)$, which is impossible at $x=1/2$.
Hence no continuous $L^1$ limit exists.

Therefore, for the corrected norm,
\[
\boxed{C([0,1])\text{ is not complete under }\|\cdot\|_1.}
\]
:::
:::
