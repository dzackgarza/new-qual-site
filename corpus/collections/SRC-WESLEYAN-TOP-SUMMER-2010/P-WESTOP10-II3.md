---
schema: qual/card@1
id: P-WESTOP10-II3
kind: problem
title: Homology of thickened-knot and slice-disk complements
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. A thickened knot is an embedding
   \[
   K:S^1\times D^2\to S^3.
   \]
   Its complement is $S^3\setminus\operatorname{im}(K)$. Calculate
   \[
   H_n(S^3\setminus\operatorname{im}(K))
   \]
   for every knot $K$ and every $n$.

2. A knot is *slice* if it extends to an embedding
   \[
   \Delta:D^2\times D^2\to B^4
   \]
   with $S^1=\partial D^2$ and $S^3=\partial B^4$. Calculate the homology groups of the slice-disk complement
   \[
   B^4\setminus\operatorname{im}(\Delta).
   \]
:::

::: {.solution}
All homology and cohomology groups below have integral coefficients.

<1>1. Let
\[
A
\coloneqq
\operatorname{im}(K)
\subseteq
S^3.
\]
Then
\[
A
\cong
S^1\times D^2
\simeq
S^1.
\]

::: {.proof}
The embedding
\[
K:S^1\times D^2\to S^3
\]
is a homeomorphism onto its image.
The disk factor
\[
D^2
\]
is contractible, so projection onto the first factor is a homotopy
equivalence
\[
S^1\times D^2
\simeq
S^1.
\]
:::

<1>2. Therefore
\[
\widetilde H^j(A)
\cong
\begin{cases}
\mathbb Z,&j=1,\\
0,&j\ne1.
\end{cases}
\]

::: {.proof}
By step <1>1,
\[
A\simeq S^1.
\]
The reduced cohomology of the circle is
\[
\widetilde H^1(S^1)
\cong
\mathbb Z
\]
and vanishes in all other degrees.
:::

<1>3. Alexander duality gives
\[
\widetilde H_i(S^3\setminus A)
\cong
\widetilde H^{,2-i}(A).
\]

::: {.proof}
For a compact locally contractible subset
\[
A\subset S^n,
\]
Alexander duality states
\[
\widetilde H_i(S^n\setminus A)
\cong
\widetilde H^{,n-i-1}(A).
\]
Here
\[
n=3.
\]
The set $A$ is a compact manifold with boundary, hence locally
contractible, so the theorem applies.
:::

<1>4. The complement of every thickened knot has homology
\[
\boxed{
H_i(S^3\setminus\operatorname{im}(K))
\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
0,&i\ge2.
\end{cases}
}
\]

::: {.proof}
By steps <1>2--<1>3,
\[
\widetilde H_i(S^3\setminus A)
\]
is nonzero only when
\[
2-i=1,
\]
that is,
\[
i=1.
\]
In that degree,
\[
\widetilde H_1(S^3\setminus A)
\cong
\mathbb Z.
\]

For
\[
i=0,
\]
Alexander duality gives
\[
\widetilde H_0(S^3\setminus A)
\cong
\widetilde H^2(A)
=
0,
\]
so the complement is connected and
\[
H_0\cong\mathbb Z.
\]
All higher reduced homology groups vanish.
:::

<1>5. Now let
\[
B
\coloneqq
\operatorname{im}(\Delta)
\subseteq
B^4.
\]
Then
\[
B
\cong
D^2\times D^2,
\]
and its intersection with the boundary is
\[
B\cap\partial B^4
\cong
S^1\times D^2.
\]

::: {.proof}
The map
\[
\Delta:D^2\times D^2\to B^4
\]
is an embedding and is assumed to extend the thickened knot on the
boundary.
Thus the boundary part corresponding to
\[
\partial D^2\times D^2
=
S^1\times D^2
\]
lies in
\[
\partial B^4=S^3.
\]
Hence the displayed pair is homeomorphic to
\[
(D^2\times D^2,S^1\times D^2).
\]
:::

<1>6. The pair
\[
(B,B\cap\partial B^4)
\]
is homotopy equivalent as a pair to
\[
(D^2,S^1).
\]

::: {.proof}
The second disk factor
\[
D^2
\]
is contractible.
Projection onto the first factor gives a homotopy equivalence of pairs
\[
(D^2\times D^2,S^1\times D^2)
\simeq
(D^2,S^1).
\]
:::

<1>7. Its relative cohomology is
\[
H^j(B,B\cap\partial B^4)
\cong
\begin{cases}
\mathbb Z,&j=2,\\
0,&j\ne2.
\end{cases}
\]

::: {.proof}
By step <1>6 it suffices to compute
\[
H^*(D^2,S^1).
\]
The quotient
\[
D^2/S^1
\]
is homeomorphic to
\[
S^2.
\]
Hence
\[
H^j(D^2,S^1)
\cong
\widetilde H^j(S^2),
\]
which is
\[
\mathbb Z
\]
in degree $2$ and zero otherwise.
:::

<1>8. Relative Alexander duality for a compact locally contractible
subset of the ball gives
\[
\widetilde H_i(B^4\setminus B)
\cong
H^{,3-i}(B,B\cap\partial B^4).
\]

::: {.proof}
The ball version of Alexander duality states that for a compact locally
contractible
\[
A\subseteq B^n
\]
meeting the boundary in
\[
A\cap S^{n-1},
\]
one has
\[
\widetilde H_i(B^n\setminus A)
\cong
H^{,n-i-1}(A,A\cap S^{n-1}).
\]
Here
\[
n=4
\]
and
\[
A=B.
\]
:::

<1>9. Therefore the slice-disk complement has homology
\[
\boxed{
H_i(B^4\setminus\operatorname{im}(\Delta))
\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
0,&i\ge2.
\end{cases}
}
\]

::: {.proof}
By steps <1>7--<1>8, reduced homology is nonzero only when
\[
3-i=2,
\]
that is,
\[
i=1.
\]
In that degree,
\[
\widetilde H_1(B^4\setminus B)
\cong
\mathbb Z.
\]

For
\[
i=0,
\]
the dual group is
\[
H^3(B,B\cap\partial B^4)
=
0,
\]
so the complement is connected and
\[
H_0\cong\mathbb Z.
\]
All higher groups vanish.
:::

<1>10. Thus both complements have the homology of a circle:
\[
\boxed{
H_*(S^3\setminus\operatorname{im}(K))
\cong
H_*(B^4\setminus\operatorname{im}(\Delta))
\cong
H_*(S^1).
}
\]

::: {.proof}
Compare steps <1>4 and <1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>4 solves part (1), and step <1>9 solves part (2).
:::
:::
