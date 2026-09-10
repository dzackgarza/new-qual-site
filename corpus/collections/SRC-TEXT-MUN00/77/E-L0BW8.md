---
schema: qual/card@1
id: E-L0BW8
kind: problem
title: The reduction algorithm applied to eight schemes
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

The proof of the classification theorem provides an algorithm for taking a proper labelling scheme for a polygonal region and reducing it to one of the four standard forms indicated in the theorem.
The appropriate equivalences are the following:

(i) $[y_0]a[y_1]a[y_2] \sim aa[y_0 y_1^{-1} y_2]$.

(ii) $[y_0]aa^{-1}[y_1] \sim [y_0 y_1]$ if $y_0 y_1$ has length at least 4.

(iii) $w_0[y_1]a[y_2]b[y_3]a^{-1}[y_4]b^{-1}[y_5] \sim w_0 aba^{-1}b^{-1}[y_1 y_4 y_3 y_2 y_5]$.

(iv) $w_0(cc)(aba^{-1}b^{-1})w_1 \sim w_0 aabbcc w_1$.

Using this algorithm, reduce each of the following schemes to one of the standard forms.

(a) $abacb^{-1}c^{-1}$

(b) $abca^{-1}cb$

(c) $abbca^{-1}ddc^{-1}$

(d) $abcda^{-1}b^{-1}c^{-1}d^{-1}$

(e) $abcda^{-1}c^{-1}b^{-1}d^{-1}$

(f) $aabcdc^{-1}b^{-1}d^{-1}$

(g) $abcdabdc$

(h) $abcdabcd$
:::

::: {.solution}
We use only cyclic permutation, flipping/relabeling, and the four equivalences (i)--(iv) stated in the exercise. Brackets below merely indicate the subwords to which an equivalence is applied.

(a)
\[
abacb^{-1}c^{-1}
 =a[b]a[cb^{-1}c^{-1}]
 \overset{(i)}\sim
 aa\,b^{-1}cb^{-1}c^{-1}.
\]
Apply (i) again to the two occurrences of \(b^{-1}\):
\[
aa\,b^{-1}[c]b^{-1}[c^{-1}]
\sim aa\,bb\,cc
\]
after relabeling. Thus the standard form is
\[
\boxed{aabbcc},
\]
so the surface is \(P_3\).

(b) Cyclically permute so the two \(b\)'s are the repeated letter:
\[
b[ca^{-1}c]b[a]
\overset{(i)}\sim
bb\,c^{-1}ac^{-1}a.
\]
Now apply (i) to the two \(c^{-1}\)'s:
\[
bb\,c^{-1}[a]c^{-1}[a]
\sim cc\,bb\,a^{-1}a.
\]
The adjacent inverse pair cancels by (ii), leaving
\[
\boxed{aabb}.
\]
Hence the surface is \(P_2\cong K\).

(c) The adjacent \(b\)'s and \(d\)'s can first be moved to the front by repeated use of (i) (with empty middle word where appropriate). After cyclic permutation/relabeling this gives
\[
abbca^{-1}ddc^{-1}\sim
bb\,dd\,(c^{-1}aca^{-1}).
\]
The last four letters are a commutator after relabeling. Thus we have two projective pairs followed by one torus pair. Applying (iv) to one projective pair and the commutator replaces those six letters by three projective pairs. Together with the untouched pair this gives
\[
\boxed{aabbccdd}.
\]
Hence the surface is \(P_4\).

(d) The scheme is of torus type. In (iii), take \(a,b\) as the first two displayed labels and \(y_3=cd\), \(y_5=c^{-1}d^{-1}\), with the other \(y_i\)'s empty. Then
\[
abcda^{-1}b^{-1}c^{-1}d^{-1}
\overset{(iii)}\sim
aba^{-1}b^{-1}cdc^{-1}d^{-1}.
\]
This is already the standard genus-two orientable form:
\[
\boxed{(aba^{-1}b^{-1})(cdc^{-1}d^{-1})},
\]
so the surface is \(T_2\).

(e) Again apply (iii) to the \(a,b,a^{-1},b^{-1}\) occurrences:
\[
abcda^{-1}c^{-1}b^{-1}d^{-1}
\sim
aba^{-1}b^{-1}c^{-1}cd d^{-1}.
\]
Two applications of (ii) cancel \(c^{-1}c\) and \(dd^{-1}\). Hence
\[
\boxed{aba^{-1}b^{-1}},
\]
and the surface is \(T_1\), the torus.

(f) Keep the initial \(aa\). In the torus-type tail choose the letters \(b,d,b^{-1},d^{-1}\) in (iii):
\[
aa\,bcd c^{-1}b^{-1}d^{-1}
\overset{(iii)}\sim
 aa\,(bdb^{-1}d^{-1})\,c^{-1}c.
\]
Cancel \(c^{-1}c\) by (ii). We obtain one projective pair followed by one commutator:
\[
aa\,(bdb^{-1}d^{-1}).
\]
Equivalence (iv) turns this into three projective pairs, so
\[
\boxed{aabbcc},
\]
and the surface is \(P_3\).

(g) Apply (i) to the two occurrences of \(a\):
\[
a[bcd]a[bdc]
\sim
 aa\,d^{-1}c^{-1}b^{-1}bdc.
\]
Cancel the adjacent \(b^{-1}b\) by (ii):
\[
aa\,d^{-1}c^{-1}dc.
\]
The last four letters form a commutator after replacing \(d^{-1},c^{-1}\) by new generators. Thus (iv) again converts one projective pair plus one torus pair into three projective pairs:
\[
\boxed{aabbcc}.
\]
Hence the surface is \(P_3\).

(h) Apply (i) to the two \(a\)'s:
\[
a[bcd]a[bcd]
\sim
 aa\,d^{-1}c^{-1}b^{-1}bcd.
\]
Successive applications of (ii) cancel \(b^{-1}b\) and \(c^{-1}c\), giving
\[
aa\,d^{-1}d.
\]
This is the length-four projective base case in the proof of Theorem 77.5; Lemma 77.1 read backwards, followed by relabeling, gives
\[
aa\,d^{-1}d\sim abab.
\]
Therefore the standard form is
\[
\boxed{abab},
\]
which represents \(P^2\).

As a check, the quotient cell structures have respectively Euler characteristics
\[
-1,0,-2,-2,0,-1,-1,1,
\]
and the schemes are orientable exactly in (d) and (e), agreeing with the eight identifications above.
:::
