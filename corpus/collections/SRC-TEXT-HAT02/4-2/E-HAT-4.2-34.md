---
schema: qual/card@1
id: E-HAT-4.2-34
kind: problem
title: "Hopf bundle composed with torus collapse"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 34; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 34 (AT.txt 19481-19484). One false intermediate
    assertion, replaced: the card said the map C_p -> C_f "is an isomorphism in degree 2", which is
    impossible. Since f_* = 0 on H_2, the cofiber sequence T^3 -> S^2 -> C_f gives the split exact
    sequence 0 -> H_2(S^2) -> H_2(C_f) -> H_1(T^3) -> 0, so H_2(C_f;Z) = Z^4 and H_1(C_f;Z) = 0,
    hence H^2(C_f;Z) = Z^4 while H^2(C_p;Z) = Z; the map is injective, which is all the argument
    needs, and the card now says so and records the computation. Nothing downstream changes: the
    degree-4 step is an isomorphism because the suspension of q has degree 1, so x-bar^2 != 0, and the
    nullhomotopy contradiction from C_f = S^2 v Sigma T^3 stands. Also verified: q_* = 0 on reduced
    homology and pi_*(T^3) = 0 above degree 1. Not checked: nothing outside this exercise.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Checked against Hatcher, Section 4.2 Exercise 34, printed
    p. 392 (PDF p. 401, whose running folio reads 392). Each step re-read: q collapses a ball and
    has degree 1; pi_i(T^3) = 0 above degree 1 and pi_1(S^2) = 0, so pq is zero on pi_*; q is zero
    on H_1 and H_2 for want of targets and p is zero on H_3, so pq is zero on reduced homology; the
    square induces a map of mapping cones restricting to the identity on the S^2 summand; C_p is
    CP^2 with a generator of square a generator in degree 4; phi^* is injective in degree 2, proved
    by composing with the isomorphism H^2(C_f) -> H^2(S^2); it is an isomorphism in degree 4 by the
    degree 1 suspension of q; hence x-bar squared is nonzero; and if f were null the cone would be
    S^2 v Sigma T^3, where every degree 2 class has zero square. The earlier account of H_2(C_f) as
    Z^4 and H_1(C_f) = 0, put in by the 2026-11-01 repair, is kept and is what makes the degree 2
    injectivity work. Not claimed: any statement about the homotopy class of pq beyond its not being
    constant.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 34. The proof reads correct. One provenance correction: the
    solution said that no retained set covers the exercise, and the retained sets' actual coverage is
    now recorded — Sam's §4.2 numbering is Hatcher's and Proudfoot's homework 7 covers 1, 2, 30, 31
    and 32, announcing 39 without a solution of it.
---

::: {.problem}
Let $p: S^3 \to S^2$ be the Hopf bundle and let $q: T^3 \to S^3$ be the quotient map collapsing the complement of a ball in the 3-dimensional torus $T^3 = S^1 \times S^1 \times S^1$ to a point.
Show that $pq: T^3 \to S^2$ induces the trivial map on $\pi_*$ and $\tilde{H}_*$, but is not homotopic to a constant map.
:::

::: {.solution}
The argument is the card's own, and a retained solution covers the exercise: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.2 Exercise 34** (`tmp/sources/hatcher-solutions-sam-2008.md`). It is checked against Hatcher, Algebraic Topology, Section 4.2 Exercise 34, and uses the mapping cone and the cofiber sequence of Section 4.2.

::: pf

