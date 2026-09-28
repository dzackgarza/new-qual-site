---
schema: qual/card@1
id: E-HAT-4.A-5
kind: problem
title: "Eilenberg--MacLane spaces and Postnikov towers"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.A, Exercise 5 and the Bestvina--Brady/Stallings construction immediately preceding the exercises; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
This problem involves the spaces constructed in the latter part of this section.

(a) Compute the homology groups of the complex $Z$ in the case $n = 3$, when $Z$ is 2-dimensional.

(b) Letting $\tilde{X}_n$ denote the $n$-dimensional complex $\tilde{X}$, show that $\tilde{X}_n$ can be obtained inductively from $\tilde{X}_{n-1}$ as the union of two copies of the mapping torus of the generating deck transformation $\tilde{X}_{n-1} \to \tilde{X}_{n-1}$, with copies of $\tilde{X}_{n-1}$ in these two mapping tori identified.
Thus there is a fiber bundle $\tilde{X}_n \to S^1 \vee S^1$ with fiber $\tilde{X}_{n-1}$.

(c) Use part (b) to find a presentation for $\pi_1(\tilde{X}_n)$, and show this presentation reduces to a finite presentation if $n > 2$ and a presentation with a finite number of generators if $n = 2$.
In the latter case, deduce that $\pi_1(\tilde{X}_2)$ has no finite presentation from the fact that $H_2(\tilde{X}_2)$ is not finitely generated.
:::

::: {.solution}
Write
\[
X_n=(S^1\vee S^1)^n
\]
and let
\[
\phi_n:\pi_1(X_n)=F_2^n\longrightarrow\mathbb Z
\]
send each of the \(2n\) standard generators to \(1\). Let
\[
\widetilde X_n\to X_n
\]
be the corresponding infinite cyclic cover, with deck generator \(T\). Hatcher's level set
\[
Z=X_3\cap f^{-1}(0)
\]
lifts homeomorphically to a subcomplex of \(\widetilde X_3\), and the construction preceding the exercise shows that \(\widetilde X_3\) is homotopy equivalent to a complex obtained from \(Z\) by attaching only 3-cells. Consequently
\[
\pi_1(Z)\cong\pi_1(\widetilde X_3).
\]

### (a) Homology of \(Z\) for \(n=3\)

In Hatcher's octahedral model of \(Z\), the six vertices are all identified to one vertex. Each of the twelve edges of the octahedron occurs with two choices of normal direction, and opposite directed edges are identified, leaving twelve 1-cells. Each of the eight triangular faces occurs with two normal directions, giving sixteen 2-cells. Thus
\[
C_0(Z)\cong\mathbb Z,
\qquad
C_1(Z)\cong\mathbb Z^{12},
\qquad
C_2(Z)\cong\mathbb Z^{16},
\]
so
\[
\chi(Z)=1-12+16=5.
\]

