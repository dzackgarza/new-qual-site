---
schema: qual/card@1
id: E-HAT-3.3-7
kind: problem
title: Degree 1 maps to $S^n$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 7; it matches the printed text. The card makes the implicit $n>0$ explicit.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: collapse the complement of an orientation-compatible ball, giving a map
    to $B/\partial B=S^n$ of local degree 1 at an interior regular value.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Re-read against the printed exercise (p.258) and restored the printed sentence, which has no
    $n>0$; the card's earlier note called that hypothesis implicit, and it is now shown to be
    forced by the definition. (This note first gave the reason as "$S^0$ has no fundamental class";
    that is false and is corrected by the first event above — $[S^0]=(1,1)$ does generate every
    local group. What fails at $n=0$ is the connectedness the definition requires of the target, and
    the equation $f_*([M])=d[S^0]$ has no solution even read naively.)
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Source-backed rewrite from the Math 538 homework solutions, HMW 4 handwritten page 1 (PDF page
    17), Hatcher 3.3 #7: collapse of the complement of an open disk to a point, the homeomorphism
    M/(M-B) -> S^n, H_n(M) = H_n(M,M-B) carrying [M] to the local class mu_B, and the removal of the
    sign by replacing the fundamental class by its negative. The card keeps its n = 0 remark, which
    is about the printed statement's own hypothesis and not part of the handout. Checked against
    Hatcher p.146 (collapsing a disk complement gives S^n) and p.236 (fundamental class).

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Two defects in the previous revision, both substantive. (1) The target pair was written
    (S^n, S^n - {pt}) although f sends M - B to the collapsed point, so the map of pairs was
    ill-formed; it is now (S^n, {f(p)}), with H_n(S^n) = H_n(S^n,{f(p)}) from the pair sequence for
    n >= 1. (2) The paragraph excluding n = 0 asserted that S^0 has no fundamental class, which is
    false: a disconnected closed orientable 0-manifold has one, namely the sum of the point classes,
    and H_0(S^0) = Z^2 with [S^0] = (1,1) does map to a generator of every local group. What fails at
    n = 0 is the definition itself, whose target must be connected, and even read naively the
    equation f_*([M]) = d[S^0] has no solution, since f_*([M]) is one of (+-1,0), (0,+-1) while
    d[S^0] = (d,d). The card now states the degree convention of p.258 and this dimension boundary
    precisely.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Repaired the remaining false local-pair assertions. The collapsed point is now named infinity
    and is distinct from y = f(p), where p lies in the open disk. The previous map
    H_n(M,M-B) -> H_n(B,B-p) was not excision; the diagram instead uses excision for the pair
    (M, M-p), deleting M-B, whose closure lies in M-p, to obtain H_n(B,B-p), and the same excision
    at y in f(B). Commutativity with the two maps induced by f and the fundamental-class
    restrictions of Theorem 3.26(a) proves the local degree, hence the global degree, is +-1. The
    dimension-zero paragraph now distinguishes Hatcher's connected-target convention from the
    componentwise fundamental class of S^0.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is the
    construction of the Math 538 homework sheet cited there. Added: the addition in
    $H_n(f(B),f(B)-\{y\})$ is identified as $H_n(S^n-\{y'\},S^n-\{y,y'\})$ through the
    homeomorphism, which is what makes the bottom row an isomorphism of the *right* pair;
    the local-degree chase made explicit step by step; and the $n=0$ exclusion stated as a
    convention of the exercise. Statement re-read at §3.3 Exercise 7, printed p. 258, with
    Theorem 3.26(a) on printed p. 236 and Theorem 2.44 on printed p. 146. Retained solution:
    Math 538 HMW 4, handwritten p. 1 (PDF p. 17), cited above.
---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds with fundamental classes $[M]$ and $[N]$, the degree of $f$ is defined to be the integer $d$ such that $f_*([M]) = d[N]$, so the sign of the degree depends on the choice of fundamental classes.
Show that for any connected closed orientable $n$-manifold $M$ there is a degree 1 map $M \to S^n$.
:::

