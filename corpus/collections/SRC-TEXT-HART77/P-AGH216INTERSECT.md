---
schema: qual/card@1
id: P-AGH216INTERSECT
kind: problem
title: Intersections of varieties, and why $I(Y \intersect Z) \neq I(Y) + I(Z)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Intersections
  - Twisted Cubic
  - Homogeneous Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared part (a) with the retained Hartshorne I.2.16 transcription. Its part (b) has a four-variable transcription error in a plane equation; the current conic and point calculation were checked against the Berkeley 256A Chapter 1 solutions, Exercise 2.16(b). Both parts are proved directly, with the nonreduced ideal sum retained.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed.

(a) The intersection of two varieties need not be a variety.
Let $Q_1, Q_2 \subseteq \PP_k^3$ be the quadric surfaces given by $x^2 - yw = 0$ and $xy - zw = 0$.
Show that $Q_1 \intersect Q_2$ is the union of a twisted cubic curve and a line.

(b) Even when the intersection of two varieties is a variety, the ideal of the intersection need not be the sum of the ideals.
Let $C \subseteq \PP_k^2$ be the conic given by $x^2 - yz = 0$, and let $L$ be the line given by $y = 0$.
Show that $C \intersect L$ is a single point $P$, but that $I(C) + I(L) \neq I(P)$.
:::

::: {.solution}
The intersections in the statement are intersections of algebraic sets.
For part (a), use coordinates $[x:y:z:w]$ on $\PP^3$; part (b) uses $[x:y:z]$ on $\PP^2$.

::: pf

::: {.pf-step #two-components-of-intersection}
The two components in (a) are
$$
\boxed{T=\{[s^2t:st^2:t^3:s^3]:[s:t]\in\PP^1\},\qquad
R=Z(x,w).}
$$

::: pf-proof
The parametrization of $T$ consists of the four degree-three monomials in $s,t$, with the pure cube $s^3$ placed last.
It is therefore the [[P-AGH212DUPLE|twisted cubic]], and in particular a closed irreducible curve.
The set $R$ is the projectivization of the two-dimensional coordinate subspace with $x=w=0$, hence is a line by [[P-AGH211LINEAR]].

Substitution of the parametrization of $T$ gives $x^2=yw$ and $xy=zw$.
Both equations also vanish on $R$.
Thus $T\cup R\subseteq Q_1\cap Q_2$.

Conversely, on the chart $w\ne0$, normalize $w=1$.
The equations give $y=x^2$ and $z=xy=x^3$, so the point is $[x:x^2:x^3:1]$, the point of $T$ with $[s:t]=[1:x]$.
On $w=0$, the first equation forces $x=0$, so the point belongs to $R$.
These cases exhaust the projective intersection and prove $Q_1\cap Q_2=T\cup R$.
:::

:::

::: {.pf-step #quadrics-irreducible-intersection-reducible}
The two quadrics are varieties, but their intersection is reducible.

::: pf-proof
The polynomial $x^2-yw$ is primitive as a polynomial in $y$ over the UFD $k[x,z,w]$, because $x^2$ and $w$ are relatively prime.
It is linear and irreducible over the fraction field of that UFD, so Gauss's lemma makes it irreducible in $k[x,y,z,w]$.
The same argument applies to $xy-zw$, viewed as a primitive linear polynomial in $z$ over $k[x,y,w]$.
Both homogeneous equations therefore define irreducible projective hypersurfaces by [[P-AGH28HYPERSURFACE]].

The point $[1:1:1:1]$ lies in $T$ but not $R$.
The point $[0:1:0:0]$ lies in $R$ but not $T$: on $T$, the equation $w=s^3=0$ forces $s=0$, giving only $[0:0:1:0]$.
Thus neither of the two nonempty closed subsets $T,R$ contains the other.
Their union from step [](#two-components-of-intersection){.pf-ref} is reducible, and those subsets are its two irreducible components by [[P-AGH25NOETHERIAN]].
This verifies the stated phenomenon in (a).
:::

:::

::: {.pf-step #point-intersection-ideal-strict}
In (b),
$$
\boxed{C\cap L=\{P\},\quad P=[0:0:1],\qquad
I(C)+I(L)=(x^2,y)\subsetneq(x,y)=I(P).}
$$

::: pf-proof
On $L$, the conic equation becomes $x^2=0$, hence $x=0$.
The remaining projective coordinate $z$ must be nonzero, giving exactly $P=[0:0:1]$.

The polynomial $x^2-yz$ is primitive and linear in $y$ over $k[x,z]$, so the Gauss-lemma argument of step [](#quadrics-irreducible-intersection-reducible){.pf-ref} makes it irreducible.
The homogeneous vanishing ideals are therefore
$$
I(C)=(x^2-yz),\qquad I(L)=(y),\qquad I(P)=(x,y)
$$
by [[P-AGH24CORRESPONDENCE]] and the coordinate-subspace calculation in [[P-AGH211LINEAR]].
Consequently
$$
I(C)+I(L)=(x^2-yz,y)=(x^2,y).
$$
This does not contain $x$.
Indeed, reduction modulo $y$ would otherwise give $x\in(x^2)$ in $k[x,z]$, which would force $1=xh$ for some polynomial $h$, an impossibility after setting $x=0$.
Since $x\in I(P)$, the containment is strict.
The radical of the sum is $(x,y)$; before taking the radical, its quotient has the nonzero square-zero element given by the class of $x$.
This proves all of (b).
:::

:::

::: pf-qed
Steps [](#two-components-of-intersection){.pf-ref} and [](#quadrics-irreducible-intersection-reducible){.pf-ref} give the reducible intersection in (a), and step [](#point-intersection-ideal-strict){.pf-ref} gives the point intersection with unequal ideals in (b).
:::

:::

:::
