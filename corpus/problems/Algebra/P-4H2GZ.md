---
schema: qual/card@1
id: P-4H2GZ
kind: problem
title: $C_H(x)=H\cap C_G(x)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that for $H\leq G$, $C_H(x) = H \intersect C_G(x)$.
:::

::: {.solution}
By definition,
\[
C_H(x)=\{h\in H:hx=xh\}
\]
and
\[
C_G(x)=\{g\in G:gx=xg\}.
\]
Hence for $h\in G$,
\[
h\in C_H(x)
\iff h\in H\text{ and }hx=xh
\iff h\in H\cap C_G(x).
\]
Therefore
\[
C_H(x)=H\cap C_G(x).
\]
:::
