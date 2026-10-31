---
schema: qual/card@1
id: E-1CMTE
kind: problem
title: Paracompactness and topological completeness in the basics review
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

After studying Chapters 6 and 7, repeat Exercises 1–6 of the Supplementary Exercises (Review of the Basics) for the following properties:

(18) paracompact

(19) topologically complete

You should be able to answer all but one of the 340 questions involved in Exercises 1–6, and all but one of the 40 questions involved in Exercise 7. These two are unsolved; see the remark in Exercise 5 of §32.
:::

::: {.solution}
The earlier supplementary exercises classify properties (1)–(17). The entries below supply properties (18) and (19) in the same order. Here “topologically complete” means that the topology admits a complete metric.

| Space in Exercise 1 | Paracompact (18) | Topologically complete (19) |
| --- | :---: | :---: |
| (a) $S_\Omega$ | No | No |
| (b) $\overline S_\Omega$ | Yes | No |
| (c) $S_\Omega\times\overline S_\Omega$ | No | No |
| (d) Ordered square | Yes | No |
| (e) $\RR_\ell$ | Yes | No |
| (f) $\RR_\ell^2$ | No | No |
| (g) $\RR^\omega$, product | Yes | Yes |
| (h) $\RR^\omega$, uniform | Yes | Yes |
| (i) $\RR^\omega$, box | ? | No |
| (j) $\RR^{[0,1]}$, product | No | No |
| (k) $\RR_K$ | No | No |

Every compact Hausdorff space and every metrizable space is paracompact. The product and uniform topologies in (g) and (h) admit complete metrics: use a weighted sum of bounded complete coordinate metrics for (g), and the bounded uniform metric for (h). A compact Hausdorff space is topologically complete exactly when it is metrizable. The ordinal spaces and ordered square in the table fail metrizability. The Sorgenfrey line is regular Lindelöf, hence paracompact, but is not metrizable. The spaces in (c), (f), and (j) are not normal; $\RR_K$ is not regular. Each therefore fails paracompactness. The space $S_\Omega$ is countably compact but noncompact; a countably compact paracompact Hausdorff space is compact, so it is not paracompact. The box-product paracompactness question is the unresolved entry identified by the source.

For Exercises 2–6, the preservation answers are:

| Operation or class | Paracompact (18) | Topologically complete (19) |
| --- | --- | --- |
| Arbitrary subspace | No | No |
| Closed subspace | Yes | Yes |
| Open subspace | No | Yes |
| Finite product | No | Yes |
| Countable product | No | Yes |
| Arbitrary product | No | No |
| Continuous image | No | No |
| Every metric space | Yes | No |
| Every compact Hausdorff space | Yes | No |

Closed subspaces of paracompact Hausdorff spaces are paracompact, whereas the open subspace $S_\Omega$ of compact $\overline S_\Omega$ is not. The Sorgenfrey plane shows that even a finite product of paracompact spaces can fail to be paracompact. Closed and open subspaces of a completely metrizable space are completely metrizable; $\QQ\subset\RR$ is an arbitrary subspace that is not. Finite and countable products of completely metrizable spaces admit complete product metrics. An uncountable product of nontrivial metric spaces need not be first countable. A discrete topology on the underlying set of any nonparacompact or non-completely-metrizable space gives a continuous surjection from a space with both properties, so neither property is preserved by continuous images. The metric space $\QQ$ is not topologically complete, while compact Hausdorff spaces that are not metrizable, such as $[0,\omega_1]$, are not topologically complete.
:::
