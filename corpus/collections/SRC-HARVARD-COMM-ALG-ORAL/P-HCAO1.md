---
schema: qual/card@1
id: P-HCAO1
kind: problem
title: Generators modulo every maximal ideal generate a finite module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Nakayama's Lemma
  - Maximal Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $A$ be a commutative ring, let $M$ be a finitely generated $A$-module, and let $x_1, \ldots, x_n \in M$.

Suppose that the images of $x_1, \ldots, x_n$ generate $M/\mathfrak mM$ for every maximal ideal $\mathfrak m$ of $A$.
Show that $x_1, \ldots, x_n$ generate $M$.
:::

::: {.solution}
Let $N=Ax_1+\cdots+Ax_n\subseteq M$ and $Q=M/N$. As a quotient of the finitely
generated module $M$, the module $Q$ is finitely generated.

::: pf

::: {.pf-step #q-equals-mq}
$Q=\mathfrak mQ$ for every maximal ideal $\mathfrak m$ of $A$.

::: pf-proof
By hypothesis the images of $x_1,\ldots,x_n$ span $M/\mathfrak mM$ over
$A/\mathfrak m$, so $M=N+\mathfrak mM$. Taking the image in $Q=M/N$ gives
$$
Q=(N+\mathfrak mM)/N=\mathfrak m(M/N)=\mathfrak mQ.
$$
:::

:::

::: {.pf-step #q-localizes-to-zero}
$Q_{\mathfrak m}=0$ for every maximal ideal $\mathfrak m$ of $A$.

::: pf-proof
The module $Q_{\mathfrak m}$ is finitely generated over the local ring
$(A_{\mathfrak m},\mathfrak mA_{\mathfrak m})$. Localizing step [](#q-equals-mq){.pf-ref} gives
$Q_{\mathfrak m}=(\mathfrak mA_{\mathfrak m})Q_{\mathfrak m}$, so Nakayama's
lemma gives $Q_{\mathfrak m}=0$.
:::

:::

::: {.pf-step #q-is-zero}
$Q=0$.

::: pf-proof
If $Q\ne0$, the annihilator $\operatorname{Ann}_A(Q)$ of the finitely generated
module $Q$ is a proper ideal, contained in some maximal ideal $\mathfrak m$.
By step [](#q-localizes-to-zero){.pf-ref}, $Q_{\mathfrak m}=0$, so each generator $q_i$ of $Q$ satisfies
$s_iq_i=0$ for some $s_i\notin\mathfrak m$. The product
$s=\prod_is_i\notin\mathfrak m$ annihilates $Q$, contradicting
$\operatorname{Ann}_A(Q)\subseteq\mathfrak m$.
:::

:::

::: pf-qed
By step [](#q-is-zero){.pf-ref}, $M/N=0$, so $N=M$ and $x_1,\ldots,x_n$ generate $M$.
:::

:::
:::
