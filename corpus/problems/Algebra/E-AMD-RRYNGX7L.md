---
schema: qual/card@1
id: E-AMD-RRYNGX7L
kind: problem
title: The cokernel of $A\in M_n(\ZZ)$ is finite of order $\abs{\det A}$ iff $\det A\neq
  0$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used Smith normal form to identify both finiteness and the cokernel order.
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (two
    assertions, no repair needed), and the existing prose solution against a fresh
    re-derivation: Smith normal form gives P, Q unimodular with PAQ diagonal
    (d_1 | ... | d_r, then zeros); multiplication by P is an isomorphism of Z^n and
    im(PAQ) = P(im A) because Q is surjective, so the cokernels are isomorphic; the
    cokernel of the diagonal matrix is the direct sum of the Z/d_i and Z^{n-r};
    that is finite exactly when r = n, and r is the rank over Q, unchanged by P and
    Q, while full rank is equivalent to det A != 0; and in that case the order is
    prod d_i = |det(PAQ)| = |det A| because P and Q are unimodular. Correct. The
    prose's "they do not change the cokernel up to isomorphism" is now given as an
    explicit isomorphism, and the rank facts are stated rather than assumed. No
    source solution is retained for this card, so no source comparison was made.
    What was not checked: any printed source.
---

::: {.exercise}
Prove that for $A\in M_n(\ZZ)$, viewed as $A:\ZZ^n\to\ZZ^n$, the cokernel is finite if and only if $\det A\ne0$, and in that case
$$
\abs{\coker A}=\abs{\det A}.
$$
:::

::: {.solution}
Let $A\in\Mat_n(\ZZ)$ act on $\ZZ^n$ by multiplication, and write $\coker A=\ZZ^n/A\ZZ^n$ for its cokernel.

::: pf

::: {.pf-step #snf}
There are $P,Q\in\GL_n(\ZZ)$ with $PAQ=\operatorname{diag}(d_1,\ldots,d_r,0,\ldots,0)$, where $d_1\mid d_2\mid\cdots\mid d_r$ are positive integers.

::: pf-proof
This is the existence of the Smith normal form over a principal ideal domain: row and column operations that add an integer multiple of one row or column to another, and that interchange or negate rows or columns, are invertible over $\ZZ$ and carry $A$ to a diagonal matrix with nonnegative entries in which each diagonal entry divides the next. The product of the operations on the left is $P$ and on the right is $Q$, both invertible over $\ZZ$, and entries equal to zero may be moved to the end because $d_i\mid d_{i+1}$ forces $d_{i+1}=0$ whenever $d_i=0$; so the nonzero entries are the first $r$. Finally $A\neq0$ or $A=0$ give $r\geq1$ or $r=0$ accordingly, the argument being uniform.
:::

:::

::: {.pf-step #coker}
$\coker A\cong\bigoplus_{i=1}^{r}\ZZ/d_i\ZZ\oplus\ZZ^{\,n-r}$.

::: pf-proof
Multiplication by $P$ is an automorphism of $\ZZ^n$, and $PAQ=P\,A\,Q$ has image $P(A\ZZ^n)$ because $Q$ is surjective; hence $x+P(A\ZZ^n)\mapsto P^{-1}x+A\ZZ^n$ is an isomorphism $\coker(PAQ)\to\coker A$. For the diagonal matrix $D=\operatorname{diag}(d_1,\ldots,d_r,0,\ldots,0)$ the image $D\ZZ^n$ is $d_1\ZZ\oplus\cdots\oplus d_r\ZZ\oplus 0$, so $\coker D=\bigoplus_{i\leq r}\ZZ/d_i\ZZ\oplus\ZZ^{n-r}$.
:::

:::

::: {.pf-step #finite}
$\coker A$ is finite if and only if $r=n$, if and only if $\operatorname{rank}_\QQ A=n$, if and only if $\det A\neq0$.

::: pf-proof
By step [](#coker){.pf-ref} the group is a direct sum of the finite groups $\ZZ/d_i\ZZ$ and of $\ZZ^{n-r}$, which is finite exactly when $n-r=0$. The rank of $D$ over $\QQ$ is the number $r$ of its nonzero diagonal entries, and rank is unchanged by multiplication by the invertible matrices $P,Q$ (over $\QQ$ they are invertible linear maps), so $r=\operatorname{rank}_\QQ A$. Finally $A$ is invertible over $\QQ$, equivalently of full rank, exactly when $\det A\neq0$.
:::

:::

::: {.pf-step}
If $\det A\neq0$ then $\abs{\coker A}=\abs{\det A}$.

::: pf-proof
In that case $r=n$ by step [](#finite){.pf-ref}, so $\coker A\cong\bigoplus_{i=1}^{n}\ZZ/d_i\ZZ$ by step [](#coker){.pf-ref} and has order $\prod_{i=1}^n d_i$. On the other hand $\det(PAQ)=\det P\cdot\det A\cdot\det Q$ and $\det P,\det Q=\pm1$ because $P,Q\in\GL_n(\ZZ)$ are unimodular, so
$$\abs{\det A}=\abs{\det(PAQ)}=\prod_{i=1}^{n}d_i.$$
The two quantities are equal, which completes the proof of both assertions.
:::

:::

:::
:::
