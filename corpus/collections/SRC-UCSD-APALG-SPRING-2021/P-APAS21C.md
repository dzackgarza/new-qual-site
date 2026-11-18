---
schema: qual/card@1
id: P-APAS21C
kind: problem
title: SVD; variational characterization of $\sigma_1$; field of values and numerical radius
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the SVD statement as stated rather than proved,
    the operator bound ||Ax|| <= sigma_1 ||x|| derived from the SVD (which the earlier prose
    used without proof), the two-sided variational identity for sigma_1 including the case A
    = 0, the three definitions with the existence of the maxima, and the chain rho <= omega
    <= sigma_1 with the eigenvalue identity x^H A x = lambda at a unit eigenvector. The
    argument is the card's own; no retained set is cited. No repair needed to the answers.
---

::: {.problem}
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex components, $M_n$ denotes the set $M_{m,n}$ with $m = n$, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) State, but do not prove, the singular-value decomposition theorem.

(b) For a given $A \in M_{m,n}$, prove that
$$
\sigma_1(A) = \max_{x,y \ne 0} \frac{\abs{y^H A x}}{\norm{y}_2 \norm{x}_2},
$$
where $\sigma_1(A)$ is the largest singular value of $A$.

(c) For any $A \in M_n$, define (i) the field of values $F(A)$; (ii) the spectral radius $\rho(A)$; and the numerical radius $\omega(A)$.
Prove that $\rho(A) \le \omega(A) \le \sigma_1(A)$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Throughout, $\sigma_{1}(A)$ is the largest singular value of $A$, $\norm{\cdot}_{2}$ the Euclidean norm, and for a vector $x$ one writes $x^{H}$ for its Hermitian transpose.

::: pf

::: {.pf-step #svd}
(a) The singular-value decomposition theorem: for every $A\in M_{m,n}$ there are unitary $U\in M_{m}$ and $V\in M_{n}$ with $A=U\Sigma V^{H}$, where $\Sigma\in M_{m,n}$ has nonnegative diagonal entries $\sigma_{1}(A)\ge\sigma_{2}(A)\ge\dots\ge0$ and all other entries $0$.

::: pf-proof
This is stated, not proved, as the exercise directs. Equivalently, the columns $v_{1},\dots,v_{n}$ of $V$ and $u_{1},\dots,u_{m}$ of $U$ satisfy $Av_{j}=\sigma_{j}(A)u_{j}$ for $j\le\min\{m,n\}$, with the remaining data irrelevant.
:::

:::

::: {.pf-step #operator-norm}
$\norm{Ax}_{2}\le\sigma_{1}(A)\norm{x}_{2}$ for every $x$.

::: pf-proof
With $A=U\Sigma V^{H}$ and $z=V^{H}x$, unitarity gives $\norm{z}_{2}=\norm{x}_{2}$ and $\norm{Ax}_{2}=\norm{\Sigma z}_{2}$. Writing $z=(z_{1},\dots,z_{n})$ and $\Sigma=\operatorname{diag}(\sigma_{1},\dots)\oplus0$,
$$
\norm{\Sigma z}_{2}^{2}=\sum_{j}\sigma_{j}^{2}\abs{z_{j}}^{2}\le\sigma_{1}^{2}\sum_{j}\abs{z_{j}}^{2}=\sigma_{1}^{2}\norm{x}_{2}^{2}.
$$
:::

:::

::: {.pf-step #upper-b}
(b) For all $x,y\ne0$, $\ \abs{y^{H}Ax}\le\sigma_{1}(A)\norm{y}_{2}\norm{x}_{2}$; hence the quotient in the statement is at most $\sigma_{1}(A)$.

::: pf-proof
By the Cauchy--Schwarz inequality in $\CC^{m}$ and step [](#operator-norm){.pf-ref},
$$
\abs{y^{H}Ax}=\abs{\langle y,Ax\rangle}\le\norm{y}_{2}\norm{Ax}_{2}\le\sigma_{1}(A)\norm{y}_{2}\norm{x}_{2}.
$$
Dividing by $\norm{y}_{2}\norm{x}_{2}>0$ gives the bound for every admissible pair, so the supremum of the quotient is at most $\sigma_{1}(A)$.
:::

:::

::: {.pf-step #attained-b}
(b) $\displaystyle\max_{x,y\ne0}\frac{\abs{y^{H}Ax}}{\norm{y}_{2}\norm{x}_{2}}=\sigma_{1}(A)$.

::: pf-proof
If $\sigma_{1}(A)=0$ the quotient vanishes identically by step [](#upper-b){.pf-ref} and the identity holds. Otherwise take the first right and left singular vectors $v_{1}$, $u_{1}$ of step [](#svd){.pf-ref}, so $Av_{1}=\sigma_{1}(A)u_{1}$; then
$$
\abs{u_{1}^{H}Av_{1}}=\sigma_{1}(A)\abs{u_{1}^{H}u_{1}}=\sigma_{1}(A),
$$
and $\norm{u_{1}}_{2}=\norm{v_{1}}_{2}=1$, so the quotient equals $\sigma_{1}(A)$ at this pair. With step [](#upper-b){.pf-ref} the supremum is attained and equals $\sigma_{1}(A)$.
:::

:::

::: {.pf-step #definitions}
(c) $F(A)=\{x^{H}Ax:\norm{x}_{2}=1\}$, $\ \rho(A)=\max\{\abs{\lambda}:\lambda\in\operatorname{eig}(A)\}$, $\ \omega(A)=\max\{\abs{z}:z\in F(A)\}=\max_{\norm{x}_{2}=1}\abs{x^{H}Ax}$.

::: pf-proof
These are the definitions asked for. Each maximum exists: the unit sphere is compact and the maps $x\mapsto x^{H}Ax$ and $x\mapsto\abs{x^{H}Ax}$ are continuous, and the eigenvalue set of an $n\times n$ matrix is finite and nonempty over $\CC$.
:::

:::

::: {.pf-step #rho-le-omega}
$\rho(A)\le\omega(A)$.

::: pf-proof
Let $\lambda$ be an eigenvalue of $A$ with eigenvector $x$ of norm $1$. Then $x^{H}Ax=\lambda x^{H}x=\lambda$, so $\lambda\in F(A)$ and $\abs{\lambda}\le\omega(A)$ by the definition of $\omega$ as a maximum over $F(A)$. Taking the maximum over the finitely many eigenvalues gives $\rho(A)\le\omega(A)$.
:::

:::

::: {.pf-step #omega-le-sigma}
$\omega(A)\le\sigma_{1}(A)$.

::: pf-proof
For $\norm{x}_{2}=1$ the Cauchy--Schwarz inequality and step [](#operator-norm){.pf-ref} give
$$
\abs{x^{H}Ax}=\abs{\langle x,Ax\rangle}\le\norm{x}_{2}\norm{Ax}_{2}\le\sigma_{1}(A),
$$
so the maximum over unit vectors is at most $\sigma_{1}(A)$.
:::

:::

::: {.pf-step}
$\rho(A)\le\omega(A)\le\sigma_{1}(A)$, so all three parts hold.

::: pf-proof
Steps [](#rho-le-omega){.pf-ref} and [](#omega-le-sigma){.pf-ref} are the two inequalities of (c); step [](#svd){.pf-ref} is (a) and steps [](#upper-b){.pf-ref} and [](#attained-b){.pf-ref} are (b).
:::

:::

:::
:::
