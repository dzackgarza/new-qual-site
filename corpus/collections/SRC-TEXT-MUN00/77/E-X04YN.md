---
schema: qual/card@1
id: E-X04YN
kind: problem
title: Elementary operations behind the classification figures
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

(a) Write down the sequence of elementary operations required to carry out the arguments indicated in Figures 77.1 and 77.2.

(b) Write down the sequence of elementary operations required to carry out the arguments indicated in Figures 77.3, 77.4, and 77.5.
:::

::: {.solution}
The figures occur in the proofs of Lemmas 77.1 and 77.3. Writing only the boundary schemes after each elementary cut/paste, the operations are as follows.

(a) **Figure 77.1.**  In Step 1 of Lemma 77.1, begin with
\[
a[y_1]a[y_2].
\]
Cut along the auxiliary arc shown in the figure, obtaining two polygonal regions with a new label on the cut edges; paste the two original \(a\)-edges, and then relabel the new boundary pair by \(a\). The resulting scheme is
\[
aa[y_1^{-1}y_2].
\]
Thus the sequence of elementary operations is
\[
\boxed{\text{cut}\;\longrightarrow\;\text{paste along the two }a\text{-edges}\;\longrightarrow\;\text{relabel}},
\]
with boundary-word effect
\[
a[y_1]a[y_2]\sim aa[y_1^{-1}y_2].
\]
If one of the bracketed words is empty, the same equivalence is obtained by the permitted permutation/flipping operations, exactly as in the proof.

**Figure 77.2.**  For
\[
[y_0]a[y_1]a[y_2]
\]
with \(y_0\ne\varnothing\), the figure's cut-and-paste gives
\[
[y_0]a[y_1]a[y_2]
\sim b[y_2]b[y_1y_0^{-1}].
\]
Apply the Figure 77.1 move to the two \(b\)'s:
\[
b[y_2]b[y_1y_0^{-1}]
\sim bb[y_2^{-1}y_1y_0^{-1}].
\]
Flip, then cyclically permute and relabel:
\[
bb[y_2^{-1}y_1y_0^{-1}]
\sim [y_0y_1^{-1}y_2]b^{-1}b^{-1}
\sim aa[y_0y_1^{-1}y_2].
\]
Hence Figure 77.2 is implemented by one cut, one paste, followed by the already established Figure 77.1 operation, a flip, a permutation, and relabelling.

(b) Now write the torus-type scheme in the form
\[
w=w_0[y_1]a[y_2]b[y_3]a^{-1}[y_4]b^{-1}[y_5].
\]

**Figure 77.3 (first cut-and-paste).** Regroup as
\[
w_0[y_1]a[y_2by_3]a^{-1}[y_4b^{-1}y_5].
\]
Cut along the auxiliary edge \(c\) and paste along the indicated \(a\)-pair. The boundary becomes
\[
w_0c[y_2by_3]c^{-1}[y_1y_4b^{-1}y_5].
\]
Relabel the auxiliary pair and regroup to obtain
\[
w'=
 w_0a[y_2]b[y_3]a^{-1}[y_1y_4]b^{-1}[y_5].
\]

**Figure 77.4 (second cut-and-paste).** Starting from \(w'\), cut and paste as shown to get
\[
w'\sim
w_0c[y_1y_4y_3]a^{-1}c^{-1}a[y_2y_5].
\]
Relabel \(c,a\) appropriately and regroup:
\[
w''=
 w_0a[y_1y_4y_3]ba^{-1}b^{-1}[y_2y_5].
\]
In the exceptional case where the auxiliary cut is unnecessary, the same word is obtained by a cyclic permutation followed by relabelling, as in the proof of Lemma 77.3.

**Figure 77.5 (third cut-and-paste).** From \(w''\), perform the final cut and paste:
\[
w''\sim
w_0ca^{-1}c^{-1}a[y_1y_4y_3y_2y_5].
\]
After relabelling and permuting this is
\[
\boxed{
 w_0aba^{-1}b^{-1}[y_1y_4y_3y_2y_5]
}.
\]
Thus Figures 77.3--77.5 are precisely the three successive cut--paste--relabel operations used to extract the commutator \(aba^{-1}b^{-1}\) in Lemma 77.3.
:::
