---
schema: qual/card@1
id: P-PRACT20-W6-04
kind: problem
title: Pointwise and uniform convergence of $x^n/(1+x^n)$ on $[0,1]$
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
  - Pointwise Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Moved choice (C) out of a display into its labelled paragraph and restored the arrows lost from the solution display, checked against Week6_solns.pdf page 2 (Problem 4, which has only choices A-C).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored two arrows lost from inline solution formulas and dropped a stray 2, checked against Week6_solns.pdf page 2 (Problem 4).
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
    on the card: the pointwise limit, the failure of uniformity through the discontinuity of the limit, and the integral identity were each re-derived
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The pointwise limit, the discontinuity of the limit ruling out uniformity, and dominated convergence for the integrals
---

::: {.problem}
Define $f_n(x) = \frac{x^n}{1 + x^n}$ for $x \in [0, 1]$, $n \in \NN$. Which of the following is true?

(A) The sequence $\{f_n\}$ converges pointwise on $[0, 1]$ to a limit function $f$.

(B) The sequence $\{f_n\}$ converges uniformly on $[0, 1]$ to a limit function $f$.

(C) $\displaystyle\lim_{n \to \infty} \int_0^1 f_n(x)\,dx = \int_0^1 \left(\lim_{n \to \infty} f_n(x)\right) dx$
:::

::: {.solution}

Let $f_n(x)=\dfrac{x^n}{1+x^n}$ on $[0,1]$.

::: pf

::: {.pf-step #pointwise}

(A) holds: $f_n\to f$ pointwise, where $f(x)=0$ for $0\le x<1$ and
$f(1)=\frac12$.

::: pf-proof

For $0\le x<1$ we have $x^n\to0$, so
$f_n(x)=\frac{x^n}{1+x^n}\to\frac{0}{1}=0$; and $f_n(1)=\frac{1}{2}$ for every
$n$. So the sequence converges pointwise on $[0,1]$ to the stated $f$, which
is what (A) asserts.

:::

:::

::: {.pf-step #notuniform}

(B) fails: the convergence is not uniform.

::: pf-proof

Each $f_n$ is continuous on $[0,1]$, being a quotient of polynomials with
denominator $1+x^n\ge1$. A uniform limit of continuous functions is
continuous, but the pointwise limit $f$ of step [](#pointwise){.pf-ref} is
discontinuous at $1$, since $f(x)=0\to0$ as $x\to1^{-}$ while $f(1)=\frac12$.
Hence the convergence is not uniform, and (B) is false.

:::

:::

::: {.pf-step #integral}

(C) holds: $\lim_n\int_0^1f_n=0=\int_0^1f$.

::: pf-proof

$0\le f_n\le1$ on $[0,1]$ and $f_n\to0$ pointwise except at the single point
$1$, so by dominated convergence with dominating function $1\in L^1[0,1]$ the
integrals tend to $0$. The limit function $f$ vanishes off the single point
$1$, so $\int_0^1f=0$ as well. Both sides are $0$ and the interchange is
valid, which is (C).

:::

:::

:::


:::
