---
schema: qual/card@1
id: P-UCLAB02W-11
kind: problem
title: Triangularization in an orthonormal basis
classification:
  areas:
  - prelim
  topics:
  - Schur Decomposition
  - Orthonormal Bases
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 11 of the official UCLA Basic Examination, Winter 2002 PDF.
    The source calls the matrix "upper triangular" but then specifies $A_{ij}=0$ for $i<j$,
    which is the standard lower-triangular index condition.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Records the terminology/index mismatch. Standard Schur triangularization gives the
    upper-triangular convention $A_{ij}=0$ for $i>j$; reversing an orthonormal basis converts
    it to the printed lower-triangular convention.
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The exam calls the matrix upper triangular and then writes A_ij = 0 for i < j, the
    lower-triangular condition; the statement now uses the upper-triangular condition A_ij
    = 0 for i > j that its words name.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the hint's criterion and its
    two directions, including the use of (W^perp)^perp = W in finite dimension, which the prose
    left implicit. The induction is carried out: T^* has an eigenvector over C, W = C w is
    T^*-invariant so W^perp is T-invariant, the inductive hypothesis applies to T restricted to
    W^perp, and appending w gives an ordered orthonormal basis with A_ij = 0 for i > j. The card's
    remark that the printed index condition i < j is the lower-triangular one is kept and now has
    its step: reversing the ordered basis gives (P^{-1} A P)_ij = A_{n+1-i,n+1-j}, so vanishing
    above the diagonal becomes vanishing below it. Statement and hint unchanged; the card says
    the argument is its own.
---

::: {.problem}
Let $V$ be a finite-dimensional complex inner-product space and let $T:V\to V$ be linear.
Prove that there exists an ordered orthonormal basis of $V$ such that the matrix $A=(A_{ij})$ of $T$ in this basis is upper triangular, i.e.,
$$
A_{ij}=0
\qquad\text{if }i>j.
$$

Hint: first show that if $S:V\to V$ is linear and $W\subset V$ is a subspace, then $W$ is $S$-invariant if and only if $W^\perp$ is $S^*$-invariant.
:::

::: {.solution}
The hint's subspace criterion is the engine: $W$ is $S$-invariant exactly when $W^\perp$ is $S^*$-invariant. Over $\CC$ the adjoint of any linear map has an eigenvector, so taking $W=\CC w$ for an eigenvector $w$ of $T^*$ gives a $T$-invariant hyperplane, and induction finishes. The printed index condition is $A_{ij}=0$ for $i>j$, which is upper triangular; the card's prose also computes the lower-triangular form, and both are recorded. The argument is this card's own: the checkout retains no solution set for this exam.

::: pf

::: {.pf-step #criterion}
For linear $S\colon V\to V$ and a subspace $W\le V$, $W$ is $S$-invariant if and only if $W^\perp$ is $S^*$-invariant.

::: pf-proof
Recall $W^\perp=\{y:\langle w,y\rangle=0\ \text{for all }w\in W\}$, and $\langle Sv,w\rangle=\langle v,S^*w\rangle$ for all $v,w$, since $S^*$ is the adjoint. If $S(W)\subseteq W$ and $y\in W^\perp$, then for every $w\in W$ one has $\langle w,S^*y\rangle=\langle Sw,y\rangle=0$ because $Sw\in W$ and $y\in W^\perp$; so $S^*y\in W^\perp$. Conversely, if $S^*(W^\perp)\subseteq W^\perp$ and $w\in W$, then for every $y\in W^\perp$ one has $\langle Sw,y\rangle=\langle w,S^*y\rangle=0$ with $S^*y\in W^\perp$, so $Sw\in(W^\perp)^\perp=W$, using finite dimensionality for $(W^\perp)^\perp=W$.
:::

:::


::: {.pf-step #upper}
There is an ordered orthonormal basis of $V$ in which the matrix $A$ of $T$ satisfies $A_{ij}=0$ for $i>j$.

::: pf-proof
Induct on $n=\dim V$, the case $n=0$ being vacuous. Over $\CC$ the characteristic polynomial of $T^*$ has a root, so there is a unit vector $w$ with $T^*w=\lambda w$ for some $\lambda\in\CC$. Put $W=\CC w$, so $W$ is $T^*$-invariant; by step [](#criterion){.pf-ref} $W^\perp$ is $T$-invariant, and $\dim W^\perp=n-1$. By induction, $T\restriction_{W^\perp}$ has an orthonormal basis $v_1,\dots,v_{n-1}$ of $W^\perp$ in which its matrix is upper triangular. Then $v_1,\dots,v_{n-1},v_n:=w$ is an ordered orthonormal basis of $V=W^\perp\oplus W$: it is orthonormal because $w$ is a unit vector orthogonal to $W^\perp$, and it spans because the two summands do. In this basis $Tv_j$ lies in $W^\perp=\operatorname{span}(v_1,\dots,v_{n-1})$ for $j\le n-1$ and has coordinates $A_{ij}$ with $A_{ij}=0$ for $i\ge j$ by the inductive hypothesis; while $Tv_n$ may have any coordinates, giving $A_{in}$ for $i\le n$. So $A_{ij}=0$ whenever $i>j$.
:::

:::


::: {.pf-step #lower}
There is also an ordered orthonormal basis in which $A_{ij}=0$ for $i<j$, which is the index condition printed on the card.

::: pf-proof
Take the basis $v_1,\dots,v_n$ of step [](#upper){.pf-ref} and list it in the reverse order $v_n,v_{n-1},\dots,v_1$, which is again an ordered orthonormal basis. If $P$ is the permutation matrix of the reversal, the new matrix is $P^{-1}AP$, and $P$ is a permutation matrix of the transposition $i\mapsto n+1-i$, so $(P^{-1}AP)_{ij}=A_{n+1-i,n+1-j}$. The condition $A_{ij}=0$ for $i>j$ becomes $(P^{-1}AP)_{ij}=0$ for $n+1-i>n+1-j$, i.e. for $i<j$. So in the reversed basis the entries vanish above the diagonal, which is exactly $A_{ij}=0$ whenever $i<j$, the condition written in the statement.
:::

:::


::: {.pf-step #conclusion}
The statement's condition is met by the basis of step [](#lower){.pf-ref}, and the triangular form in either orientation is available from the same construction.

::: pf-proof
Steps [](#upper){.pf-ref} and [](#lower){.pf-ref} give an ordered orthonormal basis with $A_{ij}=0$ for $i>j$ and one with $A_{ij}=0$ for $i<j$; the statement asks for the second, so it is proved. Nothing beyond finite dimensionality over $\CC$ and the existence of an eigenvector of $T^*$ is used, so the argument applies to every linear $T$.
:::

:::

:::
:::
