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
three numbered axioms printed there. Parts (b) and (d) are transcribed from
Hatcher, *Algebraic Topology* (2002): (b) is property (g) of degree in §2.2 with
its proof, printed p. 134, and (d) is the first half of the proof of Theorem
2.28, printed pp. 134--135; the preliminary degree of the antipodal map is
Hatcher's property (f), printed p. 134, and it is re-derived here from the axioms
because the exercise supplies the axioms and not Hatcher's homology. Parts (a)
and (c) have no located published source, and their proofs are checked against
the axioms on printed p. 367.

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
Suppose $r$ is a retraction and $i:S^n\to B^{n+1}$ the inclusion, so that
$r\circ i=\operatorname{id}_{S^n}$ by the definition of a retraction. The ball is
convex, so the straight-line homotopy $(x,t)\mapsto(1-t)x+t\mathbf 0$ makes $i$
nullhomotopic, hence constant-up-to-homotopy; by axioms (i) and (iii) applied to
that constant map, $\deg i=0$. Then axiom (ii) and axiom (iii) give
$$
1=\deg(\operatorname{id}_{S^n})=\deg(r\circ i)=\deg(r)\deg(i)=0,
$$
a contradiction.
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
Again contrapositively, suppose $h(x)\ne-x$ for every $x$, and consider
$$
g_t(x)=\frac{(1-t)h(x)+tx}{\norm{(1-t)h(x)+tx}},\qquad 0\le t\le1 .
$$
A zero of the numerator gives $(1-t)\norm{h(x)}=t\norm x$, so $1-t=t$ and
$h(x)=-x$, which is excluded; so $g_t$ is a continuous map into $S^n$, with
$g_0=h$ and $g_1=\operatorname{id}_{S^n}$. By axiom (i) and axiom (iii),
$\deg h=\deg(\operatorname{id})=1$, so a map of degree other than $1$ must take
some point to its antipode.
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
