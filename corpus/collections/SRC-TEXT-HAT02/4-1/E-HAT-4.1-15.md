---
schema: qual/card@1
id: E-HAT-4.1-15
kind: problem
title: "Every self-map of $S^n$ is a multiple of the identity"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-02
  note: >-
    The statement printed the book's closing hint twice in part (c), "(Use Gaussian elimination, for
    example.) (Use Gaussian elimination, for example.)". AT.txt:17886 prints it once, so this was a
    duplication introduced when the hint was restored, not a second printed hint; one copy is removed.
    No other statement text is touched.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17876-17886 for the exercise, 17448-17456 for Lemma 4.10,
    17395-17397 for cellular approximation). Part (a) was a black box: it said "By Lemma 4.10
    (equivalently, after simplicial approximation and a small local modification), f is homotopic to a
    map for which there is a point q with f^-1(q) = {p_1,...,p_k} and f invertible linear near each p_i",
    which is the step the exercise asks the solver to perform, and Lemma 4.10 as printed does not state
    any genericity conclusion. Part (a) now derives it: apply the lemma with Z = S^n obtained from its
    0-cell by attaching the n-cell, which homotopes f to a map f_1 that is piecewise linear on a
    polyhedron K containing f_1^{-1}(U) for a nonempty open U in the top cell; choose q in U avoiding
    the images of the lower-dimensional pieces and the singular sets of the top-dimensional affine maps,
    a finite union of proper affine subspaces; then f_1^{-1}(q) is finite and lies in the interiors of
    top-dimensional pieces, where f_1 is a nonsingular affine map. Parts (b) and (c) were read and left
    unchanged: the pinch decomposition gives [f] = sum [h_i] in pi_n(S^n), and GL_n(R) has two path
    components by sign of determinant, with the reflection having degree -1. Not checked: no recomputation
    of local degrees, and the deformation in (c) is accepted at the level of the standard argument rather
    than expanded.

---

::: {.problem}
Show that every map $f: S^n \to S^n$ is homotopic to a multiple of the identity map by the following steps.

(a) Use Lemma 4.10 (or simplicial approximation, Theorem 2C.1) to reduce to the case that there exists a point $q \in S^n$ with $f^{-1}(q) = \{p_1, \ldots, p_k\}$ and $f$ is an invertible linear map near each $p_i$.

(b) For $f$ as in (a), consider the composition $gf$ where $g: S^n \to S^n$ collapses the complement of a small ball about $q$ to the basepoint.
Use this to reduce (a) further to the case $k = 1$.

(c) Finish the argument by showing that an invertible $n \times n$ matrix can be joined by a path of such matrices to either the identity matrix or the matrix of a reflection. (Use Gaussian elimination, for example.)
:::

::: {.solution}
Let $f:S^n\to S^n$.

### (a) Reduction to finitely many regular preimages

Lemma 4.10 supplies the reduction, and here is how. Give $S^n$ the CW structure with one $0$-cell $W$ and one $n$-cell $e^n$, so that $S^n-e^n=W$, and apply the lemma with $Z=S^n$, that $W$ and $e^k=e^n$, on the domain $I^n$ of the characteristic map: it homotopes $f$ rel $f^{-1}(W)$, hence rel $\partial I^n$, to a map $f_1$ for which there is a polyhedron $K\subset S^n$ with $f_1(K)\subset e^n$ and $f_1\restrict_K$ piecewise linear, and with $K\supset f_1^{-1}(U)$ for some nonempty open $U\subset e^n$. Because the homotopy is fixed on $f^{-1}(W)\supset\partial I^n$, it glues to a homotopy of $f$ on $S^n$.

