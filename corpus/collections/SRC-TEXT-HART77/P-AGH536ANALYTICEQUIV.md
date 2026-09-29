---
schema: qual/card@1
id: P-AGH536ANALYTICEQUIV
kind: problem
title: Analytic isomorphism of curve singularities versus equivalence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.6, the retained Egbert companion note, the earlier
    analytic-isomorphism exercise, and the local plane-singularity material.
    The retained source cites Wall for the equivalence between the Puiseux
    resolution data and Hartshorne's V.3.9.4 equivalence, and gives the
    standard counterexample y^3+x^7 and y^3+x^5 y+x^7. The forward
    implication is made intrinsic below by lifting an isomorphism of complete
    plane-curve local rings to a formal ambient automorphism and iterating
    blowups. For the counterexample, both branches have the single Puiseux
    pair (3,7), while their Tjurina numbers are 12 and 11.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Show that analytically isomorphic curve singularities (I, 5.6.1) are equivalent in the sense of (3.9.4), but not conversely.
:::

::: {.solution}
We first prove the forward implication for plane curve germs.  For the
counterexample to the converse we work over a field of characteristic zero,
for example $k=\CC$.

::: pf

::: {.pf-step #ambient-automorphism-lift}
Let
$$
A_f=k[[x,y]]/(f),
\qquad
A_g=k[[x,y]]/(g)
$$
be two singular plane-curve complete local rings. Any analytic isomorphism
$$
A_f\xrightarrow{\sim}A_g
$$
lifts to an automorphism
$$
\Phi:k[[x,y]]\xrightarrow{\sim}k[[x,y]]
$$
such that
$$
\Phi(f)=u g
$$
for a unit $u\in k[[x,y]]^\times$.

::: pf-proof
An analytic isomorphism is, by (I, 5.6.1), an isomorphism of completed local
rings. Choose lifts $X,Y\in k[[x,y]]$ of the images of the residue classes
of $x,y$ under the isomorphism. Since the induced map on cotangent spaces
$$
\mathfrak m_f/\mathfrak m_f^2
\longrightarrow
\mathfrak m_g/\mathfrak m_g^2
$$
is an isomorphism, the linear parts of $X,Y$ are linearly independent.
The formal inverse-function theorem therefore makes
$$
x\longmapsto X,
\qquad
y\longmapsto Y
$$
an automorphism $\Phi$ of $k[[x,y]]$ lifting the given quotient-ring
isomorphism.

The kernel of the quotient map to $A_f$ is the principal ideal $(f)$, and
the kernel on the other side is $(g)$. Hence
$$
\Phi((f))=(g).
$$
Two generators of the same principal ideal in the domain $k[[x,y]]$ differ
by a unit, so
$$
\Phi(f)=ug.
$$
:::

:::

::: {.pf-step #automorphism-identifies-resolution-data}
A formal ambient automorphism as in step [](#ambient-automorphism-lift){.pf-ref} identifies the complete
embedded resolution data obtained by successive point blowups.

::: pf-proof
The automorphism $\Phi$ carries the maximal ideal $(x,y)$ to itself and
identifies the two curve ideals. The blowup of the closed point is the
Proj of the Rees algebra of this maximal ideal. Therefore $\Phi$ induces an
isomorphism of the two formal blowups carrying exceptional divisor to
exceptional divisor and strict transform to strict transform.

At every point where a further blowup is required, the induced isomorphism
of completed local rings again identifies the maximal ideals and the strict
transform ideals. Applying the same Rees-algebra construction recursively
identifies the next blowups. Thus the entire sequence of infinitely near
points, exceptional components, branch incidences, proximity relations, and
multiplicities is preserved.

This is precisely the embedded-resolution data entering equivalence in
(3.9.4). Hence analytically isomorphic curve singularities are equivalent.
:::

:::

::: {.pf-step #puiseux-characteristic-equivalence}
Equivalently, in characteristic zero analytic isomorphism preserves
the Puiseux characteristic, and equal Puiseux characteristic gives the same
equivalence class in (3.9.4).

::: pf-proof
This is the standard Puiseux-resolution theorem cited by the retained source
for V.3.6 (Wall, *Singular Points of Plane Curves*). The characteristic
exponents of each branch, together with pairwise contact data, determine the
successive point-blowup resolution data, and conversely that resolution data
recovers the Puiseux characteristics. Step [](#automorphism-identifies-resolution-data){.pf-ref} gives the forward statement
without needing this classification theorem; we record it here because it
will identify the counterexample below as equivalent.
:::

:::

::: {.pf-step #same-puiseux-pair}
Consider over $k=\CC$ the two irreducible plane-curve germs
$$
C_1:\quad f_1=y^3+x^7=0,
$$
and
$$
C_2:\quad f_2=y^3+x^5y+x^7=0.
$$
Both have the single Puiseux pair
$$
\boxed{(3,7)}.
$$

::: pf-proof
For $C_1$ there is the parametrization
$$
x=t^3,
\qquad
y=-t^7,
$$
so its unique branch has characteristic pair $(3,7)$.

For $C_2$, substitute
$$
x=t^3,
\qquad
y=t^7z(t).
$$
The equation becomes
$$
t^{21}\bigl(z^3+tz+1\bigr)=0.
$$
At $t=0$, the equation $z^3+1=0$ has the root $z=-1$, and
$$
\frac{\partial}{\partial z}(z^3+tz+1)\bigg|_{(0,-1)}=3\ne0.
$$
The formal implicit-function theorem therefore gives a unique
$z(t)\in\CC[[t]]$ with
$$
z(0)=-1,
\qquad
z(t)^3+t z(t)+1=0.
$$
Hence
$$
x=t^3,
\qquad
y=-t^7+\text{higher-order terms}.
$$
Since $\gcd(3,7)=1$, the gcd of the characteristic exponents has already
dropped to $1$ at exponent $7$, so there are no further Puiseux pairs.
The other two choices of the cube root of $-1$ give the same branch after
the reparametrizations $t\mapsto\zeta t$ with $\zeta^3=1$. Thus $C_2$ is
irreducible and also has Puiseux pair $(3,7)$.
:::

:::

::: {.pf-step #c1-c2-equivalent}
The singularities $C_1$ and $C_2$ are equivalent in the sense of
(3.9.4).

::: pf-proof
By step [](#same-puiseux-pair){.pf-ref}, they have identical Puiseux characteristic. The
Puiseux-resolution theorem of step [](#puiseux-characteristic-equivalence){.pf-ref} therefore gives identical embedded
resolution data, hence equivalence in the sense of (3.9.4).
:::

:::

::: {.pf-step #tjurina-number-invariant}
For a plane hypersurface germ $f=0$, put
$$
\tau(f)
=
\dim_k
\frac{k[[x,y]]}{(f,f_x,f_y)}.
$$
The Tjurina number $\tau(f)$ is invariant under analytic isomorphism of the
curve germ.

::: pf-proof
By step [](#ambient-automorphism-lift){.pf-ref}, an analytic isomorphism is induced by a formal coordinate
automorphism $\Phi$ together with multiplication of the equation by a unit:
$$
\Phi(f)=ug.
$$

The chain rule says that the two partial derivatives of $\Phi(f)$ are
invertible $k[[x,y]]$-linear combinations of $\Phi(f_x),\Phi(f_y)$, because
the Jacobian matrix of a formal coordinate automorphism is invertible.
Thus $\Phi$ carries
$$
(f,f_x,f_y)
$$
to the Tjurina ideal of $\Phi(f)$.

On the other hand,
$$
(ug,(ug)_x,(ug)_y)
=
(ug,u g_x+u_xg,u g_y+u_yg)
=
(g,g_x,g_y),
$$
because $u$ is a unit. Hence the two Tjurina algebras are isomorphic and
have the same dimension.
:::

:::

::: {.pf-step #tjurina-f1-twelve}
The first germ has
$$
\boxed{\tau(f_1)=12}.
$$

::: pf-proof
Since
$$
(f_1)_x=7x^6,
\qquad
(f_1)_y=3y^2,
$$
and the coefficients $3,7$ are units over $\CC$, one has
$$
(f_1,(f_1)_x,(f_1)_y)=(x^6,y^2).
$$
Therefore the residue classes
$$
x^i y^j,
\qquad
0\le i\le5,
\quad
0\le j\le1,
$$
form a basis of the Tjurina algebra. There are $6\cdot2=12$ such monomials.
:::

:::

::: {.pf-step #tjurina-f2-eleven}
The second germ has
$$
\boxed{\tau(f_2)=11}.
$$

::: pf-proof
The derivatives are
$$
(f_2)_x=5x^4y+7x^6,
\qquad
(f_2)_y=3y^2+x^5.
$$
Modulo the Tjurina ideal, therefore,
$$
y^2=-\frac13x^5,
\qquad
x^4y=-\frac75x^6.
$$
Using the first relation in $f_2=0$ gives
$$
2x^5y+3x^7=0,
$$
while multiplying $(f_2)_x=0$ by $x$ gives
$$
5x^5y+7x^7=0.
$$
The coefficient matrix
$$
\begin{pmatrix}2&3\\5&7\end{pmatrix}
$$
has determinant $-1$, so
$$
x^5y=x^7=0.
$$
Consequently the Tjurina ideal is generated by
$$
y^2+\frac13x^5,
\qquad
x^4y+\frac75x^6,
\qquad
x^7.
$$
For lexicographic order with $y>x$, these three generators have leading
terms
$$
y^2,
\qquad
x^4y,
\qquad
x^7,
$$
and their three $S$-polynomials reduce to zero using these same relations.
They are therefore a Gröbner basis. Hence the standard monomials are
$$
1,x,\ldots,x^6,
\qquad
y,xy,x^2y,x^3y.
$$
There are $7+4=11$ of them.
:::

:::

::: {.pf-step #not-analytically-isomorphic}
The equivalent singularities $C_1$ and $C_2$ are not analytically
isomorphic.

::: pf-proof
If they were analytically isomorphic, step [](#tjurina-number-invariant){.pf-ref} would give
$$
\tau(f_1)=\tau(f_2).
$$
But steps [](#tjurina-f1-twelve){.pf-ref} and [](#tjurina-f2-eleven){.pf-ref} give
$$
12\ne11.
$$
Thus the germs are not analytically isomorphic. Together with step [](#c1-c2-equivalent){.pf-ref},
this proves that equivalence in the sense of (3.9.4) does not imply analytic
isomorphism.
:::

:::

::: pf-qed
Steps [](#ambient-automorphism-lift){.pf-ref} and [](#automorphism-identifies-resolution-data){.pf-ref} prove that analytic isomorphism implies equivalence.
Steps [](#same-puiseux-pair){.pf-ref}, [](#c1-c2-equivalent){.pf-ref}, [](#tjurina-number-invariant){.pf-ref}, [](#tjurina-f1-twelve){.pf-ref}, [](#tjurina-f2-eleven){.pf-ref} and [](#not-analytically-isomorphic){.pf-ref} give two equivalent singularities which are not analytically
isomorphic, proving that the converse fails.
:::

:::
:::
