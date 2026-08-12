---
schema: qual/card@1
id: T-CP7OP
kind: theorem
title: "Mean Value Property for Holomorphic Functions"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.theorem title="Mean Value Property for Holomorphic Functions"}
If $f$ is holomorphic on $D_r(z_0)$ 
\[
f(z_0) 
= {1\over 2\pi} \int_0^{2\pi} f(z_0 + re^{i\theta}) \dtheta
= {1\over \pi r^2} \iint_{D_r(z_0)} f(z)\, dA
.\]
Taking the real part of both sides, one can replace $f=u+iv$ with $u$.
:::
