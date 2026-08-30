---
schema: qual/card@1
id: P-G7SZ7
kind: problem
title: We have the map
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Exact Sequences
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
We have the map

\[
\begin{align*}
\pi: \ZZ &\to \ZZ_2 \\
x &\mapsto [x]_2
\end{align*}
\]

which is a surjection and thus an epimorphism in the category ${\ZZ}\dash\mathrm{Mod}$, and if we apply the functor $\hom_\ZZ(\ZZ_2, \wait)$ to $\pi$ we obtain an induced map

\[
\begin{align*}
\overline{\pi}: \hom_{\ZZ}(\ZZ_2, \ZZ) &\to \hom_{\ZZ}(\ZZ_2, \ZZ_2) \\
f &\mapsto \pi \circ f 
.\end{align*}
\]

The claim is that $\overline{\pi}$ is *not* a surjection, and thus not an epimorphism (in the same category).

To see that this is the case, we can simply note that $\hom_\ZZ(\ZZ_2, \ZZ) = 0$ by part 3 of Problem 1, whereas $\hom_\ZZ(\ZZ_2, \ZZ_2) \neq 0$.

For example, one can define
\[
\begin{align*}
\id_{\ZZ_2}: \ZZ_2 &\to \ZZ_2\\
[x]_2 &\mapsto [x]_2 
,\end{align*}
\]
which is a nontrivial module homomorphisms.

So any such $f$ appearing must be the zero map, and thus $\overline{\pi}$ is also the zero map.
$\qed$
:::

::: {.solution}
<1>1. $R$ ring.
Proof: ideal.

<1>2. Q.E.D.
Proof: <1>1.
:::
