---
schema: qual/card@1
id: P-ALGS13A
kind: problem
title: Existence of a non-abelian group of order $2013$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 1 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1
    of the single-page paper retained at assets/attachments/SP13_200_Algebra_Qual.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; the solution read for the element of order 3 in the automorphism group of C_61
    and the resulting semidirect product; `qualc.authoring check` on the card, and `tmp/lam.sh` for the
    numbering and the QED. Not checked: no retained solution set exists for this paper to compare the
    argument with, and no other card of the collection in this pass.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared against the official UCSD Spring 2013 Algebra qualifying exam; statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Constructed an explicit nonabelian semidirect product of order 2013.
---

::: {.problem}
Does there exist a non-Abelian group of order $2013 = (3)(11)(61)$?
Justify your answer.
:::

::: {.solution}

The problem is Problem 1 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1 of the single-page paper retained at `assets/attachments/SP13_200_Algebra_Qual.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the construction: an element of order $3$ in $\operatorname{Aut}(C_{61})$ gives a semidirect product $C_{61}\rtimes C_3$ of order $2013$ whose action is nontrivial, hence a nonabelian example

Yes.

::: pf

::: pf-step

The automorphism group of $C_{61}$ contains an element of order $3$.

::: pf-proof

Since $61$ is prime,
$$
\operatorname{Aut}(C_{61})\cong (\ZZ/61\ZZ)^\times,
$$
which is cyclic of order $60$.
Because $3\mid60$, it contains an element $\varphi$ of order $3$.

:::

:::

::: pf-step

Form the semidirect product
$$
H=C_{61}\rtimes_{\varphi} C_3.
$$
Then $\cardinality{H}=183$ and $H$ is nonabelian.

::: pf-proof

Let $a$ generate $C_{61}$ and $b$ generate $C_3$, with conjugation by $b$ acting as the nontrivial automorphism $\varphi$:
$$
bab^{-1}=\varphi(a)\neq a.
$$
Thus $a$ and $b$ do not commute, so $H$ is nonabelian.
Its order is $61\cdot3=183$.

:::

:::

::: pf-step

Set
$$
G=H\times C_{11}.
$$
Then $G$ is a nonabelian group of order $2013$.

::: pf-proof

We have
$$
\cardinality{G}=183\cdot11=3\cdot11\cdot61=2013.
$$
Since the factor $H$ is nonabelian, the direct product $G$ is nonabelian.

:::

:::

:::

:::
