---
schema: qual/card@1
id: P-CAF13F
kind: problem
title: "A conformal map from the slit disk does not extend to a boundary homeomorphism"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $\varphi: \DD \setminus [0, 1) \to \DD$ be a conformal bijection.
Prove that $\varphi$ does not extend to a homeomorphism $\overline{\DD} \to \overline{\DD}$.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/Complex-Qual-Exam-Fall-13.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. The earlier version of the card asserted that a homeomorphism of the closed disc carries the interior onto the interior, and concluded a contradiction from $y\neq x$ without saying which hypotheses make $y$ and $x$ different; both are made explicit here.

Throughout, $\DD=\theset{z\mid\abs{z}<1}$ is the open unit disc, $\overline{\DD}$ its closure, $[0,1)$ is the slit on the positive real axis, and $\varphi\colon\DD-[0,1)\to\DD$ is a conformal bijection.

::: pf

::: {.pf-step #interior-preserved}
A homeomorphism $\Phi\colon\overline{\DD}\to\overline{\DD}$ carries the interior of $\overline{\DD}$ onto itself, that is $\Phi(\DD)=\DD$.

::: pf-proof
$\DD$ is the interior of $\overline{\DD}$ in $\CC$: it is open and contained in $\overline{\DD}$, and every point of $\overline{\DD}-\DD$ is a boundary point, having neighbourhoods meeting $\CC-\overline{\DD}$. Being an interior is a topological property, preserved by any homeomorphism, so the interior of $\overline{\DD}$ maps onto the interior of the image set, which is again $\overline{\DD}$; hence $\Phi(\DD)=\DD$.
:::

:::

::: {.pf-step #choose-x}
Choose $x\in(0,1)$. Then $x\in\DD$, and $x\notin\DD-[0,1)$.

::: pf-proof
$0<x<1$ gives $\abs{x}<1$, so $x\in\DD$. The set $\DD-[0,1)$ consists of the points of $\DD$ that are not in $[0,1)$, and $x\in[0,1)$ because $0\leq x<1$; so $x$ is not in the domain of $\varphi$.
:::

:::

::: {.pf-step #preimage}
Under the hypothesis that a homeomorphism $\Phi$ extends $\varphi$, there is $y\in\DD-[0,1)$ with $\Phi(y)=\Phi(x)$.

::: pf-proof
$\Phi(x)\in\DD$ by steps [](#choose-x){.pf-ref} and [](#interior-preserved){.pf-ref}. Since $\varphi$ is a bijection onto $\DD$, there is $y\in\DD-[0,1)$ with $\varphi(y)=\Phi(x)$. As $y$ lies in the domain of $\varphi$ and $\Phi$ extends $\varphi$ there, $\Phi(y)=\varphi(y)$, so $\Phi(y)=\Phi(x)$.
:::

:::

::: pf-step
Therefore no such homeomorphism $\Phi$ exists, so $\varphi$ does not extend to a homeomorphism $\overline{\DD}\to\overline{\DD}$.

::: pf-proof
Suppose $\Phi$ is such an extension. By step [](#preimage){.pf-ref} there are $y\in\DD-[0,1)$ and $x\in(0,1)$ with $\Phi(y)=\Phi(x)$; injectivity of the homeomorphism $\Phi$ gives $y=x$. But $x\in[0,1)$ while $y\notin[0,1)$, by step [](#choose-x){.pf-ref} and the choice of $y$. This contradiction shows that no homeomorphic extension exists, which is the assertion.
:::

:::

:::

:::
