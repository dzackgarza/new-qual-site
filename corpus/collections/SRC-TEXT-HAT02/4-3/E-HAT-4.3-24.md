---
schema: qual/card@1
id: E-HAT-4.3-24
kind: problem
title: "Obstructions for homotopy of lifts"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    The card previously carried no proof: its div tree had `pf-step` divs opened inside
    `pf-proof` divs and one proof block contained the single word "setup.". The solution block
    replacing it is a Lamport-structured proof of the printed exercise, built on the relative
    lifting problem of Hatcher §4.3 for the CW pair (W x I, B) and its cell count, with every
    step proved in place or cited to a numbered result.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

---

::: {.problem}
In the situation of the relative lifting problem, suppose one has two different lifts $W \to X$ that agree on the subspace $A \subset W$.
Show that the obstructions to finding a homotopy rel $A$ between these two lifts lie in the groups $H^n(W, A; \pi_n F)$.
:::

::: {.solution}
Let $p\colon X\to Y$ be a fibration with fibre $F$, let $(W,A)$ be a CW pair, let $g\colon W\to Y$ be a map, and let $f_0,f_1\colon W\to X$ be two lifts of $g$ with $f_0|_A=f_1|_A$.
Set $I=[0,1]$, let $\mathrm{pr}_W\colon W\times I\to W$ be the projection, put $G=g\circ \mathrm{pr}_W$, and set

$$
B=(W\times\{0\})\cup(A\times I)\cup(W\times\{1\})\subset W\times I .
$$

For $n\ge 1$ the coefficient system written $\pi_nF$ in $H^k(W,A;\pi_nF)$ is the local system on $W$ given by the action of $\pi_1(W)$ on $\pi_nF$ (Hatcher, Exercise 4.3.10; §3.H for cohomology with local coefficients). When that action is trivial these are ordinary cohomology groups with coefficients in the abelian group $\pi_nF$.

::: pf

