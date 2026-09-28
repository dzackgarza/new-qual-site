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
<1>1. One has
$$
A^2=I,
$$
so every eigenvalue of $A$ is either $1$ or $-1$.

::: {.proof}
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

<1>2. There is an orthogonal direct-sum decomposition
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

::: {.proof}
Since $A$ is real symmetric, the spectral theorem gives an orthonormal
basis of eigenvectors. Step <1>1 shows that all corresponding eigenvalues
are $1$ or $-1$. Thus the spans of the two kinds of eigenvectors are
$V_+$ and $V_-$ and are orthogonal complements.
:::

<1>3. If
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

::: {.proof}
If $V_+=\mathbb R^3$, step <1>2 says that $A$ fixes every vector. If
$V_-=\mathbb R^3$, it negates every vector.
:::

<1>4. If $\dim V_+=1$, then $A$ is a rotation through
$180^\circ$ about the axis $V_+$.

::: {.proof}
Let $L=V_+$. By step <1>2,
$$
V_-=L^\perp.
$$
Thus $A$ fixes every vector on the axis $L$ and sends every vector in the
perpendicular plane $L^\perp$ to its negative. On each plane perpendicular
to $L$, this is exactly rotation by angle $\pi$. Hence $A$ is rotation
through $180^\circ$ about $L$.
:::

<1>5. If $\dim V_+=2$, then $A$ is reflection across the plane $V_+$.

::: {.proof}
Let $P=V_+$. Then
$$
V_-=P^\perp
$$
is one-dimensional. Step <1>2 says that $A$ fixes $P$ pointwise and
negates the normal direction $P^\perp$. This is precisely reflection
across $P$.
:::

<1>6. These cases exhaust all possibilities.

::: {.proof}
The integer $\dim V_+$ is one of
$$
0,1,2,3.
$$
Steps <1>3--<1>5 identify the transformation in each case.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives exactly the classification stated in the problem.
:::
:::
