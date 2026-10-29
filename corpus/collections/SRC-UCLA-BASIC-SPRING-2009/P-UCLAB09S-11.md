---
schema: qual/card@1
id: P-UCLAB09S-11
kind: problem
title: Jordan normal form and the minimal polynomial
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
(a) Explain precisely the statement: “Every matrix can be brought to Jordan normal form, and the normal form is essentially unique.”
No proofs are required, but state all hypotheses and define explicitly “brought to Jordan normal form,” “Jordan normal form,” and “essentially unique.”

(b) Define the minimal polynomial of a matrix.
How can it be determined from a matrix in Jordan normal form?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Jordan normal form theorem applies to matrices
$$
A\in M_n(\CC),
$$
or more generally to matrices over an algebraically closed field.


::: pf-proof

Over an arbitrary field, the characteristic polynomial need not split into linear factors, so ordinary Jordan blocks need not exist.
Over $\CC$, every characteristic polynomial splits by the fundamental theorem of algebra.
Thus the standard Jordan normal form theorem applies.

:::

:::

::: {.pf-step #s1-2}

A Jordan block of size $r$ with eigenvalue $\lambda$ is the matrix
$$
\boxed{
J_r(\lambda)
=
\begin{pmatrix}
\lambda&1&0&\cdots&0\\
0&\lambda&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&\lambda&1\\
0&\cdots&\cdots&0&\lambda
\end{pmatrix}.
}
$$


::: pf-proof

This is the definition of a Jordan block.
Equivalently,
$$
J_r(\lambda)=\lambda I_r+N_r,
$$
where $N_r$ has ones on the superdiagonal and zeros elsewhere.

:::

:::

::: {.pf-step #s1-3}

A matrix is in *Jordan normal form* if it is block diagonal and every diagonal block is a Jordan block.


::: pf-proof

Thus a Jordan normal form has the shape
$$
J
=
J_{r_1}(\lambda_1)
\oplus\cdots\oplus
J_{r_s}(\lambda_s),
$$
where the block sizes satisfy
$$
r_1+\cdots+r_s=n.
$$

:::

:::

::: {.pf-step #s1-4}

To say that $A$ can be *brought to Jordan normal form* means that there exists an invertible matrix
$$
S\in GL_n(\CC)
$$
such that
$$
\boxed{S^{-1}AS=J}
$$
for some Jordan normal form $J$.


::: pf-proof

This is precisely similarity of $A$ to a Jordan normal form.
Equivalently, $J$ is the matrix of the same linear operator in a suitable basis.

:::

:::

::: {.pf-step #s1-5}

The Jordan normal form is *essentially unique* in the following precise sense:
for each eigenvalue $\lambda$, the multiset of sizes of the Jordan blocks with eigenvalue $\lambda$ is uniquely determined by $A$.


::: pf-proof

Thus two Jordan normal forms are similar if and only if one can be obtained from the other by permuting the Jordan blocks.
The order in which blocks are written is irrelevant, but the eigenvalue attached to each block and every block size are invariants.
This is the uniqueness assertion in the Jordan normal form theorem.

:::

:::

::: {.pf-step #s1-6}

The complete statement of the Jordan normal form theorem is therefore:
for every
$$
A\in M_n(\CC),
$$
there exists an invertible $S$ such that
$$
S^{-1}AS
$$
is block diagonal with Jordan blocks, and the resulting collection of Jordan blocks is unique up to permutation.


::: pf-proof

This combines the definitions from steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} with the existence and uniqueness assertions of the Jordan normal form theorem.
No proof of the theorem is required by the problem.

:::

:::

::: {.pf-step #s1-7}

The *minimal polynomial* of $A$ is the unique monic polynomial
$$
\boxed{\mu_A(t)\in\CC[t]}
$$
of least positive degree such that
$$
\boxed{\mu_A(A)=0}.
$$


::: pf-proof

The set
$$
\{p(t)\in\CC[t]:p(A)=0\}
$$
is a nonzero ideal because the characteristic polynomial annihilates $A$ by Cayley--Hamilton.
Since $\CC[t]$ is a principal ideal domain, this ideal has a unique monic generator.
That generator is the minimal polynomial.
Equivalently, it is the monic annihilating polynomial of least degree.

:::

:::

::: {.pf-step #s1-8}

For a Jordan block
$$
J_r(\lambda),
$$
the minimal polynomial is
$$
\boxed{(t-\lambda)^r}.
$$


::: pf-proof

One has
$$
J_r(\lambda)-\lambda I=N_r,
$$
where
$$
N_r^r=0
$$
but
$$
N_r^{r-1}\ne0.
$$
Therefore
$$
(J_r(\lambda)-\lambda I)^r=0
$$
and no lower positive power vanishes.

:::

:::

::: {.pf-step #s1-9}

Suppose the Jordan form of $A$ has, for each eigenvalue $\lambda$, largest block size
$$
m_\lambda.
$$
Then
$$
\boxed{
\mu_A(t)
=
\prod_{\lambda}
(t-\lambda)^{m_\lambda}.
}
$$


::: pf-proof

A polynomial annihilates a block diagonal matrix exactly when it annihilates every Jordan block.
By step [](#s1-8){.pf-ref}, to annihilate every block with eigenvalue $\lambda$, the polynomial must contain
$$
(t-\lambda)^{m_\lambda},
$$
where $m_\lambda$ is the size of the largest such block.
For distinct eigenvalues, these powers are relatively prime.
Thus their product is the monic polynomial of least degree annihilating all blocks simultaneously.
Similarity preserves polynomial identities, so this is also the minimal polynomial of $A$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} answer part (a), and steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref} answer part (b).

:::

:::

:::
