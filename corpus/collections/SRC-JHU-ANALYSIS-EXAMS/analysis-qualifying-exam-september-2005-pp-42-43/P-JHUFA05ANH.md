---
schema: qual/card@1
id: P-JHUFA05ANH
kind: problem
title: Surjective holomorphic maps between the right half-plane and the plane
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked both directions of September 2005 problem 8 on PDF page 43; preserved Re z greater than zero and corrected its contradictory upper-half-plane label."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Constructed the half-plane-to-plane surjection by a quadratic root sum and proved every reverse-direction holomorphic map constant by a bounded Cayley transform."
---

::: {.problem}
8. Let $H=\{z\in\mathbb C:\operatorname{Re}z>0\}$ be the right half-plane.

(a) Does there exist a surjective holomorphic map $f : H \to \mathbb { C } ?$ Either give an example or prove that one does not exist.

(b) Does there exist a surjective holomorphic map $f : \mathbb { C } \to H ?$ Either give an example or prove that one does not exist.
:::

::: solution
The answer to (a) is yes; the answer to (b) is no.

<1>1. The polynomial $p(z)=z^2-z$ maps $H$ onto $\mathbb C$.

::: proof
The restriction of this polynomial to $H$ is holomorphic.
For any $w\in\mathbb C$, let $z_1,z_2$ be the two roots,
counted with multiplicity, of $z^2-z-w=0$. The quadratic
formula gives $z_1+z_2=1$, hence
$\operatorname{Re}z_1+\operatorname{Re}z_2=1$.
At least one root has real part at least $1/2$, so lies
in $H$. That root maps to $w$. This proves surjectivity
onto the whole plane, not only onto an open subset.
:::

<1>2. Every holomorphic map from $\mathbb C$ to $H$ is constant.

::: proof
For such a map $f$, put
$$
g(z)=\frac{f(z)-1}{f(z)+1}.
$$
The denominator never vanishes because $\operatorname{Re}f>0$.
Moreover
$|f(z)+1|^2-|f(z)-1|^2=4\operatorname{Re}f(z)>0$,
so $g$ is entire and $|g|<1$. Liouville's theorem gives
$g=c$ for some $|c|<1$ [@SS03]. Solving for $f$ gives
$f=(1+c)/(1-c)$, a constant. It cannot be surjective
onto $H$, which contains more than one point. Thus no
surjective map in direction (b) exists.
:::
:::
