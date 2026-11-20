---
schema: qual/card@1
id: E-SS5.PR-1
kind: problem
title: Zeros of a bounded holomorphic function satisfy the Blaschke condition
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the removal of a zero at the origin, Jensen's formula, the bound (1), the monotone limit $R\uparrow1$, and the inequality $-\log t\ge1-t$ on $(0,1)$ which converts the logarithmic series into $\sum(1-\abs{z_n})$.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` at its printed folio (the scan runs nineteen pages ahead of the
    printed page): the statement is Problem 1 at the head of the Chapter 5 Problems, printed
    p. 156, and its printed words are the card's. The chapter, the problem number and the page
    are now named in the solution's opening sentence. Not checked in this pass: the argument, which
    the edit does not touch.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Asterisk status read from the book: Chapter 5 sets its asterisks before Problems 2, 3 and 4 only, so
    none stands before Problem 1. The remark records that. The locator by numbered statement is
    Chapter 5, Problem 1; the page readings in the earlier events are superseded by it. Not checked in this pass: the wording of the statement and the argument.
---

::: {.exercise}
This is Problem 1 of Chapter 5 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`; the statement below is its wording.

Prove that if $f$ is holomorphic in the unit disc, bounded, and not identically zero, and $z_1,z_2,\ldots$ are its zeros, with $\abs{z_k}<1$, then

$$
\sum_n(1-\abs{z_n})<\infty.
$$

*Hint.* Use Jensen's formula.
:::

::: {.remark}
The book sets no asterisk before this problem (Chapter 5, Problem 1).
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own.

::: pf

::: {.pf-step #origin}
It suffices to prove the assertion when $f(0)\neq0$.

::: pf-proof
If $f$ has a zero of order $m$ at $0$, write $f(z)=z^mg(z)$ with $g$ holomorphic, bounded and $g(0)\neq0$; the zeros of $f$ are those of $g$ together with $0$ repeated, so the series for $f$ differs from that for $g$ by a finite sum.
:::
:::

::: {.pf-step #jensen}
For $0<r<1$ with no zero on $\abs{z}=r$, $\sum_{\abs{z_n}<r}\log\frac{r}{\abs{z_n}}\le\log\frac{M}{\abs{f(0)}}$.

::: pf-proof
Jensen's formula gives $\log\abs{f(0)}+\sum_{\abs{z_n}<r}\log\frac{r}{\abs{z_n}}=\frac{1}{2\pi}\int_0^{2\pi}\log\abs{f(re^{i\theta})} d\theta$, and the integrand is at most $\log M$ because $\abs{f}\le M$; rearranging gives the bound.
:::
:::

::: {.pf-step #fixed}
For every fixed $0<R<1$, $\sum_{\abs{z_n}<R}\log\frac{1}{\abs{z_n}}\le\log\frac{M}{\abs{f(0)}}$.

::: pf-proof
Take $r>R$ in step [](#jensen){.pf-ref}: since $r>\abs{z_n}$ for the zeros counted, $\log\frac{r}{\abs{z_n}}\ge\log\frac{1}{\abs{z_n}}$, so the partial sum for $R$ is bounded by the left side of the Jensen inequality.
:::
:::

::: {.pf-step #series}
$\sum_n\log\frac{1}{\abs{z_n}}<\infty$.

::: pf-proof
The partial sums over $\abs{z_n}<R$ increase with $R$ and are bounded by the constant of step [](#fixed){.pf-ref} for every $R<1$; by monotone convergence the full series converges.
:::
:::

::: {.pf-step #conclusion}
$\sum_n(1-\abs{z_n})<\infty$.

::: pf-proof
For $0<t<1$ one has $-\log t=\int_t^1\frac{ds}{s}\ge\int_t^1ds=1-t$, so each term $1-\abs{z_n}$ is at most $\log\frac{1}{\abs{z_n}}$, and the comparison with step [](#series){.pf-ref} gives convergence.
:::
:::

:::
:::
