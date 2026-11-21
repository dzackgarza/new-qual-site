---
schema: qual/card@1
id: P-APAS20C
kind: problem
title: Positive definiteness of $\phi-t\psi$ via the smallest eigenvalue of $\psi^{-1/2}\phi\psi^{-1/2}$
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Hermitian Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 3 of the Math 202 Qualifying Exam, Spring 2020 (June 3, 2020), printed
    p. 1 of the paper's own numbered pages, is the statement the card answers, and the head of the
    solution names it; the file retained at assets/attachments/Applied-Algebra-Qual-SP20.pdf puts a
    cover page before those two numbered pages, so paper p. 1 and p. 2 are its second and third pages.
    Checked: the statement against the paper's text layer at the page named; the congruence by the
    positive definite square root and the eigenvalue comparison; `qualc.authoring check` on the card,
    and `tmp/lam.sh` for the numbering and the QED. Not checked: no retained solution set exists for
    this paper to compare the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $V$ be an inner product space of dimension $n$, and $\phi,\psi\colon V\to V$ two positive definite Hermitian maps.
You may use without proof that $\psi$ has a unique positive definite square root $\psi^{1/2}$, and that $\psi$ and $\psi^{1/2}$ are non-singular.

Let $t\in\RR$ be a real number.
Prove that $\phi-t\psi$ is positive definite if and only if $t<\lambda_n(\theta)$ (i.e., the smallest eigenvalue of $\theta$) where $\theta=\psi^{-1/2}\phi\psi^{-1/2}$.
:::

::: {.solution}

The problem is Problem 3 of the Math 202 Qualifying Exam, Spring 2020 (June 3, 2020), printed p. 1 of the paper's numbered pages — the retained file `assets/attachments/Applied-Algebra-Qual-SP20.pdf` puts a cover page before them. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the congruence by $\psi^{-1/2}$, which turns $\phi-t\psi>0$ into $\theta-tI>0$ and hence into $t<\lambda_n(\theta)$

::: pf

::: {.pf-step #s1}

$\phi - t\psi$ is positive definite iff $\psi^{-1/2}(\phi - t\psi)\psi^{-1/2}$ is positive definite.

::: pf-proof

conjugating by the invertible $\psi^{-1/2}$ preserves positive definiteness (it is a congruence).

:::

:::

::: {.pf-step #s2}

$\psi^{-1/2}(\phi - t\psi)\psi^{-1/2} = \psi^{-1/2}\phi\psi^{-1/2} - t\psi^{-1/2}\psi\psi^{-1/2} = \theta - tI$.

::: pf-proof

Step [](#s1){.pf-ref}, expanding.

:::

:::

::: {.pf-step #s3}

$\theta$ is positive definite Hermitian (it is a congruence of the positive definite $\phi$), so it is diagonalizable with positive eigenvalues $\lambda_1 \ge \cdots \ge \lambda_n > 0$.

::: pf-proof

$\theta = \psi^{-1/2}\phi\psi^{-1/2}$ is Hermitian and positive definite.

:::

:::

::: {.pf-step #s4}

$\theta - tI$ is positive definite iff all its eigenvalues are positive, i.e. iff $\lambda_i - t > 0$ for all $i$.

::: pf-proof

Step [](#s3){.pf-ref} (the eigenvalues of $\theta - tI$ are $\lambda_i - t$).

:::

:::

::: {.pf-step #s5}

This holds iff $t < \lambda_i$ for all $i$, i.e. iff $t < \lambda_n$ (the smallest eigenvalue).

::: pf-proof

Step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Hence $\phi - t\psi$ is positive definite iff $t < \lambda_n(\theta)$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
