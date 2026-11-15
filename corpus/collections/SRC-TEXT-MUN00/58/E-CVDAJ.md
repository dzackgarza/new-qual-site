---
schema: qual/card@1
id: E-CVDAJ
kind: problem
title: Consequences of an abstract degree theory on spheres
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 10, printed p. 367,
    with the degree axioms stated in the exercise. The card derives each of the four parts from the axioms: no retraction from (a), the degree of a map with no fixed point and of one that never maps a point to its antipode, and the parity conclusion for a nonvanishing tangent field, all by the straight-line homotopies to the antipodal map or the identity. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    Parts (b) and (d) now carry a published source: Hatcher, *Algebraic Topology* (2002),
    property (g) of degree in §2.2 with its proof on printed p. 134 for (b), and the first half of
    the proof of Theorem 2.28 on printed pp. 134-135 for (d); property (f) on printed p. 134 is the
    degree $(-1)^{n+1}$ of the antipodal map, held at tmp/sources/hatcher-2002-algebraic-topology.md.
    The solution transcribes those arguments, replacing Hatcher's degree in singular homology by
    the exercise's axioms, which is what the exercise supplies; the antipodal degree is re-derived
    from axioms (ii) and (iii) rather than quoted, since Hatcher's (f) rests on his homology. Parts
    (a) and (c) have no located published source and keep the card's proofs, checked against the
    printed axioms on printed p. 367: in (a) the inclusion of $S^n$ in the ball is nulhomotopic
    because the ball is convex, so its degree is $0$ by axioms (i) and (iii), and a retraction would
    give $1=0$ by (ii); in (c) the straight-line homotopy to the identity exists exactly when $h$
    misses the antipodes, so $\deg h=1$ by (i) and (iii). Checked against the book: the exercise
    text and its three axioms on printed p. 367, and, for the notion of a nonvanishing tangent
    vector field used in (d), that the exercise states it without further definition. Not claimed:
    that (a) or (c) has a published solution anywhere.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten in Lamport form with the source and its pages named in its own text
    and with the split between sourced parts (b),(d) and unsourced parts (a),(c) stated. The
    earlier proof covered the same four parts by the same homotopies and was a correct proof of the
    exercise; it was replaced because the card is to carry the published arguments.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Part (a) rewritten: it applied the degree to the inclusion $i:S^n\to B^{n+1}$ and the
    retraction $r:B^{n+1}\to S^n$, and the three axioms printed on p. 367 assign a degree only to
    a map $S^n\to S^n$, so neither $\deg i$ nor $\deg r$ is defined and the chain
    $1=\deg(r\circ i)=\deg r\deg i=0$ does not follow from them. The proof now takes the constant
    map $c:S^n\to B^{n+1}$ at $\mathbf 0$, uses convexity of the ball for $i\simeq c$, composes with
    $r$ to get $\operatorname{id}_{S^n}=r\circ i\simeq r\circ c$ with $r\circ c$ the constant map
    at $r(\mathbf 0)$, and reads off $1=0$ from axioms (i) and (iii) on those two self-maps. Part
    (c) is unaffected and was re-read: it maps $h$ to the identity through the straight line in
    $S^n$ when $h$ misses the antipodes, so it uses the axioms only on self-maps. Checked against
    the book: the exercise and its three axioms on printed p. 367; not claimed: a published source
    for (a) or (c), which none of the sets searched contains.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Parts (a) and (c) now have a published source, in place of the sentences in the 2026-11-11 and
    2026-11-14 events recording that none was located among the sets searched then. Both are
    transcribed from Takumi Murayama, *Selected Solutions to Munkres's Topology, 2nd Ed.* (Princeton
    MAT365, Fall 2012), Exercise 58.10, read 2026-11-15 in the LaTeX source of that set kept at
    tmp/sources/munkres-solutions-murayama-mat365.tex and published at
    https://github.com/awasthi/math-solutions/blob/master/Munkres/Munkres%20Solutions.tex: the
    exercise at line 1631, the proof of (a) at lines 1646-1650 with the retraction supposed at line
    1648 and the homotopy at line 1649, and the proof of (c) at lines 1659-1667 with the straight
    line homotopy at line 1662. Murayama sets (a) up in polar coordinates, where his homotopy
    H(...,t) = r(...,t) has last coordinate rho = t; the card states the same map in Cartesian
    coordinates as H(x,t) = r(tx), and the argument is otherwise his. Checked against the book: the
    exercise and its three axioms print on printed p. 367, not on p. 366 as the assignment for this
    pass said -- the page image of tmp/sources/munkres-2000-topology.pdf (printed page = PDF page -
    15) shows Exercise 9 beginning on printed p. 366 and Exercise 10 whole on p. 367 -- so this
    card's page is unchanged. A second published source for both parts was read and is not the one
    transcribed: Feryll, "Degree of Continuous Maps on S^n (9.58.9-10)", *Praying For Stockholm*,
    2015-02-01, https://feryll.blogspot.com/2015/02/degree-of-continuous-maps-on-sn-9589-10.html,
    kept at tmp/sources/feryll-2015-munkres-58-9-10.md, its (a) at line 98 and its (c) at line 114.
    Its (c) misquotes the exercise as asking about degree different from (-1)^n where printed p. 367
    asks about degree different from 1, and it states axiom (iii) for every coordinate reflection
    where printed p. 367 states it for the last coordinate only; its (c) is also a one line
    reduction to its (b) applied to the antipodal composite, not the homotopy written out. Murayama's
    statement of the exercise agrees with the book's, the last-coordinate reflection included.
    Not claimed: that either source's (b) or (d) was used -- those parts keep Hatcher.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Parts (a) and (c) were replaced by the transcription described in the preceding event, and the
    solution's opening now names Murayama for them and Hatcher for (b) and (d) in one place. Part (a)
    states the homotopy as H(x,t) = r(tx) instead of going through the inclusion and a constant map:
    its ends are the constant map at r(0) and the identity on S^n, and the contradiction is read off
    axioms (i) and (iii) on those two self-maps, with the remark kept that the axioms assign no
    degree to the inclusion or to r. Part (c) is the source's straight line homotopy
    G(x,t) = ((1-t)h(x) + tx)/||(1-t)h(x) + tx||, whose denominator vanishes only when t = 1/2 and
    h(x) = -x, the excluded case. Parts (b) and (d) and the antipodal degree step were re-read and
    are unchanged, as is the derivation of deg a = (-1)^{n+1} from axioms (ii) and (iii).
