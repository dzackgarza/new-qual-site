---
schema: qual/card@1
id: P-WESRA03-I8
kind: problem
title: Continuity from above requires finite measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 8 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    section I, item 8 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item takes a measure mu on (Y, tau(Y)) and a
    decreasing sequence F_n of sets in tau(Y) and asks whether
    mu(intersection F_n) = lim mu(F_n). The card asks the same question, answers
    no in general, and states the finiteness condition under which the identity
    does hold, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. Both halves are
    derived here: the half-line counterexample, and continuity from above proved
    from continuity from below under mu(F_1) < infinity.
---

::: {.problem}
Let $\mu$ be a measure and let $F_1\supseteq F_2\supseteq\cdots$ be measurable.
Is it always true that
$$
\mu\!\left(\bigcap_{n=1}^\infty F_n\right)=\lim_{n\to\infty}\mu(F_n)?
$$
:::

::: {.solution}

Let $\mu$ be a measure on $(Y,\tau(Y))$ and $F_1\supseteq F_2\supseteq\cdots$
measurable. The identity $\mu\bigl(\bigcap_nF_n\bigr)=\lim_n\mu(F_n)$ is not
true in general; it holds when $\mu(F_1)<\infty$.

::: pf

::: {.pf-step #counterexample}

With Lebesgue measure on $\RR$ and $F_n=[n,\infty)$, the sets decrease, their
intersection is empty, and yet $\mu(F_n)=\infty$ for every $n$.

::: pf-proof

$[n+1,\infty)\subseteq[n,\infty)$ gives the decrease; a real $x$ lies in the
intersection only if $x\ge n$ for every $n$, which is impossible, so the
intersection is empty and has measure $0$. Each $F_n$ is a half-line, of
infinite Lebesgue measure, so $\lim_n\mu(F_n)=\infty\ne0$.

:::

:::

::: {.pf-step #finite}

If $\mu(F_1)<\infty$ then $\mu\bigl(\bigcap_nF_n\bigr)=\lim_n\mu(F_n)$.

::: pf-proof

The complements $E_n=F_1\setminus F_n$ are measurable and increase to
$F_1\setminus\bigcap_nF_n$; continuity from below gives
$\mu(E_n)\to\mu(F_1)-\mu(\bigcap F_n)$. Since $F_n\subseteq F_1$ and
$\mu(F_1)<\infty$, we have $\mu(E_n)=\mu(F_1)-\mu(F_n)$ by finite additivity.
So $\mu(F_1)-\mu(F_n)\to\mu(F_1)-\mu(\bigcap F_n)$, and subtracting from the
finite number $\mu(F_1)$ gives the identity. Without the finiteness the
subtraction is illegitimate, which is exactly how the counterexample of step
[](#counterexample){.pf-ref} evades the argument.

:::

:::

::: {.pf-step #answer}

The answer to the printed question is no as stated, and yes with the
finiteness hypothesis.

::: pf-proof

Step [](#counterexample){.pf-ref} gives a decreasing sequence of measurable
sets and a measure for which the identity fails, so the identity is not a
theorem of measure theory in general; step [](#finite){.pf-ref} shows that the
failure is exactly the absence of the hypothesis $\mu(F_1)<\infty$, under
which the identity does hold. This is the decreasing counterpart of the
continuity-from-below result proved on [[P-WESRA07-II1]].

:::

:::

:::


:::
