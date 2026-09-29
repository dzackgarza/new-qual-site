---
schema: qual/card@1
id: P-BKF96-7
kind: problem
title: Possible orders of elements of $GL_2(\mathbb F_p)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Split according to the characteristic polynomial. An irreducible
    quadratic puts A in F_{p^2}^times; a split polynomial gives either a
    diagonal matrix or a scalar times a size-two unipotent block.
---

::: {.problem}
Let $p$ be prime. Show that every element of
\[
GL_2(\mathbb F_p)
\]
has order dividing either
\[
p^2-1
\qquad\text{or}\qquad
p(p-1).
\]
:::

::: {.solution}
Let
$$
A\in\GL_2(\FF_p).
$$

::: pf

::: {.pf-step #s1}

If the characteristic polynomial of $A$ is irreducible over
$\FF_p$, then the order of $A$ divides
$$
p^2-1.
$$

::: pf-proof

In this case the characteristic polynomial is also the minimal polynomial,
because both have degree $2$. Therefore
$$
\FF_p[A]
\cong
\FF_p[t]/(m_A(t)).
$$
Since $m_A$ is irreducible quadratic, this quotient is the field with
$p^2$ elements:
$$
\FF_p[A]\cong\FF_{p^2}.
$$
The matrix $A$ is invertible, so it corresponds to an element of
$$
\FF_{p^2}^{\times},
$$
a group of order $p^2-1$. By Lagrange's theorem, the order of $A$ divides
$p^2-1$.

:::

:::

::: {.pf-step #s2}

Suppose the characteristic polynomial of $A$ splits over $\FF_p$
with two distinct roots. Then the order of $A$ divides
$$
p-1.
$$

::: pf-proof

With distinct eigenvalues, $A$ is diagonalizable over $\FF_p$:
$$
A\sim
\begin{pmatrix}
\lambda&0\\
0&\mu
\end{pmatrix},
$$
where
$$
\lambda,\mu\in\FF_p^\times.
$$
Each nonzero field element satisfies
$$
\lambda^{p-1}=\mu^{p-1}=1.
$$
Hence
$$
A^{p-1}=I,
$$
so the order divides $p-1$.

:::

:::

::: {.pf-step #s3}

Suppose the characteristic polynomial is
$$
(t-\lambda)^2
$$
with $\lambda\in\FF_p^\times$. Then the order of $A$ divides
$$
p(p-1).
$$

::: pf-proof

If $A=\lambda I$, its order divides $p-1$, so the conclusion follows.
Otherwise its Jordan form over $\FF_p$ is
$$
A\sim
\lambda(I+N),
\qquad
N=
\begin{pmatrix}
0&c\\
0&0
\end{pmatrix}
$$
for some $c\neq0$, with
$$
N^2=0.
$$
The scalar matrix $\lambda I$ commutes with $I+N$. Moreover,
$$
\lambda^{p-1}=1
$$
and, in characteristic $p$,
$$
(I+N)^p
=
I+pN
=
I,
$$
because every higher power of $N$ vanishes. Therefore
$$
A^{p(p-1)}
=
\lambda^{p(p-1)}(I+N)^{p(p-1)}
=
I.
$$
Thus the order of $A$ divides $p(p-1)$.

:::

:::

::: {.pf-step #s4}

Every element of $\GL_2(\FF_p)$ has order dividing either
$$
p^2-1
$$
or
$$
p(p-1).
$$

::: pf-proof

Every quadratic characteristic polynomial is either irreducible or splits
over $\FF_p$. Step [](#s1){.pf-ref} handles the irreducible case. In the split case,
either the roots are distinct, handled by step [](#s2){.pf-ref}, or the polynomial has
a repeated root, handled by step [](#s3){.pf-ref}. Since $p-1$ divides $p(p-1)$, the
distinct-root case also satisfies the second bound.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required dichotomy.

:::

:::

:::
