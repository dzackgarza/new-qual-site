---
schema: qual/card@1
id: P-WESRA03-I10
kind: problem
title: Define the $L^p$ norm
classification:
  areas: [real-analysis]
  topics: [Function Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 10 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    section I, item 10 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item is "What is meant by the L^p norm of a
    function defined on a measure space (Y, tau(Y), mu)?" The card gives the
    definition for 1 <= p < infinity and for p = infinity, so no repair was
    needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The definitions
    are the answer; the proof block records why the quantity is a norm only on
    a.e. classes, and how the p = infinity case arises as a limit.
---

::: {.problem}
What is meant by the $L^p$ norm of a function on a measure space $(Y,\tau(Y),\mu)$?
:::

::: {.solution}

Let $(Y,\tau(Y),\mu)$ be a measure space and $f$ measurable. For $1\le
p<\infty$ the $L^p$ norm is
$$
\boxed{\norm{f}_p=\left(\int_Y\abs f^p\,d\mu\right)^{1/p},}
$$
and for $p=\infty$ it is $\norm{f}_\infty=\operatorname{ess\,sup}_{y\in
Y}\abs{f(y)}$, the least $M$ with $\abs f\le M$ $\mu$-almost everywhere. The
space $L^p(Y,\mu)$ consists of the a.e. equivalence classes with
$\norm{f}_p<\infty$.

::: pf

::: {.pf-step #definiteness}

$\norm{f}_p<\infty$ and $\norm{f}_p=0$ exactly when $f=0$ almost everywhere,
so the quantity is a norm on the a.e. classes and only a seminorm on
functions.

::: pf-proof

$\int_Y\abs f^p\,d\mu=0$ with $\abs f^p\ge0$ measurable forces $\abs f^p=0$
a.e., that is $f=0$ a.e.; conversely $f=0$ a.e. gives integral $0$. So
$\norm{f}_p=0$ holds for every function vanishing a.e. and for no other, which
is why the norm is taken on classes: on functions two distinct functions equal
a.e. have distance $0$.

:::

:::

::: {.pf-step #inequalities}

$\norm{\cdot}_p$ satisfies the triangle inequality (Minkowski) and
$\norm{cf}_p=\abs c\norm{f}_p$, so with step [](#definiteness){.pf-ref} it is
a norm on $L^p$; and $L^p$ is complete for it.

::: pf-proof

Homogeneity is immediate from $\abs{cf}^p=\abs c^p\abs f^p$ and pulling the
constant out of the integral. The triangle inequality is Minkowski's
inequality, which for $p=1$ is the triangle inequality for the integral and
for $1<p<\infty$ follows from Hölder's inequality applied to
$\abs{f+g}^p\le(\abs f+\abs g)\abs{f+g}^{p-1}$. Completeness is the
Riesz-Fischer theorem. These are the standard facts that make $L^p$ a Banach
space; the definition asked for is the norm itself.

:::

:::

::: {.pf-step #infinity}

For finite $\mu$ and $f$ essentially bounded, $\norm{f}_p\to\norm{f}_\infty$
as $p\to\infty$.

::: pf-proof

Let $M=\norm{f}_\infty$. Then $\abs f\le M$ a.e., so $\norm{f}_p\le
M\mu(Y)^{1/p}$, which tends to $M$. Conversely, for any $M'<M$ the set
$A=\{y:\abs f>M'\}$ has positive measure, and then $\norm{f}_p\ge
M'\mu(A)^{1/p}\to M'$; letting $M'\uparrow M$ gives $\liminf_p\norm{f}_p\ge
M$. The two bounds give the limit $M$, which is the sense in which the
essential supremum is the $p=\infty$ case of the family.

:::

:::

:::


:::
