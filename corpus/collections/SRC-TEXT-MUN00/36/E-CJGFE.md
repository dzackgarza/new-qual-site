---
schema: qual/card@1
id: E-CJGFE
kind: problem
title: Heredity of the seventeen basic properties
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties are preserved when one passes to a subspace?
To a closed subspace?
To an open subspace?
:::

::: {.solution}
Number the properties as in Exercise `E-PWXIV`. The preservation table is:

| property | arbitrary subspace | closed subspace | open subspace |
|---|:---:|:---:|:---:|
| (1) connected | no | no | no |
| (2) path connected | no | no | no |
| (3) locally connected | no | no | yes |
| (4) locally path connected | no | no | yes |
| (5) compact | no | yes | no |
| (6) limit point compact | no | yes | no |
| (7) locally compact Hausdorff | no | yes | yes |
| (8) Hausdorff | yes | yes | yes |
| (9) regular | yes | yes | yes |
| (10) completely regular | yes | yes | yes |
| (11) normal | no | yes | no |
| (12) first countable | yes | yes | yes |
| (13) second countable | yes | yes | yes |
| (14) Lindelöf | no | yes | no |
| (15) countable dense subset | no | no | yes |
| (16) locally metrizable | yes | yes | yes |
| (17) metrizable | yes | yes | yes |

Here are the key reasons.

- Hausdorffness, regularity, complete regularity, first/second countability, local metrizability, and metrizability are hereditary to arbitrary subspaces.
- Local connectedness and local path connectedness pass to open subspaces because an open neighborhood in the subspace is open in the ambient space locally; they need not pass to closed or arbitrary subspaces (standard sine-curve examples suffice).
- Compactness, limit point compactness, and Lindelöfness pass to closed subspaces. They do not pass to arbitrary or open subspaces in general.
- Local compact Hausdorffness passes to both open and closed subspaces, but not arbitrary subspaces: \(\mathbb Q\subset\mathbb R\) is the standard counterexample.
- Normality passes to closed subspaces but not arbitrary or open subspaces.
- Separability passes to open subspaces: if \(D\) is countable dense in \(X\) and \(U\subset X\) is open, then \(D\cap U\) is dense in \(U\). It does not pass to arbitrary or closed subspaces; the separable Sorgenfrey plane contains an uncountable closed discrete anti-diagonal.
- Connectedness and path connectedness are not hereditary even to closed or open subspaces.
:::
