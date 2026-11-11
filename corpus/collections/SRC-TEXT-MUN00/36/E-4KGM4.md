---
schema: qual/card@1
id: E-4KGM4
kind: problem
title: Properties of compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 3, printed p. 228, with Theorem 28.1, Theorem 32.3, Theorem 33.1, Theorem 29.1
    and Exercise 29.7, Exercise 27.6 and Exercise 30.5(a). No published solution was located (search
    recorded on E-PWXIV and in the COMPLAINTS.md entry). The eight guaranteed properties are
    compact, limit point compact, locally compact Hausdorff, Hausdorff, regular, completely regular,
    normal and Lindelof; the nine that are not guaranteed are excluded by two spaces. The Cantor set,
    Exercise 27.6, is compact Hausdorff, totally disconnected and without isolated points, which
    excludes connectedness, path connectedness, local connectedness and local path connectedness. The
    ordinal interval [0, omega_1], which is the one-point compactification of S_Omega by Exercise
    29.7, is compact Hausdorff and fails first countability at omega_1, separability, second
    countability, metrizability and local metrizability, which excludes those five. What was
    corrected: the page, which is 228 and not 229; and the table, whose Reason column named the
    phenomenon rather than the result, so that each row now names the theorem that decides it.
---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties does a compact Hausdorff space have?
:::

::: {.solution}
Of the properties numbered in Supplementary Exercise 1, every compact Hausdorff space has these eight, and no others are guaranteed:

| Number | Property | Deciding result |
| --- | --- | --- |
| 5 | Compact | Hypothesis |
| 6 | Limit point compact | Compactness implies limit point compactness, Theorem 28.1 |
| 7 | Locally compact Hausdorff | The whole space is a compact subspace containing a neighbourhood of each point, which is the definition of local compactness in §29; Hausdorffness is the hypothesis |
| 8 | Hausdorff | Hypothesis |
| 9 | Regular | The space is normal by Theorem 32.3, and a normal space is regular (§31) |
| 10 | Completely regular | The Urysohn lemma, Theorem 33.1, applies to a normal space, and a normal space is completely regular (§33) |
| 11 | Normal | Theorem 32.3 |
| 14 | Lindelöf | Every open cover has a finite subcover, so it has a countable one (§30) |

The remaining nine properties are not guaranteed, and two spaces exclude all of them.

**The Cantor set** $C \subset [0,1]$, Exercise 27.6, is compact Hausdorff. It is totally disconnected, Exercise 27.6(a), and has no isolated points, Exercise 27.6(d), so no point of it has a connected neighbourhood: a connected neighbourhood of $x$ would be a connected set containing $x$, hence the point $x$ itself, and $\{x\}$ is not open. This excludes connectedness, path connectedness, local connectedness and local path connectedness — properties 1 to 4. A path connected space is connected and a locally path connected space is locally connected, so the two path entries follow as well.

**The ordinal interval** $\overline S_\Omega = [0,\omega_1]$ is compact Hausdorff: it is the one-point compactification of $S_\Omega$, Exercise 29.7 with Theorem 29.1. It is not first countable at $\omega_1$, since the supremum of countably many ordinals below $\omega_1$ is again below $\omega_1$, so no countable family of neighbourhoods of $\omega_1$ is a local base. It is not separable: a countable set of ordinals below $\omega_1$ is bounded, so the final segment above that bound misses it and the set is not dense. A space with a countable dense subset has a countable basis when it is metrizable, Exercise 30.5(a), and a space with a countable basis is first countable, so $\overline S_\Omega$ is neither second countable nor metrizable, which is properties 13 and 17. It is not locally metrizable either: a neighbourhood of $\omega_1$ contains a final segment $(\alpha,\omega_1]$, which is not first countable at $\omega_1$ and so is not metrizable, property 16. That leaves no unaccounted property, and the count is eight guaranteed and nine not.
:::
