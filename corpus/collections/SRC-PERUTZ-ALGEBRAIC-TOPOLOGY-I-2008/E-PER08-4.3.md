---
schema: qual/card@1
id: E-PER08-4.3
kind: problem
title: Five models of the 3-strand braid group and the trefoil group
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 4.3 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the two group presentations, the crossing-word presentation of B3, the symmetric-product/discriminant homeomorphism, and the weighted deformation retraction onto the trefoil link complement.
---

::: {.problem}
Let $K\subset S^3$ be the left-handed trefoil knot.
This exercise compares the following groups:

- $\pi_1(S^3\setminus K)$;

- $\langle a,b\mid a^2=b^3\rangle$;

- $\langle s,t\mid sts=tst\rangle$;

- the geometric braid group $B_3=\pi_1(C_3)$, where $C_3$ is the configuration space of unordered $3$-element subsets of $\mathbb C$;

- $\pi_1(\mathbb C^2\setminus C)$, where $C=\{(X,Y):X^2=Y^3\}$ is the cuspidal cubic.

1. Show that $a\mapsto sts$ and $b\mapsto ts$ define an isomorphism
   \[
   \langle a,b\mid a^2=b^3\rangle\xrightarrow{\sim}\langle s,t\mid sts=tst\rangle.
   \]

2. With basepoint $\{-2,0,2\}\in C_3$, define loops
   \[
   \sigma(t)=\{-1-e^{\pi it},-1+e^{\pi it},2\},\qquad
   \tau(t)=\{-2,1-e^{\pi it},1+e^{\pi it}\}.
   \]
   If $s=[\sigma]$ and $t=[\tau]$, check that $sts=tst$, obtaining a homomorphism $\langle s,t\mid sts=tst\rangle\to B_3$.

3. Let $\operatorname{Sym}^3_0(\mathbb C)$ be the unordered triples $\{a,b,c\}$ with $a+b+c=0$.
   Show that
   \[
   \operatorname{Sym}^3(\mathbb C)\cong \mathbb C\times\operatorname{Sym}^3_0(\mathbb C),
   \]
   and define a homeomorphism $\operatorname{Sym}^3_0(\mathbb C)\to\mathbb C^2$ by sending $\{a,b,c\}$ to $(x,y)$ such that
   \[
   (t-a)(t-b)(t-c)=t^3+xt+y.
   \]
   Verify that $a,b,c$ are distinct if and only if $4x^3+27y^2\ne0$.
   Deduce that
   \[
   C_3\cong\mathbb C\times(\mathbb C^2\setminus C)
   \]
   and hence $B_3\cong\pi_1(\mathbb C^2\setminus C)$.

4. Show that $\mathbb C^2\setminus C$ is homotopy equivalent to $S^3\setminus K$.

5. Show that going around the resulting circle of homomorphisms gives an automorphism of $\pi_1(S^3\setminus K)$.
:::

::: {.solution}
Set
\[
G=\langle a,b\mid a^2=b^3\rangle,
\qquad
H=\langle s,t\mid sts=tst\rangle.
\]

<1>1. The assignments $a\mapsto sts$ and $b\mapsto ts$ define an isomorphism $G\cong H$.
::: {.proof}
In $H$, use the braid relation once to compute
\[
(sts)^2=(tst)(sts)=tststs=(ts)^3.
\]
Hence the assignment
\[
\phi(a)=sts,
\qquad
\phi(b)=ts
\]
respects the relation $a^2=b^3$ and defines a homomorphism
\[
\phi:G\to H.
\]

Define elements of $G$ by
\[
s_0=ab^{-1},
\qquad
t_0=b^2a^{-1}.
\]
Then
\[
s_0t_0s_0
=ab^{-1}b^2a^{-1}ab^{-1}
=a,
\]
while
\[
t_0s_0t_0
=b^2a^{-1}ab^{-1}b^2a^{-1}
=b^3a^{-1}
=a^2a^{-1}
=a.
\]
Thus $s_0t_0s_0=t_0s_0t_0$, so there is a homomorphism
\[
\psi:H\to G,
\qquad
\psi(s)=ab^{-1},
\quad
\psi(t)=b^2a^{-1}.
\]
The preceding calculation gives
\[
\psi(\phi(a))=a,
\qquad
\psi(\phi(b))=\psi(ts)=b.
\]
Thus $\psi\phi=\operatorname{id}_G$.