::: {.solution}
The construction is the one in **Math 538 homework solutions, HMW 4, handwritten p. 1 (PDF p. 17 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 Exercise 7**: collapse the complement of an open disk, identify the quotient with $S^n$, and change the orientation to remove the sign. The local-degree diagram below supplies the identifications that the sheet does not display. The statement is Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 7, printed p. 258, and it carries that exercise's convention on the degree.

Throughout, $M$ is a connected closed orientable $n$-manifold with fundamental class $[M]$, coefficients are $\ZZ$ unless written otherwise, and $\deg f=d$ means $f_*([M])=d[S^n]$ as in the exercise on printed p. 258.

::: pf

::: {.pf-step #convention}
$H_n(M)=\ZZ\cdot[M]$ and $H_n(S^n)=\ZZ\cdot[S^n]$, and for every point $x$ the maps $H_n(M)\to H_n(M,M-\theset{x})$ and $H_n(S^n)\to H_n(S^n,S^n-\theset{y})$ induced by inclusion of pairs are isomorphisms carrying the fundamental classes to generators of the local groups.

::: pf-proof
$M$ and $S^n$ are connected closed orientable $n$-manifolds, so $H_n$ of each is infinite cyclic generated by the fundamental class, and the local homology $H_n(M,M-\theset{x})$ is infinite cyclic generated by the image of $[M]$: this is Theorem 3.26(a), printed p. 236, whose second assertion is exactly the statement that the fundamental class restricts to a generator at each point. The same theorem applies to $S^n$.

:::

:::

::: {.pf-step #dimension-zero}
The construction below treats $n\ge1$; for $n=0$ the claim needs a convention that the exercise's does not supply.

::: pf-proof
For $n=0$ a connected closed orientable $0$-manifold is a point, and $S^0$ is two points, so $S^0$ is disconnected and falls outside the exercise's hypothesis that both manifolds be connected. If one extends the fundamental class componentwise, $[S^0]=(1,1)\in H_0(S^0)=\ZZ^2$ does restrict to a generator at each point, but for $M$ a point $f_*([M])$ is $(\pm1,0)$ or $(0,\pm1)$ while $d[S^0]=(d,d)$; no $d$ satisfies the equation. So the exercise is meant with $n\ge1$, which is what the construction uses.

:::

:::

::: {.pf-step #construction}
Choose an open coordinate disk $B\subset M$ and $p\in B$, let $q:M\to Q=M/(M-B)$ collapse the closed complement of $B$ to the point $\infty$, and choose a homeomorphism $h:Q\to S^n$ with $h(\infty)\ne h(q(p))$. Then $f=h\circ q:M\to S^n$ sends $M-B$ to $y'=h(\infty)$, sends $p$ to $y=h(q(p))\ne y'$, and $f$ restricted to $B$ is a homeomorphism of pairs $(B,B-\theset{p})\to(f(B),f(B)-\theset{y})$.

::: pf-proof
$M-B$ is closed in the compact space $M$ and $B$ is open, so $q$ is a quotient map whose restriction to $B$ is a homeomorphism onto its image, and $Q$ is the one-point compactification of the open disk $B$, hence homeomorphic to $S^n$; this is the argument of Theorem 2.44, printed p. 146, applied to the closed disk $\overline B$. Choosing $h$ so that $h(\infty)$ is the antipode of $h(q(p))$ makes $y\ne y'$. Since $q\restrict_B$ is a homeomorphism onto $Q-\theset{\infty}$ and $h$ is a homeomorphism, $f\restrict_B$ is a homeomorphism onto $S^n-\theset{y'}$, and it carries $B-\theset{p}$ onto $S^n-\theset{y,y'}$, which is $(f(B))-\theset{y}$ because $f(B)=S^n-\theset{y'}$.

:::

:::

::: {.pf-step #local-degree}
The following diagram commutes, all its vertical maps are isomorphisms, and the bottom horizontal map is an isomorphism:
$$
\begin{array}{ccc}
H_n(M)&\xrightarrow{\ f_*\ }&H_n(S^n)\\
\downarrow{\rho_M}&&\downarrow{\rho_S}\\
H_n(M,M-\theset{p})&\xrightarrow{f_*^{(p)}}&H_n(S^n,S^n-\theset{y})\\
\uparrow{e_M}&&\uparrow{e_S}\\
H_n(B,B-\theset{p})&\xrightarrow{(f\restrict_B)_*}&H_n(f(B),f(B)-\theset{y}).
\end{array}
$$

::: pf-proof
Commutativity is naturality of homology for the maps of pairs $f:(M,M-\theset{p})\to(S^n,S^n-\theset{y})$ and the inclusions $(B,B-\theset{p})\subset(M,M-\theset{p})$, $(f(B),f(B)-\theset{y})\subset(S^n,S^n-\theset{y})$. $\rho_M$ and $\rho_S$ are isomorphisms by step [](#convention){.pf-ref}. For $e_M$, apply excision to the pair $(M,M-\theset{p})$ with $A=M-\theset{p}$ and $Z=M-B$: $\overline Z=M-B$ is contained in $\operatorname{int}A=M-\theset{p}$ because $p\in B$, so
$$
H_n(M-Z,A-Z)=H_n(B,B-\theset{p})\longrightarrow H_n(M,M-\theset{p})
$$
is an isomorphism; the same computation inside $S^n$ with $f(B)$ in place of $B$ and $y$ in place of $p$ gives $e_S$, using that $f(B)$ is open and $y\in f(B)$. Finally $(f\restrict_B)_*$ is an isomorphism because $f\restrict_B$ is a homeomorphism of pairs by step [](#construction){.pf-ref}.

:::

:::

::: {.pf-step #degree-one}
$f_*([M])=\pm[S^n]$, and after replacing $[M]$ by the fundamental class of the opposite orientation, $f_*([M])=[S^n]$, so $\deg f=1$.

::: pf-proof
$\rho_M([M])$ is a generator of $H_n(M,M-\theset{p})$ and $\rho_S([S^n])$ is a generator of $H_n(S^n,S^n-\theset{y})$ by step [](#convention){.pf-ref}. Chasing $[M]$ around the diagram through the bottom row, which is an isomorphism, $f_*^{(p)}$ carries the generator $\rho_M([M])$ to a generator, hence to $\pm\rho_S([S^n])$; commutativity then gives $\rho_S f_*([M])=\pm\rho_S([S^n])$, and $\rho_S$ is injective, so $f_*([M])=\pm[S^n]$. Replacing $[M]$ by $-[M]$ is replacing the orientation of $M$ by the opposite one, which is legitimate because both orientations' classes are fundamental classes; then $f_*([M])=[S^n]$ and $\deg f=1$ by the definition on printed p. 258.

:::

:::

:::
:::
