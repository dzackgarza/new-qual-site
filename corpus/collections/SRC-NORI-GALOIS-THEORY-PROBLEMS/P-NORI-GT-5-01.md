---
schema: qual/card@1
id: P-NORI-GT-5-01
kind: problem
title: Galois group over a compositum of fixed fields is $H_1\cap H_2$
classification:
  areas: [algebra]
  topics:
  - Galois Correspondence
  - Fixed Fields
  - Compositum
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.1 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $L$ be a finite Galois extension of $F$. Let $H_{1}$ and $H_{2}$ be subgroups of $G = \Gal(L/F)$ and consider their fixed fields $E_{1} = L^{H_{1}}$ and $E_{2} = L^{H_{2}}$ respectively. Prove that $\Gal(L/E_{1}E_{2})$ equals $H_{1} \cap H_{2}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

An element
$$
\sigma\in G=\operatorname{Gal}(L/F)
$$
belongs to
$$
\operatorname{Gal}(L/E_1E_2)
$$
if and only if it fixes both $E_1$ and $E_2$ pointwise.


::: pf-proof

If $\sigma$ fixes the compositum $E_1E_2$ pointwise, then it certainly fixes the subfields
$$
E_1\subseteq E_1E_2
$$
and
$$
E_2\subseteq E_1E_2.
$$

Conversely, suppose $\sigma$ fixes $E_1$ and $E_2$ pointwise. The compositum $E_1E_2$ is the smallest subfield of $L$ containing both fields. Every element of it is obtained from elements of $E_1\cup E_2$ by the field operations. Since $\sigma$ fixes all generators and respects the field operations, it fixes every element of $E_1E_2$.

:::

:::

::: {.pf-step #s1-2}

For $i=1,2$,
$$
\operatorname{Gal}(L/E_i)=H_i.
$$


::: pf-proof

By definition
$$
E_i=L^{H_i}.
$$
The fundamental theorem of Galois theory for the finite Galois extension $L/F$ states that the subgroup fixing the fixed field $L^{H_i}$ pointwise is exactly $H_i$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\operatorname{Gal}(L/E_1E_2)=H_1\cap H_2.
}
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\operatorname{Gal}(L/E_1E_2)
=
\operatorname{Gal}(L/E_1)
\cap
\operatorname{Gal}(L/E_2).
$$
Substitute the identities from step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is exactly the required equality.

:::

:::

:::
