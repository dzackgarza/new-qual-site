---
schema: qual/card@1
id: P-UCLARA18F-03
kind: problem
title: UCLA analysis Fall 2018, Problem 3
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 3. Let (X, ρ) be a compact metric space and let P (X) be the set of all
probability measures on the Borel sigma-algebra of X (i.e. µ ∈ P (X) if µ is a
positive Borel measure and µ(X) = 1). Assume {µn } is a sequence in P (X) and µ
is another element of P (X) such that for all continuous f : X → R
                       Z              Z
                          f (x)dµn →      f (x)dµ (n → ∞).
                        X               X
Prove that

                             µn (E) → µ(E) (n → ∞)
whenever E is a Borel subset of X such that µ(E) = µ(E o ), where E is the closure
of E and E o is the interior of E.
:::
