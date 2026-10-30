---
schema: qual/card@1
id: P-BKS06-8B
kind: problem
title: A complex matrix with $\inner{x}{Ax}$ real for all $x$ is Hermitian
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $\langle\ ,\ \rangle$ be the standard Hermitian inner product on $\CC^{n}$.
Let $A$ be an $n \times n$ matrix with complex entries.
Suppose $\langle x, Ax \rangle$ is real for all $x \in \CC^{n}$. Prove that $A$ is Hermitian.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $B=A-A^H$. Then $x^HBx=0$ for every $x\in\CC^n$.

::: pf-proof

Since $x^HAx$ is real, $x^HAx=\overline{x^HAx}=(x^HAx)^H=x^HA^Hx$.

:::

:::

::: {.pf-step #s2}

$B=0$.

::: pf-proof

$B^H=-B$, so $B$ is normal, and by the spectral theorem $B=UDU^H$ with $U$ unitary and $D$ diagonal. If $Bx=\lambda x$ with $x\ne0$, step [](#s1){.pf-ref} gives $0=x^HBx=\lambda\norm{x}^2$, so $\lambda=0$. Hence $D=0$ and $B=0$.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $A=A^H$, so $A$ is Hermitian.

:::

:::

:::
