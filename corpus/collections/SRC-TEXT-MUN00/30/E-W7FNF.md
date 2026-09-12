---
schema: qual/card@1
id: E-W7FNF
kind: problem
title: The lower limit line and the ordered square are not metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
---

::: {.exercise}

Show that $\mathbb{R}_\ell$ and $I_0^2$ are not metrizable.
:::

::: {.solution}
For the lower limit line \(\mathbb R_\ell\), the rationals are dense, so the space is separable. If it were metrizable, every separable metric space would be second countable. But \(\mathbb R_\ell\) is not second countable: if \(\mathcal B\) were a basis, then for each \(x\in\mathbb R\) choose \(B_x\in\mathcal B\) with
\[
x\in B_x\subset[x,x+1).
\]
If \(x<y\), then \(x\in B_x\) while \(x\notin B_y\subset[y,y+1)\), so \(B_x\ne B_y\). Thus \(x\mapsto B_x\) injects the uncountable set \(\mathbb R\) into \(\mathcal B\), contradicting countability. Hence \(\mathbb R_\ell\) is not metrizable.

For the ordered square \(I_o^2=[0,1]\times[0,1]\) in the dictionary order topology, the open vertical intervals
\[
\{x\}\times(0,1),\qquad x\in[0,1],
\]
form an uncountable family of pairwise disjoint nonempty open sets. Therefore \(I_o^2\) is not separable. The ordered square is compact. If it were metrizable, compact metrizability would imply second countability, hence separability, contradiction. Thus \(I_o^2\) is not metrizable.
:::
