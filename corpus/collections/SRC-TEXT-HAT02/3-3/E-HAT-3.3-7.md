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

---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds with fundamental classes $[M]$ and $[N]$, the degree of $f$ is defined to be the integer $d$ such that $f_*([M]) = d[N]$, so the sign of the degree depends on the choice of fundamental classes.
Show that for any connected closed orientable $n$-manifold $M$ there is a degree 1 map $M \to S^n$.
:::

::: {.solution}
Hatcher's convention, printed in this exercise on p. 258, is that $M$ and $N$ are *connected* closed orientable $n$-manifolds with fundamental classes $[M]$ and $[N]$, and $\deg f=d$ where $f_*([M])=d[N]$. Theorem 3.26(a), p. 236, then says that $H_n(M)$ and $H_n(N)$ are infinite cyclic and that $[M]$ and $[N]$ restrict to generators of $H_n(M\,|\,p)$ and $H_n(N\,|\,y)$ for every point $p$ and $y$.

For $n=0$, $S^0$ is disconnected, so it is outside that convention. With the usual componentwise extension of a fundamental class, $[S^0]=(1,1)\in H_0(S^0)=\ZZ^2$ does restrict to a generator at each point; nevertheless, for $M$ a point $f_*([M])$ is one of $(\pm1,0)$ and $(0,\pm1)$, whereas $d[S^0]=(d,d)$, so the displayed equation is unsatisfiable. The construction below therefore takes $n\ge1$.

Choose an open coordinate disk $B\subset M$ and a point $p\in B$. Let $q:M\to Q=M/(M-B)$ collapse the closed complement of $B$ to a point, write $\infty=q(M-B)$, and choose a homeomorphism $h:Q\to S^n$ with $\infty$ as the antipode of $h(q(p))$; this quotient is $S^n$, as in the proof of Theorem 2.44, p. 146. Put $f=h\circ q$ and
$$
y=f(p)=h(q(p)),\qquad \infty\ne y .
$$
Thus the quotient pair is $(Q,\{\infty\})$: $f$ sends $M-B$ to $\infty$, while $p$ is sent to the distinct point $y$. Moreover $q\restrict_B$ and $h$ give a homeomorphism
$$
f\restrict_B:(B,B-\{p\})\xrightarrow{\ \cong\ }
(f(B),f(B)-\{y\})
$$
between the two displayed pairs of open sets.

The precise local-degree diagram is
$$
\begin{array}{ccccc}
H_n(M) & \xrightarrow{\ f_*\ } & H_n(S^n) \\
\Big\downarrow{\rho_M} && \Big\downarrow{\rho_S} \\
H_n(M,M-\{p\}) & \xrightarrow{\ f_*^{(p)}\ } & H_n(S^n,S^n-\{y\}) \\
\Big\uparrow{e_M} && \Big\uparrow{e_S} \\
H_n(B,B-\{p\}) & \xrightarrow{\ (f\restrict_B)_*\ } & H_n(f(B),f(B)-\{y\}) .
\end{array}
$$
All coefficients are $\ZZ$. Here $\rho_M$ and $\rho_S$ are induced by inclusions of pairs and are isomorphisms by Theorem 3.26(a). The two squares commute by naturality of homology for the same continuous maps. The vertical maps $e_M$ and $e_S$ are isomorphisms by excision: for example, with $A=M-\{p\}$ and $Z=M-B$, one has $\overline Z\subset\operatorname{int}A$ because $B$ is open and $p\in B$, so
$$
H_n(M-Z,A-Z)=H_n(B,B-\{p\})\cong H_n(M,M-\{p\}).
$$
The same computation applies inside $S^n$ with $f(B)$ replacing $B$ and $y$ replacing $p$. The bottom map is an isomorphism because $f\restrict_B$ is a homeomorphism of pairs. Consequently $f_*^{(p)}$ is an isomorphism.

Now $\rho_M([M])$ and $\rho_S([S^n])$ are local generators by the definition of a fundamental class. Hence the middle horizontal map carries one local generator to $\pm$ the other, and commutativity gives
$$
f_*([M])=\pm[S^n].
$$
If the sign is $-1$, replace $[M]$ by $-[M]$, the fundamental class for the opposite orientation of $M$. Then $f_*([M])=[S^n]$, so Hatcher's definition above gives $\deg f=1$.

The construction is the one in the Math 538 homework solutions, HMW 4, handwritten p. 1 (PDF p. 17 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #7: collapse an open disk's complement, identify the quotient with $S^n$, and change the orientation to remove the sign. The diagram above supplies the local identifications that the sheet does not display.
:::
