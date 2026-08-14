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
---

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
&= nf(1) + g(2) \\
&= n\phi_\mathrm{ev}(f) + \phi_\mathrm{ev}(g)
\end{align*}
\]

But this forces $f(\overline 0) = 0_A$ (where $\overline 0: \ZZ_m \to A$ is the zero map), we have
$$
0 = f(0) = f(m) = m f(1),
$$

we must have $mf(1) = 0$ in $A$.
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

which follows from the fact that $\ZZ_m = \generators{1 \mod m}$ and $A = \generators{1_A}$ as $\ZZ\dash$modules, so if $f(1 \mod m) = 0_A$ then
$$
f(n \mod m) = nf( 1 \mod m) = 0
$$

and so $f$ is necessarily the zero map.
So $\ker \phi = \overline 0$.

We can then apply the first isomorphism theorem,
$$
\frac{\hom_\ZZ(\ZZ_m, A)}{\ker \phi_{\mathrm{ev}}} \cong \im \phi_{\mathrm{ev}} \implies \hom_\ZZ(\ZZ_m, A) \cong A[m].
$$
