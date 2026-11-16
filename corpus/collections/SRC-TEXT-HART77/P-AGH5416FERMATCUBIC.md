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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    A published attempt located and checked on a third pass over issue #121;
    the exercise stays open on it. Algebraic Geometry II, National Taiwan
    University, 2020 Spring (course of Chin-Lung Wang), Chapter V Surfaces
    homework, Exercise 16 of section 4 (by Po-Sheng Wu), printed pp. 18-19 of
    tmp/sources/ntu-ag2-chapter5.pdf, whose printed folio is the PDF page
    number, read also in its MinerU text version
    tmp/sources/ntu-ag2-chapter5.md, gives the 27 lines as
    x_0 + w^i x_1 = x_2 + w^j x_3 = 0 over the three coordinate pairings, which
    agrees with this card's first step, and describes the automorphism group as
    diag(1, w^i, w^j, w^k) composed with a coordinate permutation, which agrees
    with the group computed below. Three defects: the displayed identity equates
    the two products instead of adding them, the Fermat cubic being
    x_0^3 + x_1^3 + x_2^3 + x_3^3 = 0; it assumes char k != 2 where the lines
    need char k != 3; and the group is computed only among the automorphisms
    induced by Aut(P^3), with no order stated. Its incidence count is right:
    "18 x 3 + 27 x 3 = 27 x 10 / 2" adds 18 x 3 = 54 pairs at its 18 points
    lying on three of the lines to its 27 listed points (1, -w^i, w^j, -w^k)
    and their permutations, which are the 81 points lying on two of the lines,
    one pair each; 54 + 81 = 135 = 27 x 10 / 2. Recomputed here over Q(w): 135
    intersecting pairs, 18 points of multiplicity three and 81 of multiplicity
    two, the 81 being the points with all four coordinates of the form +-w^r
    and exactly two minus signs, of which there are binom(4,2) 3^4 / 6 = 81 --
    no or four minus signs make the sum of the cubes +-4 and one or three make
    it +-2, neither 0 in characteristic not 2. A fourth defect is its list of
    the 18 triple points as (1, w^i, 0, 0) and its permutations, which are not
    on the surface, the sum of their cubes being 2; the triple points are
    (1, -w^i, 0, 0) and its permutations, i = 0,1,2, which is 18 points, and not
    the six of (1, -1, 0, 0). The set
    therefore supplies the explicit lines and the shape of the
    group, not a proof of the incidence relations nor of the group. No card claim
    changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the count of the eighteen triple points on 2026-11-16. The event
    above and the remark both gave them as (1, -1, 0, 0) and its permutations,
    which is six points, not eighteen; the triple points are
    (1, -omega^i, 0, 0) and their permutations for i = 0, 1, 2, eighteen of
    them. The two zero coordinates pick the pair of positions in binom(4,2) = 6
    ways, and the two nonzero entries have cubes summing to zero exactly when
    one is -omega^i times the other, which is three more classes. A point of the
    surface with exactly two zero coordinates lies on the three lines of one
    pairing through it, and one with all four coordinates nonzero lies on at
    most two, so these are exactly the points of multiplicity three, which is
    what the National Taiwan University set's own count 18 x 3 + 27 x 3 =
    27 x 10 / 2 needs: its list of them is wrong only in the sign. The 81 points
    of multiplicity two are unchanged, all four coordinates nonzero with exactly
    two negative cubes.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Under issue #121 the solution is now a transcription, one step per printed
    statement. Read at the printed places: A. Gathmann, Algebraic Geometry,
    Lemma 11.1, printed p. 90, with its proof, for the twenty-seven lines and
    their equations; Corollary 11.2(a),(b), printed pp. 90--91, for the
    incidence relations; I. Dolgachev and A. Duncan, Automorphisms of cubic
    surfaces in positive characteristic, Theorem 1.1 with Table 1, printed
    pp. 3--4, and Lemma 5.1, printed p. 25, for the two answers for the
    automorphism group, with Lemma 5.2 and its Hessian proof, printed p. 25, for
    the characteristic not 2, 3 case and Section 5.1, printed pp. 25--28, for
    the characteristic 2 case; and I. Dolgachev, Topics in Classical Algebraic
    Geometry, Theorem 9.5.7 with Table 9.4, printed pp. 386--387, whose type I is
    the Fermat cubic with group 3^3 : S_4 of order 648, as a second printed
    statement of the characteristic zero answer. Checked against the sources:
    Gathmann's coefficient argument is carried out over C and needs only a
    primitive cube root of unity and 3 not zero, which is why the card states
    char k not 3; Dolgachev--Duncan print at Section 5, p. 24, and at Section 1.3,
    p. 2, that the Fermat cubic is not reduced in characteristic 3 and that the 3C
    stratum is empty there, which is the card's reason for excluding it.
    Dolgachev--Duncan's Lemma 5.2 is printed for a Fermat hypersurface in P^n with
    n at least 4 and displays the group d^(n-1) : S_n; for the Fermat cubic, whose
    ambient space is P^3 with four coordinates, its n is 4 and the displayed
    group is 3^3 : S_4, which is Lemma 5.1's group, and the card says so instead
    of quoting the display for P^3. What this transcription does not keep is the
    card's earlier pair-by-pair congruence criterion for the incidence of the
    three families, which is not printed in the sources; what it keeps is the
    count they prove, ten lines meeting a given one and sixteen skew to it, and
    their count of five lines meeting two given skew lines.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Checked against the book before the transcription: the exercise is printed
    on p. 409 (PDF p. 424) and asks for the equations of the twenty-seven lines,
    a verification of their incidence relations, and the group of
    automorphisms. Checked in Gathmann's Lemma 11.1 that the three displayed
    families are exactly the twenty-seven lines of the Fermat cubic in its
    normalisation, that the count of nine per coordinate pairing is the count of
    pairs of cube roots of minus one, and that the four coefficient equations are
    equivalent to membership. Checked in Dolgachev--Duncan Section 5 that the
    Hermitian form H(x,y) = sum x_i F(y_i) has H(x,x) equal to the Fermat
    equation, which is what puts PSU_4(2) inside the automorphism group in
    characteristic 2, and that the order 25920 and the index two in W(E_6) are
    printed there. Not verified here: the printed page of Gathmann's own numbering
    beyond the two the card cites, since its text version marks only five-page
    blocks; and no second source was found for the incidence count beyond
    Gathmann's.

