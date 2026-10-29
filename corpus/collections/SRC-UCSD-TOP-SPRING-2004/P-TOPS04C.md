---
schema: qual/card@1
id: P-TOPS04C
kind: problem
title: "Hopf fibrations do not admit a section"
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Hopf Fibration
relations: []
review: draft
---

::: {.problem}
Let $\bK = \RR$, $\CC$, or $\quaternions$.
Show that for $n \geq 1$ the Hopf fibrations
$$
p : \bK^{n+1} \setminus \{0\} \to \bK P^n
$$
do not admit a section $s$ (i.e. there is no continuous $s$ satisfying $p \circ s = \operatorname{id}$).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A section would make $p_*:H_*(\bK^{n+1}-\{0\})\to H_*(\bK P^n)$ split surjective.

::: pf-proof

If $p\circ s=\operatorname{id}$, then $p_*\circ s_*=\operatorname{id}$ on homology.

:::

:::

::: {.pf-step #s2}

For $\bK=\CC$, no section exists.

::: pf-proof

The total space deformation-retracts onto $S^{2n+1}$, whose $H_2$ vanishes for $n\ge1$. But $H_2(\CP^n;\ZZ)\cong\ZZ$. This contradicts the split surjectivity from step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

For $\bK=\quaternions$, no section exists.

::: pf-proof

The total space deformation-retracts onto $S^{4n+3}$, whose $H_4$ vanishes, whereas $H_4(\quaternions P^n;\ZZ)\cong\ZZ$ for $n\ge1$.

:::

:::

::: {.pf-step #s4}

For $\bK=\RR$ and $n\ge2$, no section exists.

::: pf-proof

The total space deformation-retracts onto $S^n$, so $H_1(-;\FF_2)=0$. But $H_1(\RP^n;\FF_2)\cong\FF_2$, contradicting step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s5}

For $\bK=\RR$ and $n=1$, no section exists either.

::: pf-proof

After radial deformation retraction the map is the double covering $S^1\to\RP^1\cong S^1$, whose induced map on $H_1(-;\ZZ)$ is multiplication by $2$. Such a map cannot have a right inverse as a homomorphism $\ZZ\to\ZZ$.

:::

:::

::: pf-step

Thus none of the stated Hopf fibrations admits a section.

::: pf-proof

Combine steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
