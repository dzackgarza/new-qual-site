---
schema: qual/card@1
id: E-5NREC
kind: problem
title: Images of locally compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 3, printed p. 186; the two questions
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.3, PDF p. 22. The identity from the discrete
    rationals to the usual rationals is continuous with image not locally compact; a
    continuous open map does carry local compactness, images of compact neighbourhoods being
    compact neighbourhoods. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $X$ be a locally compact space.
If $f: X \to Y$ is continuous, does it follow that $f(X)$ is locally compact?
What if $f$ is both continuous and open?
Justify your answer.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.3, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both halves and the counterexample are theirs.

*Continuous alone is not enough.* Let $\QQ_{d}$ be the rationals with the discrete topology, $\QQ$ the rationals usual; the identity $i:\QQ_{d}\to\QQ$ is continuous. The discrete $\QQ_{d}$ is locally compact ($\{x\}$ is an open compact neighbourhood of $x$), but $i(\QQ_{d})=\QQ$ is not locally compact (Exercise 29.1).

*Continuous and open suffices.* Let $y=f(x)\in f(X)$; choose a compact $C\subset X$ containing a neighbourhood $U$ of $x$. Then $f(C)$ is compact (continuity of $f$) and contains the neighbourhood $f(U)$ of $y$ (openness of $f$). So $f(X)$ is locally compact.
:::
