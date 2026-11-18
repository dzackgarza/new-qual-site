---
schema: qual/card@1
id: P-APAS23B
kind: problem
title: Real eigenvalues of Hermitian matrices; Courant–Fischer; Rayleigh extrema
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
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the conjugate-transpose computation of (v^H A v) using A^H = A, and the
    observation, recorded on the card, that part (c) does not need the Courant-Fischer theorem
    that part (b) states - the two extrema over unit vectors are delivered by the spectral
    theorem alone, the theorem's content being the intermediate eigenvalues. The statement of
    Courant-Fischer is reproduced with the ordering the problem fixes. Not claimed: a retained
    solution set; the provenance names the examination paper.
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

Consider a Hermitian matrix $A \in M_n$.

(a) Show that the eigenvalues of $A$ are real.

(b) Assume that the eigenvalues of $A$ are ordered so that $\lambda_n \le \lambda_{n-1} \le \cdots \le \lambda_2 \le \lambda_1$.
State, but do not prove, the Courant–Fischer theorem.

(c) Prove that
$$
\lambda_n = \min_{x^H x = 1} x^H A x,
\quad\text{and}\quad
\lambda_1 = \max_{x^H x = 1} x^H A x.
$$
:::


::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2023 applied-algebra examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $A\in M_n$ is Hermitian, $A^H=A$, and its eigenvalues are ordered $\lambda_n\le\cdots\le\lambda_1$.

::: pf

::: {.pf-step #part-a}
Every eigenvalue of $A$ is real.

::: pf-proof
Let $Av=\lambda v$ with $v\ne0$. Then $v^HAv=\lambda v^Hv$ and, taking conjugate transposes and using $A^H=A$,
$$
\overline{\lambda}\,v^Hv=\overline{\lambda v^Hv}=(v^HAv)^H=v^HA^Hv=v^HAv=\lambda v^Hv .
$$
Since $v^Hv>0$ and is a positive real number, $\overline\lambda=\lambda$, so $\lambda\in\RR$.

:::

:::

::: {.pf-step #part-b}
With the ordering $\lambda_1\ge\cdots\ge\lambda_n$, the Courant–Fischer theorem states that for $1\le k\le n$,
$$
\lambda_k=\max_{\substack{S\le\CC^n\\\dim S=k}}\ \min_{\substack{x\in S\\ x^Hx=1}}x^HAx=\min_{\substack{S\le\CC^n\\\dim S=n-k+1}}\ \max_{\substack{x\in S\\ x^Hx=1}}x^HAx .
$$

::: pf-proof
This is the theorem as stated in the problem, which asks for it to be stated and not proved; it is recorded here so that the statement is available, and it is not used in step [](#part-c){.pf-ref}.

:::

:::

::: {.pf-step #spectral}
There is an orthonormal basis $u_1,\dots,u_n$ of $\CC^n$ with $Au_i=\lambda_iu_i$.

::: pf-proof
A Hermitian matrix is normal, hence unitarily diagonalizable: $A=UDU^H$ with $U$ unitary and $D$ diagonal, real by step [](#part-a){.pf-ref}; the columns of $U$ are the $u_i$ and the diagonal entries the $\lambda_i$.

:::

:::

::: {.pf-step #bounds}
For every $x$ with $x^Hx=1$, $\lambda_n\le x^HAx\le\lambda_1$, with equality at $x=u_n$ and at $x=u_1$ respectively.

::: pf-proof
Write $x=\sum_ic_iu_i$, so that $x^Hx=\sum_i\abs{c_i}^2=1$ and $x^HAx=\sum_i\lambda_i\abs{c_i}^2$. This is a convex combination of $\lambda_n,\dots,\lambda_1$ with nonnegative weights $\abs{c_i}^2$ summing to $1$, so it lies in $[\lambda_n,\lambda_1]$; at $x=u_n$ the weights concentrate on $\lambda_n$ and at $x=u_1$ on $\lambda_1$.

:::

:::

::: {.pf-step #part-c}
$\lambda_n=\min_{x^Hx=1}x^HAx$ and $\lambda_1=\max_{x^Hx=1}x^HAx$.

::: pf-proof
Step [](#bounds){.pf-ref} gives the two inequalities for all unit $x$, and equality at $u_n$, respectively $u_1$; the set of unit vectors is nonempty, so the minimum and maximum exist and equal $\lambda_n$ and $\lambda_1$. No use of the Courant–Fischer theorem is needed: with $x^Hx=1$ the extrema over single vectors already give $\lambda_n$ and $\lambda_1$, and the theorem's content is the corresponding statement for intermediate $\lambda_k$, which requires the constraint to other subspaces.

:::

:::

:::
:::
