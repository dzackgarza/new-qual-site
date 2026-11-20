---
schema: qual/card@1
id: P-APAS23D
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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Part A, Question 4 of the Spring 2023 Applied Algebra Qualifying Exam, printed
    p. 2 of the Part A paper retained at assets/attachments/Applied_Algebra_Part_A_SP23.pdf, is the
    statement the card answers, and the head of the solution names it. Checked: the statement against
    the paper's text layer at the page named; the stated SVD theorem, the max characterisation of
    $\sigma_1$, and $\rho(A)\le\omega(A)\le\sigma_1(A)$; `qualc.authoring check` on the card, and
    `tmp/lam.sh` for the numbering and the QED. Not checked: no retained solution set exists for this
    paper to compare the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with five steps, each carrying a `pf-proof`; the statement, the SVD as stated, and the three
    definitions of part (c) are unchanged. Cited by number only: the singular-value
    decomposition as the exercise asks it to be stated, the Cauchy--Schwarz inequality, and part
    (b) itself for the upper bound in part (c). Checked: that $\norm{\Sigma w}_2\le\sigma_1\norm
    {w}_2$ for a diagonal rectangular $\Sigma$, that $Av_1=\sigma_1u_1$ for the first columns of
    $U$ and $V$, that an eigenvalue of a unit eigenvector is a value of $x^HAx$, and that the
    maximum defining $\omega$ is attained.
---

::: {.problem}
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex components, $M_n$ denotes the set $M_{m,n}$ with $m = n$, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) State, but do not prove, the singular-value decomposition theorem.

(b) For a given $A \in M_{m,n}$, prove that
$$
\sigma_1(A) = \max_{x,y \ne 0} \frac{\abs{y^H A x}}{\norm{y}_2 \norm{x}_2},
$$
where $\sigma_1(A)$ is the largest singular value of $A$.

(c) For any $A \in M_n$, define (i) the field of values $F(A)$; (ii) the spectral radius $\rho(A)$; and (iii) the numerical radius $\omega(A)$.
Prove that $\rho(A) \le \omega(A) \le \sigma_1(A)$.
:::


::: {.solution}

The problem is Part A, Question 4 of the Spring 2023 Applied Algebra Qualifying Exam, of the Part A paper retained at `assets/attachments/Applied_Algebra_Part_A_SP23.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own.

::: pf

::: pf-step

(a) **Singular-value decomposition.** For every $A\in M_{m,n}$ there are unitary $U\in M_m$, $V\in M_n$ with
$$
A=U\Sigma V^H,
$$
$\Sigma$ diagonal rectangular with nonnegative diagonal entries $\sigma_1(A)\ge\sigma_2(A)\ge\cdots\ge0$, the singular values of $A$.

::: pf-proof

This is the statement the exercise asks to be stated and not proved. Concretely, with $p=\min(m,n)$, $\Sigma$ has $\Sigma_{ii}=\sigma_i(A)$ for $1\le i\le p$ and zero entries elsewhere; the $\sigma_i$ are the square roots of the eigenvalues of $A^HA$, which are nonnegative because $A^HA$ is positive semidefinite, and they are ordered decreasingly by convention. Unitarity of $U$ and $V$ means $U^HU=I_m$ and $V^HV=I_n$.

:::

:::

::: pf-step

(b) By Cauchy--Schwarz,
$$
\abs{y^HAx}\le\norm{y}_2\,\norm{Ax}_2\le\norm{y}_2\,\sigma_1(A)\norm{x}_2,
$$
hence $\abs{y^HAx}/(\norm{y}_2\norm{x}_2)\le\sigma_1(A)$.

::: pf-proof

The inner product on $\CC^m$ satisfies $\abs{\langle y,z\rangle}\le\norm{y}_2\norm{z}_2$ with $z=Ax$, which is the first inequality. For the second, $A=U\Sigma V^H$ with $U,V$ unitary gives $\norm{Ax}_2=\norm{\Sigma V^Hx}_2$, and a diagonal rectangular $\Sigma$ with entries at most $\sigma_1$ satisfies $\norm{\Sigma w}_2\le\sigma_1\norm{w}_2$; with $w=V^Hx$ and $\norm{w}_2=\norm{x}_2$ this is the bound. Dividing by the positive number $\norm{y}_2\norm{x}_2$ gives the displayed estimate.

:::

:::

::: pf-step

(b) With $v_1$ and $u_1$ right and left singular vectors for $\sigma_1(A)$, normalized so that $Av_1=\sigma_1(A)u_1$ and $\norm{u_1}_2=\norm{v_1}_2=1$, one has $\abs{u_1^HAv_1}=\sigma_1(A)$, so equality is attained and
$$
\sigma_1(A)=\max_{x,y\ne0}\frac{\abs{y^HAx}}{\norm{y}_2\norm{x}_2}.
$$

::: pf-proof

The singular-value decomposition provides such a pair: the first column $v_1$ of $V$ and the first column $u_1$ of $U$ satisfy $Av_1=U\Sigma V^Hv_1=\sigma_1u_1$, since $V^Hv_1=e_1$ and $\Sigma e_1=\sigma_1e_1$. Both are unit vectors because $U,V$ are unitary. Then $\abs{u_1^HAv_1}=\sigma_1\abs{u_1^Hu_1}=\sigma_1$. Steps 2 and 3 give the bound and its attainment, so the maximum is $\sigma_1(A)$.

:::

:::

::: pf-step

(c) With
$$
F(A)=\{x^HAx:x\in\CC^n,\ x^Hx=1\},\qquad
\rho(A)=\max\{\abs{\lambda}:\lambda\in\operatorname{spec}(A)\},\qquad
\omega(A)=\max_{x^Hx=1}\abs{x^HAx},
$$
every eigenvalue of $A$ lies in $F(A)$, hence $\rho(A)\le\omega(A)$.

::: pf-proof

If $Ax=\lambda x$ with $x^Hx=1$ then $x^HAx=\lambda x^Hx=\lambda$, so $\lambda\in F(A)$ and $\abs{\lambda}\le\max_{z\in F(A)}\abs{z}=\omega(A)$. Taking the maximum over eigenvalues gives $\rho(A)\le\omega(A)$. The maximum defining $\omega$ is attained because the unit sphere is compact and $x\mapsto\abs{x^HAx}$ is continuous.

:::

:::

::: pf-step

(c) Applying part (b) with $y=x$ and $\norm{x}_2=1$ gives $\abs{x^HAx}\le\sigma_1(A)$ for every unit $x$, hence $\omega(A)\le\sigma_1(A)$, and therefore
$$
\rho(A)\le\omega(A)\le\sigma_1(A).
$$

::: pf-proof

Part (b) says $\abs{y^HAx}\le\sigma_1(A)\norm{y}_2\norm{x}_2$ for all $x,y\ne0$; with $y=x$ and $\norm{x}_2=1$ this is $\abs{x^HAx}\le\sigma_1(A)$. Taking the maximum over unit $x$ gives $\omega(A)\le\sigma_1(A)$, and step 4 gives the other inequality.

:::

:::

:::
:::
