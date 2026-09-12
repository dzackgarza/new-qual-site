---
schema: qual/card@1
id: P-JHUFA05ANF
kind: problem
title: Automorphisms of the right half-plane and of $\mathbb C$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Disc Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared both parts on PDF page 43. The printed set is Re z greater than zero, so corrected its contradictory upper-half-plane name while preserving the set and the plane part."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved the complete disk-conjugation classification and its converse; for plane automorphisms proved growth at infinity from the continuous inverse, polynomiality and degree one."
---

6. (a) Describe all the automorphisms of the right half-plane
$H=\{z\in\mathbb C:\operatorname{Re}z>0\}$, meaning holomorphic bijections from $H$ onto itself.

(b) Describe all the automorphisms of C (holomorphic bijective maps from C onto C).

::: solution
Write $D=\{w:|w|<1\}$ and
$$
T(z)=\frac{z-1}{z+1},\qquad T^{-1}(w)=\frac{1+w}{1-w}.
$$
The answers are
$$
\boxed{\operatorname{Aut}(H)=
\left\{z\longmapsto T^{-1}\!\left(
\lambda\frac{T(z)-a}{1-\overline a T(z)}\right):
a\in D,\ |\lambda|=1\right\},}
$$
and
$$
\boxed{\operatorname{Aut}(\mathbb C)=
\{z\longmapsto az+b:a,b\in\mathbb C,\ a\ne0\}.}
$$

<1>1. Part (a) reduces to the disk automorphisms.

::: proof
The displayed maps $T,T^{-1}$ are inverse by substitution.
For $z\in H$ and $w\in D$,
$$
1-|T(z)|^2=\frac{4\operatorname{Re}z}{|z+1|^2}>0,
\qquad
\operatorname{Re}T^{-1}(w)=\frac{1-|w|^2}{|1-w|^2}>0.
$$
Thus they are biholomorphic maps between $H$ and $D$.
Conjugation by $T$ gives a bijection between their
automorphism groups.

For a disk automorphism $g$, take $a=g^{-1}(0)$ and let
$\phi_a(w)=(w-a)/(1-\overline a w)$. The inverse is
$(v+a)/(1+\overline a v)$; the identity
$$
1-|\phi_a(w)|^2=
\frac{(1-|a|^2)(1-|w|^2)}{|1-\overline a w|^2}
$$
and the corresponding inverse identity show that this
is a disk automorphism. Both $h=g\circ\phi_a^{-1}$ and
$h^{-1}$ fix zero. Schwarz's lemma gives
$|h(w)|\leq|w|=|h^{-1}(h(w))|\leq|h(w)|$.
Its equality case implies $h(w)=\lambda w$ with
$|\lambda|=1$ [@SS03]. Hence $g=\lambda\phi_a$.
Conversely each such map is a rotation composed with
a disk automorphism. Conjugating proves exactly the
formula for part (a), including its converse.
:::

<1>2. A plane automorphism must be a polynomial.

::: proof
Let $F:\mathbb C\to\mathbb C$ be a holomorphic bijection.
Its inverse is holomorphic, hence continuous, by the
nonvanishing derivative of an injective holomorphic
function and the inverse function theorem [@SS03].
For every $M>0$, the set
$F^{-1}(\{w:|w|\leq M\})$ is compact: it is the
continuous image of this compact disk under the inverse.
It is therefore bounded. Consequently
$|F(z)|\to\infty$ as $|z|\to\infty$.

For small nonzero $\zeta$, put $h(\zeta)=1/F(1/\zeta)$.
It is holomorphic there and tends to zero. The removable
singularity theorem extends it with $h(0)=0$ [@SS03].
Since it is nonzero off zero, its Taylor series has
a first nonzero term, so $h(\zeta)=\zeta^m u(\zeta)$
for some $m\geq1$ and holomorphic $u$ with $u(0)\ne0$.
Thus, for all sufficiently large $|z|$,
$|F(z)|\leq C|z|^m$ for a constant $C$.
Cauchy's coefficient estimate for the entire Taylor
series of $F$ gives $|c_k|\leq CR^{m-k}$ for large $R$.
Letting $R\to\infty$ shows $c_k=0$ for every $k>m$
[@SS03]. Hence $F$ is a polynomial.
:::

<1>3. The polynomial has degree one, and all such maps are automorphisms.

::: proof
The polynomial cannot be constant. If its degree were
at least two, its derivative would be a nonconstant
polynomial, hence have a complex zero by the fundamental
theorem of algebra [@SS03]. This contradicts the
nonvanishing derivative of an injective holomorphic
function. Therefore $F(z)=az+b$ with $a\ne0$.
Conversely this map is holomorphic and has the entire
inverse $w\mapsto(w-b)/a$. This proves part (b).
:::
:::
