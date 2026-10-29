---
schema: qual/card@1
id: P-UCLAB15S-11
kind: problem
title: Ten commuting real matrices of the same finite order
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Two matrices $A,B$ are called commuting if $AB=BA$.
The order of a matrix $A$ is the smallest integer $k>0$ such that $A^k=I$; if no such $k$ exists, its order is infinite.

Prove that there exist ten distinct real $2\times2$ matrices which are pairwise commuting and all have the same finite order.
:::

::: {.solution}

For
$$
k=1,\ldots,10,
$$
define
$$
\theta_k=\frac{2\pi k}{11}
$$
and let
$$
\boxed{
R_k
=
\begin{pmatrix}
\cos\theta_k&-\sin\theta_k\\
\sin\theta_k&\cos\theta_k
\end{pmatrix}.
}
$$

::: pf

::: pf-step

Each $R_k$ is a real $2\times2$ rotation matrix.


::: pf-proof

Its entries are real, and it is the standard matrix for rotation through angle
$$
\theta_k.
$$

:::

:::

::: {.pf-step #s1-2}

For any real angles $\alpha,\beta$,
$$
R(\alpha)R(\beta)
=
R(\alpha+\beta).
$$


::: pf-proof

Multiply the standard rotation matrices and use the angle-addition formulas
$$
\cos(\alpha+\beta)
=
\cos\alpha\cos\beta-\sin\alpha\sin\beta,
$$
$$
\sin(\alpha+\beta)
=
\sin\alpha\cos\beta+\cos\alpha\sin\beta.
$$

:::

:::

::: {.pf-step #s1-3}

The matrices
$$
R_1,\ldots,R_{10}
$$
are pairwise commuting.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
R_jR_k
=
R(\theta_j+\theta_k)
=
R_kR_j.
$$

:::

:::

::: {.pf-step #s1-4}

The matrices
$$
R_1,\ldots,R_{10}
$$
are pairwise distinct.


::: pf-proof

If
$$
R_j=R_k,
$$
then the two rotations have the same angle modulo $2\pi$:
$$
\theta_j\equiv\theta_k\pmod{2\pi}.
$$
Thus
$$
\frac{2\pi(j-k)}{11}
$$
is an integer multiple of $2\pi$, so
$$
11\mid(j-k).
$$
Since
$$
1\le j,k\le10,
$$
this forces
$$
j=k.
$$

:::

:::

::: {.pf-step #s1-5}

For every positive integer $m$,
$$
R_k^m
=
R\left(\frac{2\pi km}{11}\right).
$$


::: pf-proof

Apply step [](#s1-2){.pf-ref} repeatedly.

:::

:::

::: {.pf-step #s1-6}

One has
$$
R_k^{11}=I
$$
for every
$$
k=1,\ldots,10.
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
R_k^{11}
=
R(2\pi k)
=
I.
$$

:::

:::

::: {.pf-step #s1-7}

If
$$
1\le m<11,
$$
then
$$
R_k^m\ne I.
$$


::: pf-proof

If
$$
R_k^m=I,
$$
then by step [](#s1-5){.pf-ref},
$$
\frac{2\pi km}{11}
$$
must be an integer multiple of $2\pi$.
Thus
$$
11\mid km.
$$
Because $11$ is prime and
$$
1\le k\le10,
$$
one has
$$
11\nmid k.
$$
Hence
$$
11\mid m,
$$
contradicting
$$
1\le m<11.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore every $R_k$ has order exactly
$$
\boxed{11}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} shows the order divides $11$, while step [](#s1-7){.pf-ref} shows no smaller positive exponent gives the identity.

:::

:::

::: {.pf-step #s1-9}

Thus
$$
\boxed{
R_1,\ldots,R_{10}
}
$$
are ten distinct pairwise commuting real $2\times2$ matrices, all of the same finite order.


::: pf-proof

Distinctness is step [](#s1-4){.pf-ref}, pairwise commutativity is step [](#s1-3){.pf-ref}, and common order $11$ is step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required construction.

:::

:::

:::