---

::: {.problem}
For the Fermat cubic surface $x_0^3+x_1^3+x_2^3+x_3^3=0$, find the equations of the 27 lines explicitly, and verify their incidence relations.
What is the group of automorphisms of this surface?
:::

::: {.solution}
Let
$$
S=V(F)\subseteq\PP_k^3,\qquad F=x_0^3+x_1^3+x_2^3+x_3^3,
$$
with $k$ algebraically closed, and let $\omega\in k$ be a primitive cube root of unity.

In characteristic $3$ one has
$$
F=(x_0+x_1+x_2+x_3)^3,
$$
so the displayed scheme is a nonreduced triple plane and not the nonsingular cubic surface to which the $27$-line theory and the automorphism question apply; Dolgachev and Duncan print this at the opening of Section 5, printed p. 24, and record at Section 1.3, printed p. 2, that the $3C$ stratum is empty in characteristic $3$. The transcription below therefore assumes throughout that
$$
\operatorname{char}k\ne3,
$$
and it separates characteristic $2$ from the other characteristics at the automorphism group, which is also what Dolgachev and Duncan's Lemma 5.1 does.

::: pf

::: {.pf-step #twenty-seven-lines}
$S$ contains exactly $27$ lines, namely
$$
x_0+x_3\omega^k=x_1+x_2\omega^j=0,\qquad
x_0+x_2\omega^k=x_3+x_1\omega^j=0,\qquad
x_0+x_1\omega^k=x_3+x_2\omega^j=0,
$$
for $0\le j,k\le2$.

::: pf-proof
This is Lemma 11.1 of Gathmann, printed p. 90, carried out for the ground field $k$; its argument uses only that a primitive cube root of unity exists and that $3\ne0$. Up to a permutation of the coordinates every line of $\PP^3$ is given by two equations
$$
x_0=a_2x_2+a_3x_3,\qquad x_1=b_2x_2+b_3x_3
$$
with $a_2,a_3,b_2,b_3\in k$, and such a line lies in $S$ exactly when
$$
(a_2x_2+a_3x_3)^3+(b_2x_2+b_3x_3)^3+x_2^3+x_3^3=0
$$
as a polynomial in $k[x_2,x_3]$, that is exactly when
$$
a_2^3+b_2^3=-1,\qquad a_3^3+b_3^3=-1,\qquad a_2^2a_3=-b_2^2b_3,\qquad a_2a_3^2=-b_2b_3^2.
$$
If all four of $a_2,a_3,b_2,b_3$ are nonzero, then dividing the square of the third relation by the fourth gives $a_2^3=-b_2^3$, contradicting the first. So at least one is zero, and after renumbering the coordinates one may assume $a_2=0$; then the first relation gives $b_2^3=-1$, the third gives $b_3=0$, and the second gives $a_3^3=-1$. Conversely such values give a line on $S$. With $b_2=-\omega^j$ and $a_3=-\omega^k$, $0\le j,k\le2$, this is the $9$ lines $x_0+x_3\omega^k=x_1+x_2\omega^j=0$ of this coordinate pairing, and allowing the three pairings of the coordinates gives the $27$ displayed lines.
:::

:::

::: {.pf-step #incidence-ten-and-sixteen}
Each line of $S$ meets exactly $10$ of the other $26$ lines and is skew to the remaining $16$.

::: pf-proof
This is Corollary 11.2(a) of Gathmann, printed p. 91, whose proof is the verification: knowing all the lines from step [](#twenty-seven-lines){.pf-ref}, and using that permuting the coordinates and multiplying them by cube roots of unity takes any line of $S$ to any other, one may assume the given line is $L:\ x_0+x_3=x_1+x_2=0$. The lines of $S$ meeting $L$ are then exactly
$$
x_0+x_3\omega^k=x_1+x_2\omega^j=0\quad\text{with } (j,k)=(1,0),(2,0),(0,1),(0,2),
$$
which are $4$, together with
$$
x_0+x_2\omega^j=x_3+x_1\omega^j=0\quad (0\le j\le2),\qquad
x_0+x_1\omega^j=x_3+x_2\omega^j=0\quad (0\le j\le2),
$$
which are $3$ and $3$ more. That is $4+3+3=10$ lines meeting $L$, and $L$ was an arbitrary line of $S$. Since there are $26$ other lines, $16$ of them are skew to $L$.
:::

:::

::: {.pf-step #two-skew-lines-meet-five}
Two skew lines of $S$ are met by exactly $5$ further lines of $S$.

::: pf-proof
This is Corollary 11.2(b) of Gathmann, printed p. 91, whose proof he gives as "analogous" to that of (a): with the $27$ lines known explicitly from step [](#twenty-seven-lines){.pf-ref}, the two given skew lines are carried by a permutation of the coordinates and multiplications by cube roots of unity to a normal form, and the lines meeting both are read off from the list in the same way.
:::

:::

::: {.pf-step #automorphism-group-not-two-three}
If $\operatorname{char}k\ne2,3$, then
$$
\boxed{\Aut(S)\cong3^3\rtimes\Sigma_4,\qquad \cardinality{\Aut(S)}=648.}
$$

::: pf-proof
The statement is Lemma 5.1 of Dolgachev and Duncan, printed p. 25, and the proof they give for this case is Lemma 5.2 with its proof, printed p. 25. Let $Z=V(x_0^d+\cdots+x_n^d)\subseteq\PP^n$ with $d\ge3$ and $p\nmid d(d-1)$; the Hessian hypersurface of $Z$ is
$$
\operatorname{He}(Z)=\left\{(d(d-1))^n x_0^{d-2}\cdots x_n^{d-2}=0\right\},
$$
which is nontrivial under those hypotheses. The Hessian is intrinsic to the projective embedding and not to the choice of coordinates, so a projective automorphism of $Z$ induces one of $\operatorname{He}(Z)$. The automorphisms of the union of the coordinate hyperplanes are generated by permutations of the coordinates and by multiplying coordinates by constants, and for such a transformation to preserve $Z$ those constants must be $d$-th roots of unity. Lemma 5.2 is printed for the Fermat hypersurface in $\PP^n$ with $n\ge4$ and displays the group $d^{n-1}\rtimes\Sigma_n$; for the Fermat cubic, whose ambient space is $\PP^3$ with four coordinates, its $n$ is $4$, so the displayed group is $3^3\rtimes\Sigma_4$, of order $3^3\cdot4!=648$, which is the group of Lemma 5.1. The same group is printed independently by Dolgachev, Theorem 9.5.7 with Table 9.4, printed pp. 386--387, whose type I is the Fermat surface: its proof reads that an automorphism permutes the planes $t_i+\varepsilon t_j=0$ and that $\Aut(S)$ therefore "consists of permutations of the variables and multiplying the variables by cube roots of unity".
:::

:::

::: {.pf-step #automorphism-group-characteristic-two}
If $\operatorname{char}k=2$, then
$$
\boxed{\Aut(S)\cong\operatorname{PSU}_4(2),\qquad \cardinality{\Aut(S)}=25920.}
$$

::: pf-proof
This is the second case of Lemma 5.1 of Dolgachev and Duncan, printed p. 25, proved in Section 5.1, printed pp. 25--28. Let $\varphi\colon\FF_4\to\FF_4$ be the Frobenius automorphism $\varphi(x)=x^2$ and let $H$ be the Hermitian form
$$
H(x,y)=\sum_{i=0}^3x_i\varphi(y_i)
$$
on $\FF_4^4$, nondegenerate of dimension $4$. Its diagonal value is
$$
H(x,x)=x_0^3+x_1^3+x_2^3+x_3^3,
$$
which is the defining equation of $S$, so the projective special unitary group $\operatorname{PSU}_4(2)$ lies in $\Aut(S)$; it has order $25920$ and index $2$ in the Weyl group $W(\mathbf E_6)$. The map
$$
\sigma(x_0:x_1:x_2:x_3)=(\varphi(x_0):\varphi(x_1):\varphi(x_2):\varphi(x_3))
$$
preserves $S(\FF_4)$ in its diagonal form and permutes the $27$ lines preserving their configuration, so $\sigma$ acts as an element of $W(\mathbf E_6)$, and no element of $\operatorname{PSU}_4(2)$ acts in this way: the action of $\sigma$ is not geometric. Hence $\sigma$ and $\operatorname{PSU}_4(2)$ generate all of $W(\mathbf E_6)$.

The source's last step, unpacked: the action on the $27$ lines gives an injection $\Aut(S)\to W(\mathbf E_6)$ (Section 1, printed pp. 3--4), and $\operatorname{PSU}_4(2)$ has index $2$ in $W(\mathbf E_6)$, so a subgroup of $W(\mathbf E_6)$ containing $\operatorname{PSU}_4(2)$ is either $\operatorname{PSU}_4(2)$ itself or all of $W(\mathbf E_6)$. The second alternative would make every element of $W(\mathbf E_6)$ geometric and in particular $\sigma$, which the previous paragraph denies. So $\Aut(S)=\operatorname{PSU}_4(2)$.
:::

:::

::: {.pf-step #characteristic-three}
If $\operatorname{char}k=3$, the equation defines a nonreduced triple plane and the exercise's question has no smooth surface to ask it of.

::: pf-proof
In characteristic $3$ the Frobenius is additive, so $x_0^3+x_1^3+x_2^3+x_3^3=(x_0+x_1+x_2+x_3)^3$. Dolgachev and Duncan record this at the opening of Section 5, printed p. 24, and at Section 1.3, printed p. 2, where Table 1 gives the $3C$ stratum as empty for $\operatorname{char}k=2$ and $\operatorname{char}k=3$ and as $3^3\rtimes\Sigma_4$ of order $648$ for the other characteristics.
:::

:::

::: pf-qed
Step [](#twenty-seven-lines){.pf-ref} gives the equations of the $27$ lines, and steps [](#incidence-ten-and-sixteen){.pf-ref} and [](#two-skew-lines-meet-five){.pf-ref} verify their incidence relations: every line meets exactly $10$ of the other $26$ and is skew to $16$, and two skew lines are met by exactly $5$ further lines. Step [](#automorphism-group-not-two-three){.pf-ref} gives $\Aut(S)\cong3^3\rtimes\Sigma_4$ of order $648$ when $\operatorname{char}k\ne2,3$, and step [](#automorphism-group-characteristic-two){.pf-ref} gives $\Aut(S)\cong\operatorname{PSU}_4(2)$ of order $25920$ when $\operatorname{char}k=2$. In characteristic $3$ the equation is a triple plane, as step [](#characteristic-three){.pf-ref} records, so the smooth cubic surface question does not arise.
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.4, exercise 4.16, printed p. 409, read in `tmp/sources/hartshorne-1977-algebraic-geometry.md`, whose printed page is its marker minus fifteen.

Andreas Gathmann, *Algebraic Geometry* (2014), Chapter 11, read in `tmp/sources/gathmann-2014-alggeom-ch11-27-lines.md`, is the source of the lines and of the incidence count. Lemma 11.1, printed p. 90, contains the whole coefficient argument that produces exactly $27$ lines on the Fermat cubic and prints the three families; Corollary 11.2, printed pp. 90--91, then proves that exactly $10$ other lines meet a given one, working one line out in full after reducing by a coordinate permutation and multiplications by cube roots of unity, and states that the count of $5$ lines through two skew lines is analogous. What Gathmann does not print is a congruence criterion deciding, for each pair of the three families, whether the two lines meet; the incidence relations he verifies are the two counts. His chapter works over $\CC$, which the card's field $k$ replaces with any algebraically closed field of characteristic not $3$, the argument using only a primitive cube root of unity.

Igor V. Dolgachev and Alexander Duncan, *Automorphisms of cubic surfaces in positive characteristic*, read in `tmp/sources/dolgachev-duncan-2017-automorphisms-cubic-surfaces-char-p.md`, gives the automorphism group in every characteristic. Theorem 1.1 with Table 1, printed pp. 3--4, lists the possible groups by stratum: the row $3C$ has $3^3\rtimes\mathfrak S_4$ of order $648$ for $\operatorname{char}k\ne2,3$ and $\operatorname{PSU}_4(2)$ of order $25920$ for $\operatorname{char}k=2$. Lemma 5.1, printed p. 25, states both values for the Fermat cubic itself; Lemma 5.2 with its proof, printed p. 25, is the Hessian argument for the first, and Section 5.1, printed pp. 25--28, is the Hermitian-form and Frobenius argument for the second. The introduction, printed p. 2, records the same two facts in words: the group is generated by permutations and by multiplying coordinates by third roots of unity when $p\ge5$, and is $\operatorname{PSU}_4(2)$ of order $25920$ when $p=2$.

Igor V. Dolgachev, *Topics in Classical Algebraic Geometry*, Theorem 9.5.7 with Table 9.4, printed pp. 386--387, read in `tmp/sources/dolgachev-topics-classical-ag.md`, classifies all automorphism groups of nonsingular cubic surfaces in characteristic zero and lists the Fermat surface as type I with group $3^3:\mathfrak S_4$ of order $648$; his proof of that row is the permutation-of-planes argument quoted at step [](#automorphism-group-not-two-three){.pf-ref}. That duplicates the characteristic-zero half of Dolgachev--Duncan's Lemma 5.1 in a second printed place.

The nearest published attempt at the exercise itself remains Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework, exercise 16 of Section 4 (by Po-Sheng Wu), printed pp. 18--19 of `tmp/sources/ntu-ag2-chapter5.pdf`, whose printed folio is the PDF page number. It gives the $27$ lines as $x_0+\omega^ix_1=x_2+\omega^jx_3=0$ over the three coordinate pairings, which agrees with step [](#twenty-seven-lines){.pf-ref}, and describes the group as $\operatorname{diag}(1,\omega^i,\omega^j,\omega^k)$ composed with a permutation of the coordinates, which agrees with step [](#automorphism-group-not-two-three){.pf-ref}; it states no order, assumes $\operatorname{char}k\ne2$ where the lines need $\operatorname{char}k\ne3$, equates the two products $(x_0+x_1)(x_0+\omega x_1)(x_0+\omega^2x_1)$ and $(x_2+x_3)(x_2+\omega x_3)(x_2+\omega^2x_3)$ where the Fermat cubic is their sum, and lists the $18$ triple points as $(1,\omega^i,0,0)$ and its permutations, which are not on the surface, their cubes summing to $2$ rather than $0$.
:::
