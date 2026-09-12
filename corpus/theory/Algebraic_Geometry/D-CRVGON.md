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
Let $C$ be a smooth projective connected curve over an algebraically closed field of characteristic zero.
A **$g^r_d$** on $C$ is a linear system of degree $d$ and projective dimension $r$: a subspace $V \subseteq H^0(\OO_C(D))$ with $\deg D = d$ and $\dim \PP V = r$.
The **gonality** of $C$ is the least $d$ for which $C$ carries a $g^1_d$, equivalently the least degree of a nonconstant map $C \to \PP^1$.
:::

::: {.proposition}
Gonality $1$ means $C \cong \PP^1$. For genus at least $2$, gonality $2$ means $C$ is hyperelliptic; genus-$1$ curves also have gonality $2$. Gonality $3$ means $C$ is **trigonal**. Every curve of genus $g$ carries a $g^1_d$ for $d \geq \lfloor (g+3)/2 \rfloor$, and a general curve of genus $g$ has no $g^1_d$ below this bound.
:::

::: {.remark}
A base-point-free $g^1_2$ defines a degree-two map to $\PP^1$.
A base-point-free $g^2_d$ defines a morphism $\varphi:C\to\PP^2$ with $\varphi^*\OO(1)\cong\OO_C(D)$. If its image is a curve $\Gamma$, then $d=\deg(C\to\Gamma)\deg\Gamma$; $d$ is not generally the degree of the map onto its image. A series with fixed divisor $B$ gives this construction after replacing $D$ by $D-B$.
The canonical system on a non-hyperelliptic curve of genus $g\geq3$ is a $g^{g-1}_{2g-2}$.

Gonality defines loci in $\mathcal{M}_g$ and is at most $\lfloor \tfrac{g+3}{2} \rfloor$; the general curve attains this bound.
In genus $3$ and $4$ that bound forces gonality at most $3$: every non-hyperelliptic curve there is trigonal, and a plane quartic gets infinitely many $g^1_3$'s by projecting from each of its own points.
:::