Conversely, inside $H$ put $A=sts$ and $B=ts$. Then
\[
AB^{-1}=sts(ts)^{-1}=s
\]
and
\[
B^2A^{-1}=(ts)^2(sts)^{-1}=t.
\]
Hence $s,t$ lie in the image of $\phi$, so $\phi$ is surjective. Since it also has the left inverse $\psi$, it is injective. Therefore
\[
\boxed{G\cong H}.
\]
:::

<1>2. The loops $\sigma$ and $\tau$ satisfy the braid relation.
::: {.proof}
The loop $\sigma$ performs a positive half-twist exchanging the two leftmost points $-2$ and $0$ while leaving $2$ fixed. The loop $\tau$ performs the corresponding positive half-twist exchanging the two rightmost points $0$ and $2$ while leaving $-2$ fixed.

Draw the three trajectories in $[0,1]\times\mathbb C$. The concatenation
\[
\sigma*\tau*\sigma
\]
has three successive adjacent positive crossings, left--right--left; the concatenation
\[
\tau*\sigma*\tau
\]
has right--left--right. These two embedded three-strand braids differ by the standard Reidemeister-III braid isotopy: slide the middle crossing past the crossing of the other two strands. During this isotopy no two points in a time slice collide, so it is a homotopy through loops in $C_3$.

Consequently
\[
[\sigma][\tau][\sigma]
=[\tau][\sigma][\tau]
\]
in $B_3$. Thus
\[
s\longmapsto[\sigma],
\qquad
t\longmapsto[\tau]
\]
defines a homomorphism
\[
\eta:H\to B_3.
\]
:::

<1>3. In fact $\eta:H\to B_3$ is an isomorphism.
::: {.proof}
We give the standard crossing-word construction for three braids.

Represent a loop in $C_3$ by three moving points in the plane. After an arbitrarily small homotopy, make the braid generic with respect to projection to the real axis: except at finitely many times, the three real parts are distinct; at each exceptional time exactly one adjacent pair has equal real part, and the crossing is transverse. Record a letter $s^{\pm1}$ when the left adjacent pair crosses and $t^{\pm1}$ when the right adjacent pair crosses, with the sign determined by which point passes through the upper half-plane relative to the other. Reading in time order gives a word in $s^{\pm1},t^{\pm1}$.

A generic homotopy between two generic braids can itself be perturbed so that only finitely many nongeneric events occur. Passing such an event changes the crossing word in one of the following ways:

- creation or cancellation of a neighboring pair $ss^{-1}$, $s^{-1}s$, $tt^{-1}$, or $t^{-1}t$;
- a triple-crossing event, which replaces $sts$ by $tst$ or the inverse relation.

For three strands there are no distant crossings, so no commuting relation is needed. Therefore the class of the crossing word in
\[
H=\langle s,t\mid sts=tst\rangle
\]
depends only on the homotopy class of the loop in $C_3$. This defines a homomorphism
\[
\omega:B_3\to H.
\]

For the explicit elementary half-twists $\sigma,\tau$, the crossing words are respectively $s,t$. Thus
\[
\omega\eta(s)=s,
\qquad
\omega\eta(t)=t,
\]
so $\omega\eta=\operatorname{id}_H$.

Conversely, straightening a generic braid between successive crossing times gives a homotopy to the concatenation of the corresponding elementary half-twists. Hence applying $\eta$ to its crossing word recovers its class in $B_3$, so
\[
\eta\omega=\operatorname{id}_{B_3}.
\]
Therefore
\[
\boxed{H\cong B_3}.
\]
:::

