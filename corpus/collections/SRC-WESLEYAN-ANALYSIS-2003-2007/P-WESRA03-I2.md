---
schema: qual/card@1
id: P-WESRA03-I2
kind: problem
title: Define a measure on a measurable space
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    section I, item 2 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item is "Given a pair (Y, tau(Y)) as above, define
    what is meant by a measure on (Y, tau(Y))", where the preceding item
    introduced tau(Y) as a sigma-algebra. The card gives the definition with
    countable additivity, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The definition is
    the answer; the proof block derives monotonicity and finite additivity from
    it, which are the properties the section's later items use.
---

::: {.problem}
Define a measure on a measurable space $(Y,\tau(Y))$.
:::

::: {.solution}

Let $(Y,\tau(Y))$ be a measurable space, that is $Y$ a set and $\tau(Y)$ a
$\sigma$-algebra of subsets of $Y$. A measure on it is a function
$\mu\colon\tau(Y)\to[0,\infty]$ with $\mu(\emptyset)=0$ and
$$
\boxed{\mu\left(\bigcup_{n=1}^\infty E_n\right)=\sum_{n=1}^\infty\mu(E_n)}
$$
for every sequence $(E_n)$ of pairwise disjoint sets in $\tau(Y)$. It is
finite if $\mu(Y)<\infty$ and $\sigma$-finite if $Y$ is a countable union of
sets of finite measure.

::: pf

::: {.pf-step #monotone}

$\mu$ is monotone and finitely additive, and $\mu(A\setminus B)=\mu(A)-\mu(B)$
when $B\subseteq A$ and $\mu(B)<\infty$.

::: pf-proof

For $B\subseteq A$ write $A=B\cup(A\setminus B)$ as a disjoint union with
empty further terms; countable additivity gives $\mu(A)=\mu(B)+\mu(A\setminus
B)$, which is monotonicity and, when $\mu(B)<\infty$, the subtraction formula.
Finite additivity for disjoint $E_1,\dots,E_m$ follows by taking
$E_n=\emptyset$ for $n>m$, using $\mu(\emptyset)=0$.

:::

:::

::: {.pf-step #continuity}

If $A_n\in\tau(Y)$ increase to $A$ then $\mu(A_n)\to\mu(A)$; if they decrease
to $A$ and $\mu(A_1)<\infty$ then $\mu(A_n)\to\mu(A)$.

::: pf-proof

For the increasing case, the sets $B_1=A_1$ and $B_n=A_n\setminus A_{n-1}$ are
disjoint with union $A$, and $\mu(A_n)=\sum_{k\le n}\mu(B_k)$ by finite
additivity, so $\mu(A_n)$ are the partial sums of the series whose sum is
$\mu(A)$. For the decreasing case apply the increasing result to $A_1\setminus
A_n$, which increase to $A_1\setminus A$, and subtract using step
[](#monotone){.pf-ref}, which requires $\mu(A_1)<\infty$.

:::

:::

:::


:::
