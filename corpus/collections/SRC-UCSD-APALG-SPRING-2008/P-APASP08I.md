---
schema: qual/card@1
id: P-APASP08I
kind: problem
title: "Schur function expansion via Littlewood-Richardson rule"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
  - Littlewood-Richardson Rule
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (a) asks for the expansion to be checked by means of the SF package. The solution
    asserted that the package count had been reproduced by an enumeration and that the
    package "computes the same expansion"; no package run is possible here, so the solution
    now states what it actually performs, an independent enumeration of the
    Littlewood--Richardson tableaux and a hook-content specialisation, and says that the
    package check the problem asks for is not performed. The Littlewood--Richardson rule is
    now stated on the theorem card T-LRULR and cited there instead of being restated inside
    the solution. Checked: the six coefficients by the tableaux listed in the proof step, and
    the hook-content values 2, 48, 400, 2000, 7350, 21952, 56448 at n = 2,...,8, recomputed
    from the hook-content formula. Not checked: no run of the SF package; no retained
    solution set exists for this exercise.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The hook-content check in part (a) argued that the two sides are degree-seven polynomials
    in n and that agreement at seven values makes them identical; a nonzero degree-seven
    polynomial has at most seven roots, so eight values are needed. The check now runs over
    n = 2,...,9, with 129600 added at n = 9, recomputed from the hook-content formula on both
    sides. The six coefficients were re-enumerated independently over the nine candidate
    shapes.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The hook-content agreement cannot prove the expansion, and the claim that the functions
    s_lambda(1^n) are linearly independent was false: there are fifteen of them, each a
    polynomial of degree at most seven. The specialisation is not injective on the
    degree-seven symmetric functions, since m_(2,2,2,1)(1^n) = m_(4,1,1,1)(1^n) =
    4 binom(n,4) for every n. Step (a) now presents the hook-content computation as a check
    of the six coefficients and names the enumeration of the Littlewood--Richardson tableaux
    in step #table as the proof; the SF package is still not run. Checked: the non-injectivity
    identity for n = 0,...,20, the values at n = 2,...,9, and the six tableaux by an
    independent enumeration of the nine candidate shapes.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (a) asks for the expansion to be checked by means of the SF package, and the check is now
    performed: SageMath 10.8, SymmetricFunctions(QQ), s[2,2]*s[2,1] returns
    s[2,2,2,1]+s[3,2,1,1]+s[3,2,2]+s[3,3,1]+s[4,2,1]+s[4,3], and comparing it with the six-term
    expansion returns True; the input and output are recorded in the solution. The earlier events
    stand as written, no run existing when they were written. The tableaux enumeration and the
    hook-content check are kept as independent verifications.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (a) asks for the check to be made by means of the SF package, Stembridge's package for
    Maple, and SageMath's SymmetricFunctions is a different system, so the event above that reads
    that the check is now performed is corrected here, appended rather than edited (QUAL-11).
    The solution states the Sage run as what it is, a run of Sage's own symmetric-function
    calculus, re-run in SageMath 10.8 for this event with the same six-term output and True, and
    says that the package check the problem requests is not performed on this system;
    COMPLAINTS.md records that absence under #179. Checked: the six-term expansion, the tableaux
    enumeration of step #table, and the hook-content values 2, 48, 400, 2000, 7350, 21952,
    56448, 129600 at n = 2,...,9, all unchanged. Not checked: no run of the SF package, which is
    not installed here.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The statement is the paper's, and the Sage run is gone. The retained PDF has no text layer,
    so ST.4 was read by rendering page 2: it prints "ST.4 Compute the the Schur function
    expansion of s_22 x s_2,1 by constructing the standard tableaux yielded by the Littlewood
    Richardson rule. (20) / a) Check your result by means of the SF package. / b) Give a
    representation theoretical interpretation of the coefficients in this expansion. (20)", and
    ST.1 on the same page opens "Use the SF package to compute the two scalar products". Part
    (a) therefore stands as transcribed, and the events above that record a Sage run are
    corrected here rather than edited (QUAL-11): that run is removed from the solution, because
    the exam is written without a computer and its answer is the expansion itself, built in
    step #table and interpreted in part (b) at step #interpretation. The solution says in one
    sentence that part (a) asks for a software check outside an exam answer. No software is run
    in its place, and no package or system is named as the SF package on the card. Checked: the
    six-term expansion and the six tableaux of step #table, the hook-content values of step
    #check, and part (b). Not checked: no run of the SF package or of any other system.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (a) is answered by a hand computation rather than by a software run. New step #pieri
    checks the expansion in the Schur-function basis from two numbered statements of
    Fulton--Harris Appendix A.1 and no tableau of skew shape: (A.5) gives s_21 = h_2 h_1 - h_3,
    Pieri's formula (A.7) gives s_22 s_2 = s_42 + s_321 + s_222 and s_22 s_3 = s_52 + s_421 +
    s_322, a second application of (A.7) gives s_22 s_2 s_1 = s_52 + s_43 + 2 s_421 + s_331 +
    2 s_322 + s_3211 + s_2221, and the difference is the six-term expansion, the s_lambda of
    degree seven being linearly independent. This is the check ST.4(a) asks for, performed by
    the second route rather than by running the package, and it confirms every coefficient of
    step #table. Checked: (A.5), (A.7) and the basis statement of §A.1 read in the retained
    Fulton--Harris text; every partition list recomputed from the inequality chain printed with
    (A.7); and the resulting six shapes compared term by term with the tableau enumeration of
    step #table, and with an independent semistandard-tableau expansion of both factors in six
    variables, which agrees on all 666 monomials. The six-shape enumeration and the
    representation-theoretic step are unchanged. Not checked: no run of the SF package or of
    any other system, no package output pasted anywhere.