<1>4. Splitting off the center of mass gives
\[
\operatorname{Sym}^3(\mathbb C)\cong
\mathbb C\times\operatorname{Sym}^3_0(\mathbb C).
\]
::: {.proof}
For an unordered triple $Q=\{a,b,c\}$ define its mean
\[
m(Q)=\frac{a+b+c}{3}
\]
and its centered triple
\[
Q_0=\{a-m(Q),b-m(Q),c-m(Q)\}.
\]
Then the elements of $Q_0$ sum to zero. The map
\[
Q\longmapsto(m(Q),Q_0)
\]
is continuous and has continuous inverse
\[
(m,\{u,v,w\})\longmapsto\{m+u,m+v,m+w\}.
\]
Hence it is a homeomorphism.
:::

<1>5. Centered unordered triples are homeomorphic to $\mathbb C^2$ by polynomial coefficients.
::: {.proof}
If $a+b+c=0$, then
\[
(t-a)(t-b)(t-c)
=t^3+(ab+ac+bc)t-abc.
\]
Thus define
\[
h:\operatorname{Sym}^3_0(\mathbb C)\to\mathbb C^2,
\qquad
\{a,b,c\}\longmapsto(x,y)
\]
with
\[
x=ab+ac+bc,
\qquad
y=-abc.
\]
This map is continuous.

It is bijective by the fundamental theorem of algebra: every monic cubic
\[
t^3+xt+y
\]
has an unordered multiset of three complex roots, whose sum is zero because the $t^2$ coefficient vanishes. The inverse is continuous because the unordered multiset of roots of a monic polynomial depends continuously on its coefficients. Equivalently, the elementary-symmetric-polynomial map realizes the symmetric product $\operatorname{Sym}^3(\mathbb C)$ homeomorphically as the coefficient space of monic cubics. Hence $h$ is a homeomorphism.
:::

<1>6. The collision locus is the cusp discriminant.
::: {.proof}
A monic cubic
\[
t^3+xt+y
\]
has a repeated root exactly when it has a common root with its derivative
\[
3t^2+x.
\]
Its discriminant is
\[
\Delta=-4x^3-27y^2.
\]
Therefore its three roots are distinct exactly when
\[
4x^3+27y^2\neq0.
\]

Let
\[
D_{\mathrm{cusp}}=\{(x,y):4x^3+27y^2=0\}.
\]
Choose complex constants $\lambda,\mu\neq0$ with
\[
\lambda^2=27,
\qquad
\mu^3=-4.
\]
The invertible linear map
\[
(x,y)\longmapsto(X,Y)=(\lambda y,\mu x)
\]
sends $D_{\mathrm{cusp}}$ onto
\[
C=\{(X,Y):X^2=Y^3\},
\]
because
\[
X^2=27y^2,
\qquad
Y^3=-4x^3.
\]
Thus the two cusp complements are homeomorphic.
:::

<1>7. Therefore
\[
C_3\cong\mathbb C\times(\mathbb C^2\setminus C)
\]
and
\[
B_3\cong\pi_1(\mathbb C^2\setminus C).
\]
::: {.proof}
The configuration space $C_3$ is the open subset of $\operatorname{Sym}^3(\mathbb C)$ consisting of triples with distinct entries. By <1>4, translation by the mean does not affect whether entries are distinct. By <1>5--<1>6, the centered distinct triples correspond exactly to the complement of the discriminant cusp, which is linearly homeomorphic to $\mathbb C^2\setminus C$. Hence
\[
C_3\cong\mathbb C\times(\mathbb C^2\setminus C).
\]
Since $\mathbb C$ is contractible, projection onto the second factor is a homotopy equivalence, so
\[
B_3=\pi_1(C_3)
\cong
\pi_1(\mathbb C^2\setminus C).
\]
:::

