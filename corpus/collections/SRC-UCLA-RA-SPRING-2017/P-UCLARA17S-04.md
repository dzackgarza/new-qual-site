---
schema: qual/card@1
id: P-UCLARA17S-04
kind: problem
title: UCLA analysis Spring 2017, Problem 4
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 4. For n ≥ 1, let an : [0, 1) → {0, 1} denote the nth digit in the binary
expansion of x, so that
                           X
                        x=   an (x)2−n for all x ∈ [0, 1).
                            n≥1

(We remove any ambiguity from this definition by requiring that lim inf an (x) = 0
for all x ∈ [0, 1).) Let M ([0, 1)) denote the Banach space of finite complex Borel
measures on [0, 1) and define linear functionals Ln on M ([0, 1)) via
                                        Z 1
                              Ln (µ) =      an (x) dµ(x).
Show that no subsequence of the sequence Ln converges in the weak-* topology on
M ([0, 1))∗ .
:::
