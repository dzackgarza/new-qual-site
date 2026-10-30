---
schema: qual/card@1
id: P-KSRING17-043
kind: problem
title: The quotient by the intersection of two maximal ideals is a product of two fields
classification:
  areas: [algebra]
  topics:
  - Maximal Ideals
  - Chinese Remainder Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 43 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $M_{1} \neq M_{2}$ be two maximal ideals in the commutative ring $R$ and let $I = M_{1} \cap M_{2}$. Prove that $R/I$ is isomorphic to the direct sum of two fields.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The maximal ideals
$$
M_1
\qquad\text{and}\qquad
M_2
$$
are comaximal:
$$
M_1+M_2=R.
$$


::: pf-proof

Because
$$
M_1\ne M_2,
$$
the ideal $M_2$ is not contained in $M_1$. Choose
$$
x\in M_2\setminus M_1.
$$
Then
$$
M_1
\subsetneq
M_1+M_2.
$$
Since $M_1$ is maximal, every ideal properly containing $M_1$ is the whole ring. Therefore
$$
M_1+M_2=R.
$$

:::

:::

::: {.pf-step #s1-2}

The canonical map
$$
\varphi:R\to R/M_1\oplus R/M_2,
\qquad
\varphi(r)
\coloneqq
(r+M_1,r+M_2)
$$
is surjective.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
M_1+M_2=R.
$$
The two-ideal Chinese remainder theorem therefore implies that the canonical map to the product of the two quotients is surjective.

:::

:::

::: {.pf-step #s1-3}

The kernel of $\varphi$ is
$$
M_1\cap M_2
=
I.
$$


::: pf-proof

One has
$$
\varphi(r)=(0+M_1,0+M_2)
$$
if and only if
$$
r\in M_1
\qquad\text{and}\qquad
r\in M_2.
$$
Hence
$$
\ker\varphi
=
M_1\cap M_2
=
I.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
R/I
\cong
R/M_1\oplus R/M_2.
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, $\varphi$ is a surjective ring homomorphism with kernel $I$. The first isomorphism theorem gives
$$
R/I
\cong
R/M_1\oplus R/M_2.
$$

:::

:::

::: {.pf-step #s1-5}

Each quotient
$$
R/M_i
$$
is a field.


::: pf-proof

Each $M_i$ is maximal. By the maximal-ideal quotient criterion,
$$
R/M_i
$$
is a field for
$$
i=1,2.
$$

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
R/I
\text{ is isomorphic to a direct sum of two fields.}
}
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
