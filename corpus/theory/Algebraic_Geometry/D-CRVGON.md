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
Let $C$ be a smooth projective curve of genus $g$ over an algebraically closed field.
A \dfn{$g^r_d$} on $C$ is a linear system of degree $d$ and projective dimension $r$: a subspace $V \subseteq H^0(\OO_C(D))$ with $\deg D = d$ and $\dim \PP V = r$ [@Har77, Section IV.5].
The \dfn{gonality} of $C$ is the least $d$ for which $C$ carries a $g^1_d$, equivalently the least degree of a nonconstant morphism $C \to \PP^1$; the set of such $d$ is nonempty, since for a point $P$ Riemann--Roch gives $\ell((g+1)P)\ge2$, so a $g^1_{g+1}$ exists and adding base points gives a $g^1_d$ for every $d\ge g+1$ [@Har77, Theorem IV.1.3].
The curve $C$ is \dfn{trigonal} if its gonality is $3$.
:::

::: {.proposition}
Gonality $1$ means $C \cong \PP^1$.
For genus at least $2$, gonality $2$ means $C$ is hyperelliptic [@Har77, Section IV.5]; a curve of genus $1$ has gonality $2$ and a curve of genus $0$ has gonality $1$, by Riemann--Roch [@Har77, Theorem IV.1.3].
The sharper bound on gonality is Brill--Noether theory and is stated with its own hypotheses on [[D-CRVBRILLNOETHER]]; it is not asserted here.
:::

::: {.remark}
A base-point-free $g^r_d$ determines a morphism $\phi\colon C\to\PP^r$ with $\deg\phi^*\OO(1)=d$; for $r=1$ this is a map $C\to\PP^1$ of degree $d$ [@Har77, Section IV.5].
The canonical system on a curve of genus $g\ge2$ is a $g^{g-1}_{2g-2}$.

A nonhyperelliptic curve of genus $3$ is a plane quartic, and for each of its points $p$ the system $\abs{K-p}$ is a $g^1_3$ [@Har77, Example IV.5.2.1].
A nonhyperelliptic curve of genus $4$ lies on a quadric surface, whose rulings cut $g^1_3$'s, one of them when the quadric is a cone [@Har77, Example IV.5.2.2] ([[FE-CRVLOWG]]).
In particular every nonhyperelliptic curve of genus $3$ or $4$ is trigonal.
:::
