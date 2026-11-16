---
schema: qual/card@1
id: P-AGH4422FAMILYOVERAFFINELINE
kind: problem
title: A family of elliptic curves over $\AA^1_\CC$ with a section is trivial
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.22 together with the preceding torsion and etale-cover
    exercises. Cross-checked that multiplication by 2 is finite etale in
    characteristic zero and that full 2-torsion gives Legendre form. The
    proof also closes the residual quadratic-twist issue after lambda is
    shown constant.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published solution located for this exercise (issue #121). Printed
    exercise read: Hartshorne, Algebraic Geometry (1977), IV.4.22, printed
    p. 340, with the four hint clauses the proof follows. Source: Yang
    Pi-Yeh, Hartshorne Solutions (9 June 2019), Solution 4.4.22, printed
    p. 95 of tmp/sources/lfwin-hartshorne-solutions.pdf, read in its text
    version tmp/sources/lfwin-hartshorne-solutions.md and settled on the
    PDF page where the OCR breaks his formula for S. His argument is steps
    s1--s5 here: the section as origin, the four 2-torsion points as a
    finite etale cover via (II, 9.9) and unramifiedness, four copies of
    A^1 by simple connectivity of A^1_C, the sections T_0, T_1, T_lambda
    giving coordinates, and t -> lambda a constant morphism to
    A^1 - {0,1}. His last sentence, that equal lambda makes the family
    trivial, is a gap: equal fibres do not give a trivial family and
    nothing in his argument excludes a twist over A^1_C; steps s6 and s7
    supply it. Book checks: IV.4.4 and IV.4.5, printed pp. 333--334
    (Legendre form, and the six substitutions that make the parameter well
    defined), IV.4.1, printed pp. 332--333 (isomorphic curves have equal
    j), II.9.9 as he cites it. Not checked: simple connectivity of A^1_C
    in the etale topology is taken from the printed hint, as he does; both
    texts assert the four 2-torsion points of a fibre without computing
    them, and the card's s1 proves it instead.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch. The remark no longer says
    that the source's cover is unramified because its four points are
    distinct: that is the card's reason, and the source writes only
    "obviously unramified". It also no longer presents the source's
    flatness step as complete: (II, 9.9) needs the fibre of psi to have
    length four, and the source shows only that it has four closed points.
    The claim that this card is closed on a published solution is withdrawn
    here and in COMPLAINTS.md; what is located is an outline that follows
    the printed hint to the Legendre parameter, with those two steps
    asserted and with the last step, equal lambda giving a trivial family,
    missing. Checked against the book: IV.4.22 on printed p. 340, IV.4.4 and
    IV.4.5 on printed p. 318, IV.4.1 on printed pp. 317-318, II.9.9. Not
    checked: nothing new; the card's own steps were not re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch. The sentence of the
    remark that the previous pass broke is repaired: that pass left "the
    invertibility of 2. since A^1_C is simply connected", and the text now
    reads as one sentence again. The remark's "s1 supplies both" was too
    strong, and step s1 no longer asserts that [2] on an elliptic scheme is
    finite locally free of degree 4: it counts the four 2-torsion points of
    a complex elliptic curve, uses the differential of [2] for etaleness,
    and gets finiteness from Exercise III.11.2, so the step now proves what
    it claims. The event of 2026-11-16 above, whose note begins "Published
    solution located for this exercise", is restored as it was written and
    is named here. Checked against the book in this pass: IV.4.22 on printed
    p. 340, Exercise III.11.2 on printed p. 280, IV.4.1 and IV.4.4, IV.4.5
    on printed pp. 317-318. Not checked: simple connectivity of A^1_C in the
    etale topology is taken from the printed hint, as the card says.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch, on the audit trail only.
    The event of 2026-11-16 whose note begins "Repairs on the reader's report
    of this batch" is restored as it was written, and this event is appended
    after it rather than put in its place. The sentence and step-s1 repairs of
    the event above stand; the remark on the card records the published
    outline and the two steps it leaves asserted, so the obligation to cite a
    complete published solution stays open, as the remark says. Checked in
    this pass: nothing new; the card's own steps were not re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass, on the audit trail and the rule that a dated event is never
    edited. Two events of 2026-11-16 had been edited in place and are restored
    to their text at their date. (i) The event above whose note begins
    "Published solution located for this exercise" was changed by commit
    2145766034, which replaced "IV.4.4 and IV.4.5, printed pp. 333--334" by
    "printed p. 318" and "IV.4.1, printed pp. 332--333" by "IV.4.1, statement
    on printed pp. 317--318". It is restored as it was written in 114814f0e6,
    and the correction is here: those numbers were the PDF folios of the text
    version, and printed p. N is PDF p. N+15 in it. Verified in this pass in
    tmp/sources/hartshorne-1977-algebraic-geometry.md: Lemma 4.4 and Lemma
    4.5 stand between the markers of PDF pages 332 and 333, so on printed
    pp. 317--318, and the definition of the invariant of IV.4.1 is on the same
    two pages. (ii) The event above whose note begins "Second pass on the
    reader's report of this batch" was extended in place by commit 15a20526df
    with the sentence naming the text version and the offset; it is restored
    as it was written in 1abd969bbb, and that sentence is here: the pages it
    cites were read in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where printed p. N is PDF p. N+15. Checked in this pass: this card's audit
    trail in git, commit by commit, and the pages of the text version named in
    (i). Not checked: no other page was re-read, and no step was re-derived.
---

::: {.problem}
\* If $X \to \AA_{\CC}^1$ is a family of elliptic curves having a section, show that the family is trivial.

Hints: Use the section to fix the group structure on the fibres.
Show that the points of order 2 on the fibres form an étale cover of $\AA_{\CC}^1$, which must be trivial, since $\AA_{\CC}^1$ is simply connected.
This implies that $\lambda$ can be defined on the family, so it gives a map $\AA_{\CC}^1 \to \AA_{\CC}^1-\theset{0,1}$.
Any such map is constant, so $\lambda$ is constant, so the family is trivial.
:::

::: {.solution}
Put
$$
S=\AA^1_{\CC}=\Spec\CC[t],
$$
write
$$
\pi:E\longrightarrow S
$$
for the family, and let
$$
O:S\longrightarrow E
$$
be the given section.

::: pf

::: {.pf-step #s1}

The section $O$ makes $E/S$ an elliptic scheme, and its $2$-torsion
$$
E[2]=\ker[2]
$$
is a finite etale cover of $S$ of degree $4$.

::: pf-proof

The section chooses an origin on every fibre, so the fibrewise elliptic-curve
group laws assemble to the group law on the elliptic scheme $E/S$.

Every fibre is a complex elliptic curve $E_t=\CC/\Lambda_t$, and its points of
order $2$ are the four classes in $\frac12\Lambda_t/\Lambda_t\cong(\ZZ/2)^2$.
Since $2$ is invertible on $S$, the differential of $[2]$ on the relative
tangent line is multiplication by $2$, hence an isomorphism, so
$$
[2]:E\longrightarrow E
$$
is etale; base-changing an etale morphism along the zero section
$O:S\to E$ gives an etale morphism
$$
E[2]\longrightarrow S
$$
whose fibre over $t$ is those four points. The morphism $[2]$ is projective,
and its fibre over a point $y\in E_t$ is the coset $\{x:2x=y\}$ of the
four-point group $E[2]_t$, so it has finite fibres and is therefore finite
(Exercise III.11.2, printed p. 280); a base change of a finite morphism is
finite, so $E[2]\to S$ is finite, and a finite etale morphism is locally free
of degree equal to the number of points in a fibre. Therefore $E[2]\to S$ is
finite etale of degree $4$.

:::

:::

::: {.pf-step #s2}

There are four pairwise disjoint sections
$$
O,T_0,T_1,T_\lambda:S\longrightarrow E
$$
whose images are exactly $E[2]$.

::: pf-proof

The affine line over $\CC$ has no nontrivial connected finite etale covers.
Hence every finite etale cover of $S$ is a disjoint union of copies of $S$.
Applying this to the degree-$4$ cover in step [](#s1){.pf-ref} gives four sections.
One is the zero section $O$; label the other three
$$
T_0,T_1,T_\lambda.
$$
Because $E[2]\to S$ is etale, these components are disjoint.

:::

:::

::: {.pf-step #s3}

The complete linear system
$$
\abs{2O}
$$
defines a finite flat double cover
$$
q:E\longrightarrow\PP^1_S
$$
whose branch sections are exactly the images of
$$
O,T_0,T_1,T_\lambda.
$$
After an automorphism of $\PP^1_S$, the first three branch sections are
$$
\infty,\qquad 0,\qquad 1.
$$

::: pf-proof

On every elliptic fibre $E_s$, the line bundle
$$
\OO_{E_s}(2O_s)
$$
has degree $2$ and two independent sections.  Its complete linear system is
the quotient map by the involution
$$
[-1]:E_s\longrightarrow E_s.
$$
By cohomology and base change, the rank-$2$ bundle
$$
\pi_*\OO_E(2O)
$$
and its fibrewise linear systems give the relative quotient
$$
q:E\longrightarrow\PP\bigl(\pi_*\OO_E(2O)\bigr),
$$
whose restriction to every fibre has degree $2$.  This morphism is proper
and fibrewise finite, hence finite.  The fibrewise flatness criterion then
shows that it is flat.  Thus it is finite flat of degree $2$.

Every vector bundle on
$$
S=\Spec\CC[t]
$$
is free, so the target is isomorphic to $\PP^1_S$.  The fixed points of
$[-1]$ are precisely the points killed by $2$; hence the ramification
sections of $q$ are the four sections in step [](#s2){.pf-ref}, and their images are the
four branch sections.

It remains to normalize three branch sections globally.  Since
$\Pic(S)=0$, each section of $\PP^1_S$ can be represented by a unimodular
column vector in $\CC[t]^2$.  Choose vectors $v_\infty,v_0$ representing
the images of $O,T_0$.  Their sections are disjoint, so
$$
\det(v_\infty,v_0)
$$
vanishes nowhere on $S$ and hence is a unit of $\CC[t]$.  Thus the matrix
with columns $v_\infty,v_0$ lies in $\GL_2(\CC[t])$.  Its inverse gives
an automorphism of $\PP^1_S$ carrying these two sections to
$$
\infty=[1:0],
\qquad
0=[0:1].
$$

Write the image of $T_1$ in these coordinates as $[a:b]$.  Disjointness
from $\infty$ and $0$ says respectively that $b$ and $a$ vanish nowhere,
so
$$
a,b\in\CC[t]^*=\CC^*.
$$
A diagonal automorphism preserving $\infty$ and $0$ now carries $[a:b]$
to
$$
1=[1:1].
$$
This gives the required global normalization.

:::

:::

::: {.pf-step #s4}

The fourth branch section defines a morphism
$$
\boxed{
\lambda:S\longrightarrow\AA^1_{\CC}\setminus\{0,1\}.
}
$$

::: pf-proof

In the coordinate fixed in step [](#s3){.pf-ref}, write the fourth branch section as
$$
x=\lambda.
$$
It is disjoint from the section at infinity, so it takes values in the
affine chart $\AA^1_S$.  It is also disjoint from the branch sections
$x=0$ and $x=1$.  Therefore its coordinate is a regular function
$$
\lambda\in\Gamma(S,\OO_S)=\CC[t]
$$
such that neither $\lambda$ nor $\lambda-1$ vanishes anywhere on $S$.
Equivalently, it is the displayed morphism.

:::

:::

::: {.pf-step #s5}

The function $\lambda$ is constant.

::: pf-proof

Since the map in step [](#s4){.pf-ref} avoids $0$ and $1$, both
$$
\lambda
\qquad\text{and}\qquad
\lambda-1
$$
are units of $\CC[t]$.  But
$$
\CC[t]^*=\CC^*.
$$
Hence $\lambda\in\CC\setminus\{0,1\}$ is constant.

:::

:::

::: {.pf-step #s6}

The double cover $q$ is the product over $S$ of the Legendre double
cover
$$
E_\lambda:
y^2=x(x-1)(x-\lambda)
\longrightarrow
\PP^1_{\CC}.
$$

::: pf-proof

By step [](#s5){.pf-ref} the branch divisor on $\PP^1_S$ is the constant divisor
$$
B
=
\{0\}+\{1\}+\{\lambda\}+\{\infty\}.
$$
Because $2$ is invertible, the finite flat double cover has the trace
decomposition
$$
q_*\OO_E
\cong
\OO_{\PP^1_S}\oplus\mcl^{-1},
$$
where multiplication on the trace-zero summand is specified by a section
$$
s\in H^0(\PP^1_S,\mcl^{\tensor2})
$$
whose zero divisor is $B$.

The branch divisor has relative degree $4$, so
$$
\mcl^{\tensor2}\cong\OO_{\PP^1_S}(4).
$$
Moreover
$$
\Pic(S)=0
$$
and
$$
\Pic(\PP^1_S)\cong\ZZ,
$$
generated by $\OO(1)$.  Hence
$$
\mcl\cong\OO_{\PP^1_S}(2).
$$

In homogeneous coordinates $[X:Z]$, the standard section
$$
s_0=XZ(X-Z)(X-\lambda Z)
$$
of $\OO(4)$ has zero divisor $B$.  The sections $s$ and $s_0$ have the same
zero divisor, so their quotient is a global unit on $\PP^1_S$.  Such a unit
comes from
$$
\CC[t]^*=\CC^*.
$$
Thus
$$
s=c\,s_0
$$
for some $c\in\CC^*$.  Since $\CC$ is algebraically closed, write
$$
c=u^2.
$$
Rescaling the trace-zero generator by $u$ identifies the two double-cover
algebras.  Therefore
$$
E\cong E_\lambda\times_{\Spec\CC}S
$$
over $S$, with the given zero section corresponding to the point at
infinity.

:::

:::

::: {.pf-step #s7}

The family $E\to\AA^1_{\CC}$ is trivial.

::: pf-proof

Step [](#s6){.pf-ref} gives an isomorphism of elliptic schemes
$$
\boxed{
E\cong E_\lambda\times\AA^1_{\CC}
}
$$
over the base.  This is precisely the required trivialization.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} trivialize the relative $2$-torsion, steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}
produce Hartshorne's Legendre parameter and show it is constant, and steps
[](#s6){.pf-ref} and [](#s7){.pf-ref} show that no residual quadratic twist remains.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.22, printed p. 95 of `tmp/sources/lfwin-hartshorne-solutions.pdf`, text version `tmp/sources/lfwin-hartshorne-solutions.md`, executes the printed hint on p. 340 in the order of steps [](#s1){.pf-ref} to [](#s5){.pf-ref}: the section makes every fibre an elliptic curve with origin $s_0(t)$; the union of the subgroups $\ker 2_{X_t}$ has four closed points over each $t$, is flat over $\AA^1_\CC$ by (II, 9.9), and he writes that it is "obviously unramified", hence finite étale of degree four. Both of those steps are asserted rather than proved: (II, 9.9) needs the fibre of $\psi$ to have length four, and what he checks is that it has four closed points, and for the unramifiedness he gives no argument that the four points are distinct with no ramification along them. The card's step [](#s1){.pf-ref} supplies that argument, from the count of the four $2$-torsion points of a complex elliptic curve and the differential of $[2]$, which is multiplication by $2$ and hence invertible on each fibre; since $\AA^1_\CC$ is simply connected it is four copies of $\AA^1_\CC$, one of them $s_0$ and the others $s_1,s_2,s_3$, and on each fibre the coordinates $s_0(t)=\infty$, $s_1(t)=0$, $s_2(t)=1$, $s_3(t)=\lambda$ make $t\mapsto\lambda$ a morphism $\AA^1_\CC\to\AA^1_\CC\setminus\{0,1\}$, which is constant. His argument then stops short of the exercise: from the constancy of $\lambda$ he concludes that "all $X_t$ are isomorphic to each other, i.e. the family is trivial", and isomorphism of the fibres is not triviality of the family, a twist of the Legendre curve over $\AA^1_\CC$ being invisible in the fibres. Steps [](#s6){.pf-ref} and [](#s7){.pf-ref} close that step through the trace decomposition of the double cover and $\Pic(\AA^1_\CC)=0$. What the source therefore supplies is the printed outline, followed to the Legendre parameter, with the two steps above left as assertions; the completion is the card's, and the card is not closed on a published solution. Checked against the book: Lemma IV.4.4 and Lemma IV.4.5, printed p. 318, are what make every elliptic curve with a degree-two map to $\PP^1$ Legendre and the parameter well defined up to the six substitutions of 4.5, and Theorem IV.4.1, statement on printed pp. 317--318, is the statement that isomorphic elliptic curves have equal $j$, the book's form of the conclusion the hint asks for.
:::
