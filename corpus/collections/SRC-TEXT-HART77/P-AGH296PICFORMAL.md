---
schema: qual/card@1
id: P-AGH296PICFORMAL
kind: problem
title: The Picard group of a noetherian formal scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Picard Groups
  - Mittag-Leffler Condition
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts and both compatibility warnings with the retained Hartshorne II.9.6 transcription. Checked inverse systems and coherent formal modules against Stacks Project sections 12.31 and 30.23. The proof passes from stabilized ring images to their unit groups, constructs compatible trivializations from stabilized sets of isomorphisms, and lifts a frame on one fixed affine formal open at every level.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $\mathfrak{X}$ be a noetherian formal scheme, let $\mci$ be an ideal of definition, and for each $n\ge1$ let $Y_n$ be the scheme $(\mathfrak{X}, \OO_\mathfrak{X}/\mci^n)$.
Assume that the inverse system of groups $(\Gamma(Y_n, \OO_{Y_n}))$ satisfies the Mittag-Leffler condition.
Then prove that $\Pic \mathfrak{X} = \inverselim_n \Pic Y_n$.
As in the case of a scheme, we define $\Pic \mathfrak{X}$ to be the group of locally free $\OO_\mathfrak{X}\dash$modules of rank $1$ under $\tensor$.
Proceed in the following steps.

(a) Use the fact that $\ker(\Gamma(Y_{n+1}, \OO_{Y_{n+1}}) \to \Gamma(Y_n, \OO_{Y_n}))$ is a nilpotent ideal to show that the inverse system $(\Gamma(Y_n, \OO_{Y_n}^*))$ of units in the respective rings also satisfies (ML).

(b) Let $\mcf$ be a coherent sheaf of $\OO_\mathfrak{X}\dash$modules, and assume that for each $n$ there is some isomorphism $\varphi_n: \mcf/\mci^n \mcf \cong \OO_{Y_n}$.
Then show that there is an isomorphism $\mcf \cong \OO_\mathfrak{X}$.
Be careful, because the $\varphi_n$ may not be compatible with the maps in the two inverse systems $(\mcf/\mci^n \mcf)$ and $(\OO_{Y_n})$.
Conclude that the natural map $\Pic \mathfrak{X} \to \inverselim_n \Pic Y_n$ is injective.