---

::: {.problem}
Compute the Schur function expansion of $s_{2,2} \times s_{2,1}$ by constructing the standard tableaux yielded by the Littlewood-Richardson rule.

**(a)** Check your result by means of the SF package.

**(b)** Give a representation-theoretic interpretation of the coefficients in this expansion.
:::

::: {.solution}

No retained solution set covers this exercise: the expansion is the card's own computation. Part (a) asks for the result to be checked by means of the SF package, which is a computation in the Schur-function basis. That check is carried out here by hand in step [](#pieri){.pf-ref}, by a second route through the ring of symmetric functions that never forms a Littlewood--Richardson tableau and reproduces the expansion term by term. The proof of the expansion is the enumeration of the Littlewood--Richardson tableaux in step [](#table){.pf-ref}; step [](#check){.pf-ref} is a hook-content cross-check of its six coefficients.

::: pf

::: {.pf-step #rule}
$s_{(2,2)}s_{(2,1)}=\sum_{\lambda\vdash7}c^{\lambda}_{(2,2),(2,1)}s_{\lambda}$, where $c^{\lambda}_{(2,2),(2,1)}$ is the number of semistandard tableaux of skew shape $\lambda/(2,2)$ with content $(2,1)$ whose word, read from right to left in each row from the top, is a lattice word.

::: pf-proof
This is [[T-LRULR|the Littlewood--Richardson rule]] with $\mu=(2,2)$ and $\nu=(2,1)$: the coefficient $c^{\lambda}_{\mu\nu}$ counts the semistandard tableaux of skew shape $\lambda/\mu$ and content $\nu$ whose word, read from right to left in each row from the top, is a lattice word.
:::

:::

::: {.pf-step #table}
The coefficient is $1$ for exactly the six shapes $(4,3)$, $(4,2,1)$, $(3,3,1)$, $(3,2,2)$, $(3,2,1,1)$, $(2,2,2,1)$, and $0$ for all others; hence
$$s_{(2,2)}s_{(2,1)}=s_{(4,3)}+s_{(4,2,1)}+s_{(3,3,1)}+s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}.$$

::: pf-proof
A shape $\lambda\vdash7$ must contain $(2,2)$ with $\lambda/(2,2)$ of size $3$; the candidates are $(5,2),(4,3),(4,2,1),(3,3,1),(3,2,2),(3,2,1,1),(2,2,2,1),(2,2,1,1,1)$. Filling the three skew boxes with two $1$s and one $2$ and imposing semistandardness and the lattice condition gives: $(4,3)$ one tableau (entries $(1,3)=1,(1,4)=1,(2,3)=2$); $(4,2,1)$ one ($(1,3)=1,(1,4)=1,(3,1)=2$); $(3,3,1)$ one ($(1,3)=1,(2,3)=2,(3,1)=1$); $(3,2,2)$ one ($(1,3)=1,(3,1)=1,(3,2)=2$); $(3,2,1,1)$ one ($(1,3)=1,(3,1)=1,(4,1)=2$); $(2,2,2,1)$ one ($(3,1)=1,(3,2)=1,(4,1)=2$); $(5,2)$ none, since its only filling $(1,1,2)$ has word $2,1,1$; and $(2,2,1,1,1)$ none, since its three boxes lie in one column and semistandardness forbids repeated entries there. An exhaustive enumeration over all fillings confirms these counts and gives no others.
:::

:::

::: {.pf-step #pieri}
(a) The expansion is checked by the second computation below, which evaluates $s_{(2,2)}s_{(2,1)}$ in the Schur-function basis from the Jacobi--Trudi identity and Pieri's formula and so reproduces the six coefficients of step [](#table){.pf-ref} without forming a Littlewood--Richardson tableau. Write $h_m\coloneqq s_{(m)}$ for the complete symmetric function of degree $m$, with $h_0\coloneqq1$ and $h_m\coloneqq0$ for $m<0$.

::: pf-proof

::: {.pf-step #jt}
$s_{(2,1)}=h_2h_1-h_3$.

::: pf-proof
By the [[T-JTRUDI|Jacobi--Trudi identity]] with $\lambda=(2,1)$ and $n=2$,
$$s_{(2,1)}=\det\begin{pmatrix}h_2&h_3\\ h_0&h_1\end{pmatrix}=h_2h_1-h_3h_0=h_2h_1-h_3.$$
:::

:::

::: {.pf-step #pieri-two}
$s_{(2,2)}s_{(2)}=s_{(4,2)}+s_{(3,2,1)}+s_{(2,2,2)}$ and $s_{(2,2)}s_{(3)}=s_{(5,2)}+s_{(4,2,1)}+s_{(3,2,2)}$.

::: pf-proof
Pieri's formula [@FH91, (A.7)] with $\lambda=(2,2)$ and $k=3$ sums $s_{(2,2)}s_{(m)}$ over the partitions $\nu$ with
$$\nu_1\ge2\ge\nu_2\ge2\ge\nu_3\ge0,\qquad \abs{\nu}=4+m.$$
For $m=2$ the chain forces $\nu_2=2$ and $\nu_1+\nu_3=4$ with $0\le\nu_3\le2$, so $\nu$ is $(4,2)$, $(3,2,1)$ or $(2,2,2)$; for $m=3$ it forces $\nu_2=2$ and $\nu_1+\nu_3=5$ with $0\le\nu_3\le2$, so $\nu$ is $(5,2)$, $(4,2,1)$ or $(3,2,2)$.
:::

:::

::: {.pf-step #pieri-one}
$s_{(2,2)}s_{(2)}s_{(1)}=s_{(5,2)}+s_{(4,3)}+2s_{(4,2,1)}+s_{(3,3,1)}+2s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}$.

::: pf-proof
Pieri's formula [@FH91, (A.7)] with $m=1$ allows a single box in each row the chain
$$\nu_1\ge\lambda_1\ge\nu_2\ge\lambda_2\ge\cdots\ge\nu_k\ge\lambda_k\ge0$$
admits, which gives
$$s_{(4,2)}s_{(1)}=s_{(5,2)}+s_{(4,3)}+s_{(4,2,1)},\qquad s_{(3,2,1)}s_{(1)}=s_{(4,2,1)}+s_{(3,3,1)}+s_{(3,2,2)}+s_{(3,2,1,1)},\qquad s_{(2,2,2)}s_{(1)}=s_{(3,2,2)}+s_{(2,2,2,1)}.$$
A box can be added to $(2,2,2)$ only in its first or fourth row, since a box in row $2$ or row $3$ would give the non-partition $(2,3,2)$ or $(2,2,3)$. Adding the three displays and collecting equal terms gives the claim.
:::

:::

::: {.pf-step #pieri-difference}
$s_{(2,2)}s_{(2,1)}=s_{(4,3)}+s_{(4,2,1)}+s_{(3,3,1)}+s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}$.

::: pf-proof
By steps [](#jt){.pf-ref}, [](#pieri-one){.pf-ref} and [](#pieri-two){.pf-ref},
$$s_{(2,2)}s_{(2,1)}=s_{(2,2)}s_{(2)}s_{(1)}-s_{(2,2)}s_{(3)}=\bigl(s_{(5,2)}+s_{(4,3)}+2s_{(4,2,1)}+s_{(3,3,1)}+2s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}\bigr)-\bigl(s_{(5,2)}+s_{(4,2,1)}+s_{(3,2,2)}\bigr),$$
and cancelling $s_{(5,2)}$, one copy of $s_{(4,2,1)}$ and one copy of $s_{(3,2,2)}$ leaves the six-term sum. The $s_\nu$ with $\nu\vdash7$ are linearly independent, being a basis of the symmetric functions of degree $7$ [@FH91, §A.1], so the coefficients of the expansion are exactly the ones displayed.
:::

:::

:::

:::

::: {.pf-step #check}
The expansion passes the hook-content cross-check: for every $n=2,\dots,9$ one has $s_{(2,2)}(1^{n})\,s_{(2,1)}(1^{n})=\sum_{\lambda}s_{\lambda}(1^{n})$ over the six listed $\lambda$ and no others.

::: pf-proof
Each $s_{\lambda}(1^{n})$ is computed by the hook-content formula $s_{\lambda}(1^{n})=\prod_{(i,j)\in\lambda}\frac{n+j-i}{h(i,j)}$, a polynomial in $n$ of degree $7$, one linear factor for each cell. The products and sums agree at $n=2,3,4,5,6,7,8,9$ — for instance $2,48,400,2000,7350,21952,56448,129600$ on both sides. This agreement checks the coefficients; it is not by itself a proof of the expansion, because the specialisation $f\mapsto f(1^{n})$ is not injective on the degree-seven symmetric functions: $m_{(2,2,2,1)}(1^{n})=m_{(4,1,1,1)}(1^{n})=4\binom n4$ for every $n$, so two distinct symmetric functions can agree at every $n$. The proof of the expansion is the enumeration of the Littlewood--Richardson tableaux in step [](#table){.pf-ref}.
:::

:::

::: {.pf-step #interpretation}
(b) The coefficient $c^{\lambda}_{(2,2),(2,1)}$ is the multiplicity of the irreducible $S^{\lambda}$ of $S_{7}$ in the representation induced from the $S_{4}\times S_{3}$-module $S^{(2,2)}\boxtimes S^{(2,1)}$; equivalently it is the multiplicity of the $\GL_{m}$-irreducible of highest weight $\lambda$ in the tensor product $V_{(2,2)}\otimes V_{(2,1)}$.

::: pf-proof
The Littlewood–Richardson rule is exactly the branching rule for induction: for $\abs{\mu}+\abs{\nu}=\abs{\lambda}$ the coefficient $c^{\lambda}_{\mu\nu}$ equals $\langle\chi^{\lambda},\operatorname{Ind}_{S_{\abs\mu}\times S_{\abs\nu}}^{S_{\abs\lambda}}(\chi^{\mu}\boxtimes\chi^{\nu})\rangle$, the multiplicity of $S^{\lambda}$ in the induced module — here $\abs\mu=4$, $\abs\nu=3$, $\abs\lambda=7$. The passage to $\GL_{m}$ is Schur–Weyl duality, under which the Schur function $s_{\lambda}$ is the character of the irreducible $V_{\lambda}$ and multiplication of symmetric functions is the tensor product; the coefficient of $s_{\lambda}$ is then the multiplicity of $V_{\lambda}$ in $V_{(2,2)}\otimes V_{(2,1)}$ (for $m\ge7$, where all six $\lambda$ occur).
:::

:::

::: {.pf-qed}
The expansion is $s_{(2,2)}s_{(2,1)}=s_{(4,3)}+s_{(4,2,1)}+s_{(3,3,1)}+s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}$ by step [](#table){.pf-ref}, confirmed by the second computation of step [](#pieri){.pf-ref} and consistent with the hook-content values of step [](#check){.pf-ref}, with the representation-theoretic meaning of the coefficients in step [](#interpretation){.pf-ref}.
:::

:::

:::
