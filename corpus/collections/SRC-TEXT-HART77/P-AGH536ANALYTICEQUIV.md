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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.6, printed page 395, together with Remark 3.9.4 on printed page
    408, where equivalence is defined by matching monoidal transformations,
    multiplicities and incidence of the total transforms. Checked the card's
    forward step against that definition, and recomputed both Tjurina numbers:
    tau(y^3+x^7) = dim k[[x,y]]/(x^6,y^2) = 12, and for y^3+x^5y+x^7 the ideal
    reduces to (y^2+x^5/3, x^4y+7x^6/5, x^7) with standard monomials
    1,x,...,x^6,y,xy,x^2y,x^3y, so tau = 11; the Groebner basis claim was
    checked by hand on the three S-polynomials. Searched outside the twelve
    retained sets: Yang Pi-Yeh, Hartshorne Solutions, exercise 5.3.6, printed
    p. 108 (tmp/sources/lfwin-hartshorne-solutions.pdf), has the completion
    argument and asserts the counterexample without computation; Algebraic
    Geometry II, National Taiwan University, 2020 Spring, has no entry for
    Exercise 6 of section 3. Wall's Singular Points of Plane Curves was searched
    for and is a book, not downloaded; its Puiseux criterion is cited as
    printed. Not checked: the Puiseux characteristic of C_1 and C_2 beyond the
    leading pair (3,7), which the card computes by the implicit-function
    theorem for C_2 and by an explicit parametrization for C_1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The text version of the NTU Chapter V homework now exists: it is read in
    tmp/sources/ntu-ag2-chapter5.pdf and in its MinerU text version
    tmp/sources/ntu-ag2-chapter5.md. The event above predates that file, records
    what was read from the PDF alone, and is left as it was dated.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.6, printed p. 395, and Remark 3.9.4 in the text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md, whose page markers name
    PDF pages: the remark sits between the markers PDF page 408 and PDF page
    409, so printed p. 393, while exercise 3.6 follows the marker PDF page 410,
    printed p. 395. The event of 2026-11-11 above gives 408 for the remark,
    which is its PDF page; the published-solution remark below has been
    corrected to printed p. 393, and that event is left as dated. Recomputed
    both blowup chains, giving the two second strict transforms x+y''^3 and
    x(1+y'')+y''^3, and both Tjurina numbers: 12 from the ideal (x^6,y^2), and
    11 from the Groebner basis y^2+x^5/3, x^4y+7x^6/5, x^7 with standard
    monomials 1,x,...,x^6,y,xy,x^2y,x^3y, whose three S-polynomials reduce to
    zero. Corrected step c1-c2-equivalent: the two point blowups leave the
    strict transform nonsingular but tangent to E_2 with contact order 3, so the
    reduced total transform is not a normal crossing divisor and the two
    sequences are not embedded resolutions; equivalence in the sense of (3.9.4)
    rests instead on the two pairs at the last point being one pair, x = -y^3
    against x = 0, the factor 1+y'' being a unit removed by the coordinate
    change x -> x(1+y''). Corrected the word inequivalence to non-isomorphism in
    the last remark, the two germs being equivalent. Checked Yang Pi-Yeh, text
    version tmp/sources/lfwin-hartshorne-solutions.md, exercise 5.3.6, printed
    p. 108, which gives the forward implication by completion and asserts the
    counterexample with no computation. Also checked that the text version of
    Egbert, tmp/sources/hartshorne-solutions-egbert.md, exercise V.3.6, is the
    citation of Wall recorded on the card. Not checked: Wall's Singular Points
    of Plane Curves, which is not held and is cited as printed; and the National
    Taiwan University Chapter V homework, which has no entry for this exercise.
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
\frac{\partial}{\partial z}(z^3+tz+1)\evalfrom_{(0,-1)}=3\ne0.
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
This is computed, not quoted: two point blowups at the origin and at the
point over it give, for each germ, the same data, so step
[](#puiseux-characteristic-equivalence){.pf-ref} is not needed here.

Both equations have order $3$ with tangent cone $y^3$, so after the blowup of
the origin only the chart $y=xy^{\prime}$ meets the strict transforms, and
there
$$
f_1=y^3+x^7\ \mapsto\ x^3\bigl(y^{\prime 3}+x^4\bigr),
\qquad
f_2=y^3+x^5y+x^7\ \mapsto\ x^3\bigl(y^{\prime 3}+x^3y^{\prime}+x^4\bigr).
$$
Each strict transform has multiplicity $3$ at its point $(0,0)$ on the
exceptional curve $E_1$, and each has tangent cone $y^{\prime 3}$, so the
second blowup is again taken at that one point and again in the chart
$y^{\prime}=xy^{\prime\prime}$:
$$
y^{\prime 3}+x^4\ \mapsto\ x^3\bigl(y^{\prime\prime 3}+x\bigr),
\qquad
y^{\prime 3}+x^3y^{\prime}+x^4\ \mapsto\ x^3\bigl(y^{\prime\prime 3}+xy^{\prime\prime}+x\bigr).
$$
Both second strict transforms are nonsingular at the origin --- the partial
derivative with respect to $x$ is $1$ there in the first case and
$y^{\prime\prime}+1$ in the second --- and each meets the new exceptional curve
$E_2$ in the single point $y^{\prime\prime}=0$ with multiplicity $3$, being
tangent to it. So the reduced total transform is not a divisor with normal
crossings, and these two point blowups, while they do resolve both germs, are
not yet embedded resolutions.

What they do give is one and the same pair at the last point. Read in the chart
$y^{\prime}=xy^{\prime\prime}$ and written as equations in $x$ and
$y^{\prime\prime}$, the second strict transforms are
$$
x+y^{\prime\prime 3}
\qquad\text{and}\qquad
x\,(1+y^{\prime\prime})+y^{\prime\prime 3},
$$
the first for $C_1$ and the second for $C_2$, and the new exceptional curve is
$E_2:x=0$ in both cases. Since $1+y^{\prime\prime}$ is a unit at the origin,
$$
x\longmapsto x\,(1+y^{\prime\prime}),
\qquad
y^{\prime\prime}\longmapsto y^{\prime\prime}
$$
is an automorphism of the affine plane near the origin --- its inverse is
$x\mapsto x/(1+y^{\prime\prime})$ --- which carries the line $x=0$ to itself
and the second equation to the first. Both germs therefore present the same pair
at the last point, $x=-y^{\prime\prime 3}$ against $x=0$.

A monoidal transformation is local: the blowup of a point depends only on the
maximal ideal there, and the strict transform only on the local equations of the
curve and of the exceptional curves. So from that point on the two germs are
blown up at corresponding points, with the same multiplicities and the same
incidence with the exceptional curves already present. Blowing up until the total
transform is a normal crossing divisor therefore gives for the two germs the
same components ($E_1$, $E_2$, the further exceptional curves, one strict
transform of the curve, meeting in the same way), the same multiplicities at the
same centres, the same single branch over the origin, and the same behaviour at
the last step; by (3.9.4) that is equivalence. It is the common pair at the last
point, and not the two displayed blowups on their own, that makes the final
resolution sequences coincide.

The same chain gives the second cross-check: by (3.9.3),
$$
\delta=\binom32+\binom32=6
$$
for both germs, which is $\frac{(3-1)(7-1)}2$, the value the pair $(3,7)$
predicts.
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

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.3, exercise 3.6, printed p. 395, with the definition of equivalence in (3.9.4), printed p. 393, text version `tmp/sources/hartshorne-1977-algebraic-geometry.md` (printed page = its marker minus 15).

Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.3.6, printed p. 108, gives the forward implication through completion: the strict transform's local ring splits as a direct sum of the local rings at the points over $P$, and because completion is flat and commutes with this splitting, the completed local ring determines the resolution, so analytically isomorphic germs are equivalent. It then states "consider two curves $C=(x^3+y^7=0)$ and $C'=(x^3+xy^5+y^7=0)$ over $\CC$; they are equivalent but not analytically isomorphic" with no computation. Steps [](#ambient-automorphism-lift){.pf-ref} and [](#automorphism-identifies-resolution-data){.pf-ref} give the forward implication directly from the Rees-algebra description of the blowup, and steps [](#tjurina-f1-twelve){.pf-ref} and [](#tjurina-f2-eleven){.pf-ref} compute the two Tjurina numbers $12$ and $11$ that separate the germs.

Wall, *Singular Points of Plane Curves* (LMS Student Texts 63), Ch. 3, is the published source of the Puiseux-characteristic criterion of step [](#puiseux-characteristic-equivalence){.pf-ref}: equisingularity of plane branches is equivalent to equality of Puiseux characteristics, and analytic isomorphism preserves them. The book is not in `tmp/sources` and was not read; only that recorded statement is used, not a page. It is no longer needed for the equivalence of $C_1$ and $C_2$: step [](#c1-c2-equivalent){.pf-ref} now computes the two blowup sequences and compares them directly, so the non-isomorphism of the germs is what carries the counterexample and Wall's criterion is background for the standard picture.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.3.6, PDF p. 279: "See Wall's, *Singular Points of Plane Curves* where he proves that analytically isomorphic $\Rightarrow$ same puiseux characteristic $\Rightarrow$ equivalence in the sense of 3.9.4. Furthermore he shows that two curves are equisingular iff they have the same puiseux characteristic. However the example is then given of the two curves $C_1:y^3+x^7=0$ and $C_2:y^3+x^5y+x^7=0$ which are equisingular but not analytically isomorphic." Wall's book is not among the retained files, so both halves are citations; the pair of curves is his. Steps [](#ambient-automorphism-lift){.pf-ref} and [](#automorphism-identifies-resolution-data){.pf-ref} prove the forward implication directly, from the formal coordinate change lifting an analytic isomorphism and the Rees-algebra description of the blowup; the same two curves appear in steps [](#same-puiseux-pair){.pf-ref} and [](#c1-c2-equivalent){.pf-ref}, and the failure of analytic isomorphism that he asserts is step [](#not-analytically-isomorphic){.pf-ref}, by Tjurina numbers $12$ and $11$. Recorded in COMPLAINTS.
:::
