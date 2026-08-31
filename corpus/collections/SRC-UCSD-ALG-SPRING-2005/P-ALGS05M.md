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

::: problem
Show that there are infinitely many maximal right ideals in $n \times n$ matrices over the rationals when $n > 1$.
:::

::: {.solution}
<1>1. Construct right ideals via annihilators of vectors:
<2>1. Let $R = M_n(\mathbb{Q})$. The vector space $V = \mathbb{Q}^{1 \times n}$ of row vectors is a simple right $R$-module under matrix multiplication $v \cdot A = vA$.
::: {.proof}
for any $v, w \in V$ with $v \neq 0$, there exists $A \in R$ such that $vA = w$.
:::
<2>2. For any non-zero row vector $v \in V \setminus \{0\}$, define:
\[
I_v = \{A \in M_n(\mathbb{Q}) : vA = 0\} = \operatorname{Ann}_R(v).
\]
::: {.proof}
definition of annihilator of a vector.
:::
<2>3. $I_v$ is a right ideal of $R$: if $A, B \in I_v$ and $C \in R$, then $v(A + B) = vA + vB = 0$ and $v(AC) = (vA)C = 0C = 0$.
::: {.proof}
distributive and associative laws of matrix multiplication.
:::

<1>2. Show that each $I_v$ is a maximal right ideal:
<2>1. Consider the evaluation map $\Phi_v: R \to V$ given by $\Phi_v(A) = vA$.
::: {.proof}
$\Phi_v$ is a homomorphism of right $R$-modules.
:::
<2>2. Since $v \neq 0$, $\Phi_v$ is surjective: for any $w \in V$, completing $v$ to an invertible matrix $P \in \operatorname{GL}_n(\mathbb{Q})$ with first row $v$ and setting $A = P^{-1} \begin{pmatrix} w \\ 0 \\ \vdots \\ 0 \end{pmatrix}$ yields $\Phi_v(A) = vA = w$.
::: {.proof}
linear algebra over $\mathbb{Q}$.
:::
<2>3. By the First Isomorphism Theorem for modules, $R / I_v \cong V$ as right $R$-modules.
::: {.proof}
$\ker(\Phi_v) = I_v$.
:::
<2>4. Since $V \cong \mathbb{Q}^n$ is a simple right $R$-module (having no non-trivial proper submodules), $I_v$ is a **maximal right ideal** of $R$.
::: {.proof}
correspondence between maximal submodules and simple quotients.
:::

<1>3. Show that different 1-dimensional subspaces produce distinct maximal right ideals:
<2>1. If $v_1, v_2 \in V \setminus \{0\}$ are linearly independent, there exists a matrix $A \in M_n(\mathbb{Q})$ such that $v_1 A = 0$ and $v_2 A \neq 0$.
::: {.proof}
rank and linear independence in $\mathbb{Q}^n$.
:::
<2>2. Thus $A \in I_{v_1}$ but $A \notin I_{v_2}$, so $I_{v_1} \neq I_{v_2}$.
::: {.proof}
<2>1.
:::
<2>3. Therefore $I_{v_1} = I_{v_2}$ if and only if $\mathbb{Q} v_1 = \mathbb{Q} v_2$.
::: {.proof}
<2>2.
:::

<1>4. Count the number of maximal right ideals:
<2>1. For $n > 1$, consider the family of vectors $v_c = (1, c, 0, \dots, 0) \in \mathbb{Q}^{1 \times n}$ indexed by $c \in \mathbb{Q}$.
::: {.proof}
construction of pairwise non-proportional vectors.
:::
<2>2. For $c_1 \neq c_2$, the vectors $v_{c_1}$ and $v_{c_2}$ are linearly independent over $\mathbb{Q}$.
::: {.proof}
$\det\begin{pmatrix} 1 & c_1 \\ 1 & c_2 \end{pmatrix} = c_2 - c_1 \neq 0$.
:::
<2>3. By <1>3, the family $\{I_{v_c} : c \in \mathbb{Q}\}$ is an infinite collection of distinct maximal right ideals in $M_n(\mathbb{Q})$.
::: {.proof}
$\mathbb{Q}$ is infinite.
:::

<1>5. Conclusion:
$M_n(\mathbb{Q})$ contains infinitely many maximal right ideals when $n > 1$. Q.E.D.
::: {.proof}
<1>1 through <1>4.
:::
:::
