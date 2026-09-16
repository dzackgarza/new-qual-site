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
The **gonality** of $C$ is the least $d$ for which $C$ carries a $g^1_d$, equivalently the least degree of a nonconstant map $C \to \PP^1$.
:::

::: {.proposition}
Gonality $1$ means $C \cong \PP^1$, gonality $2$ means $C$ is hyperelliptic, and gonality $3$ means $C$ is **trigonal**. Every curve of genus $g$ carries a $g^1_d$ as soon as $d \geq \tfrac{1}{2}g + 1$, and for $d$ below that bound there exist curves of genus $g$ with no $g^1_d$.
:::

::: {.remark}
The notation is what an examiner uses to ask the question compactly, so it is worth being fluent: a $g^1_2$ is a degree-two map to $\PP^1$, a $g^2_d$ is a map to $\PP^2$ of degree $d$, and the canonical system on a non-hyperelliptic curve of genus $g$ is a $g^{g-1}_{2g-2}$.

Gonality is the first invariant after the genus that stratifies $\mathcal{M}_g$.
The bound $d \geq \tfrac{1}{2}g+1$ says gonality is at most $\lfloor \tfrac{g+3}{2} \rfloor$, and the general curve attains it.
In genus $3$ and $4$ that bound forces gonality at most $3$: every non-hyperelliptic curve there is trigonal, and a plane quartic gets infinitely many $g^1_3$'s by projecting from each of its own points.
:::
