---
schema: qual/card@1
id: P-WESCA07-I3
kind: problem
title: "State the local Cauchy Theorem"
classification:
  areas: [complex-analysis]
  topics:
  - Cauchy Integral Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section I, item 3 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 7 (printed p. 2 of the 2007 complex-analysis paper). The card had cited neither the
    examination nor a page; it now names both, and the statement was compared with the
    printed item and left unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had answered
    the question, which STYLE-08 forbids; it is dropped, and the step that carries the
    result is now the QED step. No argument or statement changes.

- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the PDF-page locator in the card's text is removed; the item is cited by its
    examination, section and item number only, which the retained scan prints as its heading.
    The earlier events keep their text (QUAL-11). No statement or step changes.

---

::: {.problem}
State the local Cauchy Theorem.
:::

::: {.solution}
The item is Section 1 item 3 of the Complex Analysis section of the Analysis Qualifier, Wesleyan University, Summer 2007 (statement of the local Cauchy theorem).


::: pf

::: {.pf-step #s1-1}

**Local Cauchy Theorem.** Let $U\subseteq\CC$ be open and let $f:U\to\CC$ be analytic. For every $z_0\in U$, there exists $r>0$ such that
$$
\overline{B(z_0,r)}\subseteq U
$$
and
$$
\boxed{\int_\gamma f(z)\,dz=0}
$$
for every closed piecewise $C^1$ path $\gamma$ contained in $B(z_0,r)$.


::: pf-proof

This is the local form of Cauchy's theorem: on a sufficiently small disk contained in the domain, a holomorphic function has zero integral around every closed path.

:::

:::

::: {.pf-step #s1-2}

Equivalently, for every $z_0\in U$ there is a neighborhood $V\subseteq U$ of $z_0$ on which $f$ has a holomorphic primitive $F$, so that
$$
F'=f\quad\text{on }V.
$$


::: pf-proof

Vanishing of all closed-path integrals on a connected open set is equivalent to path independence of the integral from a base point, which defines a primitive. Conversely, the integral of a derivative over every closed path is zero.

:::

:::


:::

:::
