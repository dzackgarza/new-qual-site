---
schema: qual/card@1
id: P-ALGS11G
kind: problem
title: Torsion, free, and torsionfree modules over an integral domain
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Integral Domains
relations: []
review: draft

audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 7 of the UCSD Algebra Qualifying Exam, Spring 2011, p. 2 of the
    two-page paper retained at assets/attachments/SP11_200_Algebra_Qual.pdf, is the statement the
    card answers, and the paragraph at the head of the solution records that the paper prints the
    questions and no solutions, so the argument is the card's own. Checked: the three parts and the
    printed instruction to prove or give a justified counterexample against the paper's text layer
    at the page named, and the three verdicts against them (false, true, false);
    `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering and the QED. Not
    checked: no retained solution exists to compare the argument with (the existence of a retained
    solution set would change what the card should say, and none is recorded for this collection),
    and no other card of the collection in this pass.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 7 of the official UCSD Spring 2011 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Supplied explicit counterexamples for (i) and (iii) and a basis argument for (ii).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof. The last step was broken structurally: its boxed answer lay after
    the step and after the proof root had both been closed, so the filter never saw it and the page showed
    the claim "Hence the answers are" followed by an orphaned formula. The display is now inside the step,
    which carries a justification collecting the three verdicts. The mathematics is unchanged. Nothing in
    the statement was changed.

---

::: {.problem}
Let $R$ be an integral domain.
Prove or give an example to disprove (with justification):

(i) If $M$ is a torsion $R$-module, then $\mathrm{Ann}_R(M) \neq 0$.

(ii) If $M$ is a free $R$-module, then $M$ is torsionfree.

(iii) If $M$ is a torsionfree $R$-module, then $M$ is free.
:::

::: {.solution}

The problem is Problem 7 of the UCSD Algebra Qualifying Exam, Spring 2011, printed on p. 2 of the two-page paper retained at `assets/attachments/SP11_200_Algebra_Qual.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and it supplies the justification each part asks for — a direct sum of cyclic groups for (i), the basis argument for (ii), and $\QQ$ over $\ZZ$ for (iii) — together with the verifications that the examples have the properties asserted of them.

::: pf

::: pf-step

Statement (i) is false.

::: pf-proof

Take $R=\ZZ$ and
$$
M=\bigoplus_{n\ge2}\ZZ/n\ZZ.
$$
Every element of $M$ has only finitely many nonzero coordinates, so it is killed by the least common multiple of the corresponding finitely many integers $n$.
Thus $M$ is a torsion $\ZZ$-module.

However, if $0\ne a\in\ZZ$, choose $n>\abs{a}$ with $n\nmid a$.
The element whose only nonzero coordinate is $1\in\ZZ/n\ZZ$ is not killed by $a$.
Hence no nonzero integer annihilates all of $M$, so
$$
\operatorname{Ann}_{\ZZ}(M)=0.
$$

:::

:::

::: pf-step

Statement (ii) is true.

::: pf-proof

Let $M$ be a free $R$-module with basis $(e_i)_{i\in I}$.
Suppose $0\ne r\in R$ and $rm=0$.
Write
$$
m=\sum_{i\in I}a_i e_i
$$
with only finitely many nonzero $a_i$.
Then
$$
0=rm=\sum_i (ra_i)e_i.
$$
Linear independence of the basis gives $ra_i=0$ for every $i$.
Since $R$ is an integral domain and $r\ne0$, each $a_i=0$.
Thus $m=0$, so $M$ is torsionfree.

:::

:::

::: pf-step

Statement (iii) is false.

::: pf-proof

Take $R=\ZZ$ and $M=\QQ$.
Since $\ZZ$ is a domain, if $0\ne n\in\ZZ$ and $nq=0$ in $\QQ$, then $q=0$; hence $\QQ$ is torsionfree as a $\ZZ$-module.

It is not free.
Indeed, $\QQ$ is divisible: for every $q\in\QQ$ and every integer $n\ne0$, there is $q/n\in\QQ$ with $n(q/n)=q$.
A nonzero free abelian group is not divisible: if $(e_i)$ is a basis and $e_j$ is one basis element, there is no element $x$ with $2x=e_j$, since comparing the coefficient of $e_j$ would require an integer coefficient $1/2$.
Therefore $\QQ$ is not a free $\ZZ$-module.

:::

:::

::: pf-step

Hence the answers are
$$
\boxed{\text{(i) false,}\qquad\text{(ii) true,}\qquad\text{(iii) false.}}
$$

::: pf-proof
The three verdicts collect the conclusions of the three parts proved above: the first assertion fails, the second holds, and the third fails.
:::

:::

:::
:::
