---
schema: qual/card@1
id: P-ALGS05M
kind: problem
title: "Infinitely many maximal right ideals in n × n matrices over Q"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that there are infinitely many maximal right ideals in $n \times n$ matrices over the rationals when $n > 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Construct right ideals via annihilators of vectors:

::: pf-proof

::: pf-step

Let $R = M_n(\mathbb{Q})$. The vector space $V = \mathbb{Q}^{1 \times n}$ of row vectors is a simple right $R$-module under matrix multiplication $v \cdot A = vA$.

::: pf-proof

for any $v, w \in V$ with $v \neq 0$, there exists $A \in R$ such that $vA = w$.

:::

:::

::: pf-step

For any non-zero row vector $v \in V \setminus \{0\}$, define:
\[
I_v = \{A \in M_n(\mathbb{Q}) : vA = 0\} = \operatorname{Ann}_R(v).
\]

::: pf-proof

definition of annihilator of a vector.

:::

:::

::: pf-step

$I_v$ is a right ideal of $R$: if $A, B \in I_v$ and $C \in R$, then $v(A + B) = vA + vB = 0$ and $v(AC) = (vA)C = 0C = 0$.

::: pf-proof

distributive and associative laws of matrix multiplication.

:::

:::

:::

:::

::: {.pf-step #s2}

Show that each $I_v$ is a maximal right ideal:

::: pf-proof

::: pf-step

Consider the evaluation map $\Phi_v: R \to V$ given by $\Phi_v(A) = vA$.

::: pf-proof

$\Phi_v$ is a homomorphism of right $R$-modules.

:::

:::

::: pf-step

Since $v \neq 0$, $\Phi_v$ is surjective: for any $w \in V$, completing $v$ to an invertible matrix $P \in \operatorname{GL}_n(\mathbb{Q})$ with first row $v$ and setting $A = P^{-1} \begin{pmatrix} w \\ 0 \\ \vdots \\ 0 \end{pmatrix}$ yields $\Phi_v(A) = vA = w$.

::: pf-proof

linear algebra over $\mathbb{Q}$.

:::

:::

::: pf-step

By the First Isomorphism Theorem for modules, $R / I_v \cong V$ as right $R$-modules.

::: pf-proof

$\ker(\Phi_v) = I_v$.

:::

:::

::: pf-step

Since $V \cong \mathbb{Q}^n$ is a simple right $R$-module (having no non-trivial proper submodules), $I_v$ is a **maximal right ideal** of $R$.

::: pf-proof

correspondence between maximal submodules and simple quotients.

:::

:::

:::

:::

::: {.pf-step #s3}

Show that different 1-dimensional subspaces produce distinct maximal right ideals:

::: pf-proof

::: {.pf-step #s3-1}

If $v_1, v_2 \in V \setminus \{0\}$ are linearly independent, there exists a matrix $A \in M_n(\mathbb{Q})$ such that $v_1 A = 0$ and $v_2 A \neq 0$.

::: pf-proof

rank and linear independence in $\mathbb{Q}^n$.

:::

:::

::: {.pf-step #s3-2}

Thus $A \in I_{v_1}$ but $A \notin I_{v_2}$, so $I_{v_1} \neq I_{v_2}$.

::: pf-proof

Step [](#s3-1){.pf-ref}.

:::

:::

::: pf-step

Therefore $I_{v_1} = I_{v_2}$ if and only if $\mathbb{Q} v_1 = \mathbb{Q} v_2$.

::: pf-proof

Step [](#s3-2){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s4}

Count the number of maximal right ideals:

::: pf-proof

::: pf-step

For $n > 1$, consider the family of vectors $v_c = (1, c, 0, \dots, 0) \in \mathbb{Q}^{1 \times n}$ indexed by $c \in \mathbb{Q}$.

::: pf-proof

construction of pairwise non-proportional vectors.

:::

:::

::: pf-step

For $c_1 \neq c_2$, the vectors $v_{c_1}$ and $v_{c_2}$ are linearly independent over $\mathbb{Q}$.

::: pf-proof

$\det\begin{pmatrix} 1 & c_1 \\ 1 & c_2 \end{pmatrix} = c_2 - c_1 \neq 0$.

:::

:::

::: pf-step

By step [](#s3){.pf-ref}, the family $\{I_{v_c} : c \in \mathbb{Q}\}$ is an infinite collection of distinct maximal right ideals in $M_n(\mathbb{Q})$.

::: pf-proof

$\mathbb{Q}$ is infinite.

:::

:::

:::

:::

::: pf-step

Conclusion:
$M_n(\mathbb{Q})$ contains infinitely many maximal right ideals when $n > 1$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
