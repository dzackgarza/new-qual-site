---
schema: qual/card@1
id: P-PRACT20-W6-11
kind: problem
title: Open, closed and uncountable sets containing $\QQ$
classification:
  areas:
  - prelim
  topics:
  - Topology of the Real Line
  - Lebesgue Measure
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray figure caption from another page and separated the choices, checked against Week6_solns.pdf page 5 (Problem 11).
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 5 of the retained solutions booklet GRE Prep: Miscellaneous
    Practice Problem Solutions by Christian Parkinson
    (assets/attachments/prelim-practice-week6-2020/page-5.png), which prints this
    problem together with a worked solution; the practice sheet itself is not
    retained and the collection's provenance list is empty, so the statement was
    compared with the card from that page: the printed problem lists the same five statements (A) to (E) for sets A with Q contained in A contained in R, as the card does
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The printed page gives the statement only, its solution being on a page that is not retained; the five verdicts are derived here, two of them necessarily true and three refuted by the irrationals and by Q itself.
---

::: {.problem}
Which of the following necessarily holds for $\QQ \subseteq A \subseteq \RR$?

(A) If $A$ is open, then $A = \RR$.

(B) If $A$ is closed, then $A = \RR$.

(C) If $A$ is uncountable, then $A = \RR$.

(D) If $A$ is uncountable, then $A$ is open.

(E) If $A$ is countable, then $A$ is closed.
:::

::: {.solution}

Let $A$ satisfy $\QQ\subseteq A\subseteq\RR$. The statements (A) and (B)
necessarily hold; (C), (D) and (E) do not.

::: pf

::: {.pf-step #ro}

If $A$ is open and contains $\QQ$, then $A=\RR$.

::: pf-proof

Suppose $x\notin A$. Since $A$ is open and $x\notin A$, there is
$\varepsilon>0$ with $(x-\varepsilon,x+\varepsilon)\cap A=\emptyset$; but that
interval contains a rational number, and every rational lies in $A$, a
contradiction. Since $A\subseteq\RR$ by hypothesis, $A=\RR$.

:::

:::

::: {.pf-step #closed}

If $A$ is closed and contains $\QQ$, then $A=\RR$.

::: pf-proof

$A$ is closed, so it contains its closure; and $\QQ\subseteq A$ gives
$\overline{\QQ}\subseteq\overline A=A$. Since $\QQ$ is dense in $\RR$,
$\overline\QQ=\RR$, so $\RR\subseteq A$ and $A=\RR$.

:::

:::

::: {.pf-step #rest}

(C), (D) and (E) fail: $\RR\setminus\QQ$ is uncountable and is neither $\RR$
nor open, and $\QQ$ is countable and not closed.

::: pf-proof

(C) is refuted by $A=\RR\setminus\QQ$, which is uncountable — an interval
$(n,n+1)$ contains uncountably many irrationals — and is not $\RR$. (D) fails
for the same $A$, which is not open since every ball about an irrational
contains rationals, which are not in $A$. (E) fails with $A=\QQ$, countable
and not closed, since its closure is $\RR$. So only (A) and (B) necessarily
hold for a set between $\QQ$ and $\RR$.

:::

:::

:::


:::
