---
schema: qual/card@1
id: P-UCTOP290-S12-5
kind: problem
title: "Cohomology of the suspension and vanishing of positive-degree cup products"
classification:
  areas:
  - topology
  topics:
  - Cohomology Ring
  - Suspension
relations: []
review: draft
---

::: problem
Let $\Sigma X$ be the suspension of a space $X$, and let $U, V$ be the open sets obtained as the complements of the two suspension points.
Show that $H^*(\Sigma X, U) \cong \widetilde{H}^*(\Sigma X)$.
By considering the cup product
\[
H^*(\Sigma X, U) \times H^*(\Sigma X, V) \to H^*(\Sigma X, U \cup V),
\]
deduce that the cup product of any two cohomology classes of positive degree on $\Sigma X$ is zero.
:::

::: {.solution}
<1>1. The open set $U=\Sigma X\setminus\{\text{one suspension point}\}$ is contractible, and similarly for $V$.
::: {.proof}
Removing one suspension point leaves an open cone on $X$, which contracts toward the opposite suspension point.
:::

<1>2. The map in the long exact sequence of the pair gives a natural isomorphism
$$
\boxed{H^*(\Sigma X,U)\cong\widetilde H^*(\Sigma X)}.
$$
::: {.proof}
Since $U$ is nonempty and contractible, its reduced cohomology vanishes. The reduced long exact sequence for the pair $(\Sigma X,U)$ therefore identifies relative cohomology with reduced cohomology of $\Sigma X$ in every degree.
:::

<1>3. Every positive-degree class $a\in H^*(\Sigma X)$ has a lift
$$
\bar a\in H^*(\Sigma X,U),
$$
and every positive-degree class $b$ has a lift
$$
\bar b\in H^*(\Sigma X,V).
$$
::: {.proof}
Apply <1>2 to $U$ and to $V$. In positive degree reduced and ordinary cohomology agree.
:::

<1>4. Their relative cup product lies in
$$
H^*(\Sigma X,U\cup V)=H^*(\Sigma X,\Sigma X)=0.
$$
::: {.proof}
The relative cup product has the form
$$
H^p(\Sigma X,U)\times H^q(\Sigma X,V)
\to H^{p+q}(\Sigma X,U\cup V).
$$
Since the two complements together cover the suspension, $U\cup V=\Sigma X$.
:::

<1>5. Hence every cup product of two positive-degree classes on a suspension is zero.
::: {.proof}
The natural map from the relative product in <1>4 to absolute cohomology sends $\bar a\smile\bar b$ to $a\smile b$. The relative product is zero, so
$$
\boxed{a\smile b=0.}
$$
:::
:::
