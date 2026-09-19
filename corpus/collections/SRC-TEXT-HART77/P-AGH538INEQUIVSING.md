---
schema: qual/card@1
id: P-AGH538INEQUIVSING
kind: problem
title: Inequivalent singularities with matching multiplicity data
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
    Read Hartshorne V.3.8 as transcribed in the card and the retained Egbert
    companion note, then checked the blowups directly. The statement is false
    with the displayed second equation: after the first blowup the strict
    transform of (a) has multiplicity 2, while that of (b) has multiplicity
    3. Their delta invariants are consequently 7 and 9. The card has carried
    this equation unchanged since import, and no retained Hartshorne solution
    or algebraic-geometry note in the repository supplies a different literal
    equation, so no conjectural replacement is made here.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Show that the following two singularities have the same multiplicity, and the same configuration of infinitely near singular points with the same multiplicities, hence the same $\delta_P$, but are not equivalent.

a. $x^4-x y^4=0$.

b. $x^4-x^2 y^3-x^2 y^5+y^8=0$.
:::

::: {.remark title="Erratum"}
As transcribed, the two displayed singularities do **not** have the same
multiplicities at their infinitely near singular points. After blowing up
the origin in their common tangent direction, (a) has multiplicity $2$ and
(b) has multiplicity $3$. In fact their delta invariants are $7$ and $9$.
Thus the claimed example cannot be proved with the equations printed above.
The computation is given below so that the defect is explicit rather than
silently repaired to an unverified equation.
:::

::: {.solution}
Write
$$
C_a:\quad f=x^4-xy^4=0
$$
and
$$
C_b:\quad g=x^4-x^2y^3-x^2y^5+y^8=0.
$$

<1>1. Both singularities have multiplicity $4$ at the origin and the same
unique tangent line
$$
x=0.
$$

::: {.proof}
For both equations the lowest nonzero homogeneous term is
$$
x^4.
$$
Hence both local equations have order $4$ in the maximal ideal $(x,y)$, and
their tangent cone is the quadruple line $x=0$.
:::

<1>2. Blow up the origin in the chart
$$
x=uv,
\qquad
y=v.
$$
For (a), the strict transform is
$$
\boxed{u(u^3-v)=0}.
$$

::: {.proof}
Substitution gives
$$
x^4-xy^4
=
u^4v^4-uv^5
=
v^4u(u^3-v).
$$
After removing the exceptional factor $v^4$, the strict transform is as
displayed. Its unique point on the exceptional curve $E_1:(v=0)$ is
$$
Q=(u,v)=(0,0).
$$
:::

<1>3. The infinitely near point $Q$ of (a) has multiplicity
$$
\boxed{2}.
$$

::: {.proof}
The strict-transform equation is
$$
u^4-uv.
$$
Its lowest nonzero homogeneous term is
$$
-uv,
$$
of degree $2$. Thus
$$
\mu_Q(C_{a,1})=2.
$$
The two strict branches are already smooth at $Q$: they are the line
$u=0$ and the branch $v=u^3$, with distinct tangent directions $u=0$ and
$v=0$.
:::

<1>4. After one more blowup at $Q$, the two strict branches of (a) separate,
so there are no further singular points of the strict transform.

::: {.proof}
The tangent directions at $Q$ are distinct. Under the blowup of $Q$, points
of the new exceptional curve parametrize these tangent directions, so the
two branches meet the new exceptional curve at distinct points. Each branch
was already nonsingular before this blowup, hence their strict transforms
remain nonsingular and disjoint. Further blowups may be used to make the
*total* transform simple normal crossings with the older exceptional curve,
but they occur at smooth points of the curve and contribute no further
singular multiplicities.
:::

<1>5. Therefore
$$
\boxed{\delta_0(C_a)=7}.
$$

::: {.proof}
By the multiplicity formula [[D-CRVPLSING]], the only singular strict
transform multiplicities are
$$
4,2.
$$
Hence
$$
\delta_0(C_a)
=
\binom42+\binom22
=
6+1
=7.
$$
:::

<1>6. Under the same first blowup, the strict transform of (b) is
$$
\boxed{
u^4-u^2v-u^2v^3+v^4=0.}
$$

::: {.proof}
Substitution gives
$$
\begin{aligned}
g(uv,v)
&=u^4v^4-u^2v^5-u^2v^7+v^8\\
&=v^4\bigl(u^4-u^2v-u^2v^3+v^4\bigr).
\end{aligned}
$$
Removing the exceptional factor $v^4$ gives the displayed strict transform.
On $E_1:(v=0)$ its equation is $u^4=0$, so again its unique point over the
origin is $Q=(0,0)$.
:::

<1>7. The first infinitely near point of (b) has multiplicity
$$
\boxed{3},
$$
not $2$.

::: {.proof}
At $(u,v)=(0,0)$ the lowest-degree nonzero term of
$$
u^4-u^2v-u^2v^3+v^4
$$
is
$$
-u^2v,
$$
of total degree $3$. Thus
$$
\mu_Q(C_{b,1})=3.
$$
This already contradicts the assertion that the two singularities have the
same infinitely near multiplicities.
:::

<1>8. Blowing up this multiplicity-$3$ point resolves all singularities of
the strict transform of (b).

::: {.proof}
The tangent cone at $Q$ is
$$
u^2v=0,
$$
with tangent directions $v=0$ and $u=0$.

For the direction $v=0$, use $v=uw$. Substitution into the strict-transform
equation gives, after removing the exceptional factor $u^3$,
$$
u-w-u^2w^3+uw^4=0.
$$
At $(u,w)=(0,0)$ this is nonsingular because its linear part is $u-w$.

For the direction $u=0$, use $u=vz$. After removing $v^3$ one obtains
$$
vz^4-z^2-v^2z^2+v=0.
$$
At $(v,z)=(0,0)$ this is nonsingular because its linear part is $v$.

These are the two points of the new exceptional divisor determined by the
two tangent directions. Thus the strict transform has no singular point
after this second blowup.
:::

<1>9. Therefore
$$
\boxed{\delta_0(C_b)=9}.
$$

::: {.proof}
The singular multiplicities encountered are
$$
4,3.
$$
Hence [[D-CRVPLSING]] gives
$$
\delta_0(C_b)
=
\binom42+\binom32
=
6+3
=9.
$$
:::

<1>10. The transcribed claim of V.3.8 is therefore false.

::: {.proof}
Although the two original singularities both have multiplicity $4$, their
first infinitely near singular points have different multiplicities:
$$
2\ne3.
$$
Their delta invariants also differ:
$$
7\ne9.
$$
Consequently they cannot have the same configuration with the same
multiplicities, and in particular they are not equivalent in the sense of
(3.9.4). The final inequivalence assertion is true, but the stronger claimed
matching of resolution data is not true for the equations transcribed on
this card.
:::

<1>11. Q.E.D. for the transcribed statement: the displayed equations give a
countercalculation to its claimed matching data.

::: {.proof}
Steps <1>1--<1>5 compute the infinitely near multiplicities and delta
invariant of (a); steps <1>6--<1>9 do the same for (b); step <1>10 exhibits
the contradiction to the source claim.
:::
:::
