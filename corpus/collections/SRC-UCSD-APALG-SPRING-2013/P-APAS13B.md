---
schema: qual/card@1
id: P-APAS13B
kind: problem
title: Unique Hermitian splitting $A=S+iT$ and eigenvalue real/imaginary bounds
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. Added: the verification that v^H C v is real for Hermitian C (via the
    conjugate transpose), which is what makes the two Rayleigh quotients the real and imaginary
    parts rather than only formal expressions; the spectral theorem named for the convex
    combination; and the hypothesis v != 0 in the quotient bound. Not claimed: a retained
    solution set; the provenance names the examination paper. Statement and conclusion
    unchanged.
---

::: {.problem}
(a) Prove that every $A\in M_n$ may be written uniquely as $A=S+iT$, where $S$ and $T$ are Hermitian.

(b) For any $A\in M_n$, consider the unique expansion $A=S+iT$, where $S$ and $T$ are Hermitian.
Prove that for any $\lambda\in\operatorname{eig}(A)$, it holds that
$$
\lambda_n(S)\le\operatorname{Re}(\lambda)\le\lambda_1(S)
\quad\text{and}\quad
\lambda_n(T)\le\operatorname{Im}(\lambda)\le\lambda_1(T),
$$
where, by convention, the eigenvalues of a Hermitian matrix $C\in M_n$ are arranged in nonincreasing order, i.e.,
$$
\lambda_1(C)\ge\lambda_2(C)\ge\cdots\ge\lambda_n(C).
$$
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2013 applied-algebra examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $A\in M_n$, $A^H$ is the Hermitian transpose, and the eigenvalues of a Hermitian matrix $C$ are ordered $\lambda_1(C)\ge\cdots\ge\lambda_n(C)$.

::: pf

::: {.pf-step #part-a-existence}
$S=\frac{A+A^H}{2}$ and $T=\frac{A-A^H}{2i}$ are Hermitian and $S+iT=A$.

::: pf-proof
$S^H=\frac{A^H+A}{2}=S$; and since $\overline{i}=-i$,
$$
T^H=\frac{A^H-A}{\overline{2i}}=\frac{A^H-A}{-2i}=\frac{A-A^H}{2i}=T .
$$
Then $S+iT=\frac{A+A^H}{2}+\frac{A-A^H}{2}=A$.

:::

:::

::: {.pf-step #part-a-uniqueness}
If $A=S_1+iT_1$ with $S_1,T_1$ Hermitian, then $S_1=S$ and $T_1=T$.

::: pf-proof
Taking Hermitian transposes of $A=S_1+iT_1$ gives $A^H=S_1-iT_1$. Adding and subtracting,
$$
S_1=\frac{A+A^H}{2},\qquad T_1=\frac{A-A^H}{2i},
$$
which are $S$ and $T$.

:::

:::

::: {.pf-step #rayleigh-split}
If $Av=\lambda v$ with $v\ne0$, then $\operatorname{Re}\lambda=\frac{v^HSv}{v^Hv}$ and $\operatorname{Im}\lambda=\frac{v^HTv}{v^Hv}$.

::: pf-proof
$v^HAv=\lambda v^Hv$, and substituting $A=S+iT$ gives
$$
\lambda=\frac{v^HSv}{v^Hv}+i\,\frac{v^HTv}{v^Hv}.
$$
For Hermitian $C$ the number $v^HCv=\overline{v^HCv}$ is real — indeed $(v^HCv)^H=v^HC^Hv=v^HCv$ — so the two quotients are real and are the real and imaginary parts of $\lambda$.

:::

:::

::: {.pf-step #quotient-bounds}
For Hermitian $C$ and $v\ne0$, $\lambda_n(C)\le\frac{v^HCv}{v^Hv}\le\lambda_1(C)$.

::: pf-proof
By the spectral theorem there is an orthonormal eigenbasis $u_j$ of $C$ with $Cu_j=\lambda_j(C)u_j$; writing $v=\sum_jc_ju_j$ gives $\frac{v^HCv}{v^Hv}=\frac{\sum_j\abs{c_j}^2\lambda_j(C)}{\sum_j\abs{c_j}^2}$, a convex combination of the $\lambda_j(C)$ with the nonnegative weights $\abs{c_j}^2/\sum_k\abs{c_k}^2$ summing to $1$, hence lying between the least and greatest.

:::

:::

::: {.pf-step #part-b}
$\lambda_n(S)\le\operatorname{Re}\lambda\le\lambda_1(S)$ and $\lambda_n(T)\le\operatorname{Im}\lambda\le\lambda_1(T)$.

::: pf-proof
Apply step [](#quotient-bounds){.pf-ref} to $C=S$ and to the vector $v$ of step [](#rayleigh-split){.pf-ref}: the quotient is $\operatorname{Re}\lambda$, giving the first pair of inequalities; the same with $C=T$ gives the second.

:::

:::

:::
:::
