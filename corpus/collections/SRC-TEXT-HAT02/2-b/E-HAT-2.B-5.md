---
schema: qual/card@1
id: E-HAT-2.B-5
kind: problem
title: "Homology of complements of spheres in spheres"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 5, printed page
    176; the statement matches word for word. Checked: Alexander duality gives
    H̃_i(S^n − S) ≅ H̃^{n−i−1}(S^k) = Z exactly in degree r = n−k−1, matching
    H̃_*(S^r); the normal disk D^{n−k} meets S in one transverse point of the
    coordinate disk, so the Alexander-duality coordinate of the image of [S^r] is
    ±1 and the inclusion is an isomorphism in degree r and hence in all degrees,
    with the r = 0 case read on reduced H_0. No defect.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Added the omitted case k = n. Then the embedded n-sphere is all of S^n by
    invariance of domain, so S^{n-k-1} = S^{-1} and S^n - S are both empty and the
    inclusion is an isomorphism on homology. Alexander duality for a proper subsphere
    is now invoked only after reducing to k < n. The previous r = -1 calculation did
    not cover this case.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Rechecked all cases against Hatcher p.176 and Corollary 2B.4: k = n holds
    trivially, while for k < n the normal disk meets S in one transverse point, giving
    Alexander-duality coordinate plus or minus one for the image of the normal-sphere
    fundamental class. The r = 0 reduced-H_0 interpretation remains included.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdrew the added MSE 4773641 transcription as unverified. Independent review establishes
    that ell is the image of a half-sized open k-disk, not a closed subset, and that the omitted
    definitions of D and D' prevent checking excision and generalized Schoenflies. The previous
    text also repeated the thread's h'(S^k) notation although h' has domain D^n. The earlier
    Alexander-intersection proof and k=n case are unchanged; #105's complete-solution obligation
    for this card remains open. The excision condition is evaluated on closure_X(Z) and
    interior_X(A), not on interior of A minus Z; no counterexample based on the latter is
    asserted. Pairwise acyclicity of D and its ambient complement is not enough to deduce that
    the relative group vanishes in every degree, so the relative degrees still require checking
    before this source is accepted.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Added an independent second proof, step 4, following the answer to MSE 4773641 with each
    auxiliary set and each hypothesis checked, and supplying the generalized Schoenflies theorem
    that answer invokes. Checked: ell is the image of the half-sized open k-disk, hence an open
    k-disk in S and not an open subset of S^n when k < n, so the excision closure condition
    relative to X = S^n - D' is met through the ambient open set h'(int D^n) - h'(L), which is
    contained in D; D = h'(D^n - L) is contractible because the straight-line contraction of
    D^n - L to the origin stays outside L; D' = S - ell is a compact k-manifold with boundary by
    the coordinate chart, since the half-sized boundary sphere lies in h'(int D^k) and
    S meets h'(int D^n) in h'(int D^k) there, so Putman's Generalized Schoenflies Theorem makes
    D' a closed k-disk; Hatcher Proposition 2B.1(a), printed p. 169, then makes X acyclic; and in
    the exact sequence of the excised pair the inclusion-induced map
    H_j(D - ell) -> H_j(S^n - S) sits between two vanishing relative groups, so it is an
    isomorphism in every degree. Corrected in a forward commit: the earlier version called ell
    open in S^n, wrongly took S - Sigma to be ell disjoint-union D', and mislabelled the
    connecting map of the pair sequence as the inclusion isomorphism. Not checked and not claimed: the
    MSE thread is an unreviewed user answer rather than a peer-reviewed publication, so what is
    recorded is verification of its argument, not acceptance of the thread as a published
    solution; no use is made of the retracted interior-of-A-minus-Z condition. The
    Alexander-intersection proof, the k = n case and the statement are unchanged.
---

::: {.problem}
Let $S$ be an embedded $k$-sphere in $S^n$ for which there exists a disk $D^n \subset S^n$ intersecting $S$ in the disk $D^k \subset D^n$ defined by the first $k$ coordinates of $D^n$.
Let $D^{n-k} \subset D^n$ be the disk defined by the last $n-k$ coordinates, with boundary sphere $S^{n-k-1}$.
Show that the inclusion $S^{n-k-1} \hookrightarrow S^n - S$ induces an isomorphism on homology groups.
:::

::: {.solution}
Put $r=n-k-1$.

::: pf

::: pf-step
If $k=n$, then the inclusion in the statement is an isomorphism on homology.

::: pf-proof
An embedded $n$-sphere in $S^n$ is all of $S^n$ by invariance of domain. Hence both $S^r=S^{-1}$ and $S^n-S$ are empty.
:::

:::

