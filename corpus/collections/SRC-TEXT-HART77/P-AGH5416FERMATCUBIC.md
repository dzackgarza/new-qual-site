---
schema: qual/card@1
id: P-AGH5416FERMATCUBIC
kind: problem
title: The 27 lines and the automorphism group of the Fermat cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.16 as transcribed here, the retained Andrew Egbert
    companion calculation, the 27-line configuration in V.4.10--4.11, and
    the anticanonical model of a cubic surface. The companion correctly
    points to the 6+15+6 blowup description but its final "Automorphism
    group? E6" conflates the order-51840 abstract symmetry group of the
    27-line incidence configuration with the automorphism group of the
    Fermat surface itself. The standalone problem also has a characteristic
    issue: in characteristic 3 the equation is a nonreduced triple plane,
    and in characteristic 2 the smooth Fermat cubic has an exceptional,
    larger automorphism group. The solution below gives the 27 lines and
    their incidence relations for characteristic not 3 and computes the full
    automorphism group separately in characteristic 2 and in characteristic
    not 2,3.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read all three 9-line families and solved each pairwise linear system
    independently, confirming the four incidence criteria and the 10-meets,
    16-skew count. Rechecked that the anticanonical system forces every
    surface automorphism to be projective linear. In characteristic not 2,3,
    the Hessian is the coordinate-hyperplane arrangement, forcing a monomial
    stabilizer and hence (mu_3^4/mu_3) semidirect S_4 of order 648. In
    characteristic 2, expanding F(Ax) gives A^(2)T A=cI; scalar
    normalization forces entries into F_4, and the unit-vector count
    120*36*6*3/3 gives the projective unitary order 25920. Characteristic 3
    is explicitly excluded because the equation is a triple plane.
---

::: {.problem}
For the Fermat cubic surface $x_0^3+x_1^3+x_2^3+x_3^3=0$, find the equations of the 27 lines explicitly, and verify their incidence relations.
What is the group of automorphisms of this surface?
:::

::: {.solution}
Let
$$
S=V(F)\subseteq\PP_k^3,
\qquad
F=x_0^3+x_1^3+x_2^3+x_3^3,
$$
with $k$ algebraically closed.

There is one characteristic qualification. If
$$
\operatorname{char}k=3,
$$
then
$$
F=(x_0+x_1+x_2+x_3)^3,
$$
so the displayed scheme is a nonreduced triple plane, not the nonsingular
cubic surface to which the 27-line theory applies. We therefore assume
through step <1>8 that
$$
\operatorname{char}k\ne3.
$$
The automorphism calculation is then separated according as
$\operatorname{char}k=2$ or not.

Choose a primitive cube root of unity
$$
\omega\in k,
\qquad
\omega^3=1,
\qquad
\omega\ne1,
$$
and read all subscripts $a,b,c,d$ below in $\ZZ/3$.

::: pf

::: pf-step
The surface $S$ is nonsingular.

::: pf-proof
Since $\operatorname{char}k\ne3$,
$$
\frac{\partial F}{\partial x_i}=3x_i^2.
$$
All four partial derivatives vanish only when
$$
x_0=x_1=x_2=x_3=0,
$$
which is not a point of projective space. Hence $S$ is nonsingular.
:::

:::

