---
schema: qual/card@1
id: P-BKF83-8
kind: problem
title: Symmetric orthogonal transformations of $\RR^3$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the involution identity, orthogonal eigenspace decomposition, and all four possible eigenvalue multiplicity patterns in dimension three.
---

::: {.problem}
Let $A:\mathbb R^3\to\mathbb R^3$ have a matrix, in the standard basis, that is both symmetric and orthogonal. Prove that $A$ is one of the following:

1. $I$ or $-I$;
2. a rotation through $180^\circ$ about an axis;
3. a reflection across a two-dimensional subspace.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One has
$$
A^2=I,
$$
so every eigenvalue of $A$ is either $1$ or $-1$.

::: pf-proof

Orthogonality gives
$$
A^{\mathsf T}A=I,
$$
while symmetry gives
$$
A^{\mathsf T}=A.
$$
Hence $A^2=I$. Therefore every eigenvalue $\lambda$ satisfies
$$
\lambda^2=1,
$$
so $\lambda=\pm1$.

:::

:::

::: {.pf-step #s2}

There is an orthogonal direct-sum decomposition
$$
\mathbb R^3=V_+\oplus V_-,
$$
where
$$
V_+=\ker(A-I),
\qquad
V_-=\ker(A+I),
$$
and $A$ acts as $I$ on $V_+$ and as $-I$ on $V_-$.

::: pf-proof

Since $A$ is real symmetric, the spectral theorem gives an orthonormal
basis of eigenvectors. Step [](#s1){.pf-ref} shows that all corresponding eigenvalues
are $1$ or $-1$. Thus the spans of the two kinds of eigenvectors are
$V_+$ and $V_-$ and are orthogonal complements.

:::

:::

::: {.pf-step #s3}

If
$$
\dim V_+=3
\quad\text{or}\quad
\dim V_+=0,
$$
then respectively
$$
A=I
\quad\text{or}\quad
A=-I.
$$

::: pf-proof

If $V_+=\mathbb R^3$, step [](#s2){.pf-ref} says that $A$ fixes every vector. If
$V_-=\mathbb R^3$, it negates every vector.

:::

:::

::: {.pf-step #s4}

If $\dim V_+=1$, then $A$ is a rotation through
$180^\circ$ about the axis $V_+$.

::: pf-proof

Let $L=V_+$. By step [](#s2){.pf-ref},
$$
V_-=L^\perp.
$$
Thus $A$ fixes every vector on the axis $L$ and sends every vector in the
perpendicular plane $L^\perp$ to its negative. On each plane perpendicular
to $L$, this is exactly rotation by angle $\pi$. Hence $A$ is rotation
through $180^\circ$ about $L$.

:::

:::

::: {.pf-step #s5}

If $\dim V_+=2$, then $A$ is reflection across the plane $V_+$.

::: pf-proof

Let $P=V_+$. Then
$$
V_-=P^\perp
$$
is one-dimensional. Step [](#s2){.pf-ref} says that $A$ fixes $P$ pointwise and
negates the normal direction $P^\perp$. This is precisely reflection
across $P$.

:::

:::

::: {.pf-step #s6}

These cases exhaust all possibilities.

::: pf-proof

The integer $\dim V_+$ is one of
$$
0,1,2,3.
$$
Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} identify the transformation in each case.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives exactly the classification stated in the problem.

:::

:::

:::
