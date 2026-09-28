---
schema: qual/card@1
id: P-F2XQP
kind: problem
title: Polar decomposition of operators on a Hilbert space
classification:
  areas:
  - algebra
  topics:
  - Functional Analysis
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Consider the simple operator on C given by multiplication by a complex number.
It decomposes into a stretch and a rotation.
What is the generalisation of this to operators on a Hilbert space?
:::

::: {.solution}
The generalization of $z=e^{i\theta}|z|$ is the polar decomposition.
Let $H$ be a complex Hilbert space, $T\in B(H)$, and $|T|=\sqrt{T^*T}$, the unique positive square root of the positive operator $T^*T$.
A \dfn{partial isometry} is an operator $U$ that is isometric on $(\ker U)^\perp$.

<1>1. $\norm{\,|T|x\,}=\norm{Tx}$ for every $x\in H$; hence $\ker|T|=\ker T$ and $\overline{\operatorname{im}|T|}=(\ker T)^\perp$.

::: {.proof}
$\norm{\,|T|x\,}^2=\inner{|T|^2x}{x}=\inner{T^*Tx}{x}=\norm{Tx}^2$.
Since $|T|$ is self-adjoint, $\overline{\operatorname{im}|T|}=(\ker|T|)^\perp$.
:::

<1>2. There is a partial isometry $U$ with $\ker U=\ker T$ and $T=U|T|$.

::: {.proof}
Define $U_0\colon\operatorname{im}|T|\to\operatorname{im}T$ by $U_0(|T|x)=Tx$; it is well defined and isometric by step <1>1.
It extends by continuity to an isometry $U_1\colon\overline{\operatorname{im}|T|}\to\overline{\operatorname{im}T}$.
Put $U=U_1$ on $\overline{\operatorname{im}|T|}$ and $U=0$ on its orthogonal complement $\ker|T|=\ker T$.
Then $U|T|x=Tx$ for every $x$.
:::

<1>3. If $T=WP$ with $P\ge0$ and $W$ a partial isometry with $\ker W=\ker P$, then $P=|T|$ and $W=U$.

::: {.proof}
$W^*W$ is the orthogonal projection onto $(\ker W)^\perp=(\ker P)^\perp=\overline{\operatorname{im}P}$, so $T^*T=PW^*WP=P^2$, and $P=|T|$ by uniqueness of positive square roots.
Then $W(|T|x)=Tx=U(|T|x)$, so $W=U$ on $\overline{\operatorname{im}|T|}$, and both vanish on $\ker|T|$.
:::

<1>4. If $T$ is invertible, then $U$ is unitary.

::: {.proof}
Then $\ker T=0$ and $\operatorname{im}T=H$, so $U$ is an isometry of $H$ onto $H$.
:::
:::
