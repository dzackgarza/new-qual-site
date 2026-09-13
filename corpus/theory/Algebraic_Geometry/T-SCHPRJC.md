---
schema: qual/card@1
id: T-SCHPRJC
kind: theorem
title: $\Proj S$ is a scheme, with affine charts $D_+(f) \cong \Spec S_{(f)}$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proj
  - Affine Schemes
  - Projective Space
relations:
- kind: uses
  target: D-SCHPROJ
- kind: related-to
  target: D-SCHGLUE
review: draft
prompts:
- Why is $\Proj S$ a scheme?
- What are the affine charts of $\PP^n$?
- How is $\PP^n$ defined over an arbitrary base scheme?
---

::: {.theorem}
For $f \in S_d$ homogeneous of positive degree, let $D_+(f) \da \ts{\mfp \in \Proj S \st f \notin \mfp}$.
Then
\[
(D_+(f), \ro{\OO_{\Proj S}}{D_+(f)}) \cong \Spec S_{(f)} ,
\]
where $S_{(f)}$ is the degree-zero part of $S[f\inv]$.
The $D_+(f)$ for $f \in S_+$ cover $\Proj S$, so $\Proj S$ is a scheme.
:::

::: {.example}
For $S = \kxnz$ with the usual grading, $D_+(x_i) \cong \Spec k[x_0/x_i, \dots, x_n/x_i] \cong \AA^n\slice k$, recovering the standard charts of $\PP^n\slice k$.
:::

::: {.remark}
"Why is $\Proj$ a scheme" is answered by naming the chart and the ring, not by reciting the definition: the charts are the loci where one homogeneous coordinate is invertible, and dividing by it turns degree-$d$ things into functions.
Discarding $V(S_+)$ is what makes the $D_+(f)$ a cover, since a prime containing all of $S_+$ lies in no chart.

Over a base, define $\PP^n\slice \ZZ \da \Proj \ZZ[x_0, \dots, x_n]$ and then
\[
\PP^n\slice S \da \fiberprod{\PP^n\slice \ZZ}{\Spec \ZZ}{S} .
\]
The same pattern gives $\AA^n\slice S$ from $\Spec \ZZ[x_1, \dots, x_n]$.
This is the right answer to "what is projective space over a scheme": one absolute object, base changed, rather than a fresh gluing for each base.
:::
