---
schema: qual/card@1
id: P-AP4TX
kind: problem
title: "Define a map $\\phi_\\mathrm{ev}: \\hom_\\ZZ(\\ZZ_m, A) \\to A \\\\ (f: \\ZZ_m \\to A) \\mapsto f(1)$"
classification:
  areas:
  - algebra
  topics:
  - modules
  - cyclic-groups
  - isomorphism-theorems
relations: []
review: draft
solved: false
---

::: problem
Define a map

$$
\phi_\mathrm{ev}: \hom_\ZZ(\ZZ_m, A) \to A \\
(f: \ZZ_m \to A) \mapsto f(1)
$$

Then $\phi_\mathrm{ev}$ is a $\ZZ\dash$module homomorphism, since

\[
\begin{align*}
\phi_\mathrm{ev}(nf + g) 
&= (nf + g)(1) \\
&= nf(1) + g(1) \\
&= n\phi_\mathrm{ev}(f) + \phi_\mathrm{ev}(g)
\end{align*}
\]

The image is contained in the $m\dash$torsion: for any $f$, reading $0 = m \mod m$ in $\ZZ_m$ gives
$$
0_A = f(0) = f(m \cdot 1) = m f(1),
$$

so $f(1)$ is killed by $m$.
Conversely every such element is hit: given $a\in A$ with $ma = 0$, the assignment $n \mod m \mapsto na$ is well defined, since $n \equiv n' \mod m$ makes $na - n'a$ a multiple of $ma = 0$, and it is a morphism sending $1 \mapsto a$.
So
$$
\im \phi_\mathrm{ev} = \theset{a\in A \mid ma = 0} \definedas A[m].
$$

It is also the case that
\[
\begin{align*}
\ker \phi_{\mathrm{ev}} &= \theset{f \in \hom_\ZZ(\ZZ_m, A) \mid f(1) = 0} = \theset{\overline 0},
\end{align*}
\]

which follows from $\ZZ_m = \generators{1 \mod m}$ alone: a morphism out of a cyclic module is determined by where the generator goes, and no hypothesis on $A$ is needed.
So if $f(1 \mod m) = 0_A$ then
$$
f(n \mod m) = nf( 1 \mod m) = 0
$$

and so $f$ is necessarily the zero map.
So $\ker \phi = \overline 0$.

We can then apply the first isomorphism theorem,
$$
\frac{\hom_\ZZ(\ZZ_m, A)}{\ker \phi_{\mathrm{ev}}} \cong \im \phi_{\mathrm{ev}} \implies \hom_\ZZ(\ZZ_m, A) \cong A[m].
$$
:::