::: {.pf-step #twenty-seven-lines-on-surface}
For $a,b\in\ZZ/3$, define three families of lines
$$
\begin{aligned}
A_{ab}&:
\quad x_0+\omega^a x_1=0,
\qquad
x_2+\omega^b x_3=0,\\
B_{ab}&:
\quad x_0+\omega^a x_2=0,
\qquad
x_1+\omega^b x_3=0,\\
C_{ab}&:
\quad x_0+\omega^a x_3=0,
\qquad
x_1+\omega^b x_2=0.
\end{aligned}
$$
All $27$ of these lines lie on $S$.

::: pf-proof
On $A_{ab}$ one has
$$
x_0=-\omega^a x_1,
\qquad
x_2=-\omega^b x_3.
$$
Therefore
$$
x_0^3+x_1^3
=
-\omega^{3a}x_1^3+x_1^3
=0
$$
and similarly
$$
x_2^3+x_3^3=0.
$$
Thus $F$ vanishes identically on $A_{ab}$. The same calculation, using the
other two pairings of the four coordinates, proves that every $B_{ab}$ and
$C_{ab}$ lies on $S$.
:::

:::

::: {.pf-step #lines-distinct-complete-list}
The $27$ lines in step [](#twenty-seven-lines-on-surface){.pf-ref} are pairwise distinct. Hence they are
exactly all the lines on $S$.

::: pf-proof
Within one family, the two exponents are recovered from the two defining
linear equations, so different pairs $(a,b)$ give different lines.

No $A$-line equals a $B$-line: the point
$$
[-\omega^a:1:0:0]\in A_{ab}
$$
lies on no $B_{cd}$, because the equation
$$
x_0+\omega^c x_2=0
$$
would force its nonzero coordinate $x_0$ to vanish. By symmetry no two
lines from different families coincide.

Thus step [](#twenty-seven-lines-on-surface){.pf-ref} gives $3\cdot3^2=27$ distinct lines. A nonsingular cubic
surface has exactly $27$ lines [[FE-SRFCUBIC]], so these are all of them.
:::

:::

::: {.pf-step #same-family-incidence}
For two distinct lines in the same family,
$$
\boxed{
A_{ab}\cap A_{cd}\ne\varnothing
\iff
a=c\text{ or }b=d,
}
$$
and the identical criterion holds in the $B$- and $C$-families.

::: pf-proof
Suppose first that
$$
a=c,
\qquad
b\ne d.
$$
The two equations involving $x_2,x_3$ then force
$$
x_2=x_3=0,
$$
while the common first equation gives the point
$$
[-\omega^a:1:0:0].
$$
Thus the lines meet. If instead $b=d$ and $a\ne c$, they meet at
$$
[0:0:-\omega^b:1].
$$

If $a\ne c$ and $b\ne d$, the first pair of equations forces
$x_0=x_1=0$ and the second pair forces $x_2=x_3=0$, so there is no
projective point of intersection. The other two families are obtained by
permuting the coordinates.
:::

:::

::: {.pf-step #ab-family-incidence}
Lines from the $A$- and $B$-families satisfy
$$
\boxed{
A_{ab}\cap B_{cd}\ne\varnothing
\iff
a+d\equiv b+c\pmod3.}
$$

::: pf-proof
On a common point we may write, from the equations of $A_{ab}$ and
$B_{cd}$,
$$
x_2=-\omega^b x_3,
\qquad
x_1=-\omega^d x_3.
$$
Then the two expressions for $x_0$ are
$$
x_0
=
-\omega^a x_1
=
\omega^{a+d}x_3
$$
and
$$
x_0
=
-\omega^c x_2
=
\omega^{b+c}x_3.
$$
A nonzero common point therefore exists exactly when
$$
\omega^{a+d}=\omega^{b+c},
$$
which is the displayed congruence. When it holds, taking $x_3=1$ gives the
unique point of intersection.
:::

:::

::: {.pf-step #ac-family-incidence}
Lines from the $A$- and $C$-families satisfy
$$
\boxed{
A_{ab}\cap C_{cd}\ne\varnothing
\iff
c\equiv a+b+d\pmod3.}
$$

::: pf-proof
The equations give
$$
x_2=-\omega^b x_3
$$
and then
$$
x_1=-\omega^d x_2=\omega^{b+d}x_3.
$$
Consequently the $A$-equation gives
$$
x_0=-\omega^{a+b+d}x_3,
$$
whereas the $C$-equation gives
$$
x_0=-\omega^c x_3.
$$
These are compatible exactly under the displayed congruence.
:::

:::

::: {.pf-step #bc-family-incidence}
Lines from the $B$- and $C$-families satisfy
$$
\boxed{
B_{ab}\cap C_{cd}\ne\varnothing
\iff
a+b\equiv c+d\pmod3.}
$$

::: pf-proof
Put $x_2=t$. The $C$-equation gives
$$
x_1=-\omega^d t,
$$
and comparison with
$$
x_1=-\omega^b x_3
$$
gives
$$
x_3=\omega^{d-b}t.
$$
Now
$$
x_0=-\omega^a t
$$
from $B_{ab}$, while $C_{cd}$ gives
$$
x_0
=
-\omega^c x_3
=
-\omega^{c+d-b}t.
$$
Compatibility is therefore equivalent to
$$
a+b\equiv c+d\pmod3.
$$
:::

:::

::: {.pf-step #incidence-count-ten-sixteen}
The formulas in steps [](#same-family-incidence){.pf-ref}, [](#ab-family-incidence){.pf-ref}, [](#ac-family-incidence){.pf-ref} and [](#bc-family-incidence){.pf-ref} give the complete incidence
configuration of the $27$ lines. In particular every line meets exactly
$10$ of the other lines and is skew to the remaining $16$.

::: pf-proof
Fix $A_{ab}$. By step [](#same-family-incidence){.pf-ref} it meets exactly four other $A$-lines: two with
the same first exponent and two with the same second exponent.

For each $c\in\ZZ/3$, step [](#ab-family-incidence){.pf-ref} determines a unique $d$ for which
$A_{ab}$ meets $B_{cd}$. Thus it meets exactly three $B$-lines.
Likewise, for each $d$, step [](#ac-family-incidence){.pf-ref} determines a unique $c$, so it meets
exactly three $C$-lines.

Hence $A_{ab}$ meets
$$
4+3+3=10
$$
other lines. Coordinate symmetry gives the same count for every $B$- and
$C$-line. Since there are $26$ other lines in total, each line is skew to
$16$. The preceding congruences decide every possible pair, so they give the
full incidence relations.
:::

:::

::: {.pf-step #automorphisms-are-projective-linear}
Every automorphism of the smooth cubic surface $S$ is induced by a
projective linear transformation of $\PP^3$.

::: pf-proof
Adjunction for the cubic hypersurface gives
$$
K_S
=
(K_{\PP^3}+S)|_S
=
\OO_S(-1).
$$
Thus
$$
-K_S=\OO_S(1).
$$
Every automorphism of $S$ preserves the canonical class, hence the complete
anticanonical linear system.

The given embedding
$$
S\hookrightarrow\PP^3
$$
is precisely the complete anticanonical embedding: restriction of linear
forms gives
$$
H^0(\PP^3,\OO_{\PP^3}(1))
\xrightarrow{\sim}
H^0(S,\OO_S(1)),
$$
as follows from the cubic hypersurface sequence twisted by $\OO(1)$.
Therefore the action on
$$
H^0(S,-K_S)
$$
extends the automorphism uniquely to an element of $\PGL_4(k)$.

Assume first that
$$
\operatorname{char}k\ne2,3.
$$
:::

:::

::: {.pf-step #automorphism-permutes-hyperplanes}
Any projective linear automorphism preserving $S$ permutes the four
coordinate hyperplanes.

::: pf-proof
Let $A\in\GL_4(k)$ represent a projective automorphism of $S$. Since the
homogeneous ideal of $S$ is generated by the irreducible cubic $F$, there is
$c\in k^\times$ such that
$$
F(Ax)=cF(x).
$$

The Hessian matrix of $F$ is
$$
\operatorname{Hess}(F)
=
\operatorname{diag}(6x_0,6x_1,6x_2,6x_3),
$$
so its determinant is
$$
\operatorname{hess}(F)
=
6^4x_0x_1x_2x_3.
$$
For a linear change of variables, the Hessian matrix transforms by
$$
\operatorname{Hess}(F\circ A)(x)
=
A^T\operatorname{Hess}(F)(Ax)A.
$$
Taking determinants and using $F\circ A=cF$ shows that $A$ preserves the
zero locus of $\operatorname{hess}(F)$.

Because $6\ne0$, that zero locus is exactly
$$
V(x_0x_1x_2x_3)
=
\bigcup_{i=0}^3V(x_i).
$$
Its four irreducible components are the four coordinate hyperplanes.
Therefore $A$ permutes them.
:::

:::

::: {.pf-step #aut-order-648}
If $\operatorname{char}k\ne2,3$, then
$$
\boxed{
\Aut(S)
\cong
(\mu_3^4/\mu_3)\rtimes\Sigma_4
\cong
(\ZZ/3)^3\rtimes\Sigma_4,
}
$$
and hence
$$
\boxed{|\Aut(S)|=27\cdot24=648.}
$$

::: pf-proof
By step [](#automorphism-permutes-hyperplanes){.pf-ref}, a matrix representing an automorphism is monomial: after a
permutation of the coordinates it is diagonal,
$$
\operatorname{diag}(\lambda_0,\lambda_1,\lambda_2,\lambda_3).
$$
The identity
$$
F(Ax)=cF(x)
$$
then says
$$
\lambda_0^3
=
\lambda_1^3
=
\lambda_2^3
=
\lambda_3^3
=
c.
$$
Modulo a common scalar, the four diagonal factors therefore lie in
$\mu_3$, with simultaneous multiplication by the same cube root acting
trivially in projective space. Thus the diagonal subgroup is
$$
\mu_3^4/\mu_3\cong(\ZZ/3)^3.
$$

Conversely, every such diagonal transformation preserves $F=0$, and every
permutation of the four coordinates preserves $F$. Coordinate permutations
normalize the diagonal subgroup, so the full group is the displayed
semidirect product. Its order is
$$
3^3\cdot4!=648.
$$

Now assume
$$
\operatorname{char}k=2.
$$
:::

:::

::: {.pf-step #char-two-unitary-condition}
A projective linear transformation represented by
$A\in\GL_4(k)$ preserves $S$ if and only if, after multiplying $A$ by a
scalar, one has
$$
\boxed{A^{(2)T}A=I,}
$$
and every entry of this normalized matrix lies in $\FF_4$.

::: pf-proof
In characteristic $2$,
$$
F(x)
=
x^{(2)T}x,
$$
where $x^{(2)}$ denotes coordinatewise squaring. Hence
$$
F(Ax)
=
x^{(2)T}A^{(2)T}Ax.
$$
As in step [](#automorphism-permutes-hyperplanes){.pf-ref}, preservation of $S$ is equivalent to
$$
F(Ax)=cF(x)
$$
for some $c\in k^\times$. The monomials $x_i^2x_j$ are linearly
independent, so this equality is equivalent to
$$
A^{(2)T}A=cI.
$$

Choose $t\in k^\times$ with
$$
t^3c=1
$$
and replace $A$ by the projectively equivalent matrix $tA$. We then have
$$
A^{(2)T}A=I.
$$
Transposing gives
$$
A^TA^{(2)}=I,
$$
while squaring the first matrix identity gives
$$
A^{(4)T}A^{(2)}=I.
$$
Comparison yields
$$
A^{(4)T}=A^T,
$$
hence
$$
A^{(4)}=A.
$$
Thus every entry is fixed by the fourth-power Frobenius, so it belongs to
$\FF_4$.

Conversely, every matrix over $\FF_4$ satisfying
$A^{(2)T}A=I$ preserves $F$ exactly.
:::

:::

::: {.pf-step #aut-order-25920-char-two}
In characteristic $2$,
$$
\boxed{
\Aut(S)
\cong
U_4(2)/\mu_3,
}
$$
where
$$
U_4(2)
=
\{A\in\GL_4(\FF_4):A^{(2)T}A=I\}.
$$
Moreover
$$
\boxed{|\Aut(S)|=25920.}
$$

::: pf-proof
Step [](#char-two-unitary-condition){.pf-ref} identifies the normalized linear stabilizer of $F$ with the
finite unitary group $U_4(2)$. Two normalized matrices define the same
projective transformation exactly when they differ by a scalar
$$
\lambda I
$$
with
$$
\lambda^3=1.
$$
These form the central subgroup $\mu_3$, proving the group identification.

It remains to count $U_4(2)$. For the standard Hermitian form
$$
\langle v,w\rangle=v^{(2)T}w
$$
on $\FF_4^n$, every nonzero coordinate $u$ satisfies
$$
u^3=1.
$$
Thus a vector has norm $1$ exactly when it has an odd number of nonzero
coordinates. The numbers of unit vectors in dimensions $1,2,3,4$ are
therefore
$$
\begin{aligned}
N_1&=3,\\
N_2&=\binom21 3=6,\\
N_3&=\binom31 3+\binom33 3^3=36,\\
N_4&=\binom41 3+\binom43 3^3=120.
\end{aligned}
$$

Hermitian Gram--Schmidt shows that $U_n(2)$ acts transitively on unit
vectors, with stabilizer $U_{n-1}(2)$ on the orthogonal complement. Hence
$$
|U_4(2)|
=
N_4N_3N_2N_1
=
120\cdot36\cdot6\cdot3
=
77760.
$$
Dividing by the central subgroup of order $3$ gives
$$
|\Aut(S)|
=
\frac{77760}{3}
=
25920.
$$
:::

:::

::: pf-qed
Steps [](#twenty-seven-lines-on-surface){.pf-ref} and [](#lines-distinct-complete-list){.pf-ref} give the explicit $27$ lines, and steps [](#same-family-incidence){.pf-ref}, [](#ab-family-incidence){.pf-ref}, [](#ac-family-incidence){.pf-ref}, [](#bc-family-incidence){.pf-ref} and [](#incidence-count-ten-sixteen){.pf-ref}
verify all their incidence relations. Step [](#automorphisms-are-projective-linear){.pf-ref} reduces the automorphism
problem to projective linear algebra. Steps [](#automorphism-permutes-hyperplanes){.pf-ref} and [](#aut-order-648){.pf-ref} compute the
classical automorphism group of order $648$ in characteristic different from
$2,3$, while steps [](#char-two-unitary-condition){.pf-ref} and [](#aut-order-25920-char-two){.pf-ref} give the exceptional characteristic-$2$
group of order $25920$. In characteristic $3$ the displayed equation is a
triple plane, as noted at the start, so the smooth-cubic question does not
apply.
:::

:::
:::
