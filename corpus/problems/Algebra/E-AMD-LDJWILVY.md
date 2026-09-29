---
schema: qual/card@1
id: E-AMD-LDJWILVY
kind: problem
title: If $H\le N_G(K)$ then $HK$ is a subgroup
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Centralizers and Normalizers
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that if $H \leq N_G(K)$ then $HK \leq G$, and give a counterexample showing that this condition is necessary.
:::

::: {.solution}
Let $H,K\le G$ and put $HK=\{hk:h\in H,\ k\in K\}$.

::: pf

::: {.pf-step #hk-closed-under-multiplication}
If $H\le N_G(K)$, then $HK$ is closed under multiplication.

::: pf-proof
Let $h_1k_1,h_2k_2\in HK$. Then
$$(h_1k_1)(h_2k_2)=(h_1h_2)\bigl(h_2^{-1}k_1h_2\bigr)k_2 .$$
Since $h_2\in N_G(K)$, $h_2^{-1}k_1h_2\in K$, so the product lies in $HK$.
:::

:::

::: {.pf-step #hk-closed-under-inverses}
If $H\le N_G(K)$, then $HK$ is closed under inverses.

::: pf-proof
For $hk\in HK$, $(hk)^{-1}=k^{-1}h^{-1}=h^{-1}\bigl(hk^{-1}h^{-1}\bigr)$, and $hk^{-1}h^{-1}\in K$ because $h\in N_G(K)$.
:::

:::

::: {.pf-step #hk-is-subgroup}
If $H\le N_G(K)$, then $HK\le G$.

::: pf-proof
$1=1\cdot1\in HK$, and steps [](#hk-closed-under-multiplication){.pf-ref} and [](#hk-closed-under-inverses){.pf-ref} give the subgroup criterion.
:::

:::

::: {.pf-step #s3-counterexample}
In $G=S_3$, the subgroups $H=\langle(1\,2)\rangle$ and $K=\langle(1\,3)\rangle$ satisfy $H\not\le N_G(K)$, and $HK$ is not a subgroup.

::: pf-proof
$(1\,2)(1\,3)(1\,2)=(2\,3)\notin K$, so $(1\,2)\notin N_G(K)$.
Since $H\cap K=1$, $|HK|=|H||K|/|H\cap K|=4$, and $4\nmid 6=|S_3|$, so by Lagrange's theorem $HK$ is not a subgroup.
:::

:::

::: pf-qed
Step [](#hk-is-subgroup){.pf-ref} proves the implication, and step [](#s3-counterexample){.pf-ref} shows that it fails without the hypothesis $H\le N_G(K)$.
:::

:::

:::
