---
schema: qual/card@1
id: P-MMAQ-CBHJDNZVJP
kind: problem
title: Hilbert basis theorem for $R[x]$ and $R[[x]]$
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 1 of the Algebra Preliminary Examination 2017 (University of
    Washington), printed p. 1 of the single-page paper retained at
    assets/attachments/UW-Algebra-Qual-2017.pdf, is the statement the card answers, and the
    paragraph at the head of the solution records that the paper prints no solutions, so the
    argument is the card's own. Checked: the statement, including the printed instruction to prove
    the Hilbert basis theorem rather than invoke it, against the paper's text layer at the page
    named; the solution read for the leading-coefficient argument for R[x] and the
    coefficient-ideal argument for R[[x]]; `qualc.authoring check` on the card, and `tmp/lam.sh` for
    the numbering and the QED. Not checked: no retained solution set exists for this paper to
    compare the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, and both halves checked. R[x]: the
    ideals L_d of x^d-coefficients of elements of degree at most d are ideals, form an ascending
    chain (x f has the same x^d-coefficient one degree up), stabilize by the ascending chain
    condition, and finitely many lifts of generators of L_0..L_N generate I by induction on degree,
    with the two cases m <= N and m > N (using L_m = L_N and the shifted elements x^{m-N} f_Nj)
    separated. R[[x]]: the ideals J_n of x^n-coefficients of elements of I inside x^n R[[x]] are
    ideals with J_n contained in J_{n+1}, stabilize, and the coefficient-by-coefficient cancellation
    is now written as an induction with the two cases m <= N and m > N; the corrections assemble
    into formal series h_nj, since the coefficient of x^k receives exactly one contribution, from
    stage n + k. Well-definedness of the assembled identity is stated, as the prose did. The
    statement's instruction to prove rather than use the Hilbert basis theorem is honoured: the
    theorem appears as the conclusion of a step, not as an input. Statement unchanged; the card
    says the argument is its own.
---

::: {.problem}
Let $R$ be a Noetherian ring.
Prove that $R[x]$ and $R[[x]]$ are both Noetherian.
(The first part of the question is asking you to prove the Hilbert Basis Theorem, not to use it!)
:::


::: {.solution}
For $R[x]$ the proof is the classical one: the ideals $L_d$ of leading coefficients of elements of $I$ of degree $d$ form an ascending chain, which stabilizes at some $N$, and finitely many elements lifting generators of $L_0,\dots,L_N$ generate $I$ by induction on degree. For $R[[x]]$ the same idea is applied to the ideals $J_n$ of coefficients of $x^n$ in elements of $I$ whose lowest term is $x^n$; after the chain stabilizes one cancels coefficients degree by degree, and the corrections assemble into formal series. The argument is this card's own: Problem 1 of the Algebra Preliminary Examination 2017 (University of Washington), printed p. 1 of the single-page paper retained at `assets/attachments/UW-Algebra-Qual-2017.pdf`, is the statement answered here, no retained solution set covers it, and the Hilbert basis theorem is proved here rather than invoked.

::: pf

