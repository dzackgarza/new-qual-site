---
schema: qual/card@1
id: E-HAT-3.A-1
kind: problem
title: "Euler characteristic is independent of coefficient field"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.A Exercise 1, printed p. 267. The statement
    matches the print word for word, including the hypothesis that $H_*(X;\ZZ)$ be finitely generated
    and the phrase "for any coefficient field $F$". Repaired in three places where the proof was
    incomplete rather than false: the finiteness of the two alternating sums is now stated rather
    than assumed; the characteristic-$p$ case runs Theorem 3A.3 over $F$ directly through
    Proposition 3A.5(2), (4) and (5), instead of asserting that it suffices to compute over $\FF_p$
    and extend scalars; and Theorem 3A.3 (p. 264) and Proposition 3A.5(3) (p. 265) are cited where
    the proof had said only "the universal coefficient theorem". Checked against Hatcher's
    definitions on pp. 261-266: $C_*(X;G)=C_*(X)\otimes G$, $\operatorname{Tor}_n=0$ for $n>1$, and
    Tor as defined from a free resolution. No published solution of this exercise is in the
    retained sets; recorded in COMPLAINTS.md.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 267. Its published proof is Hatcher's own: Theorem 3A.3 (universal coefficients for homology with coefficients), printed p. 264 with its complete proof, and Proposition 3A.5, printed pp. 265--266 with its complete proof, which gives the two facts the deduction needs (that $\operatorname{Tor}(\ZZ^{r},F)=0$ and that $\operatorname{Tor}(T,F)$ has dimension equal to the number of $p$-power summands killed by the characteristic). The card's proof is that deduction written out: the UCT splits $H_n(X;F)$ into $H_n(X;\ZZ)\otimes F$ plus $\operatorname{Tor}(H_{n-1}(X;\ZZ),F)$, and the alternating sum of the dimensions telescopes because the torsion correction appears with a compensating sign in the neighbouring degree. Checked against the book: the printed statement, the finite-generation hypothesis, and the two coefficient cases (characteristic zero and characteristic $p$). Not claimed: that the book prints this exercise; it prints the two theorems the exercise applies.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The proof is now the source's: tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics,
    2008), Proposition (11.6.4) on printed **p. 289** for the finite free model, Theorem (11.6.3) on
    printed p. 288 for the chain equivalence, Proposition (12.4.1) on printed p. 309 for the
    alternating sum, and Proposition (12.4.4) on printed **p. 310**, all transcribed with the two
    verifications the source compresses into "one verifies that $\psi$ is a chain map" and "some
    elementary algebra". The route is the one this card now states: a finite free chain complex
    replaces $S_*(X)$, ranks are compared along the alternating sum, and **the universal coefficient
    theorem is not used**. The source's statement is the pair version for every principal ideal
    domain, so the exercise's field case follows and the card says the source is stronger. The
    previous proof was the universal coefficient theorem route, which is what the printed exercise
    tells the reader to use; it is kept as the closing paragraph and labelled as Hatcher's route with
    its printed inputs (Theorem 3A.3, p. 264; Proposition 3A.5, pp. 265--266), so the card answers the
    exercise as printed while resting on the source for the proof. Page check: (11.6.4) is on p. 289,
    not 288 — the extracted page marker for 289 precedes it and the table of contents puts the start
    of §11.7 on p. 289 — and (12.4.1) is on p. 309, with (12.4.2)--(12.4.4) on p. 310. Checked
    against Hatcher (2002), §3.A Exercise 1, printed p. 267, quoted on the card. Not claimed: that
    tom Dieck states Hatcher's exercise or names the universal coefficient theorem.
---

::: {.problem}
Use the universal coefficient theorem to show that if $H_*(X; \ZZ)$ is finitely generated, so the Euler characteristic $\chi(X) = \sum_n (-1)^n \operatorname{rank} H_n(X; \ZZ)$ is defined, then for any coefficient field $F$ we have $\chi(X) = \sum_n (-1)^n \dim H_n(X; F)$.
:::

::: {.solution}
Hatcher's hypothesis is the source's. tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), calls a pair $(X,A)$ of finite $R$-type, for $R$ a principal ideal domain, if the $R$-modules $H_i(X,A;R)$ are finitely generated and only finitely many of them are nonzero, and puts $\chi(X,A;R)=\sum_i(-1)^i\operatorname{rank}_RH_i(X,A;R)$ (printed p. 310); with $A=\emptyset$ and $R=\ZZ$ that is the exercise's hypothesis that $\chi(X)$ is defined. The source's proof, Proposition (12.4.4) on printed p. 310, does not use the universal coefficient theorem: it replaces $S_*(X)$ by a finite free chain complex and compares ranks along the alternating sum. It proves the statement for every principal ideal domain $R$, and the exercise's coefficient field $F$ is that case.

