---
schema: qual/card@1
id: E-PWXIV
kind: problem
title: Properties of eleven standard spaces
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
---

::: {.exercise}

Consider the following properties a space may satisfy:

(1) connected, (2) path connected, (3) locally connected, (4) locally path connected, (5) compact, (6) limit point compact, (7) locally compact Hausdorff, (8) Hausdorff, (9) regular, (10) completely regular, (11) normal, (12) first-countable, (13) second-countable, (14) Lindelöf, (15) has a countable dense subset, (16) locally metrizable, (17) metrizable.

For each of the following spaces, determine (if you can) which of these properties it satisfies.
(Assume the Tychonoff theorem if you need it.)

(a) $S_\Omega$

(b) $\overline{S}_\Omega$

(c) $S_\Omega \times \overline{S}_\Omega$

(d) The ordered square

(e) $\mathbb{R}_\ell$

(f) $\mathbb{R}_\ell^2$

(g) $\mathbb{R}^\omega$ in the product topology

(h) $\mathbb{R}^\omega$ in the uniform topology

(i) $\mathbb{R}^\omega$ in the box topology

(j) $\mathbb{R}^I$ in the product topology, where $I = [0, 1]$

(k) $\mathbb{R}_K$
:::

::: {.solution}
Write **Y** for “yes,” **N** for “no,” and **?** for the box-product normality question not decided by the results used here. The columns are the properties (1)–(17) in the problem statement.

| space |1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (a) \(S_\Omega\) |N|N|N|N|N|Y|Y|Y|Y|Y|Y|Y|N|N|N|Y|N|
| (b) \(\overline S_\Omega\) |N|N|N|N|Y|Y|Y|Y|Y|Y|Y|N|N|Y|N|N|N|
| (c) \(S_\Omega\times\overline S_\Omega\) |N|N|N|N|N|Y|Y|Y|Y|Y|N|N|N|N|N|N|N|
| (d) ordered square |Y|N|Y|N|Y|Y|Y|Y|Y|Y|Y|Y|N|Y|N|N|N|
| (e) \(\mathbb R_\ell\) |N|N|N|N|N|N|N|Y|Y|Y|Y|Y|N|Y|Y|N|N|
| (f) \(\mathbb R_\ell^2\) |N|N|N|N|N|N|N|Y|Y|Y|N|Y|N|N|Y|N|N|
| (g) \(\mathbb R^\omega\), product |Y|Y|Y|Y|N|N|N|Y|Y|Y|Y|Y|Y|Y|Y|Y|Y|
| (h) \(\mathbb R^\omega\), uniform |N|N|Y|Y|N|N|N|Y|Y|Y|Y|Y|N|N|N|Y|Y|
| (i) \(\mathbb R^\omega\), box |N|N|N|N|N|N|N|Y|Y|Y|?|N|N|N|N|N|N|
| (j) \(\mathbb R^I\), product |Y|Y|Y|Y|N|N|N|Y|Y|Y|N|N|N|N|Y|N|N|
| (k) \(\mathbb R_K\) |Y|N|N|N|N|N|N|Y|N|N|N|Y|Y|Y|Y|Y|N|

The principal reasons are as follows.

**Ordinal spaces.** \(S_\Omega=[0,\omega_1)\) is countably compact (hence limit point compact), locally compact Hausdorff, hereditarily normal, first countable, and locally metrizable; it is not compact, Lindelöf, separable, second countable, or metrizable. Its one-point compactification \(\overline S_\Omega=[0,\omega_1]\) is compact Hausdorff and normal, but fails first countability and local metrizability at \(\omega_1\). Neither ordinal space is connected or locally connected. The product in (c) is locally compact Hausdorff and completely regular, and every countable subset lies in a compact bounded rectangle, so it is limit point compact. It is not normal: the diagonal and the top edge give the standard nonseparable closed pair. This also forces failure of Lindelöfness; first countability already fails because of the second factor.

**Ordered square.** It is a compact linear continuum, hence connected, locally connected, compact Hausdorff, and normal. Its path components are the vertical fibers, so it is neither path connected nor locally path connected. It is first countable but not separable or second countable. Since a compact Hausdorff locally metrizable space would be metrizable, its nonmetrizability also implies it is not locally metrizable.

**Sorgenfrey spaces.** The Sorgenfrey line is completely normal, first countable, Lindelöf, and separable, but it is disconnected, not locally connected, not locally compact, not second countable, and not metrizable. Its square remains Hausdorff, regular, completely regular, first countable, and separable, but is not normal or Lindelöf; hence it is not metrizable. Neither space is locally metrizable.

**Infinite powers of \(\mathbb R\).** In the product topology on \(\mathbb R^\omega\), coordinatewise straight-line paths show path connectedness and local path connectedness, while the standard product metric gives all metric/countability properties; it is not compact, limit point compact, or locally compact. In the uniform topology, components are the bounded-difference classes; uniform balls of radius \(<1\) are convex, so the space is locally path connected but globally disconnected. It is metrizable but nonseparable and non-Lindelöf. In the box topology, components/path components are the classes of points differing in only finitely many coordinates, so it is neither connected nor locally connected. It is completely regular but not first countable, separable, Lindelöf, or metrizable. The normality entry is left **?** here: the source notes the classical CH-positive result rather than a ZFC theorem.

For \(\mathbb R^I\) with \(I=[0,1]\), the product is path connected and locally path connected, Hausdorff and completely regular, and has a countable dense subset by §30. It is not first countable, locally compact, or metrizable. Stone's theorem gives nonnormality; regular Lindelöf spaces are normal, so it is not Lindelöf either.

**The \(K\)-topology.** \(\mathbb R_K\) is connected but not path connected (§27), and it is not locally connected at \(0\). It is Hausdorff and second countable, hence first countable, Lindelöf, and separable. It is not regular, so it is neither completely regular, normal, nor metrizable; in particular it is not locally compact Hausdorff. It is nevertheless locally metrizable: near \(0\), a basic neighborhood \((a,b)-K\) has the usual subspace topology, and near a point of \(K\) one can choose a small interval meeting \(K\) in at most that point, again giving the usual metrizable subspace topology.
:::
