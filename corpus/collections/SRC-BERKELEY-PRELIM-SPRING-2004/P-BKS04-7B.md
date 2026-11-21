---
schema: qual/card@1
id: P-BKS04-7B
kind: problem
title: A common eigenvector when $AB-BA$ is a linear combination of $A$ and $B$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2004
    prelim solutions, Problem 7B, PDF p. 8, the file named in the collection's provenance),
    which the card now cites; it previously carried no citation. Added: why the eigenspace of A
    is B-stable in the commuting case, so that a common eigenvector exists over C; the proof
    that some eigenvalue lambda of A has lambda + beta not an eigenvalue, which the sheet
    asserts from finiteness alone and which needs that the translation has no fixed point when
    beta != 0; and the last step, that a common eigenvector of A and C is an eigenvector of B
    because B is a linear combination of them. Statement unchanged.
---

::: {.problem}
Let $A$ and $B$ be $n\times n$ matrices with complex entries, such that $AB-BA$ is a linear combination of $A$ and $B$. Prove that there exists a nonzero vector $v$ that is an eigenvector of both $A$ and $B$.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2004 prelim solutions, Problem 7B, PDF p. 8** (`assets/attachments/s04solution.pdf`, the file named in this collection's `provenance`): the split into the commuting case and $C=AB-BA=\alpha A+\beta B$ with $\beta\ne0$, the identity $AC-CA=\beta C$, and the choice of an eigenvalue $\lambda$ with $\lambda+\beta$ not an eigenvalue of $A$ are that solution's. The card proves the last of these choices and draws the conclusion for $B$, both of which the sheet leaves implicit.

Throughout $A,B\in M_n(\CC)$ with $AB-BA=\alpha A+\beta B$ for $\alpha,\beta\in\CC$; "eigenvector of $A$" means a nonzero vector.

::: pf

::: {.pf-step #commuting}
If $\alpha=\beta=0$ there is a common eigenvector.

::: pf-proof
Then $AB=BA$, so for an eigenvector $v\ne0$ of $A$ with eigenvalue $\lambda$ the eigenspace $E_\lambda=\ker(A-\lambda I)$ is $B$-stable: if $Aw=\lambda w$ then $A(Bw)=B(Aw)=\lambda Bw$. Over $\CC$, every linear operator on a nonzero finite-dimensional space has an eigenvector, so $B$ restricted to $E_\lambda$ has an eigenvector $w\in E_\lambda$, and $w$ is a common eigenvector.

:::

:::

::: {.pf-step #reduction}
If $\beta\ne0$ then $B=\beta^{-1}(C-\alpha A)$ with $C\coloneqq AB-BA$, and $AC-CA=\beta C$; a common eigenvector of $A$ and $C$ is one of $A$ and $B$.

::: pf-proof
$C=\alpha A+\beta B$ by hypothesis, so $B=(C-\alpha A)/\beta$. Since $C$ is built from $A$ and $B$,
$$
AC-CA=\alpha(AA-AA)+\beta(AB-BA)=\beta(AB-BA)=\beta C .
$$
If $v$ is a common eigenvector of $A$ and $C$, then $Bv=\beta^{-1}(Cv-\alpha Av)$ is a scalar multiple of $v$, so $v$ is an eigenvector of $B$ as well. If $\alpha\ne0$ the roles of $A$ and $B$ may be exchanged, so $\beta\ne0$ may be assumed.

:::

:::

::: {.pf-step #eigenvalue}
There is an eigenvalue $\lambda$ of $A$ with $\lambda+\beta\notin\operatorname{spec}(A)$.


::: pf-proof
$\operatorname{spec}(A)$ is a finite nonempty set of at most $n$ complex numbers, and $\lambda\mapsto\lambda+\beta$ has no fixed point when $\beta\ne0$. If $\lambda+\beta$ were an eigenvalue for every eigenvalue $\lambda$, that map would carry the finite set $\operatorname{spec}(A)$ into itself and hence bijectively onto itself, so iterating would place the infinitely many distinct values $\lambda,\lambda+\beta,\lambda+2\beta,\dots$ inside the finite set $\operatorname{spec}(A)$, a contradiction.

:::

:::

::: {.pf-step #common}
With $\lambda$ as above and $v\ne0$ with $Av=\lambda v$, one has $Cv=0$, so $v$ is a common eigenvector of $A$ and $C$.

::: pf-proof
$ACv=CAv+\beta Cv=\lambda Cv+\beta Cv=(\lambda+\beta)Cv$ by step [](#reduction){.pf-ref}. So $Cv$ is either $0$ or an eigenvector of $A$ with eigenvalue $\lambda+\beta$; that eigenvalue is not in $\operatorname{spec}(A)$ by step [](#eigenvalue){.pf-ref}, so $Cv=0$. Hence $Av=\lambda v$ and $Cv=0\cdot v$ with $v\ne0$, that is $v$ is a common eigenvector.

:::

:::

::: {.pf-step #conclusion}
There is a nonzero $v$ that is an eigenvector of both $A$ and $B$.

::: pf-proof
In the commuting case this is step [](#commuting){.pf-ref}; otherwise step [](#common){.pf-ref} produces $v$, and step [](#reduction){.pf-ref} makes it an eigenvector of $B$.

:::

:::

:::
:::