- event: solution-reviewed
  by: claude
  date: 2026-11-15
  note: >-
    All four parts were read against their sources and the book: (a) and (c) against Murayama as
    named above, (b) and (d) against Hatcher, *Algebraic Topology* (2002), printed pp. 134-135, and
    the exercise and its axioms against printed p. 367. Checked that each transcribed step uses only
    the axioms the exercise supplies, and that no step applies a degree to a map that is not a
    self-map of S^n. Not checked: Murayama's and Feryll's own (b) and (d), which are not used.
---

::: {.exercise}

Suppose that to every map $h: S^n \to S^n$ we have assigned an integer, denoted by $\deg h$ and called the degree of $h$, such that:

(i) Homotopic maps have the same degree.

(ii) $\deg(h \circ k) = (\deg h) \cdot (\deg k)$.

(iii) The identity map has degree 1, any constant map has degree 0, and the reflection map $\rho(x_1, \ldots, x_{n+1}) = (x_1, \ldots, x_n, -x_{n+1})$ has degree $-1$.

[One can construct such a function, using the tools of algebraic topology. Intuitively, $\deg h$ measures how many times $h$ wraps $S^n$ about itself; the sign tells you whether $h$ preserves orientation or not.] Prove the following:

(a) There is no retraction $r: B^{n+1} \to S^n$.

(b) If $h: S^n \to S^n$ has degree different from $(-1)^{n+1}$, then $h$ has a fixed point.
[Hint: Show that if $h$ has no fixed point, then $h$ is homotopic to the antipodal map $a(x) = -x$.]

