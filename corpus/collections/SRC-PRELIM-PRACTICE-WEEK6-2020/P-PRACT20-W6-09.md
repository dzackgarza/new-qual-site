---
schema: qual/card@1
id: P-PRACT20-W6-09
kind: problem
title: Compactness, boundedness of continuous functions and connectedness in $\RR^n$
classification:
  areas:
  - prelim
  topics:
  - Compactness
  - Heine-Borel Theorem
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the empty set misread as alpha, checked against Week6_solns.pdf (Problem 9).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced OCR-garbled norm in the solution with the source's f(x) = ||x||, checked against Week6_solns.pdf page 5 (Problem 9).
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 5 of the retained solutions booklet GRE Prep: Miscellaneous
    Practice Problem Solutions by Christian Parkinson
    (assets/attachments/prelim-practice-week6-2020/page-5.png), which prints this
    problem together with a worked solution; the practice sheet itself is not
    retained and the collection's provenance list is empty, so the statement was
    compared with the card from that page: the printed problem's three statements (A), (B), (C) are those on the card, word for word, including the hypothesis that K is a nonempty subset of R^n
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The printed solution's three verdicts, (A) and (B) true and (C) false, are reproduced here with the arguments written out: a finite subcover for (A), the contrapositive by Heine-Borel with the two unbounded examples for (B), and the printed disconnected compact set for (C).
---

::: {.problem}
Let $\emptyset \neq K \subseteq \RR^n$. Which of the following statements are true?

(A) If $K$ is compact, then every continuous real-valued function on $K$ is bounded.

(B) If every continuous real-valued function on $K$ is bounded, then $K$ is compact.

(C) If $K$ is compact, then $K$ is connected.
:::

::: {.solution}

Let $\emptyset\ne K\subseteq\RR^n$. The statements (A) and (B) are true and
(C) is false.

::: pf

::: {.pf-step #atrue}

(A) If $K$ is compact, every continuous real-valued function on $K$ is
bounded.

::: pf-proof

Let $f\colon K\to\RR$ be continuous. The sets $U_n=f^{-1}(-n,n)$ are open in
$K$ and cover it, since every value of $f$ is a real number; compactness gives
a finite subcover, and because the sets are nested, $K\subseteq U_N$ for the
largest index $N$ in that subcover. Hence $\abs{f(x)}<N$ for all $x\in K$, so
$f$ is bounded.

:::

:::

::: {.pf-step #btrue}

(B) If every continuous real-valued function on $K$ is bounded, then $K$ is
compact.

::: pf-proof

Contrapositively, suppose $K$ is not compact. By Heine-Borel for subsets of
$\RR^n$, a set is compact exactly when it is closed and bounded, so $K$ is
either not closed or not bounded. If $K$ is unbounded, $f(x)=\norm x$ is
continuous on $K$ and unbounded. If $K$ is not closed, there is a point
$x_0\notin K$ that is a limit point of $K$; then $f(x)=\frac{1}{\norm{x-x_0}}$
is continuous on $K$, since the denominator never vanishes there, and it is
unbounded because points of $K$ approach $x_0$. So a continuous unbounded
function exists on any noncompact $K$, which is the contrapositive.

:::

:::

::: {.pf-step #cfalse}

(C) If $K$ is compact, then $K$ is connected — false.

::: pf-proof

Take $K=[-2,-1]^n\cup[1,2]^n$: a finite union of closed bounded sets, hence
closed and bounded, hence compact, and it is the union of two disjoint
nonempty closed subsets at positive distance from one another, so it is
disconnected. So compactness does not imply connectedness, and the answer is
(A) and (B).

:::

:::

:::


:::
