---
schema: qual/card@1
id: FF-D2KJJ
kind: fact
title: 'Full tor complex table:'
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.fact}
E.g. top-left is $ \operatorname{Tor}_*^{\mathbf{Z}}(C_n, C_m) $.

First row: $ C_n\otimes_{\mathbf{Z}}A = A/nA $ and $ \operatorname{Tor}_1^{\mathbf{Z}}(C_n, A) = A[n] $.

Second row: $ {\mathbf{Z}}\otimes_{\mathbf{Z}}A = A $ and $ \operatorname{Tor}_1^{\mathbf{Z}}({\mathbf{Z}}, A) = 0 $ since $ {\mathbf{Z}} $ is projective.

Third row: $ G\otimes_{\mathbf{Z}}{\mathbf{Q}}= {\mathbf{Q}}\otimes_{\mathbf{Z}}G = 0 $ for $ G $ any group

Also $ \operatorname{Tor}(A, B) = \operatorname{Tor}(B, A) $.
| $ \operatorname{Tor}_*^{\mathbf{Z}}(V, H) $ | $ C_m $ | $ {\mathbf{Z}} $ | $ {\mathbf{Q}} $ | |:---------------------|:-----------------------------------------------|:----------------------------------------------|:------------------------------------------| | $ C_n $ | $ C_m/nC_m \oplus C_m[n]t = C_d \oplus C_d t $ | $ {\mathbf{Z}}/n{\mathbf{Z}}\oplus {\mathbf{Z}}[n]t = C_n \oplus C_nt $ | $ {\mathbf{Q}}/n{\mathbf{Q}}\oplus {\mathbf{Q}}[n]t =0\oplus 0t $ | | $ {\mathbf{Z}} $ | $ {\mathbf{Z}}/m{\mathbf{Z}}+ {\mathbf{Z}}[m]t = C_m + C_m t $ | $ {\mathbf{Z}}+ 0t $ | $ {\mathbf{Q}}+ 0t $ | | $ {\mathbf{Q}} $ | $ {\mathbf{Q}}/n{\mathbf{Q}}+ {\mathbf{Q}}[n]t = 0 + 0t $ | $ {\mathbf{Q}}+ 0t $ | $ 0 + 0t $ |
:::
