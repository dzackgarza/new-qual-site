---
schema: qual/card@1
id: E-HAT-4.B-1
kind: problem
title: "Hopf invariant of compositions"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-08
  note: >-
    Read Hatcher p.427: C_h=S^n\cup_h e^{2n} first with m=n, then 'When m>n'
    the cohomology is Z in 0,n,2n and the generators x_h in H^n and y_h in
    H^{2n} are obtained there, then specialized to m=2n-1. Thus the Hopf
    invariant as defined has n>1 (2n-1>n), where deg h=0 gives the Z's. The
    odd-n vanishing H=0 for odd n (p.427, x^2=-x^2) is within that n>1 domain,
    not a definition for arbitrary degree-d S^1->S^1 maps, whose cones need not
    have H^1=H^2=Z. The exercise is read with that n>1 domain.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    The composition proof is correct for its n>1 domain: C_{gf}->C_g (identity on
    S^n, degree d on 2n-cell) and C_f->C_{gf} (degree d on S^n, degree 1 on
    2n-cell) give the two pullback identities. No n=1 case is missing; the
    previous claim that n>=2 omitted n=1 and was repairable by odd vanishing
    misread the domain, since odd vanishing does not supply the missing H^n,
    H^{2n}=Z. No change to the proof text is needed.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: $C_h$ has three cells and its only
    possible boundary is multiplication by $\deg h=0$ because $2n-1>n$ makes $h$ null; the Hopf
    invariant is the coefficient of $x_h^2$ on the generator $y_h$ and is well defined under the
    $\pm1$ ambiguity of generators; and the two attaching squares give the coefficient statements
    $x_g\mapsto x_{gf}$, $y_g\mapsto d\,y_{gf}$ and $x_{gf}\mapsto d\,x_f$, $y_{gf}\mapsto y_f$, from
    which $d\,H(g)$ and $d^2H(f)$ follow. Added: the well-definedness of $H(h)$ under change of
    generators, the exact form of the boundary map as the degree of the collapsed attaching map, and
    the division by the generator $y_f$, which is legitimate because $H^{2n}$ is infinite cyclic.
    No defect found in the statement, §4.B Exercise 1; no retained solution set covers it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 436 carries the running head 427.
    The durable part of the locator is that printed page; the file path names this machine's copy and
    `tmp/sources` does not survive a VM reset. No mathematics changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.B Exercise 1, with the definition of the Hopf invariant in §4.B, the
    cellular chain complex of $C_h$ (the cellular boundary formula of §2.2 and Theorem 2.35), the
    universal coefficient theorem (Theorem 3.2), Corollary 4.9, Corollary 4.25 and the group
    structure on $\pi_m$ from §4.1. The two coefficient computations are right: a map $\varphi$ of
    mapping cones that is the identity on $S^n$ and has degree $d$ on the top cell pulls $x_g$ back
    to a generator and $y_g$ back to $d\,y_{gf}$, giving $H(gf)=d\,H(g)$; a map $\psi$ that is
    $g$ on $S^n$ and has degree $1$ on the top cell pulls back to $d^2x_f^2=H(gf)y_f$, giving
    $H(gf)=d^2H(f)$. Two defects repaired. (1) The vanishing of the boundaries was justified by
    "$\partial_{2n}$ is multiplication by the degree of $h$, and $h$ is nullhomotopic since
    $2n-1>n$". The target of $\partial_{2n}$ is $C_{2n-1}$, which is $0$ because no cell has
    dimension $2n-1$: $\partial_{2n}$ is not a multiplication $\ZZ\to\ZZ$ at all. And the reason
    given is false: $\pi_3(S^2)=\ZZ$ with $n=2$ makes $2n-1=3>2$, the Hopf map is not null, and
    $C_h=\CP^2$ has the correct cohomology precisely because the boundary is absent rather than
    zero-by-nullhomotopy. The step now lists the three degrees carrying cells and notes that no
    boundary lands anywhere nonzero. (2) The step moving from $f$ to the cone map silently used
    $[g\circ f]=\deg(f)\,[g]$, which is not in the book as such; it is now a step, proved from the
    pinch definition of the sum in $\pi_m$ and the fact that precomposition by a based self-map of
    the source sphere distributes over that sum. The text cited a page for the definition of the
    Hopf invariant; by the owner's correction of this date it cites §4.B, and no page. The published
    statement of the two identities is tom Dieck, *Algebraic Topology*, §20.8.7, items (2) and (3),
    which is now named as the statement and not as the proof. No retained solution set covers the
    exercise: Sam's set ends with §4.3. Not checked: no certificate.

