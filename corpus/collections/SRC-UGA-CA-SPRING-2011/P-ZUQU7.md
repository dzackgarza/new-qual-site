---
schema: qual/card@1
id: P-ZUQU7
kind: problem
title: Injective conformal maps of $\{\operatorname{Re} z>0,\ |z-1|>1\}$ onto the
  disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
  - Fractional Linear Transformations
  - Blaschke Factors
relations: []
review: draft
---

::: {.problem}
Define
\[  
G \definedas \theset{z\in \CC\suchthat \Re(z) > 0, \, \abs{z-1} > 1}
.\]

Find all of the injective conformal maps $G\to \DD$.
These may be expressed as compositions of maps, but explain why this list is complete.
:::

::: {.solution}
Interpreting a conformal map $G\to\mathbb D$ here as a biholomorphism onto
$\mathbb D$, first construct one such map. Put
\[
T(z)=\frac1z.
\]
Since
\[
\operatorname{Re}\frac1z=\frac{\operatorname{Re}z}{|z|^2},
\]
the condition $\operatorname{Re}z>0$ becomes $\operatorname{Re}T(z)>0$.
Moreover
\[
|z-1|>1
\iff |z|^2>2\operatorname{Re}z
\iff \operatorname{Re}\frac1z<\frac12.
\]
Thus $T$ maps $G$ biholomorphically onto the vertical strip
\[
S=\{w:0<\operatorname{Re}w<1/2\}.
\]
Next
\[
E(w)=e^{2\pi i w}
\]
maps $S$ biholomorphically onto the upper half-plane, and the Cayley map
\[
C(\zeta)=\frac{\zeta-i}{\zeta+i}
\]
maps the upper half-plane biholomorphically onto $\mathbb D$. Hence
\[
\Phi(z)=C(E(T(z)))
=\frac{e^{2\pi i/z}-i}{e^{2\pi i/z}+i}
\]
is one biholomorphism $G\to\mathbb D$.

Every disk automorphism has the form
\[
A_{a,\theta}(w)=e^{i\theta}\frac{w-a}{1-\bar a w},
\qquad a\in\mathbb D,\quad \theta\in\mathbb R.
\]
Therefore all conformal bijections $G\to\mathbb D$ are
\[
\boxed{A_{a,\theta}\circ\Phi}.
\]
Indeed, if $F:G\to\mathbb D$ is any other biholomorphism, then
$F\circ\Phi^{-1}$ is an automorphism of $\mathbb D$, so it is one of the
$A_{a,\theta}$ above. This also proves completeness of the list.

If ``injective conformal map into $\mathbb D$'' is read without the usual
onto requirement, the displayed family is not exhaustive (for example
$r\Phi$, $0<r<1$, is injective but not onto); the classification above is the
standard conformal-equivalence interpretation of the question.
:::
