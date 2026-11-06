---
schema: qual/card@1
id: P-PRACT20-W6-05
kind: problem
title: Uniformly continuous functions on $(0,1)$ have limits at $0$
classification:
  areas:
  - prelim
  topics:
  - Uniform Continuity
  - Cauchy Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the statement was read as printed and the proof re-derived; the argument uses only uniform continuity and completeness of the reals
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. Cauchyness of the image sequence from uniform continuity, then convergence by completeness, with independence of the sequence
---

::: {.problem}
Suppose that $f : (0, 1) \to \RR$ is uniformly continuous.
Let $\{x_{n}\}$ be a sequence in $(0, 1)$ such that $x_{n} \to 0$. Show that the sequence $\{f(x_{n})\}$ converges.
[Note: generalizing this fact, one can show that if $U \subset \RR^{n}$ is open and bounded, then $f : U \to \RR$ is uniformly continuous iff $f$ can be continuously extended to the closure $\overline{U}$.]
:::

::: {.solution}

Let $f\colon(0,1)\to\RR$ be uniformly continuous and let $x_n\in(0,1)$ with
$x_n\to0$.

::: pf

::: {.pf-step #cauchy}

$(x_n)$ is Cauchy in $(0,1)$, hence $(f(x_n))$ is Cauchy in $\RR$.

::: pf-proof

A convergent sequence in a metric space is Cauchy: given $\eta>0$ there is $N$
with $\abs{x_n}<\eta$ for $n\ge N$, so $\abs{x_n-x_m}<\eta$ for $m,n\ge N$.
Uniform continuity gives, for $\varepsilon>0$, a $\delta>0$ such that
$\abs{f(s)-f(t)}<\varepsilon$ whenever $\abs{s-t}<\delta$; with $N$ chosen for
$\eta=\delta$, all $m,n\ge N$ satisfy $\abs{f(x_n)-f(x_m)}<\varepsilon$.

:::

:::

::: {.pf-step #converges}

$(f(x_n))$ converges in $\RR$.

::: pf-proof

$\RR$ is complete, so a Cauchy sequence of real numbers converges. Hence
$\lim_nf(x_n)$ exists, which is the assertion; and the value is
$\lim_{x\to0^{+}}f(x)$, since for any other sequence $y_n\to0$ in $(0,1)$ the
same argument applies and $\abs{f(x_n)-f(y_n)}\to0$ by uniform continuity, so
the limit does not depend on the sequence. This is the one-dimensional case of
the extension theorem quoted on the card.

:::

:::

:::


:::