::: {.pf-step #complement-homology}
For $k<n$, both $S^r$ and $S^n-S$ have reduced homology $\ZZ$ in degree $r$ and zero in every other degree.

::: pf-proof
Now $r\ge0$, and Alexander duality for the embedded proper subsphere $S\cong S^k$ gives
$$
\widetilde H_i(S^n\setminus S)\cong\widetilde H^{\,n-i-1}(S)
\cong
\begin{cases}\ZZ,&i=r,\\0,&i\ne r.\end{cases}
$$
The source sphere $S^r$ has the same reduced homology groups.
:::

:::

::: {.pf-step #normal-generator}
The image of the oriented fundamental class of $S^r$ is a generator of $\widetilde H_r(S^n\setminus S)$.

::: pf-proof
Inside the coordinate disk $D^n$, the normal disk $D^{n-k}$ meets $S\cap D^n=D^k$ at its center and nowhere else. The boundary of the normal disk is the sphere in the statement. Under Alexander duality, evaluation of the image of its oriented fundamental class on the fundamental class of $S$ is the intersection number of this normal disk with $S$. Excision restricts that intersection calculation to the coordinate disk, where the two coordinate disks meet in one transverse point with local intersection number $+1$ or $-1$. Thus the image has Alexander-duality coordinate $\pm1$, so it is a generator.
:::

:::

::: {.pf-step #schoenflies-pair}
A second proof, independent of Alexander duality and of any intersection number, follows [the answer to Math StackExchange question 4773641](https://math.stackexchange.com/questions/4773641) with every step checked, and supplies the generalized Schoenflies theorem that answer invokes.

::: pf-proof
Let $h\colon S^k\to S^n$ and $h'\colon D^n\to S^n$ be embeddings with $S=h(S^k)$ and $h'(D^n)\cap S=h'(D^k)$, the second being the hypothesis of the exercise. Put $\ell_0=\{x\in D^k:\norm{x}<\tfrac12\}$, $L=D^k\setminus\ell_0$, and
$$
\ell=h'(\ell_0),\qquad
D=h'(D^n\setminus L),\qquad
D'=h(S^k)\setminus\ell .
$$
Thus $L=\{x\in D^k:\tfrac12\le\norm{x}\le1\}$ is a closed shell and $D^k=L\sqcup\ell_0$. Since $h'(D^n)\cap S=h'(D^k)$, we have $D\cap S=h'(D^k\setminus L)=\ell$, so $D\cap D'=\varnothing$, and $(S^n\setminus D')\setminus\ell=S^n\setminus h(S^k)$. The answer writes $h'(S^k)$ where $h(S^k)$ is meant, since $h'$ has domain $D^n$.

$D$ is acyclic. A point of $D^n\setminus L$ whose last $n-k$ coordinates all vanish has its first $k$ coordinates in $\ell_0$. For a point with some last coordinate nonzero, every point of the segment joining it to $0$ except $0$ itself again has a nonzero last coordinate, hence lies outside $D^k\supseteq L$, while the whole segment lies in the convex set $D^n$. So the straight-line contraction of $D^n\setminus L$ to $0$ stays in $D^n\setminus L$, and $D$ is contractible.

For $k\ge1$, $D'$ is a closed $k$-disk. Let $\Sigma=h'(\{x\in\RR^k:\norm{x}=\tfrac12\})$, an embedded $(k-1)$-sphere in $S$ lying in $h'(D^k)$, and $\bar\ell=h'(\{x\in\RR^k:\norm{x}\le\tfrac12\})$. Then $S\setminus\Sigma=\ell\sqcup(S\setminus\bar\ell)$ and $D'\setminus\Sigma=S\setminus\bar\ell$, while $\Sigma\subseteq D'$, so $D'$ is not contained in $S\setminus\Sigma$. By Proposition 2B.1(b) applied in the $k$-sphere $S$, $\widetilde H_0(S\setminus\Sigma)\cong\ZZ$, and $S\setminus\Sigma$ is open in $S$ hence locally path connected, so it has exactly two components; as $\ell$ and $S\setminus\bar\ell$ are nonempty disjoint open sets covering it, they are those two components. Since $\norm{x}=\tfrac12$ on $\Sigma$ while $\norm{x}=1$ on $\partial D^n$, the compact set $\Sigma$ lies in $h'(\operatorname{int}D^k)$; and there $S$ agrees with the coordinate chart, because $h'(\operatorname{int}D^n)$ is open in $S^n$ by invariance of domain and
$$
S\cap h'(\operatorname{int}D^n)=h'(D^k)\cap h'(\operatorname{int}D^n)=h'(\operatorname{int}D^k).
$$
Hence $h'^{-1}$ carries $D'$ near $\Sigma$ to the closed half-space $\{x\in\operatorname{int}D^k:\norm{x}\ge\tfrac12\}$, whose boundary sphere $\{\norm{x}=\tfrac12\}$ maps onto $\Sigma$, while $D'\setminus\Sigma=S\setminus\bar\ell$ is open in $S$. Thus $D'=\overline{S\setminus\bar\ell}$ is a compact $k$-manifold with boundary $\Sigma$, namely the closure of that component of $S\setminus\Sigma$. That manifold hypothesis is not automatic --- for the non-simply-connected side of the Alexander horned sphere the corresponding closure is not a manifold --- but the coordinate chart supplies it here. For $k\ge2$ the Generalized Schoenflies Theorem ([Andrew Putman, *The generalized Schoenflies theorem*, §1](https://academicweb.nd.edu/~andyp/notes/Schoenflies.pdf)), applied to the embedding $\Sigma\subset S\cong S^k$ and to the component $S\setminus\bar\ell$, whose closure is $D'$, then makes that closure a disk, so $D'\cong D^k$; for $k=1$, $S\cong S^1$, $\ell$ is an open interval and $D'$ a closed interval.

So $D'$ is an embedded closed $k$-disk in $S^n$, and Hatcher's Proposition 2B.1(a), printed p. 169, gives
$$
\widetilde H_i(S^n\setminus D')=0\qquad\text{for all }i .
$$
Set $X=S^n\setminus D'$ and $A=D$; then $X$ is path-connected and $A\ne\varnothing$. With $Z=\ell$ we have $Z\subset A\subset X$. The closure of $\ell$ in $S^n$ is $\bar\ell=\ell\cup\Sigma$ with $\Sigma\subseteq D'$, so $\overline Z^{\,X}=\ell$. Also $\ell$ lies in the ambient open set $U=h'(\operatorname{int}D^n)\setminus h'(L)$, which is contained in $D=A$: $h'(\operatorname{int}D^n)$ is open in $S^n$ because $h'$ is an open embedding on $\operatorname{int}D^n$ by invariance of domain, $h'(L)$ is compact hence closed in $S^n$, and $\ell\cap h'(L)=h'(\ell_0\cap L)=\varnothing$. Hence $\ell\subseteq\operatorname{int}_{S^n}(A)\subseteq\operatorname{int}_X(A)$. Note that $\ell$ is an open $k$-disk in $S$ and is not open in $S^n$ when $k<n$; the closure condition is met through the ambient neighbourhood $U$, not through $\ell$ itself. The hypothesis of Hatcher's excision theorem, Theorem 2.20, therefore holds, and excision gives isomorphisms in every degree
$$
H_j(X,A)\cong H_j\bigl((S^n\setminus D')\setminus\ell,\,D\setminus\ell\bigr)
=H_j\bigl(S^n\setminus h(S^k),\,h'(D^n\setminus D^k)\bigr),
$$
the right-hand side using $D'\cup\ell=S$ and $(D^n\setminus L)\setminus\ell_0=D^n\setminus D^k$.

Both $X$ and $A$ are acyclic, so the exact sequence of the pair $(X,A)$ gives $H_j(X,A)=0$ for $j>0$, and also $H_0(X,A)=0$ because $X$ is path-connected and $A\ne\varnothing$. Now $D\setminus\ell=h'(D^n\setminus D^k)$, and $D^n\setminus D^k$ deformation retracts onto $\{0\}^k\times S^{n-k-1}$: collapse the first $k$ coordinates to $0$, which keeps every point outside $D^k$ since its last coordinates stay nonzero, then push the last $n-k$ coordinates radially out to the unit sphere. Hence $D\setminus\ell$ is homotopy equivalent to the sphere $S^{n-k-1}$ of the statement. In the exact sequence of the excised pair
$$
\cdots\to H_j(S^n\setminus S,\,D\setminus\ell)\to H_{j-1}(D\setminus\ell)\xrightarrow{\ i_*\ }H_{j-1}(S^n\setminus S)\to H_{j-1}(S^n\setminus S,\,D\setminus\ell)\to\cdots
$$
both relative groups adjacent to $H_{j-1}(D\setminus\ell)\to H_{j-1}(S^n\setminus S)$ vanish, so the map $i_*$ induced by the inclusion $D\setminus\ell\hookrightarrow S^n\setminus S$ is an isomorphism in every degree, $j\ge1$ covering every degree. Composing $i_*$ with the homotopy equivalence of $D\setminus\ell$ with $S^{n-k-1}$, the inclusion $S^{n-k-1}\hookrightarrow S^n\setminus S$ induces an isomorphism on homology in every degree, which is the statement, reached without the Alexander-duality steps above.

For $k=0$ no Schoenflies theorem is needed: $D^0$ is a point, $L=\varnothing$, $D=h'(D^n)$, $\ell=h'(D^0)$, $S=S^0$, and $D'=S^0\setminus\ell$ is a single point, so $X=S^n\setminus D'\cong\RR^n$ is acyclic by Proposition 2B.1(a) itself, $D\setminus\ell=h'(D^n\setminus D^0)\simeq h'(\partial D^n)=S^{n-1}$, and both closure conditions hold because $\ell$ lies in the $S^n$-open set $h'(\operatorname{int}D^n)\subseteq D$.
:::

:::

::: pf-step
By the Alexander-duality route of steps [](#complement-homology){.pf-ref} and [](#normal-generator){.pf-ref}, the inclusion induces an isomorphism on reduced homology in every degree, and also on ordinary $H_0$.

::: pf-proof
For $k<n$, step [](#complement-homology){.pf-ref} leaves only degree $r$ to check, and step [](#normal-generator){.pf-ref} shows that the inclusion sends a generator to a generator. For $r=0$, the oriented fundamental class of $S^0$ is the difference of its two points, so the same local intersection calculation applies in reduced $H_0$. Reduced homology determines ordinary homology in positive degrees and determines ordinary $H_0$ here since both spaces are nonempty. The case $k=n$ was already verified directly.
:::

:::

:::
:::
