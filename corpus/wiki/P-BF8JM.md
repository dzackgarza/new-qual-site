---
schema: qual/card@1
id: P-BF8JM
kind: problem
title: "This is true. By the Galois correspondence, it suffices to show that \u2026"
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - normal-subgroups
  - field-extensions
relations: []
review: draft
---

::: problem
This is true.
By the Galois correspondence, it suffices to show that $H \definedas \Gal(M/L)$ is a normal subgroup of $G \definedas \Gal(M/ K)$.
To that end, let $\phi \in G$, so $\phi: M \to M$ is a lift of $\id_K$.
Then $H \normal G$ iff $\phi H \phi\inv = H$.
Letting $\sigma \in H$, we need to show that
$$
(\phi\inv \circ \sigma \circ \phi)(L) = L,
$$
i.e. that this composition is some automorphism of $M$ that fixes $L$.

Consider how this acts on elements of $L$.
If $\ell \in L$, then $\ell = \sum k_i \ell_i$ since $L$ is a finite-degree extension, thus algebraic, thus spanned by some basis $\ell_i \in L$ as a vector space over $K$.

In particular, since $\phi$ is some $M\dash$automorphism, it restricts to an $L\dash$automorphism, which must send each $\ell_i$ to some conjugate $\ell_i'$.
Similarly, $\phi\inv(\ell_i') = \ell_i$.

We thus have
\[
\begin{align*}
(\phi\inv \sigma \phi)(a) &=
(\phi\inv \sigma \phi)(\sum k_i \ell_i) \\
&= (\phi\inv \sigma)(\sum k_i \phi(\ell_i)) \\
&= (\phi\inv \sigma)(\sum k_i \ell_i') \\
&= (\phi\inv)(\sum k_i \sigma(\ell_i')) \\
&= (\phi\inv)(\sum k_i \ell_i') \quad\text{since $\sigma$ fixes $L$}\\
&= \sum k_i \phi\inv(\ell_i') \\
&= \sum k_i \ell_i \\
,\end{align*}
\]

and so this composite fixes $L$ as desired.
This $H \normal G$, which is what we wanted to show.
:::