<1>8. The cusp complement strongly deformation retracts onto the complement of its link in $S^3$.
::: {.proof}
The cusp equation
\[
X^2=Y^3
\]
is invariant under the positive weighted scaling
\[
\rho\cdot(X,Y)=(\rho^3X,\rho^2Y),
\qquad \rho>0.
\]
Indeed,
\[
(\rho^3X)^2=(\rho^2Y)^3
\iff
X^2=Y^3.
\]

For each nonzero $(X,Y)$ there is a unique $r=r(X,Y)>0$ satisfying
\[
r^6|X|^2+r^4|Y|^2=1,
\]
because the left side is a strictly increasing continuous function of $r$ from $0$ to $\infty$. The implicit inverse is continuous in $(X,Y)$.

For $u\in[0,1]$, set
\[
r_u=(1-u)+u\,r(X,Y)>0
\]
and
\[
H_u(X,Y)=(r_u^3X,r_u^2Y).
\]
Weighted scaling preserves both $C$ and its complement, so $H_u$ stays in $\mathbb C^2\setminus C$ whenever it starts there. At $u=1$,
\[
|r^3X|^2+|r^2Y|^2=1,
\]
so the endpoint lies on $S^3$. If $(X,Y)\in S^3$, uniqueness gives $r=1$, hence $H_u(X,Y)=(X,Y)$ for all $u$.

Thus $H$ is a strong deformation retraction
\[
\mathbb C^2\setminus C
\searrow
S^3\setminus(C\cap S^3).
\]
:::

<1>9. The link $C\cap S^3$ is a trefoil isotopic to $K$.
::: {.proof}
Parametrize the cusp by
\[
(X,Y)=(u^3,u^2).
\]
On $S^3$ one has
\[
|u|^6+|u|^4=1,
\]
so $|u|=r_0$ is a fixed positive number. Writing $u=r_0e^{i\theta}$ gives
\[
C\cap S^3
=
\left\{
(r_0^3e^{3i\theta},r_0^2e^{2i\theta})
:\theta\in\mathbb R/2\pi\mathbb Z
\right\}.
\]
After swapping the two complex coordinates, this becomes a $(2,3)$-torus knot
\[
(r_0^2e^{2i\theta},r_0^3e^{3i\theta}).
\]
Vary the two positive radii continuously along the family of Clifford tori
\[
|z|=R_1,
\qquad
|w|=R_2,
\qquad
R_1^2+R_2^2=1,
\]
from $(R_1,R_2)=(r_0^2,r_0^3)$ to $(1/\sqrt2,1/\sqrt2)$. This gives an isotopy through embedded $(2,3)$-torus knots. By the isotopy extension theorem it extends to an ambient isotopy of $S^3$.

The terminal knot is
\[
\theta\longmapsto
\left(\frac1{\sqrt2}e^{2i\theta},
      \frac1{\sqrt2}e^{3i\theta}\right),
\]
which is the trefoil $K$ from the source, up to the harmless coordinate swap and orientation convention. Therefore
\[
S^3\setminus(C\cap S^3)\cong S^3\setminus K.
\]
Combining with <1>8 gives
\[
\boxed{\mathbb C^2\setminus C\simeq S^3\setminus K}.
\]
:::

<1>10. Going around the full circle gives an automorphism of $\pi_1(S^3\setminus K)$.
::: {.proof}
The successive arrows are:
\[
\pi_1(S^3\setminus K)
\xrightarrow{\cong}
G
\xrightarrow{\phi}
H
\xrightarrow{\eta}
B_3
\xrightarrow{\cong}
\pi_1(\mathbb C^2\setminus C)
\xrightarrow{\cong}
\pi_1(S^3\setminus K).
\]
The first arrow is Proposition 4.7. The second is an isomorphism by <1>1. The third is an isomorphism by <1>3. The fourth is an isomorphism by <1>7. The fifth is an isomorphism by <1>8--<1>9.

A composition of isomorphisms is an isomorphism. Since the source and target of the full composite are the same group, the resulting endomorphism of
\[
\pi_1(S^3\setminus K)
\]
is an automorphism.

Consequently all five groups listed in the problem are mutually isomorphic.
:::
:::