(c) If $h: S^n \to S^n$ has degree different from 1, then $h$ maps some point $x$ to its antipode $-x$.

(d) If $S^n$ has a nonvanishing tangent vector field $v$, then $n$ is odd.
[Hint: If $v$ exists, show the identity map is homotopic to the antipodal map.]
:::

::: {.solution}
The exercise is §58 Exercise 10, printed p. 367, and its hypotheses are the
three numbered axioms printed there. Parts (a) and (c) are transcribed from
Takumi Murayama, *Selected Solutions to Munkres's Topology, 2nd Ed.* (Princeton
MAT365, Fall 2012), Exercise 58.10, in the LaTeX source of that set kept at
`tmp/sources/munkres-solutions-murayama-mat365.tex` and published at
https://github.com/awasthi/math-solutions/blob/master/Munkres/Munkres%20Solutions.tex:
the exercise at line 1631, the proof of (a) at lines 1646--1650 and the proof of
(c) at lines 1659--1667. Murayama sets (a) up in polar coordinates, where the
last coordinate of his homotopy is the radius $\rho=t$; the card states the same
map in Cartesian coordinates, as $H(x,t)=r(tx)$. Parts (b) and (d) are
transcribed from Hatcher, *Algebraic Topology* (2002): (b) is property (g) of
degree in §2.2 with its proof, printed p. 134, and (d) is the first half of the
proof of Theorem 2.28, printed pp. 134--135; the preliminary degree of the
antipodal map is Hatcher's property (f), printed p. 134, and it is re-derived
here from the axioms because the exercise supplies the axioms and not Hatcher's
homology.

Write $a(x)=-x$ for the antipodal map of $S^n$, and let
$\rho(x_1,\dots,x_{n+1})=(x_1,\dots,x_n,-x_{n+1})$ be the reflection of axiom
(iii).

::: pf

