---
schema: qual/card@1
id: P-BKF97-7
kind: problem
title: Monotonicity of the index of symmetric quadratic forms
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the variational characterization of inertia: positive and negative
    eigenvalue counts are the maximal dimensions of positive- and
    negative-definite subspaces. The quadratic-form inequality gives the two
    required monotonicities.
---

::: {.problem}
Define the index of a real symmetric matrix $A$ to be the number of strictly positive eigenvalues of $A$ minus the number of strictly negative eigenvalues.
Suppose $A,B$ are real symmetric $n\times n$ matrices such that
\[
x^TAx\le x^TBx
\]
for every $x\in\mathbb R^n$.
Prove that the index of $A$ is at most the index of $B$.
:::

::: {.solution}

For a real symmetric matrix $M$, let
$$
p(M)
$$
be the number of positive eigenvalues and
$$
q(M)
$$
the number of negative eigenvalues, counted with multiplicity. Thus
$$
\operatorname{ind}(M)=p(M)-q(M).
$$

::: pf

::: {.pf-step #p-is-max-positive-definite-dim}
The number $p(M)$ is the largest possible dimension of a subspace
$V\subseteq\RR^n$ on which
$$
x^TMx>0
$$
for every nonzero $x\in V$.

::: pf-proof
By the spectral theorem, $\RR^n$ is the orthogonal direct sum
$$
E_+(M)\oplus E_0(M)\oplus E_-(M)
$$
of the positive, zero, and negative eigenspaces. On the subspace
$E_+(M)$, the quadratic form is positive definite, and
$$
\dim E_+(M)=p(M).
$$

Conversely, suppose $\dim V>p(M)$. Since
$$
\dim\bigl(E_0(M)\oplus E_-(M)\bigr)
=
n-p(M),
$$
the dimension formula forces
$$
V\cap\bigl(E_0(M)\oplus E_-(M)\bigr)
\neq
\{0\}.
$$
For a nonzero vector in this intersection,
$$
x^TMx\leq0,
$$
so $V$ cannot be positive definite. Hence $p(M)$ is maximal.
:::

:::

::: {.pf-step #q-is-max-negative-definite-dim}
The number $q(M)$ is the largest possible dimension of a subspace
$W\subseteq\RR^n$ on which
$$
x^TMx<0
$$
for every nonzero $x\in W$.

::: pf-proof
Apply the argument of step [](#p-is-max-positive-definite-dim){.pf-ref} to the negative eigenspace $E_-(M)$.
Equivalently, apply step [](#p-is-max-positive-definite-dim){.pf-ref} to the symmetric matrix $-M$.
:::

:::

::: {.pf-step #p-A-leq-p-B}
One has
$$
p(A)\leq p(B).
$$

::: pf-proof
On the positive eigenspace $E_+(A)$,
$$
x^TAx>0
$$
for every nonzero $x$. The hypothesis gives
$$
x^TBx
\geq
x^TAx
>0.
$$
Thus $E_+(A)$ is also a positive-definite subspace for the quadratic form
of $B$. By step [](#p-is-max-positive-definite-dim){.pf-ref},
$$
\dim E_+(A)
\leq
p(B).
$$
Since $\dim E_+(A)=p(A)$, the claim follows.
:::

:::

::: {.pf-step #q-B-leq-q-A}
One has
$$
q(B)\leq q(A).
$$

::: pf-proof
On the negative eigenspace $E_-(B)$,
$$
x^TBx<0
$$
for every nonzero $x$. The hypothesis gives
$$
x^TAx
\leq
x^TBx
<0.
$$
Thus $E_-(B)$ is a negative-definite subspace for the quadratic form of
$A$. By step [](#q-is-max-negative-definite-dim){.pf-ref},
$$
\dim E_-(B)
\leq
q(A),
$$
which is exactly $q(B)\leq q(A)$.
:::

:::

::: {.pf-step #index-inequality}
The index of $A$ is at most the index of $B$.

::: pf-proof
Steps [](#p-A-leq-p-B){.pf-ref} and [](#q-B-leq-q-A){.pf-ref} give
$$
p(A)\leq p(B)
$$
and
$$
-q(A)\leq-q(B).
$$
Adding,
$$
p(A)-q(A)
\leq
p(B)-q(B).
$$
These are the two indices by definition.
:::

:::

::: pf-qed
Step [](#index-inequality){.pf-ref} is the required inequality.
:::

:::

:::
