---
schema: qual/card@1
id: P-WESRA07-II6
kind: problem
title: The $L^1$ norm on $C([0,1])$ and the incompleteness of $C([0,1])$ under it
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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-30
  note: 'The source prints the norm as \|f\| := \int_0^1 f\,dm, without absolute values, which is not a norm (it takes the value -1 at f = -1 and vanishes at f(x) = x - 1/2). The statement now uses \int_0^1 |f|\,dm, the intended L^1 norm.'
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The event of 2026-10-30 said the statement "now uses" the norm
    \int_0^1 |f| dm, and the statement did not: the problem block still printed
    \norm{f} = \int_{[0,1]} f dm without absolute values, while the remark called
    that non-norm "as printed" and the solution proved the norm axioms for
    \int |f| dm. Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf, rendered at 400 dpi: PDF p. 3,
    whose folio is 2, Part II item 6, prints "For each f in C([0,1]) we set
    ||f|| = \int_{[0,1]} f dm" with no absolute-value bars, and then asks
    "(a) Explain why this defines a norm on C([0,1])". So the examination itself is
    defective at (a) and not only the extraction; no bars appear at 400 dpi. The
    statement now carries \int |f| dm, the intended norm, which QUAL-01 asks of a
    false statement, and the remark records the printed text and why it fails. The
    solution is unchanged, and its two parts are the examination's (a) and (b).

---

::: {.problem}
For $f\in C([0,1],\RR)$ define
$$
\norm{f}\coloneqq\int_{[0,1]}\abs{f}\,dm.
$$

1. Explain why this defines a norm on $C([0,1])$.

2. Is $C([0,1])$ complete with respect to this norm?
:::

::: {.remark}
The examination prints $\norm{f}=\int_{[0,1]}f\,dm$ without absolute values, and that
functional is not a norm: it is negative at $f=-1$ and vanishes at $f(x)=x-\tfrac12$, so
part (a) is not true of it as it stands. The norm proved below is the intended one,
$\int_{[0,1]}\abs{f}\,dm$. The item is Part II, item 6, of the Real Analysis section of the
Wesleyan analysis qualifier, Summer 2007, in the retained scan `assets/attachments/analysis_2003-2007.pdf`.
:::

::: {.solution}

::: pf

::: pf-step

$\norm{\cdot}$ is a norm on $C([0,1])$.

::: pf-proof

Homogeneity $\norm{cf} = \abs{c}\norm{f}$ and the triangle inequality $\norm{f+g}\le\norm{f}+\norm{g}$ follow from $\abs{cf} = \abs{c}\abs{f}$, $\abs{f+g}\le\abs{f}+\abs{g}$ and linearity and monotonicity of the integral.
If $\norm{f}=0$, then $\abs{f}=0$ almost everywhere.
A continuous $f$ with $f(x_0)\ne 0$ satisfies $\abs{f}>\abs{f(x_0)}/2$ on an interval of positive length around $x_0$, so $f\equiv0$.

:::

:::

::: pf-step

$\boxed{C([0,1])\text{ is not complete under }\norm{\cdot}.}$

::: pf-proof

Let $h=\mathbf1_{[1/2,1]}$, and let $h_n\in C([0,1])$ be $0$ on $[0,1/2-1/n]$, $1$ on $[1/2+1/n,1]$, and linear between.
Then $\norm{h_n-h}\le 2/n$, where the norm is the $L^1$ norm on $L^1([0,1])$, so $(h_n)$ is Cauchy.
If $h_n\to g$ for some $g\in C([0,1])$, then $g=h$ in $L^1$ by uniqueness of $L^1$ limits, so $g=h$ almost everywhere.
Continuity then forces $g=0$ on $[0,1/2)$ and $g=1$ on $(1/2,1]$, which no continuous function satisfies at $x=1/2$.

:::

:::

:::

:::