(c) Given an invertible sheaf $\mcl_n$ on $Y_n$ for each $n$, and given isomorphisms $\mcl_{n+1} \tensor \OO_{Y_n} \cong \mcl_n$, construct maps $\mcl_{n'} \to \mcl_n$ for each $n' \geq n$ so as to make an inverse system, and show that $\mcl = \inverselim_n \mcl_n$ is a coherent sheaf on $\mathfrak{X}$.
Then show that $\mcl$ is locally free of rank $1$, and thus conclude that the map $\Pic \mathfrak{X} \to \inverselim_n \Pic Y_n$ is surjective.
Be careful here, because even though each $\mcl_n$ is locally free of rank $1$, the open sets needed to make them free might get smaller and smaller with $n$.

(d) Show that the hypothesis that $(\Gamma(Y_n, \OO_{Y_n}))$ satisfies (ML) holds if either $\mathfrak{X}$ is affine, or the $Y_n$ are projective over a common field $k$ with the transition morphisms taken over $k$.
See (III, Ex. 11.5--11.7) for further examples and applications.
:::

::: {.solution}
Put $A_n=\Gamma(Y_n,\OO_{Y_n})$ and $G_n=A_n^\times$.
The latter is also $\Gamma(Y_n,\OO_{Y_n}^*)$: the local inverses of an everywhere invertible section agree and glue.
For an inverse system, the Mittag--Leffler condition means that the images in each fixed term stabilize [@Har10a, Chapter II, §9].
All the sheaves on the thickenings are regarded as sheaves on their common underlying space $|\mathfrak X|$.

<1>1. For $m\ge n$, the kernel of $A_m\to A_n$ is nilpotent, and
$$
\im(G_m\to G_n)=\bigl(\im(A_m\to A_n)\bigr)^\times.
$$

::: {.proof}
A section in the kernel belongs to the ideal sheaf $\mci^n/\mci^m$ on $Y_m$.
A product of $q$ such sections vanishes whenever $nq\ge m$.
Thus the ring kernel is nilpotent.

For any ring $R$ and nilpotent ideal $J$, the map $R^\times\to(R/J)^\times$ is surjective.
Indeed, lift a unit and its inverse to $a,b\in R$.
Then $ab=1+c$ with $c\in J$, and $1+c$ has inverse $1-c+c^2-\cdots$, a finite sum because $c$ is nilpotent.
Hence $a$ is a unit with inverse $b(1+c)^{-1}$.
Apply this to the surjection from $A_m$ onto its image in $A_n$.
It gives the displayed equality, with the units on the right taken in that image subring.
It does not assume that $A_m\to A_n$ is surjective or that an arbitrary subring contains inverses of all its elements which are units in the ambient ring.
:::

<1>2. The inverse system $(G_n)$ satisfies the Mittag--Leffler condition, proving (a).

::: {.proof}
Fix $n$.
The assumed Mittag--Leffler condition on $(A_n)$ gives $N\ge n$ such that
$$
\im(A_m\to A_n)=\im(A_N\to A_n)\qquad(m\ge N).
$$
Equality of these additive-group images is equality of their image subrings, with the same identity and multiplication.
Their unit groups are consequently equal.
Step <1>1 identifies these groups with the images of $G_m$ in $G_n$, so those images stabilize as well.
:::

<1>3. In (b), the isomorphisms $\mcf/\mci^n\mcf\cong\OO_{Y_n}$ can be chosen compatibly for all $n$.

::: {.proof}
Write $F_n=\mcf/\mci^n\mcf$ and let
$$
T_n=\operatorname{Isom}_{\OO_{Y_n}}(F_n,\OO_{Y_n}).
$$
Each $T_n$ is nonempty by hypothesis.
Postmultiplication by a unit gives a free transitive action of $G_n$ on $T_n$: two trivializations differ by a unique automorphism of $\OO_{Y_n}$, hence by a unique global unit.
Reduction gives maps $T_m\to T_n$ compatible with $G_m\to G_n$ because $F_m\otimes\OO_{Y_n}=F_n$.

For fixed $n$, the image of $T_m$ in $T_n$ is one orbit of the subgroup $\im(G_m\to G_n)$.
These images are nonempty and form a decreasing family.
By step <1>2 their acting subgroups stabilize.
Once the subgroups agree, two nested nonempty orbits must coincide: if they share a point, both are the orbit of that point under the same subgroup.
Thus the images of $T_m$ in $T_n$ stabilize.
Denote the stable image by $T_n^\infty$.

The maps $T_{n+1}^\infty\to T_n^\infty$ are surjective.
To see this, choose $m$ so large that the images from $T_m$ have stabilized at both $n$ and $n+1$.
Any element of $T_n^\infty$ lifts from $T_m$, and the image of that lift at $n+1$ lies in $T_{n+1}^\infty$.
Choose an element in $T_1^\infty$ and recursively lift it through these surjections.
The resulting sequence $(\psi_n)$ is a compatible family of trivializations, rather than the initially unrelated family $(\varphi_n)$.
:::

<1>4. The sheaf in (b) is trivial, and the restriction homomorphism
$$
\Phi:\Pic(\mathfrak X)\longrightarrow\varprojlim_n\Pic(Y_n)
$$
is injective.

::: {.proof}
Coherent formal sheaves are recovered from their compatible reductions [@Har10a, Proposition II.9.6], so
$$
\mcf\cong\varprojlim_n F_n.
$$
The compatible isomorphisms $\psi_n$ from step <1>3, together with their compatible inverses, give
$$
\mcf\cong\varprojlim_n\OO_{Y_n}=\OO_{\mathfrak X}.
$$
This proves the first assertion of (b).

For an invertible sheaf $L$ on $\mathfrak X$, set $L_n=L\otimes\OO_{Y_n}$.
These restrictions preserve tensor products, so the assignment $[L]\mapsto([L_n])$ defines the homomorphism $\Phi$.
Invertible sheaves on a noetherian formal scheme are coherent.
If $[L]$ belongs to its kernel, every $L_n$ is trivial, so the preceding argument with $\mcf=L$ gives $L\cong\OO_{\mathfrak X}$.
Thus $\Phi$ has zero kernel.
:::

<1>5. The data in (c) give a coherent sheaf $L=\varprojlim_n L_n$ with $L/\mci^nL\cong L_n$.

::: {.proof}
Let $\alpha_n:L_{n+1}\otimes\OO_{Y_n}\xrightarrow{\cong}L_n$ be the given isomorphism.
Define $t_{n+1,n}$ as the quotient map $L_{n+1}\to L_{n+1}\otimes\OO_{Y_n}$ followed by $\alpha_n$.
Define every longer transition as the composite of these adjacent transitions and $t_{n,n}=\id$.
The composition identities then hold by construction.

The adjacent maps are surjective with kernel $\mci^n L_{n+1}$.
More generally, repeated reduction gives $L_m\otimes\OO_{Y_n}\cong L_n$ for every $m\ge n$, with the composite just defined as its quotient map.
Each $L_n$ is coherent on the noetherian scheme $Y_n$.
These are precisely the compatibility conditions of [@Har10a, Proposition II.9.6].
That proposition gives coherence of $L$ and the asserted identifications of all its reductions.
:::

<1>6. The sheaf $L$ in step <1>5 is locally free of rank one, and $\Phi$ is surjective.

::: {.proof}
Fix a point of $\mathfrak X$ and choose an affine formal neighborhood $\mathfrak U$ on which $L_1$ is trivial.
This is possible because the affine formal opens form a basis and $L_1$ is invertible.
Write $U_n$ for the corresponding affine open of $Y_n$, and choose a frame $s_1\in\Gamma(U_1,L_1)$.

Suppose a frame $s_n$ has been chosen.
The surjection $L_{n+1}|_{U_{n+1}}\to L_n|_{U_n}$ is a surjection of quasi-coherent sheaves on the affine scheme $U_{n+1}$, with $L_n$ regarded there through the quotient structure sheaf.
Exactness of affine sections therefore lifts $s_n$ to a section $s_{n+1}$ of $L_{n+1}$ on that same open [@Har10a, Proposition II.5.6].
At every stalk, express $s_{n+1}$ in a local frame of $L_{n+1}$.
Its coefficient becomes a unit after reduction to $U_n$, since $s_n$ is a frame.
The kernel of this local ring quotient is nilpotent, so the coefficient itself is a unit by the calculation in step <1>1.
Hence $s_{n+1}$ is a frame on all of $U_{n+1}$.

Induction gives compatible frames on the fixed neighborhood $\mathfrak U$, without shrinking it as $n$ increases.
They define compatible isomorphisms $\OO_{U_n}\xrightarrow{\cong}L_n|_{U_n}$.
Taking their inverse limits and using the sectionwise construction of limits [@Har10a, Proposition II.9.2] gives
$$
\OO_{\mathfrak U}\xrightarrow{\cong}L|_{\mathfrak U}.
$$
Thus $L$ is invertible.

An element of $\varprojlim_n\Pic(Y_n)$ gives representatives $L_n$ and choices of adjacent isomorphisms $\alpha_n$ as in step <1>5.
The invertible $L$ just constructed restricts to every prescribed class, so it maps to that element under $\Phi$.
This proves surjectivity; the uniqueness of its class follows from step <1>4.
:::

<1>7. Both sufficient hypotheses in (d) imply the required Mittag--Leffler condition.

::: {.proof}
If $\mathfrak X$ is affine, every $Y_n$ is affine.
The sequence
$$
0\to\mci^n/\mci^{n+1}\to\OO_{Y_{n+1}}
\to\OO_{Y_n}\to0
$$
is exact as a sequence of quasi-coherent sheaves on the affine scheme $Y_{n+1}$.
Taking sections gives a surjection $A_{n+1}\to A_n$.
All longer transition maps are then surjective, so their images in a fixed $A_n$ are always $A_n$.

In the projective case, each $A_n$ is finite-dimensional over $k$ by finiteness of coherent cohomology [@Har10a, Theorem III.5.2].
The transition maps are $k$-linear.
For fixed $n$, the images of $A_m$ in $A_n$ form a descending sequence of vector subspaces of a finite-dimensional space.
Their dimensions eventually stop decreasing, after which nested subspaces of equal dimension are equal.
Thus these images stabilize, proving the Mittag--Leffler condition.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove (a), steps <1>3--<1>4 prove (b), steps <1>5--<1>6 prove (c), and step <1>7 proves (d).
Since restriction is a homomorphism and is both injective and surjective, the requested canonical isomorphism is
$$
\boxed{\Pic(\mathfrak X)\xrightarrow{\cong}\varprojlim_n\Pic(Y_n),
\qquad [L]\longmapsto([L\otimes\OO_{Y_n}])_{n\ge1}.}
$$
:::
:::
