---
schema: qual/card@1
id: P-AMH-ALG-SG16-07
kind: problem
title: Amherst algebra study guide problem 7
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
(February 2013) Let $G$ be a group, let $H\subseteq G$ be a subgroup, and let $N\trianglelefteq G$ be a normal subgroup.
Define
\[
NH=\{xh:x\in N\text{ and }h\in H\}.
\]
Prove that $NH$ is a subgroup of $G$.
:::

::: {.solution}
Proof.
(Nonempty): Since N and H are both nonempty, we may choose x∈ N and h∈ H. Then xh∈NH , so NH⁄= ∅. (Closed under ∗): Given x,y ∈ NH , write x = n1h1 and y = n2h2, for some n1,n 2 ∈ N and h1,h 2∈H. Since N is a normal subgroup of G, we have h1N =Nh 1. Thus, there is some n3∈N such that h1n2 =n3h1. So xy = (n1h1)(n2h2) =n1(h1n2)h2 =n1(n3h1)h2 = (n1n3)(h1h2)∈NH, as desired, since n1n3∈N and h1h2∈H. (Closed under inverses): Given x∈NH , write x =nh with n∈N and h∈H. Since N is a normal subgroup of G, we have hN =Nh.
Thus, there is some n1∈N such that nh =hn1. So x−1 = (nh)−1 = (hn1)−1 =n−1 1 h−1∈NH, as desired, since n−1 1 ∈N and h−1∈H. QED Alternate Proof.
(Nonempty): Since N andH are both nonempty, we may choose x∈N andh∈H. Then xh∈NH , so NH⁄= ∅. (Closed under ∗): Given x,y ∈ NH , write x = n1h1 and y = n2h2, for some n1,n 2 ∈ N and h1,h 2∈H. Then xy = (n1h1)(n2h2) =n1(h1n2)(h−1 1 h1)h2 = ( n1(h1n2h−1 1 ) ) (h1h2). Nown1,n 2∈N, and hence h1n2h−1 1 ∈N since N is normal, and therefore n1(h1n2h−1 1 )∈N. Since h1h2∈H, then the above equation shows xy∈NH , as desired.
(Closed under inverses): Given x∈NH , write x =nh with n∈N and h∈H. Then x−1 = (nh)−1 =h−1n−1 = (h−1n−1h)h−1. Nowh−1n−1h∈N since N is normal in G, and h−1∈H, so the above equation shows x−1∈NH , as desired.
QED
:::
