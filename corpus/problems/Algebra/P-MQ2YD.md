---
schema: qual/card@1
id: P-MQ2YD
kind: problem
title: Matrices satisfying a given polynomial over algebraically closed and finite
  fields
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Matrices
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) What can you say about $n \times n$ matrices $A$ that satisfy a given polynomial $P(x) = 0$ over an algebraically closed field $k = \bar{k}$? How many similarity classes and how many such matrices are there?
(2) What about over a finite field $\mathbb{F}_q$? How many similarity classes and how many individual matrices satisfy $P(A) = 0$?
:::

::: solution
**Goal:** Classify and count matrices satisfying $P(A) = 0$ via Jordan/Rational canonical forms over algebraically closed and finite fields.

<1>1. Algebraic Constraint on Matrices Satisfying $P(A) = 0$:
    *Proof:*
    <2>1. A matrix $A \in M_n(K)$ satisfies $P(A) = 0$ if and only if its minimal polynomial $\mu_A(x)$ divides $P(x)$:
        $$\mu_A(x) \mid P(x).$$
    <2>2. Consequently, all eigenvalues of $A$ in $\bar{K}$ must be roots of $P(x)$.

<1>2. Over an Algebraically Closed Field $k = \bar{k}$ (e.g. $k = \mathbb{C}$):
    *Proof:*
    <2>1. **Structure via Jordan Canonical Form:**
        - $P(x) = c \prod_{i=1}^m (x - \lambda_i)^{e_i}$ with distinct roots $\lambda_1, \dots, \lambda_m \in k$.
        - The Jordan blocks $J_d(\lambda)$ of $A$ can only have eigenvalues $\lambda \in \{\lambda_1, \dots, \lambda_m\}$, and the maximum block size for $\lambda_i$ is at most $e_i$.
    <2>2. **Number of Similarity Classes (Jordan forms):**
        - A similarity class is determined by integer partitions $\nu_i \vdash n_i$ of the algebraic multiplicities $\sum_{i=1}^m n_i = n$, where the largest part of $\nu_i$ is $\le e_i$.
        - Since $n$ and $m$ are finite, the number of valid partition tuples $(\nu_1, \dots, \nu_m)$ is **finite**.
    <2>3. **Total Number of Matrices:**
        - If $k$ is infinite (like $\mathbb{C}$), each similarity class is an orbit under the $\operatorname{GL}_n(k)$ conjugation action $\mathcal{O}(A) = \{P A P^{-1} \mid P \in \operatorname{GL}_n(k)\}$.
        - Since $\dim(\mathcal{O}(A)) = n^2 - \dim(C(A)) > 0$ for non-scalar matrices, there are **uncountably infinitely many (continuum)** individual matrices satisfying $P(A) = 0$ (unless $n=1$ or $A$ is scalar).

<1>3. Over a Finite Field $\mathbb{F}_q$:
    *Proof:*
    <2>1. **Number of Similarity Classes (Rational Canonical Forms):**
        - Over $\mathbb{F}_q$, $P(x) = \prod_{j=1}^r f_j(x)^{e_j}$ where each $f_j(x)$ is a monic irreducible polynomial in $\mathbb{F}_q[x]$ of degree $d_j$.
        - A similarity class is uniquely determined by a valid sequence of invariant factors $d_1(x) \mid d_2(x) \mid \cdots \mid d_k(x)$ such that $\sum \deg(d_i) = n$ and $d_k(x) \mid P(x)$.
        - Since $n$ is finite, there are only **finitely many similarity classes**.
    <2>2. **Exact Number of Matrices via Orbit-Stabilizer Theorem:**
        - The total number of matrices $A \in M_n(\mathbb{F}_q)$ with $P(A) = 0$ is the sum of sizes of their similarity classes (conjugacy orbits in $M_n(\mathbb{F}_q)$):
            $$N = \sum_{[\text{RCF } C]} |\mathcal{O}(C)| = \sum_{[\text{RCF } C]} \frac{|\operatorname{GL}_n(\mathbb{F}_q)|}{|C_{\operatorname{GL}_n(\mathbb{F}_q)}(C)|}$$
            where $|\operatorname{GL}_n(\mathbb{F}_q)| = \prod_{i=0}^{n-1} (q^n - q^i) = q^{n(n-1)/2} \prod_{i=1}^n (q^i - 1)$, and the centralizer order $|C_{\operatorname{GL}_n(\mathbb{F}_q)}(C)|$ is computed from the invariant factor degrees.
        - Since $M_n(\mathbb{F}_q)$ is finite ($|M_n(\mathbb{F}_q)| = q^{n^2}$), the total number of such matrices is a **finite, computable integer**.

<1>4. Conclusion:
    Over $k = \bar{k}$, similarity classes are classified by Jordan forms (finite count), with infinitely many matrices per orbit. Over $\mathbb{F}_q$, there are finitely many similarity classes, and the total matrix count is given by the sum of orbit sizes $\sum [G : C_G(C_i)]$. Q.E.D.
:::