---

::: {.problem}
This is Exercise 1 of Section 4.B of Hatcher, *Algebraic Topology* (2002); the statement below is its wording.

Show that the Hopf invariant of a composition $S^{2n-1} \xrightarrow{f} S^{2n-1} \xrightarrow{g} S^n$ is given by $H(gf) = (\deg f) H(g)$, and for a composition $S^{2n-1} \xrightarrow{f} S^n \xrightarrow{g} S^n$ the Hopf invariant satisfies $H(gf) = (\deg g)^2 H(f)$.
:::

::: {.solution}
No retained solution set covers this exercise — Sam's set stops at §4.3 and none of the other sets retained for this project has a §4.B solution — so the argument below is the card's own. The two identities are stated as elementary properties of the invariant in tom Dieck, *Algebraic Topology*, §20.8.7, items (2) and (3); the proof is the card's, from the definition of the Hopf invariant in Hatcher §4.B and the cellular cohomology of the mapping cone.

Throughout $n>1$, $C_h=S^n\cup_h e^{2n}$ is the mapping cone of a map $h\colon S^{2n-1}\to S^n$, and $x_h\in H^n(C_h;\ZZ)$, $y_h\in H^{2n}(C_h;\ZZ)$ are generators with $x_h^2=H(h)y_h$ as in Hatcher §4.B.

::: pf