Identify $e^n$ with $\RR^n$ and write $K$ as a finite polyhedral complex -- a finite union of convex polyhedra closed under taking faces -- on each piece of which $f_1$ is affine. Let $N\subset e^n$ be the union of the images of the pieces of dimension less than $n$, which lie in affine subspaces of dimension less than $n$, together with, for each $n$-dimensional piece, the image of the set on which that piece's affine map is singular, which is again an affine subspace of dimension less than $n$. Thus $N$ is a finite union of proper affine subspaces, so $U\setminus N$ is nonempty; choose $q$ in it.
Since $q\in U$ and $K\supset f_1^{-1}(U)$, the preimage $f_1^{-1}(q)$ lies in $K$. On each $n$-dimensional piece the affine map is nonsingular, hence injective, so it has at most one preimage of $q$, and it has one exactly when $q$ lies in its image; on each lower-dimensional piece it has none. Since interiors of pieces of the complex are disjoint and cover $K$ minus the lower-dimensional pieces, any preimage of $q$ lies in the interior of a unique $n$-dimensional piece, where a whole ball around it lies in that piece. Hence
$$
f_1^{-1}(q)=\{p_1,\dots,p_k\}
$$
is finite, and at each $p_i$ the map $f_1$ agrees with an invertible affine map on a neighbourhood of $p_i$ in its piece, that is, with an invertible linear map in suitable coordinates. Choose pairwise disjoint small balls $B_i$ about the $p_i$'s and a ball $B$ about $q$ so that
$$
f\restrict_{B_i}:B_i\to B
$$
is linear and invertible in these coordinates.

### (b) Split into one-preimage pieces

Let
$$
g:S^n\to S^n
$$
collapse the complement of the interior of $B$ to the basepoint. Choose spherical coordinates centered at $q$ and let $B$ be a polar ball. The map $g$ preserves each radial direction, stretches the radial coordinate of $B$ across the full interval from $q$ to the antipode, and sends all points outside $B$ to the antipode. Linear interpolation between the identity radial coordinate and this stretched coordinate is a homotopy from $\operatorname{id}_{S^n}$ to $g$. Thus
$$
gf\simeq f.
$$

The map $gf$ is constant off the union of the $B_i$'s. Collapsing the complement of the interiors of the $B_i$'s identifies the domain with a wedge
$$
S^n\vee\cdots\vee S^n
$$
of $k$ spheres, and $gf$ factors as
$$
S^n\xrightarrow{\text{pinch}}\bigvee_{i=1}^k S^n
\xrightarrow{h_1\vee\cdots\vee h_k}S^n,
$$
where each $h_i$ has exactly one preimage of $q$ and is linear near that point. In $\pi_n(S^n)$, this says
$$
[f]=[h_1]+\cdots+[h_k].
$$
So it remains to classify the case $k=1$.

### (c) The one-preimage case

For such a map, the local model near the unique preimage is an invertible matrix
$$
A\in GL_n(\RR).
$$
The group $GL_n(\RR)$ has exactly two path-components, distinguished by the sign of the determinant. Gaussian elimination through invertible matrices (or polar decomposition) gives a path in $GL_n(\RR)$ from $A$ to
$$
I\quad\text{if }\det A>0,
$$
and to a reflection
$$
R=\operatorname{diag}(-1,1,\dots,1)
\quad\text{if }\det A<0.
$$
Using this path inside the local ball and keeping the map constant outside gives a homotopy of $h_i$ to the identity map when $\det A>0$, and to a reflection when $\det A<0$. The latter represents $-[\operatorname{id}_{S^n}]$ in $\pi_n(S^n)$.

Hence, if
$$
\varepsilon_i=\operatorname{sign}(\det Df_{p_i})\in\{\pm1\},
$$
then
$$
[f]=\sum_{i=1}^k\varepsilon_i[\operatorname{id}_{S^n}].
$$
Writing
$$
d=\sum_i\varepsilon_i\in\ZZ,
$$
we obtain
$$
\boxed{f\simeq d\cdot\operatorname{id}_{S^n}.}
$$
Thus every self-map of $S^n$ is homotopic to an integral multiple of the identity.
:::
