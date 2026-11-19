---
schema: qual/card@1
id: P-WESCA04-T1
kind: problem
title: "State the Casorati–Weierstrass theorem"
classification:
  areas: [complex-analysis]
  topics:
  - Casorati-Weierstrass
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.1, item 1 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 33, printed page 1: section 1.1 item 1 of
    the Preliminary Examination in Analysis, Wesleyan University, August 2, 2004. The
    page had cited only the extraction; it now names the examination, its item and the
    page of the scan. The statement is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had answered
    the question, which STYLE-08 forbids; it is dropped, and the step that carries the
    result is now the QED step. No argument or statement changes.

---

::: {.problem}
State the Casorati–Weierstrass theorem.
:::

::: {.solution}
The item is section 1.1 item 1 of the Preliminary Examination in Analysis, Wesleyan University,
August 2, 2004 (statement of the Casorati--Weierstrass theorem), on PDF p. 33 of the retained scan
assets/attachments/analysis_2003-2007.pdf, printed page 1.


::: pf

::: {.pf-step #s1-1}

**Casorati--Weierstrass Theorem.**

Let $f$ be holomorphic on a punctured neighborhood
$$
0<\abs{z-z_0}<r
$$
and suppose $z_0$ is an essential singularity of $f$.
Then for every
$$
0<\rho<r,
$$
the image
$$
f\bigl(
\{z:0<\abs{z-z_0}<\rho\}
\bigr)
$$
is dense in
$$
\CC.
$$


::: pf-proof

Equivalently, for every
$$
w\in\CC
$$
and every
$$
\varepsilon>0,
$$
there exists
$$
z
$$
with
$$
0<\abs{z-z_0}<\rho
$$
such that
$$
\abs{f(z)-w}<\varepsilon.
$$

Equivalently again, every complex number is a limit of values
$$
f(z_n)
$$
along some sequence
$$
z_n\to z_0,
\qquad
z_n\ne z_0.
$$

:::

:::


:::

:::
