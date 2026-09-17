---
schema: qual/card@1
id: P-AGH294COHEXT
kind: problem
title: Coherence of the middle term of an exact sequence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Coherent Sheaves
  - Exact Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the entire statement with the retained Hartshorne II.9.4 transcription. The proof uses II.9.3 to lift a finite generating set of the coherent quotient, then realizes the middle sheaf as a cokernel of a morphism between coherent sheaves without presupposing its coherence.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Use (Ex. 9.3) to prove that if
$$
0 \to \mcf' \to \mcf \to \mcf'' \to 0
$$
is an exact sequence of $\OO_\mathfrak{X}\dash$modules on a noetherian formal scheme $\mathfrak{X}$, and if $\mcf', \mcf''$ are coherent, then $\mcf$ is coherent also.
:::

::: {.solution}
Write $a:\mcf'\hookrightarrow\mcf$ and $b:\mcf\twoheadrightarrow\mcf''$ for the given maps.
Coherence on a noetherian formal scheme is local, so work on an arbitrary affine formal open $\mathfrak U\subseteq\mathfrak X$ and restrict all sheaves and maps to it.
For coherent formal sheaves, finite direct sums, kernels and cokernels of morphisms are coherent [@Har10a, Theorem II.9.7 and Corollary II.9.9].
These closure properties concern morphisms whose source and target are already coherent; no such assumption is made about $\mcf$.

<1>1. There is a surjection $q:\OO_{\mathfrak U}^{\oplus s}\twoheadrightarrow\mcf''$ and a lift $\widetilde q:\OO_{\mathfrak U}^{\oplus s}\to\mcf$ with $b\widetilde q=q$.

::: {.proof}
Write $\mathfrak U=\operatorname{Spf}A$ with $A$ noetherian and complete for its defining ideal.
The affine formal module correspondence identifies $\mcf''$ with the sheaf associated to the finite $A$-module $\Gamma(\mathfrak U,\mcf'')$ [@Har10a, Theorem II.9.7].
A finite set of module generators therefore gives global sections generating the sheaf and a surjection $q$ as asserted.
By [[P-AGH293EXACTGLOBAL]], applied to the given sequence with coherent kernel $\mcf'$, the map
$$
\Gamma(\mathfrak U,\mcf)\longrightarrow\Gamma(\mathfrak U,\mcf'')
$$
is surjective.
Lift each of the $s$ chosen sections through this map.
Their images define $\widetilde q$, and $b\widetilde q=q$ because the maps agree on the standard generators of the free sheaf.
:::

<1>2. Put $R=\ker q$.
There is an exact sequence
$$
0\longrightarrow R\xrightarrow{\gamma}
\mcf'\oplus\OO_{\mathfrak U}^{\oplus s}
\xrightarrow{\beta}\mcf\longrightarrow0
$$
in which the first two sheaves are coherent.

::: {.proof}
Since $q$ is a morphism between coherent sheaves, $R$ is coherent by the closure property stated before step <1>1.
The restriction of $\widetilde q$ to $R$ has zero composite with $b$, so it factors uniquely through $a$ as a map $\lambda:R\to\mcf'$.
Define
$$
\gamma(r)=(-\lambda(r),r),\qquad
\beta(u,v)=a(u)+\widetilde q(v).
$$
Here the second component of $\gamma$ uses $R\subseteq\OO_{\mathfrak U}^{\oplus s}$.
The equality $a\lambda=\widetilde q|_R$ makes $\beta\gamma=0$, and the second component makes $\gamma$ injective.

Exactness of the remaining terms can be checked at a stalk.
For an element of $\mcf$, its image in $\mcf''$ lifts through $q$; subtracting the corresponding image under $\widetilde q$ leaves an element of $a(\mcf')$.
Thus $\beta$ is surjective.
If $a(u)+\widetilde q(v)=0$, applying $b$ gives $q(v)=0$, so $v\in R$.
Then injectivity of $a$ gives $u=-\lambda(v)$, which says $(u,v)=\gamma(v)$.
This proves exactness.
Both $R$ and $\mcf'\oplus\OO_{\mathfrak U}^{\oplus s}$ are coherent, as required.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 identifies $\mcf|_{\mathfrak U}$ with the cokernel of a morphism between coherent formal sheaves.
It is therefore coherent by [@Har10a, Corollary II.9.9].
The construction applies on every affine formal open, and these opens cover $\mathfrak X$.
Locality of coherence proves that $\mcf$ is coherent on $\mathfrak X$.
:::
:::
