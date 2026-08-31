---
schema: qual/card@1
id: E-HAT-1.3-17
kind: exercise
title: "Normal covering spaces from group extensions"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Given a group $G$ and a normal subgroup $N$, show that there exists a normal covering space $\tilde{X} \to X$ with $\pi_1(X) \approx G$, $\pi_1(\tilde{X}) \approx N$, and deck transformation group $G(\tilde{X}) \approx G/N$.

::: {.solution}
<1>1. Choose a CW complex $X$ with $\pi_1(X) \cong G$ (e.g., the presentation complex of $G$; a $K(G,1)$).
::: {.proof}
every group is the fundamental group of a CW complex (attach $2$-cells for relations and kill higher homotopy).
:::

<1>2. Let $p : \tilde X \to X$ be the connected covering corresponding to the subgroup $N \le \pi_1(X) \cong G$.
::: {.proof}
covering space theory (for nice $X$, connected coverings are classified by conjugacy classes of subgroups of $\pi_1$).
:::

<1>3. Then $\pi_1(\tilde X) \cong N$.
::: {.proof}
<1>2 ($p_*(\pi_1(\tilde X)) = N$).
:::

<1>4. The covering is normal iff $N$ is normal in $\pi_1(X)$.
::: {.proof}
a covering is normal (regular) iff the corresponding subgroup is normal.
:::

<1>5. Hence, since $N \triangleleft G$, the covering $\tilde X \to X$ is normal.
::: {.proof}
<1>4.
:::

<1>6. The group of deck transformations is $G(\tilde X) \cong \pi_1(X)/p_*(\pi_1(\tilde X)) \cong G/N$.
::: {.proof}
for a normal covering, the deck group is the quotient of the base fundamental group by the image of the covering.
:::

<1>7. Q.E.D.
::: {.proof}
<1>3, <1>5, <1>6.
:::
:::
