---
schema: qual/card@1
id: P-AGH538INEQUIVSING
kind: problem
title: Multiplicity data of two quadruple-point singularities
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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.8, printed page 395, and checked the falsity of its assertion
    independently: (a) x^4-xy^4 = x(x^3-y^4) has multiplicity 4 and tangent
    cone x^4, and after x = uv, y = v the strict transform is v^4 u(u^3-v),
    which has multiplicity 2 at the origin, so delta = C(4,2)+C(2,2) = 7;
    (b) x^4-x^2y^3-x^2y^5+y^8 has multiplicity 4 and its strict transform
    v^4(u^4-u^2v-u^2v^3+v^4) has multiplicity 3 at the origin, so
    delta = C(4,2)+C(3,2) = 9. Different delta means different configurations of
    infinitely near points with multiplicities, by Example 3.9.3 on printed page
    408. Searched outside the twelve retained sets: NTU 2020, Exercise 8 of
    section 3, PDF p. 13 (tmp/sources/ntu-ag2-chapter5.pdf), obtains delta = 7
    and 9 and then guesses a different equation for (b). Not checked: whether
    the printed (b) was meant to be the guessed x^4-x^2y^2-x^2y^5+y^8; the card
    states the printed equation and proves it.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source says "Show that" the two displayed singularities have matching infinitely near multiplicities and delta invariants but are not equivalent; with these equations the first infinitely near multiplicities are 2 and 3 and the delta invariants are 7 and 9. No corrected equation is known, so the statement now says "Prove or disprove", and the solution disproves the matching claim.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch (issue #121). Re-read the
    printed exercise at V.3.8, printed p. 395, which is PDF p. 410 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where the printed page
    is the marker minus 15, and re-derived both germs by hand: in the chart
    x = uv, y = v the strict transforms are v^4 u(u^3-v) and
    v^4(u^4-u^2v-u^2v^3+v^4), of multiplicity 2 and 3 at the origin, and the
    second germ needs one more blowup, in the two tangent directions v = uw
    and u = vz, before both charts are nonsingular. The mathematics of the
    steps stands and is not changed. Read in their text versions the three
    sets that reach the exercise: the National Taiwan University set,
    Exercise 8 of section 3, text version
    tmp/sources/ntu-ag2-chapter5.md, with (a) on PDF p. 13 and (b) on PDF
    p. 14 of the PDF beside it, which gets delta = 7 and 9 and then guesses a
    different equation for (b); Egbert, Exercise V.3.8, PDF p. 284, text
    version tmp/sources/hartshorne-solutions-egbert.md, who asserts the
    equality of the configurations and counts 3 charts for (a) against 4 for
    (b); and Yang Pi-Yeh, Solution 5.3.8, printed pp. 108-109, text version
    tmp/sources/lfwin-hartshorne-solutions.md, whose own two charts give the
    sequences 4,2 and 4,3 and who then writes "So on these two curves,
    delta_(0,0) are the same" with neither delta computed, which is false for
    the printed equations. The remark now names those text versions, opens
    with the reason no published solution can exist for a false printed
    assertion, and records Yang's entry, which the card did not carry; the
    body gives printed p. 393 where it cites (3.9.4), and Egbert is said to
    reach non-equivalence rather than the falsity of the printed claim. The
    note of 2026-11-11 above gives "Example 3.9.3 on printed page 408"; the
    printed page is 393 and 408 is the PDF page, the marker for which stands
    just above Example 3.9.3. That note is left as written. The note of
    2026-10-29 above had also been rewritten in place; it is restored to the
    text it was dated with, and the sentence that text carries, that the
    statement had been changed to "Prove or disprove", is false of the card:
    the printed "Show that" stands, and the card proves the printed assertion
    false. Not checked:
    whether the printed (b) was meant to be the guessed
    x^4-x^2y^2-x^2y^5+y^8; Egbert's Singular session, which was read only;
    whether Yang's charts resolve the total transform.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed for issue #121 from the two published places that compute the
    exercise's numbers, the exercise itself being false as printed.
    Algebraic Geometry II, National Taiwan University, 2020 Spring, Chapter V
    Surfaces homework solutions, Exercise 8 of §3 (Yi-Heng), PDF p. 13 for (a)
    and PDF p. 14 for (b) of tmp/sources/ntu-ag2-chapter5.pdf, read in the text
    version tmp/sources/ntu-ag2-chapter5.md, whose page markers are coarse so
    the pages were read off the PDF: in its coordinates xy_1=x_1y and its
    chart y_1=1 the first germ becomes x_1^4-x_1y, called a node, hence
    delta = 7, and the second becomes a point of multiplicity 3 whose next
    blowup is nonsingular, hence delta = 9; the steps now quote both. Its
    printed equation for (b) repeats a middle term where the chart requires
    x_1^2y and x_1^2y^3, which the card records while keeping the equation the
    substitution gives. Math StackExchange question 2867504, text version
    tmp/sources/mse-2867504-hart-v38-infinitely-near-points.md, comment 5918658
    by the asker computes the proper transform of the first germ after
    (x,y) -> (xy,y) as x^4-xy with multiplicity 2, and comment 5918691
    withdraws the earlier reply that both proper transforms have multiplicity
    3; those comments are now cited on the steps that establish the
    multiplicity of (a). Left on the card as its own: the two second-blowup
    charts of (b), which the NTU entry asserts non-singular without writing,
    the separation of the two branches of (a), the delta values as binomial
    sums, and the step from two different delta invariants to non-equivalence,
    by (3.9.3) and (3.9.4) of the book on printed p. 393. No published proof of
    the printed assertion can exist, the multiplicity sequences being 4,2 and
    4,3; the record in COMPLAINTS.md states that and names what is published.
    Checked against Hartshorne V.3.8, printed p. 395. Not checked: Egbert's
    Singular session and Yang Pi-Yeh's entry, which the previous pass read and
    which were not re-read this pass; the NTU entry's guessed replacement
    equation, which the card does not adopt; and any printing of these sources
    other than their text versions.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The public statement is repaired under QUAL-01, and the printed text is kept
    here because it is false. Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.8, printed p. 395, reads: "Show that the following two
    singularities have the same multiplicity, and the same configuration of
    infinitely near singular points with the same multiplicities, hence the same
    delta_P, but are not equivalent. (a) x^4 - x y^4 = 0. (b) x^4 - x^2 y^3 -
    x^2 y^5 + y^8 = 0." The claim of the same configuration with the same
    multiplicities, and hence of the same delta_P, fails for the equations
    printed: the multiplicity sequences are 4,2 and 4,3, and delta_0 is 7 and 9,
    as the steps compute and as NTU Exercise 8 of §3 and Stack Exchange comment
    5918658 corroborate. The statement now asks what those equations support: the
    common multiplicity, the two configurations with their multiplicities, the
    two delta invariants, and non-equivalence. The solution's opening sentence no
    longer calls itself the refutation of the exercise, and step claim-false now
    claims the difference of the two invariants and the non-equivalence rather
    than the falsity of a statement the card no longer makes. The rendered
    remark is also reduced to the mathematics and the citations, the sentences
    stating what is or is not published leaving it (QUAL-08).
---

::: {.problem}
Show that the following two singularities have the same multiplicity, compute for each its configuration of infinitely near singular points with their multiplicities and its $\delta_P$, and show that they are not equivalent.

(a) $x^4-x y^4=0$.

(b) $x^4-x^2 y^3-x^2 y^5+y^8=0$.
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

Both germs have multiplicity $4$ at the origin, and their first infinitely near points do not have the same multiplicity: the strict transform of $C_a$ in the chart $x=uv$, $y=v$ is $u^4-uv=u(u^3-v)$, of order $2$, while that of $C_b$ is $u^4-u^2v-u^2v^3+v^4$, whose lowest term is $u^2v$, of order $3$. The two therefore do not have the same configuration of infinitely near singular points with the same multiplicities, and their delta invariants are
$$
\delta_0(C_a)=\binom42+\binom22=7,\qquad
\delta_0(C_b)=\binom42+\binom32=9.
$$
The two multiplicities and the two values of $\delta_0$ are computed in Exercise 8 of §3 of Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework solutions (solution by Yi-Heng), PDF p. 13 for (a) and PDF p. 14 for (b), and the first blowup of (a) is Math StackExchange question 2867504, "Configuration of infinitely near points", comment 5918658. That the two germs are not equivalent is step [](#claim-false){.pf-ref}.

::: pf

::: {.pf-step #same-multiplicity-tangent}
Both singularities have multiplicity $4$ at the origin and the same
unique tangent line
$$
x=0.
$$

::: pf-proof
For both equations the lowest nonzero homogeneous term is
$$
x^4.
$$
Hence both local equations have order $4$ in the maximal ideal $(x,y)$, and
their tangent cone is the quadruple line $x=0$.
:::

:::

::: {.pf-step #a-first-blowup-transform}
Blow up the origin in the chart
$$
x=uv,
\qquad
y=v.
$$
For (a), the strict transform is
$$
\boxed{u(u^3-v)=0}.
$$

::: pf-proof
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

This is the first blowup of Exercise 8 of §3, part (a), PDF p. 13, done there in the coordinates $xy_1=x_1y$ and in the chart $y_1=1$, where the curve is $x_1^4-x_1y$; and it is Math StackExchange comment 5918658, whose substitution $(x,y)\mapsto(xy,y)$ gives $x^4y^4-xy^5$ and the proper transform $x^4-xy$. The letters are the only difference: this card's $u$ is their $x_1$ and its $v$ is their $y$.
:::

:::

::: {.pf-step #a-infinitely-near-mult-two}
The infinitely near point $Q$ of (a) has multiplicity
$$
\boxed{2}.
$$

::: pf-proof
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

Math StackExchange comment 5918658 puts the multiplicity as "the singular point $(0,0)$ has multiplicity $2$" for this proper transform, and Exercise 8 of §3, part (a), PDF p. 13, calls the same curve a node.
:::

:::

::: {.pf-step #a-branches-separate}
After one more blowup at $Q$, the two strict branches of (a) separate,
so there are no further singular points of the strict transform.

::: pf-proof
The tangent directions at $Q$ are distinct. Under the blowup of $Q$, points
of the new exceptional curve parametrize these tangent directions, so the
two branches meet the new exceptional curve at distinct points. Each branch
was already nonsingular before this blowup, hence their strict transforms
remain nonsingular and disjoint. Further blowups may be used to make the
*total* transform simple normal crossings with the older exceptional curve,
but they occur at smooth points of the curve and contribute no further
singular multiplicities.
:::

:::

::: {.pf-step #a-delta-seven}
Therefore
$$
\boxed{\delta_0(C_a)=7}.
$$

::: pf-proof
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

Exercise 8 of §3, part (a), PDF p. 13, prints the value: "which is a node. Thus, $\delta=7$".
:::

:::

::: {.pf-step #b-first-blowup-transform}
Under the same first blowup, the strict transform of (b) is
$$
\boxed{
u^4-u^2v-u^2v^3+v^4=0.}
$$

::: pf-proof
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

This blowup is that of Exercise 8 of §3, part (b), PDF p. 14, in the same coordinates $xy_1=x_1y$ and the chart $y_1=1$. The source prints the strict transform as $x_1^4-x_1^2y^3-x_1^2y^3+y^4$, the middle term being repeated where the chart requires $x_1^2y$ and $x_1^2y^3$; the equation above is the one the substitution gives.
:::

:::

::: {.pf-step #b-infinitely-near-mult-three}
The first infinitely near point of (b) has multiplicity
$$
\boxed{3},
$$
not $2$.

::: pf-proof
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

:::

::: {.pf-step #b-resolves-after-blowup}
Blowing up this multiplicity-$3$ point resolves all singularities of
the strict transform of (b).

::: pf-proof
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

:::

::: {.pf-step #b-delta-nine}
Therefore
$$
\boxed{\delta_0(C_b)=9}.
$$

::: pf-proof
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

Exercise 8 of §3, part (b), PDF p. 14, prints the value: "then the strict transformation is non-singular. Thus, $\delta=9$".
:::

:::

::: {.pf-step #claim-false}
The two singularities have different infinitely near multiplicities and
different $\delta_P$, and they are not equivalent.

::: pf-proof
Both singularities have multiplicity $4$, but their
first infinitely near singular points have different multiplicities:
$$
2\ne3.
$$
Their delta invariants also differ:
$$
7\ne9.
$$
Consequently they do not have the same configuration with the same
multiplicities, and in particular they are not equivalent in the sense of
(3.9.4), printed p. 393: that equivalence preserves multiplicities and incidence at every step, while by (3.9.3), printed p. 393, $\delta_P$ is the sum of $\binom{r_Q}{2}$ over the infinitely near singular points, so the two values $7$ and $9$ separate the germs.
:::

:::

::: pf-qed
Steps [](#same-multiplicity-tangent){.pf-ref}, [](#a-first-blowup-transform){.pf-ref}, [](#a-infinitely-near-mult-two){.pf-ref}, [](#a-branches-separate){.pf-ref} and [](#a-delta-seven){.pf-ref} compute the infinitely near multiplicities and delta
invariant of (a); steps [](#b-first-blowup-transform){.pf-ref}, [](#b-infinitely-near-mult-three){.pf-ref}, [](#b-resolves-after-blowup){.pf-ref} and [](#b-delta-nine){.pf-ref} do the same for (b); step [](#claim-false){.pf-ref} compares them and disproves the assertion.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.3, exercise 3.8, printed p. 395, with (3.9.3) and (3.9.4) on printed p. 393. The printed assertion that the two germs have the same configuration of infinitely near singular points with the same multiplicities, hence the same $\delta_P$, is false: the multiplicity sequences are $4,2$ and $4,3$, with $\delta_0=7$ and $9$.

Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 8 of §3 (solution by Yi-Heng), PDF pp. 13--14, blows up both germs in the coordinates $xy_1=x_1y$. For (a) the chart $y_1=1$ gives $x_1^4-x_1y$, "which is a node. Thus, $\delta=7$". For (b) the same chart gives a point of multiplicity $3$, and after one more blowup the strict transform is nonsingular, "Thus, $\delta=9$". The equation the entry prints for (b) is $x_1^4-x_1^2y^3-x_1^2y^3+y^4$, whose middle term is repeated where the chart requires $x_1^2y$ and $x_1^2y^3$. The entry then adds "I guess the equation in (b) should be $x^4-x^2y^2-x^2y^5+y^8$, then after the first blowing up, it has a cusp. As a result, (a) and (b) is not equivalent while their $\delta$'s are both 7", which replaces the printed equation by a different one and asserts, without computing either, that the two $\delta$'s agree for the replaced pair.

Math StackExchange question 2867504, "Configuration of infinitely near points", is the same observation asked about this exercise. Comment 5918658 by the asker computes the proper transform of the first curve after $(x,y)\mapsto(xy,y)$ as $x^4-xy$, with a singular point of multiplicity $2$, which is step [](#a-first-blowup-transform){.pf-ref} and step [](#a-infinitely-near-mult-two){.pf-ref}; comment 5918691 by Asal Beag Dubh withdraws his earlier reply that both proper transforms have a point of multiplicity $3$.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.3.8, PDF p. 284: "Clearly these two singularities have the same multiplicity by looking at the lowest term (it's 4). The configuration of infinitely near singular points can be seen as in 3.7 ... To see they are not equivalent, note to compute the multiplicity sequence, we use the list `L=resolve(I,1)` command as in 3.7 which gives 3 charts for (a) yet (4) for (b)." He asserts the equality of configurations without computing the sequences; his chart count is three for (a) against four for (b).

Yang Pi-Yeh, *Hartshorne Solutions* (2019), Solution 5.3.8, printed pp. 108--109, its (a) on p. 108 and its (b) on p. 109: in each germ he sets $x=x_1y_1$, $y=y_1$, records the singular point of $x_1^4-x_1y_1$ as of multiplicity $2$ and that of $x_1^4-x_1^2y_1-x_1^2y_1^3+y_1^4$ as of multiplicity $3$, blows up once more, calls the result smooth in (a), where one further blowup is asked for the normal crossings, and nonsingular at the origin in (b), and closes "So on these two curves, $\delta_{(0,0)}$ are the same. But two curves are not equivalent." The sequences his two charts produce are $4,2$ and $4,3$, so the two $\delta$'s are $7$ and $9$, and the equality he states is asserted without either being computed.
:::
