---
schema: qual/card@1
id: P-5AS2X
kind: problem
title: The center of $M_n(R)$ is $Z(R)I_n$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Matrices
  - Rings
relations: []
review: draft
---

::: {.problem}
Let $R$ be a ring with identity $1_R \ne 0$, and let $M_n(R)$ be the ring of $n \times n$ matrices over $R$ ($n \ge 1$).

(a) Show that the center of the ring $M_n(R)$ consists precisely of scalar matrices of the form $r I_n$ where $r \in Z(R)$ is in the center of $R$.

(b) Show that $Z(M_n(R)) \cong Z(R)$ as rings.
:::

::: {.solution}
For $1 \le i, j \le n$ let $E_{i,j} \in M_n(R)$ be the matrix unit with $1_R$ in position $(i, j)$ and $0$ elsewhere.

::: pf

::: {.pf-step #s1}

(a) $Z(M_n(R)) = \{r I_n : r \in Z(R)\}$.

::: pf-proof

::: {.pf-step #s1-1}

A matrix $A=(a_{k,\ell})$ that commutes with every $E_{i,j}$ is a scalar matrix $rI_n$ with $r\in R$.

::: pf-proof

For all $i,j,k,\ell$,
$$(A E_{i, j})_{k, \ell} = a_{k, i} \delta_{j, \ell},\qquad (E_{i, j} A)_{k, \ell} = \delta_{k, i} a_{j, \ell}.$$
Taking $k = i$ and $\ell = j$ gives $a_{i, i} = a_{j, j}$ for all $i,j$, so the diagonal entries share a common value $r$. Taking $k \ne i$ and $\ell = j$ gives $a_{k, i} = 0$, so every off-diagonal entry vanishes. Hence $A = r I_n$.

:::

:::

::: {.pf-step #s1-2}

If $rI_n$ is central, then $r\in Z(R)$.

::: pf-proof

For $s \in R$, $(r s) I_n = (r I_n)(s I_n) = (s I_n)(r I_n) = (s r) I_n$, and comparing $(1,1)$ entries gives $rs = sr$.

:::

:::

::: {.pf-step #s1-3}

If $r \in Z(R)$, then $rI_n$ is central.

::: pf-proof

For $B = (b_{i, j}) \in M_n(R)$, $(r I_n B)_{i, j} = r b_{i, j} = b_{i, j} r = (B (r I_n))_{i, j}$.

:::

:::

::: pf-qed

A central matrix commutes with every $E_{i,j}$, so steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give $Z(M_n(R))\subseteq\{rI_n : r\in Z(R)\}$; step [](#s1-3){.pf-ref} gives the reverse inclusion.

:::

:::

:::

::: pf-step

(b) The map $\Phi\colon Z(R) \to Z(M_n(R))$, $\Phi(r) = r I_n$, is a ring isomorphism.

::: pf-proof

For $r_1, r_2 \in Z(R)$,
$$\Phi(r_1 + r_2) = \Phi(r_1) + \Phi(r_2),\qquad \Phi(r_1 r_2) = (r_1 I_n)(r_2 I_n) = \Phi(r_1) \Phi(r_2),\qquad \Phi(1_R) = I_n.$$
If $\Phi(r) = 0$, then the $(1,1)$ entry gives $r = 0$, so $\Phi$ is injective. By step [](#s1){.pf-ref} every element of $Z(M_n(R))$ is $\Phi(r)$ for some $r \in Z(R)$.

:::

:::

:::

:::
