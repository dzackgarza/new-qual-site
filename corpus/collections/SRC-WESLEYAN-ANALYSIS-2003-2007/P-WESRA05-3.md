---
schema: qual/card@1
id: P-WESRA05-3
kind: problem
title: Norm-induced metrics, Banach spaces, and uniform boundedness
classification:
  areas: [real-analysis]
  topics: [Functional Analysis, Banach Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 32: item 3 of the Real Analysis
    Preliminary Examination, 2005, parts (a)-(d), printed there under the heading of the
    exam. The page had cited only the extraction; it now names the examination, its item
    and the page of the scan. The statement is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The Baire-category step bounded Th for norm h strictly below r and then scaled to the
    constant 2m/r, which that hypothesis does not give: h of norm exactly r was needed.
    The bound is taken over the closed ball, which lies in the closed set E_m, and the
    scaling is written out. The constant 2m/r and the statement are unchanged.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the PDF-page locator in the card's text is removed; the item is cited by its
    examination, section and item number only, which the retained scan prints as its heading.
    The earlier events keep their text (QUAL-11). No statement or step changes.

---

::: {.problem}
Let $B$ be a real vector space.

1. Define a norm on $B$.

2. Give the metric induced by a norm and prove that it is a metric.

3. Define a Banach space.

4. State the Uniform Boundedness Theorem for a family of bounded linear maps from the Banach space $B$ to a normed space $N$, and explain the main idea of its proof.
:::

::: {.solution}
The item is item 3 of the Real Analysis Preliminary Examination, 2005 (norms, the metric
they induce, Banach spaces, and the uniform boundedness theorem with the idea of its
proof).

::: pf

::: pf-step

Define a norm.

::: pf-proof

A norm is a map $\norm{\cdot}:B\to[0,\infty)$ such that for all $x,y\in B$ and $a\in\RR$,
$$
\norm{x}=0\iff x=0,
\qquad
\norm{ax}=\abs{a}\,\norm{x},
\qquad
\norm{x+y}\le\norm{x}+\norm{y}.
$$

:::

:::

::: pf-step

Construct the induced metric.

::: pf-proof

Define
$$
d(x,y)=\norm{x-y}.
$$
Then $d(x,y)\ge0$, and
$$
d(x,y)=0\iff x-y=0\iff x=y.
$$
Also
$$
d(x,y)=\norm{x-y}=\norm{-(y-x)}=d(y,x),
$$
and the norm triangle inequality gives
$$
d(x,z)=\norm{x-z}
\le\norm{x-y}+\norm{y-z}
=d(x,y)+d(y,z).
$$
Thus $d$ is a metric.

:::

:::

::: pf-step

Define a Banach space.

::: pf-proof

A normed vector space is a Banach space if it is complete for the metric induced by its norm; equivalently, every norm-Cauchy sequence converges in norm to an element of the space.

:::

:::

::: pf-step

State Uniform Boundedness.

::: pf-proof

Let $B$ be Banach, let $N$ be normed, and let $\mathcal T$ be a family of bounded linear operators $T:B\to N$.
If for every $x\in B$,
$$
\sup_{T\in\mathcal T}\norm{Tx}<\infty,
$$
then
$$
\boxed{\sup_{T\in\mathcal T}\norm{T}<\infty.}
$$
This is the Uniform Boundedness Principle, or Banach--Steinhaus theorem.

:::

:::

::: pf-step

Explain the Baire-category argument.

::: pf-proof

For $m\in\NN$, set
$$
E_m=\left\{x\in B:\sup_{T\in\mathcal T}\norm{Tx}\le m\right\}.
$$
Each $E_m$ is closed, because it is the intersection over $T\in\mathcal T$ of the closed sets $\{x:\norm{Tx}\le m\}$.
Pointwise boundedness says
$$
B=\bigcup_{m=1}^\infty E_m.
$$
Since $B$ is complete, Baire's theorem implies that some $E_m$ contains a ball
$$
B(x_0,r)\subseteq E_m.
$$
If $\norm{h}\le r$, then $x_0$ and $x_0+h$ lie in $E_m$ (the closed ball lies in $E_m$ because $E_m$ is closed), so for every $T\in\mathcal T$,
$$
\norm{Th}
\le\norm{T(x_0+h)}+\norm{Tx_0}
\le2m.
$$
By scaling — writing $x\ne0$ as $x=(\norm{x}/r)h$ with $h=rx/\norm{x}$, so that $\norm{h}=r$ —
$$
\norm{Tx}\le \frac{2m}{r}\norm{x}.
$$
Hence
$$
\sup_{T\in\mathcal T}\norm{T}\le\frac{2m}{r}<\infty.
$$

:::

:::

:::

:::
