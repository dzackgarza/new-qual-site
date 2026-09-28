---
schema: qual/card@1
id: D-CRVGON
kind: definition
title: Linear series $g^r_d$, and the gonality of a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Gonality
  - Curves
relations:
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- What does the notation $g^r_d$ mean?
- What is the gonality of a curve?
- Which curves are trigonal?
---

::: {.definition}
A \dfn{$g^r_d$} on a curve $C$ is a linear system of degree $d$ and projective dimension $r$: a subspace $V \subseteq H^0(\OO_C(D))$ with $\deg D = d$ and $\dim \PP V = r$.
The \dfn{gonality} of $C$ is the least $d$ for which $C$ carries a $g^1_d$, equivalently the least degree of a nonconstant map $C \to \PP^1$.
The curve $C$ is \dfn{trigonal} if its gonality is $3$.
:::

::: {.proposition}
Gonality $1$ means $C \cong \PP^1$. For genus at least $2$, gonality $2$ means $C$ is hyperelliptic; genus-$1$ curves also have gonality $2$. Every curve of genus $g$ carries a $g^1_d$ for $d \geq \lfloor (g+3)/2 \rfloor$, and a general curve of genus $g$ has no $g^1_d$ below this bound.
:::

::: {.remark}
A base-point-free $g^r_d$ determines a morphism $\phi\colon C\to\PP^r$ with $\deg\phi^*\OO(1)=d$; for $r=1$ this is a map $C\to\PP^1$ of degree $d$.
The canonical system on a curve of genus $g\ge2$ is a $g^{g-1}_{2g-2}$.

For $g=3$ and $g=4$, $\lfloor (g+3)/2\rfloor=3$, so every non-hyperelliptic curve of genus $3$ or $4$ is trigonal.
A smooth plane quartic has a $g^1_3$ for each of its points $p$: the lines through $p$ cut out $p$ plus three further points.
:::
