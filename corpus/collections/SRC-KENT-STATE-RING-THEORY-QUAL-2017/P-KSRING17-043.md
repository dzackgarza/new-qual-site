---
schema: qual/card@1
id: P-KSRING17-043
kind: problem
title: The quotient by the intersection of two maximal ideals is a product of two fields
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 43 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
[NEW] Let $M _ { 1 } \neq M _ { 2 }$ be two maximal ideals in the commutative ring R and let $I = M _ { 1 } \cap M _ { 2 }$ Prove that $R / I$ is isomorphic to the direct sum of two fields.
:::

::: {.solution}
<1>1. The maximal ideals
$$
M_1
\qquad\text{and}\qquad
M_2
$$
are comaximal:
$$
M_1+M_2=R.
$$

::: {.proof}
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

<1>2. The canonical map
$$
\varphi:R\to R/M_1\oplus R/M_2,
\qquad
\varphi(r)
\coloneqq
(r+M_1,r+M_2)
$$
is surjective.

::: {.proof}
By step <1>1,
$$
M_1+M_2=R.
$$
The two-ideal Chinese remainder theorem therefore implies that the canonical map to the product of the two quotients is surjective.
:::

<1>3. The kernel of $\varphi$ is
$$
M_1\cap M_2
=
I.
$$

::: {.proof}
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

<1>4. Therefore
$$
R/I
\cong
R/M_1\oplus R/M_2.
$$

::: {.proof}
By steps <1>2--<1>3, $\varphi$ is a surjective ring homomorphism with kernel $I$. The first isomorphism theorem gives
$$
R/I
\cong
R/M_1\oplus R/M_2.
$$
:::

<1>5. Each quotient
$$
R/M_i
$$
is a field.

::: {.proof}
Each $M_i$ is maximal. By the maximal-ideal quotient criterion,
$$
R/M_i
$$
is a field for
$$
i=1,2.
$$
:::

<1>6. Hence
$$
\boxed{
R/I
\text{ is isomorphic to a direct sum of two fields.}
}
$$

::: {.proof}
Combine steps <1>4 and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
