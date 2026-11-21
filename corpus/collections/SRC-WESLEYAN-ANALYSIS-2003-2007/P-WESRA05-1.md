---
schema: qual/card@1
id: P-WESRA05-1
kind: problem
title: Sigma-algebras, limsup and liminf of sets, and finite cardinalities
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    assets/attachments/analysis_2003-2007.pdf at PDF p. 31: item 1 of the Real Analysis
    Preliminary Examination, 2005, whose heading is printed on that page. The page had
    cited only the extraction; it now names the examination, its item and the page of
    the scan. The statement is unchanged, and the printed symbols
    $\overline{A}$ and $\underline{A}$ for the two sets are reproduced in meaning.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the PDF-page locator in the card's text is removed; the item is cited by its
    examination, section and item number only, which the retained scan prints as its heading.
    The earlier events keep their text (QUAL-11). No statement or step changes.

---

::: {.problem}
Let $X$ be nonempty and let $\mathcal A$ be a collection of subsets of $X$.

1. Define what it means for $\mathcal A$ to be a sigma-algebra.

2. If $A_1,A_2,\ldots\in\mathcal A$, prove that the set of points belonging to infinitely many $A_n$ lies in $\mathcal A$.

3. Prove that the set of points belonging to all but finitely many $A_n$ lies in $\mathcal A$.

4. Describe the relationship between these two sets.

5. If $X$ has exactly five points, determine the possible cardinalities of sigma-algebras on $X$.
:::

::: {.solution}
The item is item 1 of the Real Analysis Preliminary Examination, 2005 (sigma-algebras;
the sets of points lying in infinitely many, resp. all but finitely many, members of a
sequence; and the possible cardinalities of a sigma-algebra on a five-point set).
The printed statement names the two sets $\overline{A}$ and $\underline{A}$; the card
states them in words.

::: pf

::: pf-step

Definition.

::: pf-proof

A sigma-algebra $\mathcal A$ on $X$ is a collection of subsets of $X$ such that
$$
X\in\mathcal A,
$$
$A\in\mathcal A$ implies $X\setminus A\in\mathcal A$, and whenever $A_1,A_2,\ldots\in\mathcal A$,
$$
\bigcup_{n=1}^\infty A_n\in\mathcal A.
$$

:::

:::

::: pf-step

The infinitely-often set is measurable.

::: pf-proof

The set of points belonging to infinitely many $A_n$ is
$$
\limsup_{n\to\infty}A_n
=
\bigcap_{N=1}^\infty\bigcup_{n\ge N}A_n.
$$
Since sigma-algebras are closed under countable unions and intersections, this set belongs to $\mathcal A$.

:::

:::

::: pf-step

The eventually-always set is measurable.

::: pf-proof

The set of points belonging to all but finitely many $A_n$ is
$$
\liminf_{n\to\infty}A_n
=
\bigcup_{N=1}^\infty\bigcap_{n\ge N}A_n.
$$
Again this belongs to $\mathcal A$.

:::

:::

::: pf-step

Compare the two sets.

::: pf-proof

If a point belongs to all but finitely many $A_n$, then it certainly belongs to infinitely many of them.
Therefore
$$
\boxed{\liminf A_n\subseteq\limsup A_n.}
$$
Equality holds exactly when no point belongs to infinitely many $A_n$ and also to infinitely many complements $A_n^c$.

:::

:::

::: pf-step

Determine the possible sizes on a five-point set.

::: pf-proof

Every sigma-algebra on a finite set is determined by its atoms, which form a partition of $X$.
If there are $k$ atoms, then every measurable set is a union of atoms, so the sigma-algebra has exactly
$$
2^k
$$
elements.

Since $X$ has five points, the number $k$ of nonempty atoms may be any integer from $1$ through $5$.
Each value occurs, by choosing a partition of $X$ into $k$ nonempty blocks.
Hence the possible cardinalities are
$$
\boxed{2,4,8,16,32.}
$$

:::

:::

:::

:::
