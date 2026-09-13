---
schema: qual/card@1
id: P-UCLARA18S-06
kind: problem
title: UCLA analysis Spring 2018, Problem 6
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 6. Let T denote the unit circle in the complex plane and let P(T) denote
the space of Borel probability measures on T and P(T × T) denote the space of
Borel probability measures on T × T. Fix µ, ν ∈ P(T) and define
        n               ZZ                            Z               Z
  M = γ ∈ P(T × T) :            f (x)g(y) dγ(x, y) =     f (x) dµ(x) · g(y) dν(y)
                            T×T                        T               T
                                                      o
                                   for all f, g ∈ C(T) .
Show that F : M → R defined by
                            ZZ
                                        sin2 θ−φ   dγ eiθ , eiφ
                                                               
                   F (γ) =                    2
                                  T×T
achieves its minimum on M.
:::
