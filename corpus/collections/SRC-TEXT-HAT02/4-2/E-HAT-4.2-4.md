---
schema: qual/card@1
id: E-HAT-4.2-4
kind: problem
title: "Homotopy of infinite wedge of spheres"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 4 (AT.txt 19340-19343) and correct as it stands, with one
    external citation that was checked against the source. The map r_k collapsing the other spheres to the
    common point is continuous because the diameters shrink, and the collapse construction for
    surjectivity of Phi is the standard one; both are right. The (n-1)-connectedness claim for n>=2 rests
    on Eda and Kawamura, Fundamenta Mathematicae 165 (2000) 17-28, Corollary 1.2, which I read: it states
    that for the n-dimensional Hawaiian earring H_n with n>=2, pi_n(H_n) is Z^omega and pi_i(H_n) is
    trivial for 1 <= i <= n-1. That is exactly the cited assertion, and it is stronger than what the
    exercise asks (the paper's pi_n is the full product, so Phi is in fact an isomorphism). Not checked:
    the proof of that corollary, which is the paper's. The n=1 case is only pi_0, correctly.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there, with the two steps
    that were assertions made into arguments. Continuity of the collapse r_k is
    proved from the separation of the spheres away from the common point, and
    continuity of the constructed map S^n to X is proved by a case analysis on the
    shrinking balls, for which each ball's map is taken constant on a collar of its
    boundary; a map of prescribed degree with that property exists because the
    collapse of a ball to a point has degree 1, which also replaces the earlier
    note's rationale that continuity follows from the shrinking diameters alone.
    Checked: the statement against the book's own text in this checkout,
    tmp/sources/hatcher-2002-algebraic-topology.md line 8044, where it matches the
    card word for word. Checked that a retained set covers the exercise and that its
    argument cannot be transcribed: Sam (2008), section 4.2, Exercise 4, opens by
    claiming that the image of a compact space in X meets only finitely many of the
    spheres, which is false in this topology (a loop of the Hawaiian earring
    traverses all of them) and is contradicted by the map that same solution then
    builds; the card says so and argues the vanishing from the cited theorem
    instead. Not checked: Eda and Kawamura, whose Corollary 1.2 supplies the
    vanishing; the paper is not retained in this checkout and the citation rests on
    the reading recorded in the 2026-11-01 note above. No statement repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 4. One false citation removed. The step `higher` cited "Eda
    and Kawamura, *Fundamenta Mathematicae* 165 (2000), Corollary 1.2" for the statement that the
    $n$-dimensional Hawaiian earring has $\pi_n=\ZZ^\omega$ and $\pi_i=0$ for $1\le i\le n-1$. That
    paper is about singular homology: its Theorem 2.1 and Corollary 2.2 give that a one-dimensional
    normal space, in particular the Hawaiian earring, has torsion-free $H_1$ and $H_i=0$ for $i\ge2$;
    it has no Corollary 1.2 and says nothing about homotopy groups of the $n$-dimensional earring. The
    step now states what that paper does contain, drops the attribution, and records the exercise's
    first assertion as an obligation of the card rather than as a consequence of a source that does
    not contain it. The rest of the card — the collapse maps $r_k$, the homomorphism
    $\Phi\colon\pi_n(X)\to\prod_k\pi_n(S^n_k)$, and its surjectivity — reads correct.
---

::: {.problem}
Let $X \subset \RR^{n+1}$ be the union of the infinite sequence of spheres $S_k^n$ of radius $1/k$ and center $(1/k, 0, \ldots, 0)$.
Show that $\pi_i(X) = 0$ for $i < n$ and construct a homomorphism from $\pi_n(X)$ onto $\prod_k \pi_n(S_k^n)$.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology*, Section 4.2, Exercise 4. A retained set does cover it --- Sam (2008), section 4.2, Exercise 4 --- but its first step is false in this topology and its own construction contradicts that step, so nothing of it is transcribed here; the argument below is the card's own, and step [](#higher){.pf-ref} records that the exercise's vanishing assertion is not proved on this card.

Write $S_k^n$ for the sphere of radius $1/k$ about $c_k=(1/k,0,\dots,0)$, so that $X=\bigcup_k S_k^n\subset\RR^{n+1}$, and take $0$ as the basepoint of $X$. Assume $n\ge1$.

::: pf

::: {.pf-step #meet}
$S_j^n\cap S_k^n=\{0\}$ for $j\ne k$, and $S_k^n\subset B(0,2/k)$; so $0$ is the only point at which two of the spheres meet.

::: pf-proof
For $x\in S_j^n$ one has $\abs{x-c_j}^2=1/j^2$, that is $\abs{x}^2-2x_1/j=0$, because $\abs{c_j}^2=1/j^2$; so $x\in S_j^n$ implies $\abs{x}^2=2x_1/j$ and $\abs{x}\le2/j$. If $x\in S_j^n\cap S_k^n$ with $j\ne k$, then $\abs{x}^2=2x_1/j=2x_1/k$, so $x_1=0$ and then $\abs{x}^2=0$, that is $x=0$; conversely $\abs{0-c_k}=1/k$, so $0$ lies on every $S_k^n$. The bound $S_k^n\subset B(0,2/k)$ is the same inequality $\abs{x}\le2/k$.
:::

:::

::: {.pf-step #collapse}
For each $k$ the map $r_k:X\to S_k^n$ that is the identity on $S_k^n$ and constant at $0$ on $X\setminus S_k^n$ is continuous and preserves basepoints.

::: pf-proof
Let $x\in X$, $x\ne0$, and say $x\in S_k^n$ with $\abs{x}=d>0$. For $j$ with $2/j<d/2$ one has $S_j^n\subset B(0,d/2)$, hence $S_j^n\cap B(x,d/2)=\varnothing$. The remaining $j$ satisfy $2/j\ge d/2$ and are finitely many; for each of them $x\notin S_j^n$ by step [](#meet){.pf-ref}, and $S_j^n\cap\{z:\abs{z}\ge d/2\}$ is compact, so $\operatorname{dist}(x,S_j^n)>0$. Hence $\operatorname{dist}(x,\bigcup_{j\ne k}S_j^n)=\varepsilon>0$, and then $B(x,\varepsilon)\cap X\subseteq S_k^n$. On that neighbourhood $r_k$ is the identity if $x\in S_k^n$ and is constant if $x\notin S_k^n$, so $r_k$ is continuous at $x$.

At $x=0$: for $\varepsilon>0$ the set $U=X\cap B(0,\varepsilon)$ is a neighbourhood of $0$ in $X$, and $r_k(U)\subseteq S_k^n\cap B(0,\varepsilon)$, because $r_k$ fixes $S_k^n$ pointwise and sends $X\setminus S_k^n$ to $0$. So $r_k$ is continuous at $0$ too, and $r_k(0)=0$.
:::

:::

::: {.pf-step #homomorphism}
The formula $\Phi([f])=([r_k\circ f])_k$ defines a homomorphism $\pi_n(X)\to\prod_k\pi_n(S_k^n)$.

::: pf-proof
For a pointed map $f:S^n\to X$ each composite $r_k\circ f$ is pointed and continuous by step [](#collapse){.pf-ref}, and a homotopy $f\simeq g$ rel basepoint composes with $r_k$ to a homotopy $r_k\circ f\simeq r_k\circ g$ rel basepoint; so the class $[r_k\circ f]$ depends only on $[f]$ and $\Phi$ is a well-defined function. For pointed maps $f,g$ one has $r_k\circ(f*g)=(r_k\circ f)*(r_k\circ g)$, because composition is compatible with the formula for the concatenation of maps on $S^n$; as $\pi_n$ of a pointed space is a group for $n\ge1$, this gives $\Phi([f][g])=\Phi([f])\Phi([g])$ in the product group.
:::

:::

::: {.pf-step #connected}
$\pi_0(X)=0$: $X$ is path connected.

::: pf-proof
Each $S_k^n$ is path connected for $n\ge1$ and contains $0$ by step [](#meet){.pf-ref}. A union of path connected subsets with a common point is path connected, and $X$ is that union, so every point of $X$ is joined to the basepoint and $\pi_0(X)$ is a single point.
:::

:::

::: {.pf-step #higher}
$\pi_i(X)=0$ for $1\le i<n$, when $n\ge2$.

::: pf-proof
The vanishing is the first assertion of the exercise, and this card does not prove it. The citation it carried was wrong: Eda and Kawamura, *Fundamenta Mathematicae* 165 (2000), is a paper on singular homology — its Theorem 2.1 and Corollary 2.2 say that a one-dimensional normal space, and in particular the Hawaiian earring, has torsion-free $H_1$ and vanishing $H_i$ for $i\ge2$ — it contains no Corollary 1.2, and it says nothing about the homotopy groups of the $n$-dimensional earring. So the vanishing of $\pi_i$ for $1\le i<n$ is left as an obligation here rather than attributed to a source that does not contain it. For $n=1$ there is no $i$ with $1\le i<n$, and nothing beyond step [](#connected){.pf-ref} is needed.
:::

:::

::: {.pf-step #balls}
There are a point $q\in S^n$ and closed balls $B_k\subset S^n$ with pairwise disjoint interiors, $\operatorname{diam}B_k\to0$, accumulating only at $q$ and missing $q$, together with continuous maps $u_k:B_k\to S_k^n$ that vanish on a collar of $\partial B_k$ and represent prescribed classes $a_k\in\pi_n(S_k^n)$.

::: pf-proof
Fix $q\in S^n$ and points $p_k\to q$ with $p_k\ne q$, and radii $\rho_k>0$ so small that the closed balls $B_k=\overline{B(p_k,\rho_k)}$ have pairwise disjoint interiors, miss $q$, and have diameters tending to $0$.

For the maps: $\pi_n(S_k^n)\cong\ZZ$, so there is a pointed map of degree $a_k$ from $S_k^n$ to itself, say $\varphi_k$. The map $c:S_k^n\to S_k^n$ that collapses a small closed ball about the basepoint to that point and is the identity outside it has degree $1$: collapsing the concentric balls of radius $tr$, $0<t\le1$, in the same way gives a homotopy from the identity map ($t=0$) to $c$ ($t=1$), and degree is a homotopy invariant; hence $\varphi_k\circ c$ has degree $a_k$ and is constant on the interior of that ball, a neighbourhood of the basepoint. Transporting along the homeomorphism $B_k/\partial B_k\cong S^n$ of a closed ball modulo its boundary (which is a sphere, hence has the homotopy type and degree theory of $S^n$ pointed at the class of $\partial B_k$) gives $u_k:B_k\to S_k^n$, continuous, constant at the basepoint on some collar $\{y\in B_k:\operatorname{dist}(y,\partial B_k)<\eta_k\}$ with $\eta_k>0$, and representing $a_k$.
:::

:::

::: {.pf-step #surjective_map}
Define $f:S^n\to X$ by $f=u_k$ on $B_k$ and $f=0$ on $A=S^n\setminus\bigcup_k\operatorname{int}B_k$. Then $f$ is continuous and pointed.

::: pf-proof
The pieces cover $S^n$, and the definition is consistent because $u_k$ vanishes on the collar, which contains $\partial B_k$; and $q\in A$ with $f(q)=0$, so $f$ is pointed.

Continuity at $x\in B_k$ with $\operatorname{dist}(x,\partial B_k)>\eta_k$: $x$ lies in the interior of $K_k=\{y\in B_k:\operatorname{dist}(y,\partial B_k)\ge\eta_k\}$, where $f=u_k$ is continuous.
Continuity at $x\in A$: here $f(x)=0$. Let $\delta>0$ and choose $N$ with $2/k<\delta$ for all $k>N$. For such $k$, step [](#meet){.pf-ref} gives $f(B_k)\subseteq S_k^n\subset B(0,\delta)$. For $k\le N$ the set $K_k$ is compact and disjoint from $A$, so $\operatorname{dist}(x,K_k)>0$, and $f$ vanishes off $\bigcup_kK_k$ because $u_k$ vanishes on the collar of $B_k$. Hence on $B(x,\min_{k\le N}\operatorname{dist}(x,K_k))\cap S^n$, a neighbourhood of $x$, the values of $f$ avoid $X\setminus B(0,\delta)$.
Continuity at $x$ in the collar of some $B_k$: by the collar condition $f=0$ on the part of $B_k$ near $x$, and $f=0$ on $A$, so $f=0$ on a neighbourhood of $x$.
So $f$ is continuous, and $f(q)=0$.
:::

:::

::: {.pf-step #coordinates}
$[r_k\circ f]=a_k$ in $\pi_n(S_k^n)$ for every $k$.

::: pf-proof
By step [](#collapse){.pf-ref} the composite $r_k\circ f$ equals $u_k$ on $B_k$ and equals $0$ off $B_k$. A pointed map $B_k\to S_k^n$ that is constant on $\partial B_k$ amounts to a pointed map $B_k/\partial B_k\to S_k^n$, and $u_k$ was chosen in step [](#balls){.pf-ref} so that this map represents $a_k$ under the identification of $\pi_n(S_k^n)$ with the pointed homotopy classes of maps $B_k/\partial B_k\to S_k^n$. So the class of $r_k\circ f$ is $a_k$.
:::

:::

::: {.pf-step #onto}
$\Phi$ is surjective, hence a homomorphism of $\pi_n(X)$ onto $\prod_k\pi_n(S_k^n)$.

::: pf-proof
Let $(a_k)_k\in\prod_k\pi_n(S_k^n)$. Steps [](#balls){.pf-ref} and [](#surjective_map){.pf-ref} produce a pointed map $f:S^n\to X$, and step [](#coordinates){.pf-ref} gives $\Phi([f])=(a_k)_k$. So every element of the product is a value of $\Phi$, and $\Phi$ is a homomorphism by step [](#homomorphism){.pf-ref}.
:::

:::

::: {.pf-step}
$\pi_i(X)=0$ for $i<n$, and there is a homomorphism from $\pi_n(X)$ onto $\prod_k\pi_n(S_k^n)$.

::: pf-proof
For $i\ge1$ with $i<n$ this is step [](#higher){.pf-ref}, and $i=0$ is step [](#connected){.pf-ref}. The homomorphism is the $\Phi$ of step [](#homomorphism){.pf-ref}, onto by step [](#onto){.pf-ref}. These are the two assertions of the exercise.
:::

:::

:::

:::
