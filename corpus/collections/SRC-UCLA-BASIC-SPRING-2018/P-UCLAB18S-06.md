---
schema: qual/card@1
id: P-UCLAB18S-06
kind: problem
title: Determinant of a $5\times5$ circulant matrix
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Compute
$$
\det\begin{pmatrix}
1&2&4&8&16\\
2&4&8&16&1\\
4&8&16&1&2\\
8&16&1&2&4\\
16&1&2&4&8
\end{pmatrix}.
$$
:::

::: {.solution}

Let
$$
\zeta=e^{2\pi i/5}.
$$

::: pf

::: pf-step

The matrix is circulant, with associated polynomial
$$
p(z)
=
1+2z+4z^2+8z^3+16z^4.
$$


::: pf-proof

Each row is obtained from the preceding row by a cyclic left shift.
For a $5\times5$ circulant matrix with first row
$$
(1,2,4,8,16),
$$
the corresponding polynomial is the displayed polynomial.

:::

:::

::: {.pf-step #s1-2}

The eigenvalues of the matrix are
$$
\boxed{
p(1),p(\zeta),p(\zeta^2),p(\zeta^3),p(\zeta^4).
}
$$


::: pf-proof

For
$$
j=0,1,2,3,4,
$$
let
$$
v_j
=
\begin{pmatrix}
1\\
\zeta^j\\
\zeta^{2j}\\
\zeta^{3j}\\
\zeta^{4j}
\end{pmatrix}.
$$
The cyclic-shift structure gives
$$
Mv_j
=
p(\zeta^j)v_j
$$
up to replacing $\zeta^j$ by its inverse depending on the shift convention.
Since the set
$$
\{1,\zeta,\zeta^2,\zeta^3,\zeta^4\}
$$
is invariant under inversion, the multiset of eigenvalues is exactly the displayed set.
The vectors $v_j$ form a basis because the Fourier matrix is invertible.

:::

:::

::: {.pf-step #s1-3}

For every $z$,
$$
\boxed{
(2z-1)p(z)
=
32z^5-1.
}
$$


::: pf-proof

The polynomial is a finite geometric series:
$$
p(z)
=
\sum_{k=0}^4(2z)^k.
$$
Thus
$$
(2z-1)p(z)
=
(2z)^5-1
=
32z^5-1.
$$

:::

:::

::: {.pf-step #s1-4}

If
$$
z^5=1,
$$
then
$$
\boxed{
p(z)
=
\frac{31}{2z-1}.
}
$$


::: pf-proof

Substitute
$$
z^5=1
$$
into step [](#s1-3){.pf-ref}:
$$
(2z-1)p(z)
=
32-1
=31.
$$
Also
$$
2z-1\ne0
$$
because
$$
z=\frac12
$$
is not a fifth root of unity.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\det M
=
\frac{31^5}
{\displaystyle\prod_{j=0}^4(2\zeta^j-1)}.
$$


::: pf-proof

The determinant is the product of the eigenvalues from step [](#s1-2){.pf-ref}.
Apply step [](#s1-4){.pf-ref} to each fifth root of unity.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
\prod_{j=0}^4(2\zeta^j-1)
=
31.
}
$$


::: pf-proof

The fifth roots of unity are precisely the roots of
$$
z^5-1.
$$
Hence
$$
\prod_{j=0}^4
\left(
\frac12-\zeta^j
\right)
=
\left(\frac12\right)^5-1
=
\frac1{32}-1
=
-\frac{31}{32}.
$$
Since there are five factors,
$$
\prod_{j=0}^4
\left(
\zeta^j-\frac12
\right)
=
\frac{31}{32}.
$$
Multiplying each factor by $2$ gives
$$
\prod_{j=0}^4(2\zeta^j-1)
=
2^5\frac{31}{32}
=
31.
$$

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{
\det M
=
31^4
=
923521.
}
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}:
$$
\det M
=
\frac{31^5}{31}
=
31^4.
$$
Finally,
$$
31^2=961
$$
and
$$
961^2=923521.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required determinant.

:::

:::

:::