::: {.pf-step #cylinder}
A homotopy rel $A$ from $f_0$ to $f_1$ all of whose levels are lifts of $g$ is the same thing as a solution of the relative lifting problem of Hatcher §4.3 for the CW pair $(W\times I,B)$, the fibration $p$, the map $G$, and the partial lift $h_0\colon B\to X$ of $G|_B$ given by $h_0(w,0)=f_0(w)$, $h_0(w,1)=f_1(w)$ and $h_0(a,t)=f_0(a)$ for $w\in W$, $a\in A$ and $t\in I$.

::: pf-proof
On $A\times\{0\}$ the first and the third formula both give $f_0(a)$, and on $A\times\{1\}$ the second gives $f_1(a)$ while the third gives $f_0(a)$, which is the same since $f_0|_A=f_1|_A$. The three closed sets $W\times\{0\}$, $A\times I$ and $W\times\{1\}$ cover $B$, so the pasting lemma makes $h_0$ a well-defined continuous map. It lifts $G|_B$: $p h_0(w,0)=p f_0(w)=g(w)=G(w,0)$ and $p h_0(w,1)=p f_1(w)=g(w)=G(w,1)$ because $f_0$ and $f_1$ lift $g$, and $p h_0(a,t)=p f_0(a)=g(a)=G(a,t)$.

A continuous $H\colon W\times I\to X$ with $pH=G$ and $H|_B=h_0$ gives the homotopy $H_t(w)=H(w,t)$, which satisfies $H_0=f_0$, $H_1=f_1$, $H_t(a)=h_0(a,t)=f_0(a)$ for $a\in A$ and $pH_t=g$. Conversely a homotopy $H_t$ rel $A$ from $f_0$ to $f_1$ through lifts of $g$ gives the continuous map $H(w,t)=H_t(w)$, which satisfies $pH=G$ and restricts to $h_0$ on $B$. The two passages are inverse to each other, both being the correspondence between a map on $W\times I$ and the family of its restrictions to the slices $W\times\{t\}$.
:::

:::

::: {.pf-step #cylinder-cells}
$(W\times I,B)$ is a CW pair, and its $(k+1)$-cells are exactly the cells $e^k\times(0,1)$ with $e^k$ a $k$-cell of $W$ not contained in $A$; hence they are in bijection with the $k$-cells of the relative CW complex $(W,A)$.

::: pf-proof
Let $I$ carry the cell structure with the two $0$-cells $\{0\}$ and $\{1\}$ joined by the $1$-cell $(0,1)$. By the product cell structure (Hatcher, Chapter 0, “Products” and “Suspension”) the cells of $W\times I$ are

$$
e^k\times\{0\},\qquad e^k\times\{1\},\qquad e^k\times(0,1)
$$

for the cells $e^k$ of $W$. The product topology on $W\times I$ and its topology as this cell complex coincide, because $I$ has finitely many cells, so this is a CW structure on the space $W\times I$.

The subspaces $W\times\{0\}$ and $W\times\{1\}$ are subcomplexes, with cells $e^k\times\{0\}$ and $e^k\times\{1\}$, and $A\times I$ is a subcomplex, with cells $e^k\times\{0\}$, $e^k\times\{1\}$ and $e^k\times(0,1)$ for the cells $e^k$ lying in $A$. A union of subcomplexes is a subcomplex, so $B$ is one and its cells are exactly the cells listed. The cells of $W\times I$ that are not cells of $B$ are therefore the cells $e^k\times(0,1)$ of dimension $k+1$ with $e^k$ not contained in $A$, and these are indexed by the $k$-cells of $(W,A)$.
:::

:::

::: {.pf-step #relative-obstructions}
Assume that $p\colon X\to Y$ has a Moore–Postnikov tower of principal fibrations; by Theorem 4.71 this holds as soon as $\pi_1(X)$ acts trivially on $\pi_n(M_p,X)$ for all $n>1$, where $M_p$ is the mapping cylinder of $p$. Then the relative lifting problem of step [](#cylinder){.pf-ref} has, for each $n\ge 1$, an obstruction class $\omega_n\in H^{n+1}(W\times I,B;\pi_nF)$, defined once a lift over $Z_{n-1}$ has been chosen and $\omega_1,\dots,\omega_{n-1}$ vanish, with $\pi_1F$ required to be abelian when $n=1$; and the problem has a solution if and only if some compatible choice of the successive lifts makes every $\omega_n$ vanish.

::: pf-proof
In such a tower each $Z_{n+1}\to Z_n$ is a principal fibration with fibre $K(\pi_nF,n)$, so $Z_{n+1}$ is the pullback of the path fibration over $K(\pi_nF,n+1)$ along a map $k_n\colon Z_n\to K(\pi_nF,n+1)$, and a lift of $W\times I$ to $Z_{n+1}$ over a given lift to $Z_n$ amounts to a nullhomotopy of the composite $W\times I\to Z_n\to K(\pi_nF,n+1)$. That nullhomotopy is prescribed on $B$, and the composite together with it is a map $W\times I\cup CB\to K(\pi_nF,n+1)$. Hatcher constructs the class of such a map in §4.3 (“Obstruction Theory”, the paragraph preceding Proposition 4.72): the obstruction is the class

$$
\omega_n\in H^{n+1}(W\times I\cup CB,CB;\pi_nF)\cong H^{n+1}(W\times I,B;\pi_nF),
$$

the displayed isomorphism being excision for the pair $(W\times I\cup CB,CB)$, and for a constant coefficient system the identification of homotopy classes of maps into $K(\pi_nF,n+1)$ with cohomology classes is the bijection of Theorem 4.57. Proposition 4.72 states that a lift $W\times I\to Z_n$ extending the given lift on $B$ exists if and only if $\omega_n=0$, so iterating over $n$ produces the sequence of classes, each defined only after the previous ones are killed and a lift to the previous stage is chosen. Hatcher states the outcome for the relative lifting problem in §4.3, in the paragraph following Proposition 4.72: “Having a lift to $Z_1$, the analysis proceeds exactly as before. One finds a sequence of obstructions $\omega_n\in H^{n+1}(W,A;\pi_nF)$, assuming $\pi_1F$ is abelian in the case $n=1$. A lift to $X$ exists, extending the given lift on $A$, if each successive $\omega_n$ is zero.” That is the statement used here, with the pair $(W\times I,B)$ in place of $(W,A)$.

Conversely, if a lift $W\times I\to X$ extending $h_0$ exists, then composing it with $X\to Z_n$ gives a lift to $Z_n$ extending the given lift on $B$, since the maps of the tower are compatible by construction, so $\omega_n=0$ for the successive choices of lifts that this solution determines, again by Proposition 4.72.

The preliminary stage of the tower, the lift to the covering space $Z_1$, is a covering-space question that Hatcher treats separately just before the quoted passage, observing that the choice of lift agreeing with the given one on the subspace can fail only when that subspace has more than one component; the classes $\omega_n$ are those of the stages $n\ge 1$ that follow it.
:::

:::

::: {.pf-step #cochain-shift}
For every abelian group $G$ and every $m\ge 0$ there is an isomorphism $H^{m+1}(W\times I,B;G)\cong H^m(W,A;G)$, induced by an isomorphism of the two relative cellular cochain complexes that lowers degree by one; for coefficients in a local system on $W$, pulled back to $W\times I$, the same holds.

::: pf-proof

::: {.pf-step #cochain-computes}
For a CW pair $(Z,C)$ the relative cellular cochain complex may be taken to be the dual $\operatorname{Hom}(C_*^{CW}(Z,C),G)$ of the relative cellular chain complex, and its cohomology is the singular cohomology $H^{*}(Z,C;G)$.

::: pf-proof
The relative cellular chain complex is free, and its homology is the singular homology of the pair: the cells of the quotient CW complex $Z/C$ are the cells of $Z$ that are not in $C$, with attaching maps obtained by composing those of $Z$ with the quotient map (Hatcher, Chapter 0, “Quotients”), so its cellular chain complex is the relative one, and its homology is $H_*(Z/C)\cong H_*(Z,C)$ by Theorem 2.35 and Proposition 2.22, CW pairs being good. Theorem 3.2 then computes the cohomology of the dual of a free chain complex from its homology by the universal coefficient formula; applied to the relative cellular chain complex and to the singular chain complex of the pair, which also consists of free groups, it gives in both cases a group isomorphic to $\operatorname{Hom}(H_n(Z,C),G)\oplus\operatorname{Ext}(H_{n-1}(Z,C),G)$. In the same way the relative cellular cochain group in degree $n$, which is $H^n(Z^n\cup C,Z^{n-1}\cup C;G)$, is $\operatorname{Hom}\big(H_n(Z^n\cup C,Z^{n-1}\cup C),G\big)=\operatorname{Hom}(C_n^{CW}(Z,C),G)$, because the relative homology vanishes in degree $n-1$; this is the identification asserted in Theorem 3.5 between the cellular cochain complex and the dual of the cellular chain complex, and under it the cellular coboundary is the dual of the boundary.
:::

:::

::: {.pf-step #cochain-groups}
For every $m\ge 0$ the groups $C^{m+1}(W\times I,B;G)=\operatorname{Hom}(C_{m+1}^{CW}(W\times I,B),G)$ and $C^m(W,A;G)=\operatorname{Hom}(C_m^{CW}(W,A),G)$ are isomorphic, by the assignment $c\mapsto\tilde c$ with $\tilde c(e^m)=c\big(e^m\times(0,1)\big)$.

::: pf-proof
By step [](#cylinder-cells){.pf-ref} the $(m+1)$-cells of $(W\times I,B)$ are the cells $e^m\times(0,1)$ for the $m$-cells $e^m$ of $W$ not in $A$, and the $m$-cells of $(W,A)$ are exactly those cells $e^m$. A relative cellular chain group is free on the relative cells, so the two dual groups are free on the same index set and the displayed assignment, which matches the cell $e^m\times(0,1)$ with the cell $e^m$, is an isomorphism.
:::

:::

::: {.pf-step #cochain-differentials}
The isomorphism of step [](#cochain-groups){.pf-ref} carries the coboundary of $(W\times I,B)$ to the coboundary of $(W,A)$: for every $c\in C^{m+1}(W\times I,B;G)$ and every $m$-cell $e^m$ of $W$ not in $A$ one has $\big\langle \delta c,\,e^m\times(0,1)\big\rangle=\big\langle \delta\tilde c,\,e^m\big\rangle$.

::: pf-proof
By step [](#cochain-computes){.pf-ref} the coboundary is the dual of the cellular boundary. The relative cellular chain complex of a CW pair is the quotient of the absolute complex by the chains carried by the subcomplex: by Hatcher's description of quotient cell complexes (Chapter 0, “Quotients”) the quotient $(W\times I)/B$ is a cell complex whose cells are exactly the cells of the pair $(W\times I,B)$, its attaching maps are those of $W\times I$ followed by the collapse, and its cellular chain complex is the relative one; the relative boundary of $e^m\times(0,1)$ is therefore the image of its absolute boundary. The cellular boundary formula for a product cell (Hatcher, §3.B, “The Cross Product in Homology”) gives, for the $1$-cell $(0,1)$ of $I$ with $d(0,1)=\{1\}-\{0\}$,

$$
d\big(e^m\times(0,1)\big)=de^m\times(0,1)+(-1)^m e^m\times\big(\{1\}-\{0\}\big).
$$

The cells $e^m\times\{0\}$ and $e^m\times\{1\}$ lie in $B$, so a relative cochain, extended by zero on the cells of $B$, takes the value $0$ on those two terms. Hence

$$
\big\langle \delta c,\,e^m\times(0,1)\big\rangle=\big\langle c,\,de^m\times(0,1)\big\rangle=\big\langle \tilde c,\,de^m\big\rangle=\big\langle \delta\tilde c,\,e^m\big\rangle,
$$

where the middle equality expands $de^m$ in the cells $e^{m-1}$ of $W$ and applies the definition of $\tilde c$ to each term, and the last equality is again the coboundary as the dual of the boundary.
:::

:::

::: {.pf-step #cochain-conclusion}
Consequently $H^{m+1}(W\times I,B;G)\cong H^m(W,A;G)$ for every $m\ge 0$, the isomorphism being induced by the degree-lowering isomorphism of cochain complexes of step [](#cochain-groups){.pf-ref}, which by step [](#cochain-differentials){.pf-ref} commutes with the coboundaries; for coefficients in a local system $\mathcal G$ on $W$, pulled back to $W\times I$, the same argument applies, since the fibre of the pulled-back system at a point of the cell $e^m\times(0,1)$ is the fibre at the corresponding point of $e^m$ and parallel translation in the pulled-back system along the $I$ direction is the identity, so the incidence numbers of the two relative complexes agree, and cellular cohomology with local coefficients computes singular cohomology with local coefficients (Hatcher, §3.H).

::: pf-proof
An isomorphism of cochain complexes induces an isomorphism of cohomology, and the complexes compared in steps [](#cochain-groups){.pf-ref} and [](#cochain-differentials){.pf-ref} are, by step [](#cochain-computes){.pf-ref}, complexes computing the singular cohomology of $(W\times I,B)$ and of $(W,A)$.
:::

:::

:::

:::

::: pf-qed
By step [](#relative-obstructions){.pf-ref} the obstruction classes of the successive stages of the relative lifting problem attached to the two lifts are classes $\omega_n\in H^{n+1}(W\times I,B;\pi_nF)$ for $n\ge 1$, and by step [](#cochain-shift){.pf-ref} with $m=n$, in the coefficient system $\pi_nF$, each of those groups is isomorphic to $H^n(W,A;\pi_nF)$. Transporting the classes across that isomorphism places the $n$-th obstruction to a homotopy rel $A$ from $f_0$ to $f_1$ through lifts of $g$ in $H^n(W,A;\pi_nF)$, for $n\ge 1$, with $\pi_1F$ abelian when $n=1$. By step [](#cylinder){.pf-ref} such a homotopy is exactly a solution of that lifting problem, so the classes $\omega_n$ can be made to vanish successively precisely when the homotopy exists; and, as Hatcher notes in the paragraphs following Proposition 4.72, the class at stage $n$ depends on the choices of the earlier lifts, so what is located in each group is the class of that stage rather than one intrinsic class attached to the pair of lifts.
:::

:::

:::
