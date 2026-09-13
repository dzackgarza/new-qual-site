---
schema: qual/card@1
id: P-AMH-ALG-SG16-31
kind: problem
title: Amherst algebra study guide problem 31
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(March 2008) Let g(x) = x2 + 3∈ F7[x], where F7 ={0, 1, 2, 3, 4, 5, 6} is the ﬁeld of seven elements. (a) Prove that g is reducible in F7[x]. (b) Let⟨g⟩⊆ F7[x] denote the principal ideal {gh| h∈ F7[x]}. Find an ideal I⊆ F7[x] such that ⟨g⟩ ⊊I ⊊ F 7[x].
:::

::: {.solution}
Proof. (a) Plugging each element of F7 into g soon shows g(2) = 0, so that ( x− 2) is a factor of g.
Long division reveals that g(x) = (x− 2)(x + 2), conﬁrming that g is reducible.
(b) Let I =⟨x− 2⟩⊆ F7[x]. Any element of ⟨g⟩ is of the form hg for some h∈ F7[x], and hence
hg =
(
(x + 2)h
)
· (x− 2)∈I.
Thus, we have⟨g⟩⊆ I⊆ F7[x]. However, x− 2⁄∈⟨ g⟩, because any multiple hg of g must either be
0 or have degree deg(hg)≥ degg = 2, whereas deg(x− 2) = 1. Finally, 1 ⁄∈I, because any multiple
h· (x− 2) of (x− 2) must either be 0 or have degree ≥ deg(x− 2) = 1, whereas deg(1) = 0.
Hence,⟨g⟩ ⊊I ⊊ F 7[x]. QED
:::