::: {.pf-step #cohomology}
$H^k(C_h;\ZZ)=\ZZ$ for $k=0,n,2n$ and $0$ otherwise.

::: pf-proof
$C_h$ has exactly one cell in each of the dimensions $0$, $n$ and $2n$, and none in any other dimension, so its cellular chain complex is $\ZZ$ in those three degrees and $0$ elsewhere. A boundary $\partial_k\colon C_k\to C_{k-1}$ can be nonzero only if both $C_k$ and $C_{k-1}$ are nonzero, which would need $k-1\in\{0,n,2n\}$ and $k\in\{0,n,2n\}$; for $n>1$ the three numbers $1$, $n+1$ and $2n+1$ are all outside $\{0,n,2n\}$, so no such $k$ exists and every boundary vanishes. In particular there is no $(2n-1)$-cell, so $\partial_{2n}$ has zero target; the vanishing is a matter of which cells exist and does not require the attaching map $h$ to be null, which for $n=2$ it is not, $\pi_3(S^2)$ being infinite cyclic. Hence the homology is $\ZZ$ in the three degrees and $0$ elsewhere, and by the universal coefficient theorem, Theorem 3.2, so is the integral cohomology, the free groups having no Ext term.
:::

:::

::: {.pf-step #definition}
For generators $x_h,y_h$ the integer $H(h)$ is defined by $x_h^2=H(h)y_h$, and it is independent of the choice of generators.

::: pf-proof
$H^{2n}(C_h;\ZZ)=\ZZ\,y_h$ is infinite cyclic by step [](#cohomology){.pf-ref}, so $x_h^2$ is a unique integer multiple of $y_h$. Replacing $x_h$ by $-x_h$ leaves the square unchanged, and replacing $y_h$ by $-y_h$ changes the sign of the coefficient, which Hatcher's convention removes by tying $y_h$ to a fixed generator of $H^{2n}(D^{2n},\partial D^{2n})$ through the characteristic map of the $2n$-cell (§4.B). A homotopy of $h$ gives a homotopy equivalence $C_h\simeq C_{h'}$ carrying one chosen pair of generators to the other, so $H$ depends only on the homotopy class.
:::

:::

::: {.pf-step #degree-action}
If $f\colon S^{2n-1}\to S^{2n-1}$ has degree $d$ and $g\colon S^{2n-1}\to S^n$, then $[g\circ f]=d\,[g]$ in $\pi_{2n-1}(S^n)$.

::: pf-proof
Write $m=2n-1\ge3$ and let $c\colon S^m\to S^m\vee S^m$ be the map collapsing the equator. The sum in $\pi_m$ is defined by $[u]+[v]=[(u\vee v)\circ c]$. For any based $\alpha\colon S^m\to S^m$ one has $c\circ\alpha\simeq(\alpha\vee\alpha)\circ c$, both sides being the pinch followed by $\alpha$ on each summand, so $[(u+v)\circ\alpha]=[(u\alpha)+(v\alpha)]$: precomposition with $\alpha$ is a homomorphism of the abelian group $\pi_m(S^n)$. By Corollary 4.25 the degree gives an isomorphism $\pi_m(S^m)\cong\ZZ$, so the class of $f$ is $d$ times the class of the identity, that is $f$ is homotopic to the $d$-fold sum of the identity. Precomposition is a homomorphism, so $g\circ f$ is homotopic to the $d$-fold sum of $g\circ\mathrm{id}$, which is $d[g]$.
:::

:::

::: {.pf-step #first}
If $f\colon S^{2n-1}\to S^{2n-1}$ has degree $d$ and $g\colon S^{2n-1}\to S^n$, then $H(gf)=d\,H(g)$.

::: pf-proof
The attaching map of the top cell of $C_{gf}$ is $gf$, and by step [](#degree-action){.pf-ref} $gf\simeq d\cdot g$. A map of pairs $(D^{2n},S^{2n-1})\to(D^{2n},S^{2n-1})$ is determined up to homotopy rel the boundary by the degree of its boundary restriction, so there is a cellular $\varphi\colon C_{gf}\to C_g$ that is the identity on $S^n$ and restricts to a map of degree $d$ on the top cell; the compatibility on the boundary is exactly $gf\simeq d\cdot g$, the attaching map of the top cell of $C_g$ being $g$ composed with degree $d$. On cohomology $\varphi^*(x_g)$ is a generator of $H^n(C_{gf})$ by step [](#cohomology){.pf-ref}, since $\varphi$ is the identity on $S^n$ and both classes restrict to the same generator of $H^n(S^n)$; and $\varphi^*(y_g)=\pm d\,y_{gf}$ by the convention of step [](#definition){.pf-ref}, the characteristic map of the top cell having degree $d$ after $\varphi$. Write $\varphi^*(x_g)=x_{gf}$ and $\varphi^*(y_g)=\varepsilon d\,y_{gf}$ with $\varepsilon=\pm1$. Applying $\varphi^*$ to $x_g^2=H(g)y_g$ gives $x_{gf}^2=\varepsilon d\,H(g)\,y_{gf}$, while $x_{gf}^2=H(gf)y_{gf}$ by step [](#definition){.pf-ref}; $y_{gf}$ generates an infinite cyclic group, and $H(gf)$ is defined with the same sign convention as $H(g)$, so comparing coefficients gives $H(gf)=d\,H(g)$.
:::

:::

::: {.pf-step #second}
If $f\colon S^{2n-1}\to S^n$ and $g\colon S^n\to S^n$ has degree $d$, then $H(gf)=d^2\,H(f)$.

::: pf-proof
Now the attaching map $gf$ of $C_{gf}$ is the composite of $f$ with $g$, so there is a cellular $\psi\colon C_f\to C_{gf}$ restricting to $g$ on the bottom sphere and to a map of degree $1$ on the top cell: the boundary of the top cell maps by $g\circ f$, which is the attaching map needed. On cohomology $\psi^*(x_{gf})=\pm d\,x_f$, since the bottom sphere carries $g$ of degree $d$ and $H^n(C_f)=H^n(C_{gf})=\ZZ$; and $\psi^*(y_{gf})=\pm y_f$, the top cell carrying a degree-$1$ map. Applying $\psi^*$ to $x_{gf}^2=H(gf)y_{gf}$ gives $d^2x_f^2=\pm H(gf)y_f$, that is $d^2H(f)y_f=\pm H(gf)y_f$; the generator $y_f$ is not torsion and the sign conventions of step [](#definition){.pf-ref} are consistent, so $H(gf)=d^2H(f)$.
:::

:::

::: {.pf-step}
$\boxed{H(gf)=(\deg f)H(g)\ \text{for}\ gf\colon S^{2n-1}\xrightarrow{f}S^{2n-1}\xrightarrow{g}S^n \quad\text{and}\quad H(gf)=(\deg g)^2H(f)\ \text{for}\ gf\colon S^{2n-1}\xrightarrow{f}S^n\xrightarrow{g}S^n.}$

::: pf-proof
The first identity is step [](#first){.pf-ref} and the second is step [](#second){.pf-ref}; in each, the degree enters through the induced map of mapping cones on the bottom or the top cell, and the cup product compares coefficients on the generator of $H^{2n}$, which is infinite cyclic so that a coefficient equality is an equality of integers.
:::

:::

:::
:::
