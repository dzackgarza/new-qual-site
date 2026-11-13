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
---

::: {.problem}
Use the universal coefficient theorem to show that if $H_*(X; \ZZ)$ is finitely generated, so the Euler characteristic $\chi(X) = \sum_n (-1)^n \operatorname{rank} H_n(X; \ZZ)$ is defined, then for any coefficient field $F$ we have $\chi(X) = \sum_n (-1)^n \dim H_n(X; F)$.
:::

::: {.solution}
That $\chi(X)$ is defined says that each $H_n(X;\ZZ)$ is finitely generated and that $H_n(X;\ZZ)=0$ for all but finitely many $n$. Write
$$
H_n(X;\ZZ)\cong \ZZ^{r_n}\oplus T_n
$$
with $T_n$ finite, and $r_n=0=T_n$ for $n\gg0$. For a field $F$ the dimensions $\dim_FH_n(X;F)$ are computed by the universal coefficient theorem, Theorem 3A.3 (p. 264):
$$
0\longrightarrow H_n(X;\ZZ)\otimes F
\longrightarrow H_n(X;F)
\longrightarrow \operatorname{Tor}(H_{n-1}(X;\ZZ),F)\longrightarrow 0 .
$$
The sequence is exact, so the middle dimension is the sum of the two outer ones.

*Characteristic zero.* If $\operatorname{char}F=0$ then $F$ is torsionfree as a $\ZZ$-module, so $\operatorname{Tor}(H_{n-1}(X;\ZZ),F)=0$ by Proposition 3A.5(3) (p. 265), while $T_n\otimes F=0$ because every element of the finite group $T_n$ is killed by an integer that acts invertibly on $F$. Hence $H_n(X;F)\cong \ZZ^{r_n}\otimes F\cong F^{r_n}$, with $\dim_FH_n(X;F)=r_n$.

*Characteristic $p$.* Let $\operatorname{char}F=p$. By the structure theorem for finite abelian groups, $T_n\cong\bigoplus_j\ZZ/p_j^{k_j}$ is a direct sum of cyclic groups of prime-power order, and
$$
\ZZ/m\otimes F\cong F/mF=
\begin{cases}F,&p\mid m,\\ 0,&p\nmid m,\end{cases}
$$
so $\dim_F(T_n\otimes F)$ is the number $t_n$ of $p$-power cyclic summands of $T_n$; this number is also $\dim_{\FF_p}(T_n/pT_n)=\dim_{\FF_p}T_n[p]$ and is zero for $n\gg0$. Proposition 3A.5(4) (p. 265) replaces $H_{n-1}(X;\ZZ)$ by its torsion subgroup, Proposition 3A.5(5) gives $\operatorname{Tor}(\ZZ/m,F)\cong\ker(F\xrightarrow{m}F)$, which is $F$ for $p\mid m$ and $0$ otherwise, and additivity in the first variable, Proposition 3A.5(2), gives
$$
\operatorname{Tor}(H_{n-1}(X;\ZZ),F)\cong\operatorname{Tor}(T_{n-1},F)\cong T_{n-1}\otimes F,
\qquad \dim_F\operatorname{Tor}(H_{n-1}(X;\ZZ),F)=t_{n-1}.
$$
Hence
$$
\dim_FH_n(X;F)=r_n+t_n+t_{n-1},
$$
and the alternating sum of the torsion terms telescopes over the finitely many nonzero $t_n$:
$$
\sum_n(-1)^n(t_n+t_{n-1})=\sum_n(-1)^nt_n-\sum_n(-1)^nt_n=0.
$$
Therefore
$$
\sum_n(-1)^n\dim_FH_n(X;F)
=\sum_n(-1)^nr_n
=\chi(X).
$$
:::

::: {.remark title="Published solution"}
Hatcher, *Algebraic Topology* (2002): Theorem 3A.3 (universal coefficients), printed p. 264 with its proof, and Proposition 3A.5, printed pp. 265--266 with its proof. The exercise is Exercise 1 of §3.A, printed p. 267.
:::