*The finite free model.* (Proposition (11.6.4), printed p. 289.) Let $R$ be a principal ideal domain and $C=(C_n)$ a chain complex of free $R$-modules with finitely generated homology. For each $n$ let $F_n$ be a finitely generated submodule of $Z_n(C)$ which the quotient map $Z_n(C)\to H_n(C)$ carries onto $H_n(C)$, and let $G_n$ be the kernel of $F_n\to H_n(C)$. Put
$$
D_n=F_n\oplus G_{n-1},\qquad d_n(x,y)=(y,0).
$$
Then $D=(D_n,d_n)$ is a free chain complex of finite type with $H_n(D)=F_n/G_n\cong H_n(C)$. Since $G_n$ is a free submodule of $B_n(C)$, a submodule of a free module over a principal ideal domain being free, there are homomorphisms $\varphi_n:G_n\to C_{n+1}$ with $c_{n+1}\varphi_n(y)=y$ for $y\in G_n$. The degreewise maps
$$
\psi_n:D_n=F_n\oplus G_{n-1}\longrightarrow C_n,\qquad (x,y)\longmapsto x+\varphi_{n-1}(y)
$$
form a chain map, because $x\in Z_n(C)$ gives $c_n\psi_n(x,y)=c_n\varphi_{n-1}(y)=y=\psi_{n-1}(y,0)=\psi_{n-1}d_n(x,y)$; and $\psi$ induces an isomorphism on homology, so by Theorem (11.6.3) (printed p. 288) it is a chain equivalence.

Applied to $C=S_*(X)$, which is a complex of free $\ZZ$-modules with finitely generated homology, this gives a chain complex $D$ of finitely generated free abelian groups, chain equivalent to $S_*(X)$, and $D_n=0$ for $n\gg0$ because then $H_n(X;\ZZ)=0$ and hence $F_n=0$. That is the reduction the source uses: "the singular complex $S_*(X)$ is chain equivalent to a chain complex $D_*$ of finitely generated free abelian groups with only finitely many of the $D_n$ non-zero".

*The Euler computation.* (Proposition (12.4.4), printed p. 310.) For a principal ideal domain $R$, $D\otimes R$ is a free chain complex of finite type over $R$, and $\psi\otimes\id_R$ is a chain equivalence, so $H_n(D\otimes R)\cong H_n(X;R)$; in particular $X$ is of finite $R$-type. The rank function is additive in the sense of the source's definition on printed p. 309: for an exact sequence $0\to M'\to M\to M''\to0$ of finitely generated $R$-modules, tensoring with the fraction field $K$ of $R$ is exact and gives $\dim_KM\otimes K=\dim_KM'\otimes K+\dim_KM''\otimes K$. Proposition (12.4.1), printed p. 309 and proved there by induction on the length of the complex, therefore gives
$$
\sum_i(-1)^i\operatorname{rank}_R(D_i\otimes R)=\sum_i(-1)^i\operatorname{rank}_RH_i(D\otimes R)=\sum_i(-1)^i\operatorname{rank}_RH_i(X;R)=\chi(X;R).
$$
Since $D_i$ is free of rank $d_i$ over $\ZZ$, $D_i\otimes R$ is free of rank $d_i$ over $R$, and applying (12.4.1) once more, now with the additive invariant $\operatorname{rank}_\ZZ$ over $\ZZ$,
$$
\chi(X;R)=\sum_i(-1)^id_i=\sum_i(-1)^i\operatorname{rank}_\ZZ D_i=\sum_i(-1)^i\operatorname{rank}_\ZZ H_i(X;\ZZ)=\chi(X).
$$
Taking $R=F$ a field, where $\operatorname{rank}_F=\dim_F$, gives $\chi(X)=\sum_n(-1)^n\dim_FH_n(X;F)$, and the right side is a finite sum because $H_n(X;F)$ is of finite dimension and vanishes for $n\gg0$.

*The route the exercise itself names.* Hatcher's exercise says to use the universal coefficient theorem, and that route reaches the same conclusion from printed inputs. Theorem 3A.3 (p. 264) gives the exact sequence $0\to H_n(X;\ZZ)\otimes F\to H_n(X;F)\to\operatorname{Tor}(H_{n-1}(X;\ZZ),F)\to0$, so $\dim_FH_n(X;F)$ is the sum of the two outer dimensions; with $H_n(X;\ZZ)\cong\ZZ^{r_n}\oplus T_n$ and $t_n$ the number of $p$-power cyclic summands of $T_n$, Proposition 3A.5 (pp. 265--266) gives $\dim_FH_n(X;F)=r_n$ for $\operatorname{char}F=0$ and $r_n+t_n+t_{n-1}$ for $\operatorname{char}F=p$. In both cases the torsion terms cancel in the alternating sum, since $\sum_n(-1)^n(t_n+t_{n-1})=0$, leaving $\sum_n(-1)^nr_n=\chi(X)$.

Checked against Hatcher, *Algebraic Topology* (2002), §3.A Exercise 1, printed p. 267: "Use the universal coefficient theorem to show that if $H_*(X;\ZZ)$ is finitely generated, so the Euler characteristic $\chi(X)=\sum_n(-1)^n\operatorname{rank}H_n(X;\ZZ)$ is defined, then for any coefficient field $F$ we have $\chi(X)=\sum_n(-1)^n\dim H_n(X;F)$." The source proves the statement for every principal ideal domain and every pair $(X,A)$, not only for a field and a space.
:::

::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008): Proposition (11.6.4) on printed p. 289, the finite free model; the definition of finite $R$-type, Proposition (12.4.1) on printed p. 309 and Propositions (12.4.3) and (12.4.4) on printed p. 310, the alternating-sum computation. Proposition (12.4.4) is the exercise's statement for every principal ideal domain, proved without the universal coefficient theorem, whose route the exercise names and which the solution's last paragraph gives. The exercise is Exercise 1 of §3.A, printed p. 267.
:::
