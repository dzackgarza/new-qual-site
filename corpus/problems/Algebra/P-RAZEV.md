---
schema: qual/card@1
id: P-RAZEV
kind: problem
title: Wedderburn's theorem and rational group algebras
classification:
  areas:
  - algebra
  topics:
  - Group Rings
  - Semisimplicity
  - Algebras
relations: []
review: draft
---

::: {.problem}
State the Artin--Wedderburn theorem for finite-dimensional semisimple algebras, and describe the rational group algebras of $C_5$, $C_2\times C_2$, and $Q_8$.
:::

::: {.solution}
::: pf

::: pf-step
(Artin--Wedderburn.) Every finite-dimensional semisimple algebra over a field $k$ is isomorphic to a finite product $\prod_i M_{n_i}(D_i)$, where each $D_i$ is a finite-dimensional division algebra over $k$; the $n_i$ and the $D_i$ up to isomorphism are unique up to order.

::: pf-proof
This is the Artin--Wedderburn theorem. Since $\QQ$ has characteristic $0$, Maschke's theorem makes $\QQ[G]$ semisimple for every finite group $G$, so it applies to the three algebras below.
:::

:::

::: pf-step
$\QQ[C_5]\cong\boxed{\QQ\times\QQ(\zeta_5)}$.

::: pf-proof
$\QQ[C_5]\cong\QQ[x]/(x^5-1)$ and $x^5-1=(x-1)\Phi_5(x)$ with $\Phi_5$ irreducible over $\QQ$ and coprime to $x-1$. The Chinese remainder theorem gives $\QQ[x]/(x-1)\times\QQ[x]/(\Phi_5)\cong\QQ\times\QQ(\zeta_5)$.
:::

:::

::: {.pf-step #klein}
$\QQ[C_2\times C_2]\cong\boxed{\QQ^4}$.

::: pf-proof
$\QQ[C_2]\cong\QQ[x]/(x^2-1)\cong\QQ\times\QQ$ by the Chinese remainder theorem, and $\QQ[C_2\times C_2]\cong\QQ[C_2]\otimes_\QQ\QQ[C_2]\cong(\QQ\times\QQ)\otimes_\QQ(\QQ\times\QQ)\cong\QQ^4$.
:::

:::

::: pf-step
$\QQ[Q_8]\cong\boxed{\QQ^4\times\quaternions_\QQ}$, where $\quaternions_\QQ\coloneqq\QQ\langle i,j\mid i^2=j^2=-1,\ ij=-ji\rangle$ is the rational Hamilton quaternion division algebra.

::: pf-proof
Let $z=-1\in Q_8$, a central element of order $2$, and $e_\pm\coloneqq(1\pm z)/2$, central orthogonal idempotents with $e_++e_-=1$. Then $\QQ[Q_8]\cong\QQ[Q_8]e_+\times\QQ[Q_8]e_-$. The first factor is $\QQ[Q_8/\langle z\rangle]\cong\QQ[C_2\times C_2]\cong\QQ^4$ by step [](#klein){.pf-ref}, so the second factor has dimension $8-4=4$. The homomorphism $\QQ[Q_8]\to\quaternions_\QQ$ sending $i,j$ to $i,j$ is surjective and sends $z$ to $-1$, so it kills $e_+$ and maps $\QQ[Q_8]e_-$ onto the $4$-dimensional $\quaternions_\QQ$; it is therefore an isomorphism on that factor. $\quaternions_\QQ$ is a division algebra because $a+bi+cj+dk\ne0$ has inverse $(a-bi-cj-dk)/(a^2+b^2+c^2+d^2)$.
:::

:::

:::
:::
