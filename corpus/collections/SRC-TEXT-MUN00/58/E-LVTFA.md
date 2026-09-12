---
schema: qual/card@1
id: E-LVTFA
kind: problem
title: Homotopy equivalence is an equivalence relation
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Show that given a collection $\mathcal{C}$ of spaces, the relation of homotopy equivalence is an equivalence relation on $\mathcal{C}$.
:::

::: {.solution}
Reflexivity: every space \(X\) is homotopy equivalent to itself via \(\operatorname{id}_X\).

Symmetry: if \(f:X\to Y\) and \(g:Y\to X\) satisfy
\[
gf\simeq\operatorname{id}_X,\qquad fg\simeq\operatorname{id}_Y,
\]
then the same equations show that \(g\) is a homotopy equivalence from \(Y\) to \(X\) with homotopy inverse \(f\).

Transitivity: suppose \(X\simeq Y\) via \(f:X\to Y\), \(g:Y\to X\), and \(Y\simeq Z\) via \(u:Y\to Z\), \(v:Z\to Y\). Then \(u f:X\to Z\) and \(g v:Z\to X\) satisfy
\[
(gv)(uf)=g(vu)f\simeq g\,\operatorname{id}_Y f=gf\simeq\operatorname{id}_X,
\]
and similarly
\[
(uf)(gv)=u(fg)v\simeq u\,\operatorname{id}_Yv=uv\simeq\operatorname{id}_Z.
\]
Thus \(X\simeq Z\). Hence homotopy equivalence is an equivalence relation.
:::
