---
schema: qual/card@1
id: P-UCLAB09F-05
kind: problem
title: Linear independence of exponentials with distinct exponents
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
Let $\alpha_1,\ldots,\alpha_n\in\RR$ be distinct.
Suppose $a_1,\ldots,a_n\in\RR$ satisfy
$$
\sum_{i=1}^n a_i e^{\alpha_i t}=0
\qquad\text{for every }t\in(-1,1).
$$
Prove that $a_i=0$ for all $i$.
You may use the differentiation operator and the linear-algebra theorem on eigenvectors with distinct eigenvalues.
:::

::: {.solution}

For each $i$, define
$$
\phi_i(t)=e^{\alpha_i t}
$$
on $(-1,1)$.

::: pf

::: {.pf-step #s1-1}

Let
$$
W=\operatorname{span}\{\phi_1,\ldots,\phi_n\}.
$$
The differentiation operator
$$
D:W\to W
$$
is well-defined.


::: pf-proof

For each $i$,
$$
D\phi_i
=
\phi_i'
=
\alpha_i\phi_i.
$$
Thus the derivative of every spanning vector lies in $W$. By linearity of differentiation, the derivative of every vector in $W$ also lies in $W$.

:::

:::

::: {.pf-step #s1-2}

Each $\phi_i$ is a nonzero eigenvector of $D$ with eigenvalue $\alpha_i$.


::: pf-proof

Step [](#s1-1){.pf-ref} gives
$$
D\phi_i=\alpha_i\phi_i.
$$
Also
$$
\phi_i(t)=e^{\alpha_i t}>0
$$
for every $t$, so $\phi_i$ is not the zero function.

:::

:::

::: {.pf-step #s1-3}

The functions
$$
\phi_1,\ldots,\phi_n
$$
are linearly independent.


::: pf-proof

The eigenvalues
$$
\alpha_1,\ldots,\alpha_n
$$
are pairwise distinct by hypothesis. By the linear-algebra theorem that eigenvectors belonging to distinct eigenvalues are linearly independent, step [](#s1-2){.pf-ref} implies that $\phi_1,\ldots,\phi_n$ are linearly independent in $W$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{a_1=\cdots=a_n=0}.
$$


::: pf-proof

The assumed identity
$$
\sum_{i=1}^n a_i e^{\alpha_i t}=0
$$
for every $t\in(-1,1)$ is the vector-space relation
$$
\sum_{i=1}^n a_i\phi_i=0
$$
in $W$. By step [](#s1-3){.pf-ref}, the functions $\phi_i$ are linearly independent, so every coefficient $a_i$ must vanish.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
