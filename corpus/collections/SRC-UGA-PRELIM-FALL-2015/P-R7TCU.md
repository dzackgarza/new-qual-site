---
schema: qual/card@1
id: P-R7TCU
kind: problem
title: A $3\times 3$ matrix with eigenvalues $-1,0,1$ satisfies $A^3=A$
classification:
  areas:
  - prelim
  topics:
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
---

::: problem
Suppose $A$ is a $3\times3$ matrix with real entries and eigenvalues $-1$, $0$, and $1$. Prove that $A^3=A$.
:::

::: solution
1. We have $p_A(x) = (x+1)(x-1)(x) = x^3 - x$ and so by Cayley-Hamilton, $A^3 - A = 0 \implies A^3 = A$.
   $\qed$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $A \in M_3(\mathbb{R})$ be a $3 \times 3$ matrix with eigenvalues $-1, 0, 1$.
Prove that $A^3 = A$.

<1>1. The characteristic polynomial of $A$ is $p_A(x) = x(x-1)(x+1) = x^3 - x$.
Proof: <2>1. $A$ is a $3 \times 3$ matrix, so $\deg(p_A(x)) = 3$ and its leading coefficient is $1$ (using $p_A(x) = \det(xI - A)$). <2>2. The roots of $p_A(x)$ are the eigenvalues of $A$, which are given as $\lambda_1 = 0, \lambda_2 = 1, \lambda_3 = -1$.
<2>3. Since these are $3$ distinct roots for a degree $3$ monic polynomial, $p_A(x) = (x-0)(x-1)(x+1) = x(x^2-1) = x^3 - x$.

<1>2. By the Cayley-Hamilton Theorem, $p_A(A) = O$, where $O$ is the $3 \times 3$ zero matrix.
Proof: The Cayley-Hamilton Theorem states that every square matrix over a commutative ring satisfies its own characteristic polynomial.
Hypotheses are satisfied since $A \in M_3(\mathbb{R})$.

<1>3. $A^3 = A$.
Proof: By <1>1 and <1>2: $$p_A(A) = A^3 - A = O \implies A^3 = A.$$ Q.E.D.
:::
