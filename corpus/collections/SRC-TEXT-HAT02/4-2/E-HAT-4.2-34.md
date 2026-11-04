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

---

::: {.problem}
Let $p: S^3 \to S^2$ be the Hopf bundle and let $q: T^3 \to S^3$ be the quotient map collapsing the complement of a ball in the 3-dimensional torus $T^3 = S^1 \times S^1 \times S^1$ to a point.
Show that $pq: T^3 \to S^2$ induces the trivial map on $\pi_*$ and $\tilde{H}_*$, but is not homotopic to a constant map.
:::

::: {.solution}
Let
$$
f=pq:T^3\xrightarrow{q}S^3\xrightarrow{p}S^2,
$$
where $p$ is the Hopf map and $q$ collapses the complement of an embedded $3$-ball.

For homotopy groups, $\pi_1(S^2)=0$, while
$$
\pi_i(T^3)=0\qquad(i>1)
$$
because the universal cover of $T^3$ is $\RR^3$. Hence $f_*$ is zero on every homotopy group.

For reduced homology, $q_*$ is zero in degrees $1$ and $2$ because $S^3$ has no homology there, and
$$
p_*:H_3(S^3)\to H_3(S^2)
$$
is zero. Thus $f_*$ is zero on all reduced homology groups.

To see that $f$ is nevertheless essential, compare mapping cones. The commutative square
$$
\begin{array}{ccc}
T^3&\xrightarrow{q}&S^3\\
f\downarrow&&\downarrow p\\
S^2&=&S^2
\end{array}
$$
induces a map
$$
C_f\longrightarrow C_p.
$$
Contravariantly, this gives
$$
H^*(C_p)\longrightarrow H^*(C_f).
$$
The Hopf mapping cone is $C_p\simeq\CP^2$. If $x\in H^2(C_p;\ZZ)$ is its standard generator, then
$$
x^2\ne0\in H^4(C_p;\ZZ).
$$
The induced map is injective in degree $2$: it is the identity on the $S^2$ subspace, and since $f_*$ is zero on $H_2$ the cofiber sequence $T^3\to S^2\to C_f$ gives the split exact sequence $0\to H_2(S^2;\ZZ)\to H_2(C_f;\ZZ)\to H_1(T^3;\ZZ)\to0$, so $H_2(C_f;\ZZ)\cong\ZZ^4$ and $H_1(C_f;\ZZ)=0$, hence $H^2(C_f;\ZZ)\cong H^2(S^2;\ZZ)\oplus H^1(T^3;\ZZ)$. In degree $4$, the quotient description of mapping cones identifies the induced map with the suspension of
$$
q:T^3\to S^3.
$$
The map $q$ has degree $1$, so this map is also an isomorphism on $H^4$. Therefore the image $\bar x\in H^2(C_f)$ satisfies
$$
\bar x^2\ne0.
$$

If $f$ were nullhomotopic, then
$$
C_f\simeq S^2\vee\Sigma T^3.
$$
Every degree-$2$ class in this wedge has square zero: $S^2$ has no degree-$4$ cohomology, the cup product on a suspension is zero, and products between wedge summands are zero. This contradicts $\bar x^2\ne0$. Hence
$$
\boxed{pq\text{ is not nullhomotopic}.}
$$
:::