::: {.pf-step #maps}
Let $f=pq:T^3\xrightarrow{q}S^3\xrightarrow{p}S^2$, where $p$ is the Hopf bundle and $q$ collapses the complement of an embedded closed $3$-ball in $T^3$ to a point; $q$ has degree $1$.

::: pf-proof
$q$ is the quotient map of a closed ball to a point; its restriction to the interior of that ball is a homeomorphism onto $S^3$ minus a point, so $q$ is a degree $1$ map: the preimage of a regular value outside the collapsed point is a single point at which $q$ is a local homeomorphism.
:::

:::

::: {.pf-step #pi}
$f_*=0$ on every homotopy group.

::: pf-proof
$\pi_1(S^2)=0$, so $(pq)_*$ is zero on $\pi_1$. For $i>1$, $\pi_i(T^3)=0$ because the universal cover of $T^3$ is $\RR^3$, which is contractible; hence $f_*:\pi_i(T^3)\to\pi_i(S^2)$ has zero source for $i>1$.
:::

:::

::: {.pf-step #homology}
$f_*=0$ on every reduced homology group.

::: pf-proof
For $i=1,2$ the target $H_i(S^3)=0$, so $q_*=0$ there and $f_*=p_*q_*=0$. For $i=3$ the target $H_3(S^2)=0$, so $p_*=0$; and for $i>3$ both groups vanish.
:::

:::

::: {.pf-step #cone}
The commutative square with rows $q$ and the identity on $S^2$ induces a map $\varphi:C_f\to C_p$ of mapping cones, and $\varphi$ restricts to the identity on the copy of $S^2$.

::: pf-proof
A commutative square of maps induces a map of the mapping cones, by naturality of the construction $C_f=CA\cup_f B$. Both cones contain $B=S^2$ as the target, and on that summand the induced map is the identity because the square's bottom map is the identity.
:::

:::

::: {.pf-step #cp}
$C_p\simeq\CP^2$; if $x\in H^2(C_p;\ZZ)$ is a generator then $x^2\ne0$ in $H^4(C_p;\ZZ)\cong\ZZ$.

::: pf-proof
The mapping cone of the Hopf map $p:S^3\to S^2$ is $\CP^2$, since $\CP^2$ is obtained from $\CP^1=S^2$ by attaching a $4$-cell along the Hopf map. Its cohomology is $\ZZ$ in degrees $0,2,4$ with $x^2$ a generator of $H^4$, the standard cup product structure of projective space.
:::

:::

::: {.pf-step #injective}
$\varphi^*:H^2(C_p;\ZZ)\to H^2(C_f;\ZZ)$ is injective.

:::: pf-proof

::: {.pf-step #cf}
$H^2(C_f;\ZZ)\cong H^2(S^2;\ZZ)\oplus H^1(T^3;\ZZ)$.

::: pf-proof
Because $f_*=0$ on $H_2$, the cofiber sequence $T^3\to S^2\to C_f$ gives the split exact sequence
$$
0\to H_2(S^2;\ZZ)\to H_2(C_f;\ZZ)\to H_1(T^3;\ZZ)\to0,
$$
so $H_2(C_f;\ZZ)\cong\ZZ^4$ and $H_1(C_f;\ZZ)=0$ (the sequence continues with $H_1(S^2)=0$). The universal coefficient theorem then gives $H^2(C_f;\ZZ)\cong\operatorname{Hom}(H_2(C_f),\ZZ)\oplus\operatorname{Ext}(H_1(C_f),\ZZ)\cong\ZZ^4$, and the displayed decomposition follows from $H^2(S^2)=\ZZ$ and $H^1(T^3)=\ZZ^3$.
:::

:::

::: {.pf-step #factor}
The composite $H^2(C_p)\xrightarrow{\varphi^*}H^2(C_f)\to H^2(S^2)$ is the restriction $H^2(C_p)\to H^2(S^2)$, an isomorphism.

::: pf-proof
The second map is induced by the inclusion $S^2\subset C_f$, and by step [](#cone){.pf-ref} the composite is induced by the identity on that $S^2$. The restriction $H^2(C_p)\to H^2(S^2)$ is an isomorphism because $C_p$ is obtained from $S^2$ by attaching a single $4$-cell, so $C^2$ and $C^3$ of the cone agree with those of $S^2$.
:::

:::

::: {.pf-step}
$\varphi^*$ is injective in degree $2$.

::: pf-proof
Its composite with the projection $H^2(C_f)\to H^2(S^2)$ is an isomorphism by step [](#factor){.pf-ref}; a map whose composite with another map is injective is itself injective.
:::

:::

:::

:::

::: {.pf-step #degree4}
$\varphi^*$ is an isomorphism in degree $4$.

::: pf-proof
Both groups are $\ZZ$: $H^4(C_p;\ZZ)\cong\ZZ$ by step [](#cp){.pf-ref}, and $H^4(C_f;\ZZ)\cong H^4(S^2)\oplus H^4(\Sigma T^3)=H^3(T^3;\ZZ)\cong\ZZ$ by the same decomposition as in step [](#cf){.pf-ref}. The quotient description of mapping cones identifies $\varphi$ in this degree with the suspension of $q:T^3\to S^3$, which is a map $\Sigma T^3\to\Sigma S^3=S^4$ of degree $1$ by step [](#maps){.pf-ref}; a degree $1$ map induces an isomorphism on top cohomology.
:::

:::

::: {.pf-step #square}
With $\bar x=\varphi^*(x)\in H^2(C_f;\ZZ)$ one has $\bar x^2\ne0$.

::: pf-proof
$\varphi^*$ is a ring homomorphism, so $\bar x^2=\varphi^*(x^2)$. Now $x^2$ generates $H^4(C_p;\ZZ)\cong\ZZ$ by step [](#cp){.pf-ref}, and $\varphi^*$ is an isomorphism in degree $4$ by step [](#degree4){.pf-ref}, so $\varphi^*(x^2)\ne0$.
:::

:::

::: {.pf-step #null}
If $f$ were nullhomotopic then $C_f\simeq S^2\vee\Sigma T^3$, and every degree-$2$ class of that wedge would have square zero.

::: pf-proof
A nullhomotopy of $f$ gives $C_f\simeq C_{\text{const}}\simeq S^2\vee\Sigma T^3$. In the cohomology of a wedge the products between classes supported on different summands vanish; the class $\bar x$ has positive degree, so its square is the product of two classes supported on the same summand, and in $\tilde H^*(S^2)$ it vanishes because $H^4(S^2)=0$, while in $\tilde H^*(\Sigma T^3)$ it vanishes because the cup product of two positive-degree classes in a suspension is zero, the diagonal being nullhomotopic in a suspension.
:::

:::

::: {.pf-step}
$pq$ is not homotopic to a constant map.

::: pf-proof
Steps [](#pi){.pf-ref} and [](#homology){.pf-ref} give the triviality on homotopy and reduced homology; step [](#square){.pf-ref} gives a class of nonzero square in $H^*(C_f)$, which step [](#null){.pf-ref} shows to be impossible for a nullhomotopic map. Hence
$$
\boxed{pq\text{ induces zero on }\pi_*\text{ and }\tilde H_*\text{ but is not nullhomotopic}.}
$$
:::

:::

:::
:::
