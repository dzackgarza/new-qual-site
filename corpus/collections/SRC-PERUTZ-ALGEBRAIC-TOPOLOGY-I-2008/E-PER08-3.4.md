---
schema: qual/card@1
id: E-PER08-3.4
kind: problem
title: Perutz Algebraic Topology I Exercise 3.4
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
In this exercise we show that the modular group, PSL 2(Z) =SL2(Z)/{±I},
is the free product (Z/2)∗ (Z/3). Deﬁne three elements of SL2(Z),
S =
[ 0 1
−1 0
]
, T =
[ 1 −1
0 1
]
, U =ST =
[ 0 1
−1 1
]
.
(a) Verify that S2 =U3 =−I.
(b) Show that, for any A∈ SL2(Z), there is an n∈ Z such that the matrix[
a b
c d
]
=ATn has c = 0 or|d|≤| c|/2.
(c) Explain how to ﬁnd an integer l≥ 0 and a sequence of integers n1,...,n l
such that either ATn1STn2S...ST l or ATn1STn2S...ST lS has 0 as its
lower-left entry.
(d) Show that S and T generate SL2(Z).
(e)* Deﬁne θ :⟨a,b | a2,b 3⟩ = ( Z/2)∗ (Z/3) → PSL 2(Z) to be the unique
homomorphism such that θ(a) = ±S and θ(b) = ±U. Remind yourself
how PSL 2(R) acts on the upper half-plane H⊂ C by M¨ obius maps. Take
1⁄= w∈ (Z/2)∗ (Z/3). Prove that the M¨ obius map µw corresponding to
θ(w)∈PSL 2(R) has the property that µw(D)∩D =∅, where
D ={z∈ H : 0< Rez <1/2,|z− 1|> 1}.
[Hint: consider A :={z∈ H : Re z > 0} and B :={z∈ H :|z− 1| >
max(1,|z|)}.] Deduce that θ is an isomorphism.
:::