::: {.pf-step #antipodal-degree}
$\deg a=(-1)^{n+1}$.

::: pf-proof
For $i=1,\dots,n+1$ let $\sigma_i$ change the sign of the $i$-th coordinate and
fix the others. The permutation matrix $P$ interchanging the coordinates $i$ and
$n+1$ is a homeomorphism of $S^n$ with $\sigma_i=P\rho P^{-1}$, and by axiom
(ii) and axiom (iii)
$$
\deg(\sigma_i)=\deg(P)\deg(\rho)\deg(P^{-1})=\deg(P)\deg(P^{-1})\cdot(-1).
$$
Axioms (ii) and (iii) also give
$\deg(P)\deg(P^{-1})=\deg(P\circ P^{-1})=\deg(\operatorname{id})=1$, so
$\deg(P)\deg(P^{-1})=1$ and $\deg\sigma_i=-1$. Since $a=\sigma_1\circ\cdots\circ\sigma_{n+1}$
and the composition of sign changes is the sign change of every coordinate,
$$
\deg a=\prod_{i=1}^{n+1}\deg\sigma_i=(-1)^{n+1}
$$
by axiom (ii).
:::

:::

::: {.pf-step}
(a) There is no retraction $r:B^{n+1}\to S^n$.

::: pf-proof
Suppose a retraction $r:B^{n+1}\to S^n$ exists, and let $i:S^n\to B^{n+1}$ be
the inclusion. For $x\in S^n$ and $t\in I$ the point $tx$ lies on the radius
from $\mathbf 0$ through $x$ at distance $t$ from the centre, so it is in
$B^{n+1}$, and $H(x,t)=r(tx)$ is a continuous map $S^n\times I\to S^n$. Its two
ends are $H(x,0)=r(\mathbf 0)$, which does not depend on $x$, so that $H_0$ is
the constant map at $r(\mathbf 0)$, and $H(x,1)=r(x)=x$ because
$r\circ i=\operatorname{id}_{S^n}$, so that $H_1=\operatorname{id}_{S^n}$. Both
ends are self-maps of $S^n$, and $H$ is a homotopy between them, so axiom (i)
gives $\deg H_0=\deg H_1$, while axiom (iii) gives $\deg H_0=0$ for the constant
map and $\deg H_1=1$ for the identity. Hence $1=0$, and no such $r$ exists.

The axioms assign a degree only to a map $S^n\to S^n$, so the argument never
mentions $\deg i$ or $\deg r$, which are not defined for the inclusion
$i:S^n\to B^{n+1}$ or the retraction $r:B^{n+1}\to S^n$; it composes with $r$
first, which is what brings the homotopy back to self-maps of $S^n$.
:::

:::

::: {.pf-step #no-fixed-point}
(b) If $h:S^n\to S^n$ has $\deg h\ne(-1)^{n+1}$, then $h$ has a fixed point.

::: pf-proof
It suffices to prove the contrapositive. Suppose $h(x)\ne x$ for every
$x\in S^n$, and consider the straight-line map
$$
f_t(x)=\frac{(1-t)h(x)-tx}{\norm{(1-t)h(x)-tx}},\qquad 0\le t\le1 .
$$
The denominator does not vanish: $(1-t)h(x)-tx=\mathbf 0$ with
$0<t<1$ gives $(1-t)\norm{h(x)}=t\norm x$, that is $1-t=t$, and then
$h(x)=x$; and at $t=0$ or $t=1$ the vector is $h(x)$ or $-x$. So $f_t$ is a
continuous map into $S^n$ for each $t$, by continuity of $h$ in $x$ and of the
formula in $t$, with $f_0=h$ and $f_1=a$. By axiom (i), $\deg h=\deg a$, and
$\deg a=(-1)^{n+1}$ by step [](#antipodal-degree){.pf-ref}. So a map without
fixed points has degree $(-1)^{n+1}$, and a map of the other degree has one.
:::

:::

::: {.pf-step}
(c) If $h:S^n\to S^n$ has $\deg h\ne1$, then $h(x)=-x$ for some $x$.

::: pf-proof
Again contrapositively, suppose $h(x)\ne-x$ for every $x\in S^n$, and set
$$
G(x,t)=\frac{(1-t)h(x)+tx}{\norm{(1-t)h(x)+tx}},\qquad 0\le t\le1 .
$$
The denominator does not vanish: if $(1-t)h(x)+tx=\mathbf 0$, then
$(1-t)h(x)=-tx$, and comparing norms, with $\norm{h(x)}=\norm x=1$, gives
$1-t=t$, so $t=1/2$ and $h(x)=-x$, which is excluded. Hence $G$ is defined, and
it is continuous on $S^n\times I$, being a composition of continuous functions of
$x$ and $t$; its values lie in $S^n$ because the numerator has the norm of the
denominator, and $G(x,0)=h(x)$, $G(x,1)=x$. So $G$ is a homotopy from $h$ to
$\operatorname{id}_{S^n}$, and axioms (i) and (iii) give
$\deg h=\deg(\operatorname{id})=1$. A map whose degree is not $1$ therefore
takes some point to its antipode.
:::

:::

::: {.pf-step}
(d) If $S^n$ has a nonvanishing tangent vector field $v$, then $n$ is odd.

::: pf-proof
Regard $v(x)$ as a vector of $\RR^{n+1}$; tangency means $x$ and $v(x)$ are
orthogonal, and $v(x)\ne\mathbf 0$ by hypothesis, so after replacing $v(x)$ by
$v(x)/\norm{v(x)}$ we may suppose $\norm{v(x)}=1$ for all $x$. Then for
$0\le t\le\pi$,
$$
f_t(x)=(\cos t)x+(\sin t)v(x)
$$
has norm $\cos^2t+\sin^2t=1$, using the orthogonality, so $f_t$ is a continuous
map of $S^n$ into itself; $f_0=\operatorname{id}_{S^n}$ and
$f_\pi=a$. By axiom (i), $\deg(\operatorname{id})=\deg a$, that is
$1=(-1)^{n+1}$ by axiom (iii) and step [](#antipodal-degree){.pf-ref}, which
forces $n+1$ even, that is $n$ odd.
:::

:::

:::
:::
