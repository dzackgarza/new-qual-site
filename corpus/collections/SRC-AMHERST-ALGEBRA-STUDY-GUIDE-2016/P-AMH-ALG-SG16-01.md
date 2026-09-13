---
schema: qual/card@1
id: P-AMH-ALG-SG16-01
kind: problem
title: Amherst algebra study guide problem 1
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
(January 2012) Let G be a group, and let H,K ⊆ G be subgroups of G. Prove the following standard theorem about subgroups: that H∩K is a subgroup of G.
:::

::: {.solution}
Proof. (Nonempty) Since H and K are subgroups of G, we have e∈H and e∈K. So e∈H∩K,
and hence H∩K⁄= ∅.
(Closed under∗) Given a,b∈H∩K, we have ab∈H and ab∈K since H and K are closed under
the operation. So ab∈H∩K, as desired.
(Closed under−1) Givena∈H∩K, we havea−1∈H anda−1∈K sinceH andK are closed under
inverses. So ab∈H∩K as desired.
Thus,H∩K is a subgroup of G. QED
See 3 for another problem where you have to prove that a subset is a subgroup.
Cyclic Subroups. An element g∈G generates the cyclic subgroup ⟨g⟩ ={gm|m∈ Z}. There are many
therorems about cyclic groups, but for the algebra exam, one key fact to know is that g has ﬁnite order if
and only if⟨g⟩ is ﬁnite, in which case o(g) =o(⟨g⟩). [Do you know why this fact is true?]
See 2 and 6 for problems involving cyclic subgroups.
Lagrange’s Theorem. This theorem says that if H is a subgroup of a ﬁnite group G, then the order of H
divides the order of G. That is, |H|
⏐⏐|G|. When g is an element of a ﬁnite group G, Lagrange’s Theorem has
several important consequences:
• If|G| is prime, then G is cyclic.
• For allg∈G, we have o(g)
⏐⏐|G|.
• For allg∈G, we have g|G| =e.
These consequences all follow from Lagrange, using the fact that for any g∈ G, we have o(g) =|⟨g⟩|.
[Be sure you know how to use this fact to prove the statements above!] In fact, on the comps, if you have
a ﬁnite group G and want to conclude any of the three bulleted statements above, you may justify simply
by saying “by Lagrange’s Theorem.” See 2 , 8 , and 9 for problems that use these corollary versions of
Lagrange’s Theorem.
:::