We compute \(H_1\) from the fundamental group. The presentation obtained in part (c) below for \(\pi_1(\widetilde X_3)\) has five generators and only conjugacy/commutator-type relators, hence its abelianization is free abelian of rank five. Therefore
\[
H_1(Z;\mathbb Z)\cong\mathbb Z^5.
\]
Since \(Z\) is connected, \(H_0(Z)\cong\mathbb Z\). Also \(H_2(Z)\) is a subgroup of the free abelian group \(C_2(Z)\), hence is free abelian. Euler characteristic now gives
\[
5=1-5+\operatorname{rank}H_2(Z),
\]
so
\[
H_2(Z;\mathbb Z)\cong\mathbb Z^9.
\]
There is no homology above dimension two. Hence
\[
\boxed{
H_i(Z;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^5,&i=1,\\
\mathbb Z^9,&i=2,\\
0,&i>2.
\end{cases}}
\]

### (b) Recursive mapping-torus description

Write
\[
X_n=X_{n-1}\times(S^1_a\vee S^1_b).
\]
Over the wedge point in the last factor the fiber of the induced map
\[
\widetilde X_n\longrightarrow S^1_a\vee S^1_b
\]
is naturally \(\widetilde X_{n-1}\). Traversing either loop \(S^1_a\) or \(S^1_b\) increases the total exponent sum by one, so the monodromy on the fiber is exactly the generating deck transformation
\[
T:\widetilde X_{n-1}\to\widetilde X_{n-1}.
\]
Therefore the inverse image of each of the two circles is the mapping torus \(M_T\). These two mapping tori intersect precisely in the common fiber over the wedge point. Thus
\[
\boxed{\widetilde X_n=M_T\cup_{\widetilde X_{n-1}}M_T,}
\]
and in particular
\[
\boxed{\widetilde X_{n-1}\longrightarrow\widetilde X_n
\longrightarrow S^1\vee S^1}
\]
is a fiber bundle with monodromy \(T\) around each circle.

### (c) Presentations

Let
\[
H_n=\pi_1(\widetilde X_n),
\qquad
\tau_n=(T_*)\in\operatorname{Aut}(H_n).
\]
If
\[
H_{n-1}=\langle S\mid R\rangle,
\]
then van Kampen applied to the two mapping tori gives
\[
H_n=
\left\langle
S,a,b\ \middle|\
R,
asa^{-1}=\tau_{n-1}(s),
bsb^{-1}=\tau_{n-1}(s)\ (s\in S)
\right\rangle.
\tag{1}
\]

For \(n=1\), \(\widetilde X_1\) is the infinite cyclic cover of the two-petal rose. Choosing one family of lifted edges as a maximal tree shows
\[
H_1\cong F(c_i\mid i\in\mathbb Z),
\qquad
\tau_1(c_i)=c_{i+1}.
\]
Applying (1) for \(n=2\) gives
\[
H_2=
\left\langle
c_i,a,b\ \middle|\
ac_i a^{-1}=c_{i+1},
bc_i b^{-1}=c_{i+1}\ (i\in\mathbb Z)
\right\rangle.
\]
Eliminating \(c_i=a^ic_0a^{-i}\) leaves the finite generating set \(c=c_0,a,b\) and the relations
\[
ba^ica^{-i}b^{-1}=a^{i+1}ca^{-(i+1)}
\qquad(i\in\mathbb Z).
\tag{2}
\]
Thus \(H_2\) is finitely generated.

The deck automorphism \(\tau_2\) fixes \(a,b\) and sends
\[
c\longmapsto aca^{-1}.
\]
Hence the relators in (2) form one \(\tau_2\)-orbit. When we apply (1) once more to construct \(H_3\), the stable letter implementing \(\tau_2\) makes all the relators (2) conjugates of the single relator with \(i=0\). Thus \(H_3\) has a finite presentation. Explicitly one may take generators
\[
c,a,b,d,e
\]
with the single old relator
\[
bcb^{-1}=aca^{-1},
\]
together with the finitely many relations saying that both \(d\) and \(e\) implement \(\tau_2\):
\[
[d,a]=[d,b]=[e,a]=[e,b]=1,
\qquad
dcd^{-1}=aca^{-1},
\qquad
ece^{-1}=aca^{-1}.
\]
Its abelianization is therefore \(\mathbb Z^5\), as used in part (a).

For \(n>3\), induction in (1) is immediate: if \(H_{n-1}\) has a finite presentation, then adjoining two stable letters and finitely many conjugation relations gives a finite presentation of \(H_n\). Hence
\[
\boxed{H_n\text{ is finitely presented for every }n>2,}
\]
while \(H_2\) has a presentation with finitely many generators.

Finally \(\widetilde X_2\) is a 2-dimensional \(K(H_2,1)\), and Hatcher's construction gives that
\[
H_2(\widetilde X_2;\mathbb Z)
\]
is not finitely generated. If \(H_2\) had a finite presentation, its finite presentation 2-complex could be completed to a \(K(H_2,1)\) by attaching cells only in dimensions at least three; this would force \(H_2(H_2;\mathbb Z)\) to be finitely generated, a contradiction. Therefore
\[
\boxed{\pi_1(\widetilde X_2)=H_2\text{ is finitely generated but not finitely presented}.}
\]
:::
