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
---

Let $p: S^3 \to S^2$ be the Hopf bundle and let $q: T^3 \to S^3$ be the quotient map collapsing the complement of a ball in the 3-dimensional torus $T^3 = S^1 \times S^1 \times S^1$ to a point.
Show that $pq: T^3 \to S^2$ induces the trivial map on $\pi_*$ and $\tilde{H}_*$, but is not homotopic to a constant map.

::: {.solution}
Let
\[
f=pq:T^3\xrightarrow{q}S^3\xrightarrow{p}S^2,
\]
where \(p\) is the Hopf map and \(q\) collapses the complement of an embedded \(3\)-ball.

For homotopy groups, \(\pi_1(S^2)=0\), while
\[
\pi_i(T^3)=0\qquad(i>1)
\]
because the universal cover of \(T^3\) is \(\mathbb R^3\). Hence \(f_*\) is zero on every homotopy group.

For reduced homology, \(q_*\) is zero in degrees \(1\) and \(2\) because \(S^3\) has no homology there, and
\[
p_*:H_3(S^3)\to H_3(S^2)
\]
is zero. Thus \(f_*\) is zero on all reduced homology groups.

To see that \(f\) is nevertheless essential, compare mapping cones. The commutative square
\[
\begin{array}{ccc}
T^3&\xrightarrow{q}&S^3\\
f\downarrow&&\downarrow p\\
S^2&=&S^2
\end{array}
\]
induces a map
\[
C_f\longrightarrow C_p.
\]
Contravariantly, this gives
\[
H^*(C_p)\longrightarrow H^*(C_f).
\]
The Hopf mapping cone is \(C_p\simeq\mathbb{CP}^2\). If \(x\in H^2(C_p;\mathbb Z)\) is its standard generator, then
\[
x^2\ne0\in H^4(C_p;\mathbb Z).
\]
The induced map is an isomorphism in degree \(2\), since it is the identity on the \(S^2\) subspace. In degree \(4\), the quotient description of mapping cones identifies the induced map with the suspension of
\[
q:T^3\to S^3.
\]
The map \(q\) has degree \(1\), so this map is also an isomorphism on \(H^4\). Therefore the image \(\bar x\in H^2(C_f)\) satisfies
\[
\bar x^2\ne0.
\]

If \(f\) were nullhomotopic, then
\[
C_f\simeq S^2\vee\Sigma T^3.
\]
The degree-\(2\) class coming from the \(S^2\)-summand would have square zero, a contradiction. Hence
\[
\boxed{pq\text{ is not nullhomotopic}.}
\]
:::
