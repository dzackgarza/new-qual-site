---
schema: qual/card@1
id: P-TFOOH
kind: problem
title: "Suppose $\\theset{f_n}_{n\\in \\NN}$ is a sequence of analytic functions on $\\DD \\definedas \\theset{z\\in \\CC \\suchthat \\abs{z} < 1}$. Show that\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - morera
  - uniform-convergence
  - sequences-of-functions
  - holomorphic-functions
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of analytic functions on $\DD \definedas \theset{z\in \CC \suchthat \abs{z} < 1}$.

Show that if $f_n\to g$ for some $g: \DD \to \CC$ uniformly on every compact $K\subset \DD$, then $g$ is analytic on $\DD$.


:::

:::{.solution}
By Morera's theorem, it suffices to show $\int_T f = 0$ for all triangles $T \subseteq \DD$.
Noting that $T$ is closed and bounded and thus compact, $f_n\to g$ uniformly on $T$.
Since the $f_n$ are holomorphic, $\int_T f_n = 0$ for all $n$, and thus
\[
\int_T g = \int_T \lim f_n = \lim_n \int_T f_n = \lim_n 0 = 0
,\]
where moving the limit through the integral is justified by uniform convergence.
:::

