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

---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds with fundamental classes $[M]$ and $[N]$, the degree of $f$ is defined to be the integer $d$ such that $f_*([M]) = d[N]$, so the sign of the degree depends on the choice of fundamental classes.
Show that for any connected closed orientable $n$-manifold $M$ there is a degree 1 map $M \to S^n$.
:::

::: {.solution}
Write $[M]\in H_n(M;\ZZ)$ and $[S^n]\in H_n(S^n;\ZZ)$ for the fundamental classes; by the definition quoted in the exercise, a map $f$ has degree $d$ when $f_*([M])=d\,[S^n]$, and the sign depends on the two classes.

Take $n\ge1$ for the construction below. The case $n=0$ is worth stating exactly, because it is the boundary of the definition rather than of the topology. The definition requires the target to be a *connected* closed orientable manifold, and $S^0$ is not connected, so "a degree 1 map $M\to S^0$" is not covered by it. $S^0$ does have a fundamental class in the sense of p. 236: $H_0(S^0;\ZZ)=\ZZ^2$ and $[S^0]=(1,1)$, whose image in each local group $H_0(S^0\,|\,\{p\})=\ZZ$ is a generator. But for $M$ a point every map has $f_*([M])\in\{(\pm1,0),(0,\pm1)\}$, whereas $d\,[S^0]=(d,d)$, so no integer $d$ satisfies $f_*([M])=d[S^0]$ at all: for $n=0$ there is no degree 1 map, and the statement of the exercise is a statement about $n\ge1$.

So let $B\subset M$ be an open disk, a ball whose closure lies in a larger ball, and fix $p\in B$. Define
$$
f:M\longrightarrow S^n
$$
as the collapse of $M-B$ to a point followed by a homeomorphism: $f$ is the composite $M\to M/(M-B)\xrightarrow{\ \cong\ }S^n$, where collapsing the complement of a disk in a connected closed $n$-manifold gives $S^n$ (as in the proof of Theorem 2.44, p. 146). Thus $f$ maps $B$ onto $S^n-\{f(p)\}$ and $M-B$ onto the point $f(p)$.

As a map of pairs, $f$ is a map $(M,M-B)\to(S^n,\{f(p)\})$ — not to $(S^n,S^n-\{f(p)\})$, since $f(M-B)=\{f(p)\}$ — and on the target the pair sequence of $(S^n,\{f(p)\})$, together with $H_i(\{f(p)\})=0$ for $i>0$, gives
$$
H_n(S^n)\xrightarrow{\ \cong\ }H_n(S^n,\{f(p)\})\qquad(n\ge1).
$$
On the source, excision for the ball gives $H_n(M,M-B)\cong H_n(B,B-\{p\})\cong\ZZ$, and the pair sequence of $(M,M-B)$ shows that $H_n(M)\to H_n(M,M-B)$ is an isomorphism sending $[M]$ to the local class $\mu_p$: that is exactly the condition that the image of $[M]$ in $H_n(M\,|\,p)$ be a generator. Under these two identifications $f_*$ becomes an isomorphism of infinite cyclic groups, so $f_*[M]=\pm[S^n]$. If the sign is $-1$, replace $[M]$ by its negative, the fundamental class of the opposite orientation of $M$; then $f_*[M]=[S^n]$ and $\deg f=1$.

This is the solution printed in the Math 538 homework solutions, HMW 4, handwritten page 1 (PDF page 17 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #7: it defines $f$ by sending an open disk $B$ to $S^n-\{\mathrm{pt}\}$ and $M-B$ to $\{\mathrm{pt}\}$, notes that $M/(M-B)\to S^n$ is a homeomorphism, and concludes $f_*[M]=\pm[S^n]$ with the sign removed "since we can choose the other orientation of $M$".
:::
