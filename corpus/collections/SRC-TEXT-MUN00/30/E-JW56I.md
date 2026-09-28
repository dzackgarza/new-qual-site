---
schema: qual/card@1
id: E-JW56I
kind: problem
title: Countability axioms of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Countability
  - Order Topology
relations: []
review: draft
---

::: {.exercise}

Which of our four countability axioms does $S_\Omega$ satisfy?
What about $\overline{S}_\Omega$?
:::

::: {.solution}
The four countability properties under discussion are first countability, second countability, Lindelöfness, and existence of a countable dense subset.

For \(S_\Omega=[0,\Omega)\):

- It is first countable. Every \(\alpha<\Omega=\omega_1\) is a countable ordinal. If \(\alpha\) is a successor, it has an obvious countable local basis. If \(\alpha\) is a limit ordinal, choose an increasing sequence \(\alpha_n\uparrow\alpha\); then intervals \((\alpha_n,\alpha]\) form a countable local basis at \(\alpha\).
- It is not separable. The closure of any countable subset \(D\subset S_\Omega\) is bounded below some countable ordinal \(\beta<\Omega\), since \(\sup D<\Omega\). Thus \(D\) cannot be dense.
- Therefore it is not second countable, since second countable spaces are separable.
- It is not Lindelöf. The open cover \(\{[0,\alpha):\alpha<\Omega\}\) has no countable subcover, since the supremum of countably many countable ordinals is still \(<\Omega\).

For \(\overline S_\Omega=[0,\Omega]\):

- It is compact, hence Lindelöf.
- It is not first countable at \(\Omega\). A countable local basis would give countably many left endpoints whose supremum is still \(<\Omega\), leaving a smaller neighborhood of \(\Omega\) not refined by the basis.
- It is not separable for the same boundedness reason as above: every countable subset has supremum \(<\Omega\), so it misses a final interval.
- Hence it is not second countable.

Thus \(S_\Omega\) satisfies only first countability, while \(\overline S_\Omega\) satisfies only Lindelöfness among the four axioms.
:::
