---
schema: qual/card@1
id: P-EJKY7
kind: problem
title: $\pi_1$ and $H^*$ of $S^1$ with $2$-cells attached via $z^3$ and $z^5$; not
  homeomorphic to $S^2$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Fundamental Group
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: claude-opus-5.5
  date: 2026-10-29
  note: "Rewrote the bulleted solution as a structured proof. The earlier text gave H_1(X) = 1, called 3Z + 5Z = Z a ring identity, and gave the cohomology ring as an exterior algebra on a degree-2 class."
---

::: {.problem}
Let $X$ be $S^1$ with two $2$-cells attached via $z\mapsto z^5$ and $z\mapsto z^3$.

(a) Compute $\pi_1(X)$ and $H^*(X)$ as a ring.

(b) Show that $X$ is not homeomorphic to $S^2$.
:::

::: {.solution}

Give $X$ the CW structure with one $0$-cell $v$, one $1$-cell $e$ (so that $X^{(1)}=S^1$), and $2$-cells $e_1,e_2$ attached by $z\mapsto z^3$ and $z\mapsto z^5$.

::: pf

::: {.pf-step #pi1}

$\pi_1(X)=\boxed{1}$.

::: pf-proof

By van Kampen, $\pi_1(X)=\langle a\mid a^3,a^5\rangle$, where $a$ is the class of $e$. Since $a=a^{6}a^{-5}=(a^3)^2(a^5)^{-1}$, the group is trivial.

:::

:::

::: {.pf-step #homology}

$H_0(X)\cong\ZZ$, $H_1(X)=0$, $H_2(X)\cong\ZZ$, and $H_k(X)=0$ for $k\ge3$.

::: pf-proof

The cellular chain complex is
$$0\to\ZZ e_1\oplus\ZZ e_2\xrightarrow{d_2}\ZZ e\xrightarrow{d_1}\ZZ v\to0,$$
with $d_1=0$ and $d_2(e_1)=3e$, $d_2(e_2)=5e$. Since $\gcd(3,5)=1$, $d_2$ is onto, so $H_1=0$, and $\ker d_2=\ZZ(5e_1-3e_2)\cong\ZZ$, so $H_2\cong\ZZ$. There are no cells above dimension $2$.

:::

:::

::: pf-step

$H^*(X)\cong\boxed{\ZZ[x]/(x^2)}$ with $\abs{x}=2$.

::: pf-proof

All homology groups in step [](#homology){.pf-ref} are free, so by the universal coefficient theorem $H^k(X)\cong\Hom(H_k(X),\ZZ)$: this is $\ZZ$ for $k=0,2$ and $0$ otherwise. Let $x$ generate $H^2(X)$. The product $x^2$ lies in $H^4(X)=0$, and $1\in H^0$ is the unit.

:::

:::

::: pf-step

$X$ is not homeomorphic to $S^2$.

::: pf-proof

Let $p$ be a point in the interior of $e_1$. Then $X\setminus\{p\}$ deformation retracts onto $S^1\cup_{z^5}e_2$, by radial projection of the punctured $2$-cell $e_1$ onto its boundary. That space has fundamental group $\langle a\mid a^5\rangle\cong\ZZ/5$. If $h:X\to S^2$ were a homeomorphism, it would restrict to a homeomorphism $X\setminus\{p\}\to S^2\setminus\{h(p)\}\cong\RR^2$, which is simply connected. This contradicts $\pi_1(X\setminus\{p\})\cong\ZZ/5$.

:::

:::

:::

:::
