---
schema: qual/card@1
id: P-BJDIE
kind: problem
title: Order of $\GL_n(\FF_q)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Bases
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 3 of the Algebra Preliminary Examination of September 8, 2008
    (University of Washington), printed p. 1 of the two-page paper retained at assets/attachments/UW-
    Algebra-Qual-2008.pdf, is the statement the card answers, and the paragraph at the head of the
    solution records that the paper prints no solutions, so the argument is the card's own. Checked: the
    statement against the paper's text layer at the page named; the solution read for the column-by-
    column count of ordered bases of F_q^n; `qualc.authoring check` on the card, and `tmp/lam.sh` for
    the numbering and the QED. Not checked: no retained solution set exists for this paper to compare
    the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Show that the order of the group $\GL_n(\FF_q)$ of invertible $n\times n$ matrices over the field $\FF_q$ of $q$ elements is $(q^n-1)(q^n-q)\cdots(q^n-q^{n-1})$.
:::

::: {.solution}

The problem is Problem 3 of the Algebra Preliminary Examination of September 8, 2008 (University of Washington), printed p. 1 of the two-page paper retained at `assets/attachments/UW-Algebra-Qual-2008.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the count itself: an invertible matrix is an ordered basis of $\FF_q^n$, and the number of ordered bases is $(q^n-1)(q^n-q)\cdots(q^n-q^{n-1})$, one factor for each column

An invertible $n\times n$ matrix over $\FF_q$ is the same thing as an ordered basis of the vector space $\FF_q^n$, namely its ordered list of columns.

::: pf

::: {.pf-step #s1}

The first column can be any nonzero vector, giving $q^n-1$ choices.

::: pf-proof

There are $q^n$ vectors in $\FF_q^n$, and only the zero vector is forbidden.

:::

:::

::: {.pf-step #s2}

After choosing $k$ linearly independent columns, the next column has $q^n-q^k$ choices.

::: pf-proof

The span of $k$ independent vectors is a $k$-dimensional subspace, hence has $q^k$ elements. The next column must lie outside that span.

:::

:::

::: pf-step

Therefore
$$
\abs{\GL_n(\FF_q)}=(q^n-1)(q^n-q)(q^n-q^2)\cdots(q^n-q^{n-1}).
$$

::: pf-proof

Choose the columns successively and multiply the numbers of choices from steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