::: {.pf-step #L-ideal}
For $d\ge0$ let $L_d$ be the set of coefficients of $x^d$ in elements of $I$ of degree at most $d$. Then $L_d$ is an ideal of $R$ and $L_d\subseteq L_{d+1}$.

::: pf-proof
$0\in L_d$ (the zero polynomial). If $a,a'\in L_d$ with witnesses $f,f'$, then $f\pm f'$ has degree at most $d$ and $x^d$-coefficient $a\pm a'$, so $a\pm a'\in L_d$; and for $r\in R$ the polynomial $rf$ has $x^d$-coefficient $ra$, so $ra\in L_d$. Hence $L_d$ is an ideal. For the inclusion: if $f$ has degree at most $d$ and $x^d$-coefficient $a$, then $xf$ has degree at most $d+1$ and $x^{d+1}$-coefficient $a$, so $a\in L_{d+1}$.
:::

:::


::: {.pf-step #stabilize}
The chain $L_0\subseteq L_1\subseteq\cdots$ stabilizes: there is $N$ with $L_m=L_N$ for all $m\ge N$.

::: pf-proof
$R$ is Noetherian, so it satisfies the ascending chain condition on ideals; an ascending chain of ideals must be eventually constant, which gives $N$.
:::

:::


::: {.pf-step #choose}
For each $0\le d\le N$ there are finitely many $f_{d1},\dots,f_{dr_d}\in I$, of degree at most $d$, whose $x^d$-coefficients generate $L_d$.

::: pf-proof
$L_d$ is an ideal of the Noetherian ring $R$, hence finitely generated; choose generators $a_1,\dots,a_{r_d}$ and, for each, a witness $f_{dj}\in I$ of degree at most $d$ with $x^d$-coefficient $a_j$. Finitely many $d$'s, finitely many generators each, so the total is finite.
:::

:::


::: {.pf-step #generate}
$I$ is generated by the finite set $\{f_{dj}:0\le d\le N,\ 1\le j\le r_d\}$.

::: pf-proof
Induct on the degree of $f\in I$, the case $f=0$ being trivial. Let $m=\deg f$ and $a$ its leading coefficient. If $m\le N$, then $a\in L_m$ is an $R$-linear combination $a=\sum_jc_jb_j$ of the $x^m$-coefficients $b_j$ of the $f_{mj}$; the polynomial $f-\sum_jc_jf_{mj}$ lies in $I$ and has degree below $m$, so by induction it lies in the ideal generated by the chosen set, and hence so does $f$. If $m>N$, then $a\in L_m=L_N$, so $a=\sum_jc_jb_j$ with $b_j$ the $x^N$-coefficients of $f_{Nj}$; each $x^{m-N}f_{Nj}$ has degree $m$ and $x^m$-coefficient $b_j$, so $f-\sum_jc_jx^{m-N}f_{Nj}\in I$ has degree below $m$, and induction finishes. So every element of $I$ lies in the ideal generated by the finite set, which is contained in $I$; hence they are equal.
:::

:::


::: {.pf-step #poly-noetherian}
$R[x]$ is Noetherian.

::: pf-proof
Every ideal $I\subseteq R[x]$ is finitely generated by step [](#generate){.pf-ref}, which is the definition of $R[x]$ being Noetherian. This is the Hilbert basis theorem, proved and not assumed.
:::

:::


::: {.pf-step #J-ideal}
For $n\ge0$ let $J_n$ be the set of coefficients of $x^n$ in elements of $I\cap x^nR[[x]]$. Then $J_n$ is an ideal of $R$ and $J_n\subseteq J_{n+1}$.

::: pf-proof
$0\in J_n$. If $a,a'\in J_n$ with witnesses $f,f'$, then $f\pm f'$ lies in $I\cap x^nR[[x]]$ and has $x^n$-coefficient $a\pm a'$; and $rf$ likewise, so $J_n$ is an ideal. If $f\in I\cap x^nR[[x]]$ has $x^n$-coefficient $a$, then $xf\in I\cap x^{n+1}R[[x]]$ has $x^{n+1}$-coefficient $a$, so $a\in J_{n+1}$.
:::

:::


::: {.pf-step #J-stabilize}
There is $N$ with $J_m=J_N$ for all $m\ge N$, and for $0\le n\le N$ there are finitely many $g_{n1},\dots,g_{nr_n}\in I\cap x^nR[[x]]$ whose $x^n$-coefficients generate $J_n$.

::: pf-proof
The chain $J_0\subseteq J_1\subseteq\cdots$ stabilizes by the ascending chain condition in the Noetherian ring $R$. Each $J_n$ is finitely generated, and a finite generating set of coefficients is lifted to witnesses as in step [](#choose){.pf-ref}.
:::

:::


::: {.pf-step #cancel}
Let $I_0$ be the ideal generated by all the $g_{nj}$, $0\le n\le N$. Then every $f\in I$ lies in $I_0$.

::: pf-proof
We cancel the coefficients of $f$ in increasing order. Suppose that after finitely many corrections the current remainder $f'$ lies in $I\cap x^mR[[x]]$, i.e. its coefficients below degree $m$ vanish. If $m\le N$, the $x^m$-coefficient $a$ of $f'$ lies in $J_m$, so $a=\sum_jc_jb_j$ with $b_j$ the $x^m$-coefficients of the $g_{mj}$; subtracting $\sum_jc_jg_{mj}$ kills the $x^m$-coefficient and changes no coefficient of lower degree, because each $g_{mj}$ lies in $x^mR[[x]]$. If $m>N$, then $a\in J_m=J_N$, so $a=\sum_jc_jb_j$ with $b_j$ the $x^N$-coefficients of the $g_{Nj}$, and subtracting $\sum_jc_jx^{m-N}g_{Nj}$ kills the $x^m$-coefficient without disturbing lower ones. By induction on $m$ every coefficient of $f$ is killed by correction terms of this form.
:::

:::


::: {.pf-step #assemble}
The corrections assemble to the identity $f=\sum_{n\le N}\sum_jh_{nj}g_{nj}$ with $h_{nj}\in R[[x]]$.

::: pf-proof
For each pair $(n,j)$ let $h_{nj}$ be the formal series whose coefficient of $x^k$ is the coefficient used at stage $m=n+k$ multiplying $g_{nj}$; this is well defined because exactly one stage contributes to each degree, and it lies in $R[[x]]$. Hence $h_{nj}\in R[[x]]$. The coefficient of any fixed power $x^m$ in $\sum_{n\le N}\sum_jh_{nj}g_{nj}$ depends only on the finitely many stages up to $m$, where the recursive construction says the coefficient agrees with that of $f$; so the identity holds in $R[[x]]$, and $f\in I_0$.
:::

:::


::: {.pf-step #series-noetherian}
$R[[x]]$ is Noetherian.

::: pf-proof
Every ideal $I\subseteq R[[x]]$ equals the finitely generated ideal $I_0$ of step [](#assemble){.pf-ref}, since $I_0\subseteq I$ by construction and $I\subseteq I_0$ is what was proved.
:::

:::


::: {.pf-step #conclusion}
Both $R[x]$ and $R[[x]]$ are Noetherian when $R$ is.

::: pf-proof
Steps [](#poly-noetherian){.pf-ref} and [](#series-noetherian){.pf-ref} give the two assertions, each proved from the ascending chain condition in $R$ rather than from the Hilbert basis theorem as a black box.
:::

:::

:::
:::
