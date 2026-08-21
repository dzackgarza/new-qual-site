---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW4
kind: problem
title: Verify the parallelogram law for an inner-product norm (warm-up)
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Hilbert Spaces
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Show that an inner product space satisfies the parallelogram law with its induced norm:
$$
\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2.
$$
(For simplicity, you may assume that this is an inner product space over $\mathbb R$.)
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Expand both sides using bilinearity and symmetry of the inner product.
Proof: for $x, y$ in a real inner product space, \[\lVert x+y\rVert^2 = \langle x+y, x+y\rangle = \lVert x\rVert^2 + 2\langle x, y\rangle + \lVert y\rVert^2,\] \[\lVert x-y\rVert^2 = \langle x-y, x-y\rangle = \lVert x\rVert^2 - 2\langle x, y\rangle + \lVert y\rVert^2.\] <1>2. Add.
Proof: adding the two identities, the cross terms cancel: \[\lVert x+y\rVert^2 + \lVert x-y\rVert^2 = 2\lVert x\rVert^2 + 2\lVert y\rVert^2.\] <1>3. Q.E.D.
:::
