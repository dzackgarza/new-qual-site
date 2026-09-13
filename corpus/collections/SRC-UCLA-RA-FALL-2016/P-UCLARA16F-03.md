---
schema: qual/card@1
id: P-UCLARA16F-03
kind: problem
title: UCLA analysis Fall 2016, Problem 3
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 3. If X is a compact metric space, we denote by P(X) be the set of
positive Borel measures µ on X with µ(X) = 1.
   (a) Let ϕ : X → [0, ∞] be a lower-semicontinuous function on a compact metric
space X. Show that if µ and µn for n ∈ N are in P(X) and µn → µ with respect
to the weak-star topology on P(X), then
                            Z                Z
                               φ dµ ≤ lim inf φ dµn .
                                        n→∞

  (b) Let K ⊂ Rd be a compact set. For µ ∈ P(K), we define
                             Z Z
                      E(µ) =                dµ(x)dµ(y).
                              K K   |x − y|
Here |z| denotes the Euclidean norm of z ∈ Rd .
  Show that the function E : P(K) → [0, ∞] attains its minimum on P(K) (which
could possibly be ∞).
:::
