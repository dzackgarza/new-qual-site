---
schema: qual/card@1
id: P-CAF09A
kind: problem
title: "Principal value of the logarithm of e^{3+7i}"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Find the principal value of $\log(e^{3+7i})$.
:::

::: solution
The principal logarithm is
\[
\operatorname{Log} w=\log|w|+i\operatorname{Arg}w,
\qquad -\pi<\operatorname{Arg}w\le\pi.
\]
Now
\[
e^{3+7i}=e^3e^{7i}.
\]
Since
\[
7-2\pi\in(-\pi,\pi],
\]
the principal argument of $e^{7i}$ is $7-2\pi$. Therefore
\[
\boxed{\operatorname{Log}(e^{3+7i})=3+i(7-2\pi).}
\]
:::
