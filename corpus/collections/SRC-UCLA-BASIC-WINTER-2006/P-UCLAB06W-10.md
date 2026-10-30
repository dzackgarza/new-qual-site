---
schema: qual/card@1
id: P-UCLAB06W-10
kind: problem
title: Unitary triangularization of a complex linear operator
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $T:V\to V$ be a linear operator on a finite-dimensional complex inner product space.
Show that there exists an ordered orthonormal basis for $V$ such that the matrix $A=(a_{ij})$ of $T$ in this basis is upper triangular, that is, $a_{ij}=0$ if $j<i$.

You may not use canonical-form theorems without proof.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every linear operator on a nonzero finite-dimensional complex vector space has an eigenvector.


::: pf-proof

Let $R$ be a linear operator on a nonzero complex vector space of dimension $n$. Its characteristic polynomial
$$
\det(\lambda I-R)
$$
has degree $n$, so by the fundamental theorem of algebra it has a root $\lambda\in\CC$. Hence
$$
\det(\lambda I-R)=0,
$$
and therefore $\ker(\lambda I-R)\ne0$. Any nonzero vector in this kernel is an eigenvector of $R$.

:::

:::

::: {.pf-step #s1-2}

The assertion holds in dimensions $0$ and $1$.


::: pf-proof

In dimension $0$ there is nothing to prove. In dimension $1$, every unit vector is an orthonormal basis and every $1\times1$ matrix is upper triangular.

:::

:::

::: {.pf-step #s1-3}

Assume the assertion holds in dimension $n-1$, and let $\dim V=n\ge2$. Choose a unit eigenvector $e_1$ of $T$, with
$$
T(e_1)=\lambda e_1.
$$
Let
$$
W=e_1^\perp
$$
and let $P_W:V\to W$ be orthogonal projection. Define
$$
R=P_W\circ T\restrict_W:W\to W.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives a nonzero eigenvector of $T$; rescale it to norm $1$. The orthogonal complement $W$ has dimension $n-1$. Orthogonal projection onto $W$ exists in finite-dimensional inner-product spaces, so the displayed formula defines a linear operator $R$ on $W$.

:::

:::

::: {.pf-step #s1-4}

There is an ordered orthonormal basis
$$
e_2,\ldots,e_n
$$
of $W$ in which the matrix of $R$ is upper triangular.


::: pf-proof

The space $W$ has dimension $n-1$. Apply the induction hypothesis to the linear operator $R:W\to W$.

:::

:::

::: {.pf-step #s1-5}

The ordered list
$$
e_1,e_2,\ldots,e_n
$$
is an orthonormal basis of $V$.


::: pf-proof

The vector $e_1$ is unit, and $e_2,\ldots,e_n$ is an orthonormal basis of $e_1^\perp$. Hence all $n$ vectors are pairwise orthonormal. Since $V=\CC e_1\oplus e_1^\perp$, they span $V$.

:::

:::

::: {.pf-step #s1-6}

In the basis from step [](#s1-5){.pf-ref}, the matrix $A=(a_{ij})$ of $T$ satisfies
$$
a_{ij}=0
\qquad\text{whenever }j<i.
$$


::: pf-proof

For the first column,
$$
T(e_1)=\lambda e_1,
$$
so
$$
a_{i1}=0
$$
for every $i>1$.

Now fix $j\ge2$. Write
$$
T(e_j)=\alpha_j e_1+w_j,
\qquad
w_j\in W.
$$
Applying $P_W$ gives
$$
w_j=P_WT(e_j)=R(e_j).
$$
By step [](#s1-4){.pf-ref}, the matrix of $R$ in the basis $e_2,\ldots,e_n$ is upper triangular. Therefore the coefficient of $e_i$ in $R(e_j)$ is zero whenever
$$
2\le j<i\le n.
$$
The $e_i$-coefficient of $T(e_j)$ agrees with that of $w_j=R(e_j)$ for every $i\ge2$. Hence
$$
a_{ij}=0
$$
whenever $j<i$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the base cases, and steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref} prove the induction step. Thus every finite-dimensional complex linear operator has an ordered orthonormal basis in which its matrix is upper triangular, without invoking a canonical-form theorem.

:::

:::

:::
