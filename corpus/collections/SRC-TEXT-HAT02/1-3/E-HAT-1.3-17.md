---
schema: qual/card@1
id: E-HAT-1.3-17
kind: problem
title: Normal covering spaces from group extensions
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Given a group $G$ and a normal subgroup $N$, show that there exists a normal covering space $\tilde{X} \to X$ with $\pi_1(X) \approx G$, $\pi_1(\tilde{X}) \approx N$, and deck transformation group $G(\tilde{X}) \approx G/N$.
:::

::: {.solution}

::: pf

::: pf-step

Choose a CW complex $X$ with $\pi_1(X) \cong G$ (e.g., the presentation complex of $G$; a $K(G,1)$).

::: pf-proof

every group is the fundamental group of a CW complex (attach $2$-cells for relations and kill higher homotopy).

:::

:::

::: {.pf-step #s2}

Let $p : \tilde X \to X$ be the connected covering corresponding to the subgroup $N \le \pi_1(X) \cong G$.

::: pf-proof

covering space theory (for nice $X$, connected coverings are classified by conjugacy classes of subgroups of $\pi_1$).

:::

:::

::: {.pf-step #s3}

Then $\pi_1(\tilde X) \cong N$.

::: pf-proof

Step [](#s2){.pf-ref} ($p_*(\pi_1(\tilde X)) = N$).

:::

:::

::: {.pf-step #s4}

The covering is normal iff $N$ is normal in $\pi_1(X)$.

::: pf-proof

a covering is normal (regular) iff the corresponding subgroup is normal.

:::

:::

::: {.pf-step #s5}

Hence, since $N \triangleleft G$, the covering $\tilde X \to X$ is normal.

::: pf-proof

Step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

The group of deck transformations is $G(\tilde X) \cong \pi_1(X)/p_*(\pi_1(\tilde X)) \cong G/N$.

::: pf-proof

for a normal covering, the deck group is the quotient of the base fundamental group by the image of the covering.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

:::
