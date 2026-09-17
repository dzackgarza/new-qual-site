---
schema: qual/card@1
id: P-AGH254COKERCHAR
kind: problem
title: Quasi-coherence as a local cokernel of free sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-coherent Sheaves
  - Coherent Sheaves
  - Presentations
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both assertions with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.4. Checked the arbitrary direct sums, affine shrinking, and finite-relation argument independently.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Show that a sheaf of $\OO_X$-modules $\mcf$ on a scheme $X$ is quasi-coherent if and only if every point of $X$ has a neighborhood $U$ such that $\mcf|_U$ is isomorphic to a cokernel of a morphism of free sheaves on $U$.

If $X$ is noetherian, then $\mcf$ is coherent if and only if it is locally a cokernel of a morphism of free sheaves of finite rank.
These properties were originally the definition of quasi-coherent and coherent sheaves.
:::

::: {.solution}
For an open set $U\subseteq X$, put $\OO_U=\OO_X|_U$.
For an index set $I$, write $A^{(I)}=\bigoplus_{i\in I}A$ and $\OO_U^{(I)}=\bigoplus_{i\in I}\OO_U$.
On $U=\Spec A$, the associated-sheaf functor is exact and commutes with direct sums, so
$$
\widetilde{A^{(I)}}\cong\OO_U^{(I)}
$$
[@Har10a, Propositions II.5.1 and II.5.2].

<1>1. A [[D-QNTZY|quasi-coherent]] sheaf has the required local presentation by free sheaves.

::: {.proof}
For each $x\in X$, choose an affine neighborhood $U=\Spec A$ and an $A$-module $M$ with $\mcf|_U\cong\widetilde M$.
Choose a free module $A^{(J)}$ surjecting onto $M$, and a free module $A^{(I)}$ surjecting onto the kernel.
This gives an exact sequence
$$
A^{(I)}\xrightarrow{u}A^{(J)}\longrightarrow M\longrightarrow0.
$$
Applying the associated-sheaf functor gives
$$
\OO_U^{(I)}\xrightarrow{\widetilde u}\OO_U^{(J)}
\longrightarrow\mcf|_U\longrightarrow0.
$$
Thus $\mcf|_U$ is the asserted cokernel.
:::

<1>2. A sheaf locally presented as a cokernel of free sheaves is [[D-QNTZY|quasi-coherent]].

::: {.proof}
Fix $x\in X$ and an open neighborhood on which the given presentation exists.
Shrink it to an affine neighborhood $U=\Spec A$ of $x$.
Restriction is exact and commutes with direct sums, as can be checked on stalks, so there is still an exact sequence
$$
\OO_U^{(I)}\xrightarrow{v}\OO_U^{(J)}\longrightarrow\mcf|_U\longrightarrow0.
$$
By [[P-AGH253TILDEADJ]], the morphism $v$ corresponds to an $A$-linear map
$$
u:A^{(I)}\longrightarrow\Gamma(U,\OO_U^{(J)})\cong A^{(J)}.
$$
Its associated-sheaf morphism is $v$, since both have this effect on global sections and the correspondence is injective.
Set $M=\operatorname{coker}u$.
Exactness of the associated-sheaf functor identifies $\widetilde M$ with the cokernel of $v$, hence with $\mcf|_U$.
These affine neighborhoods give the defining local descriptions of a [[D-QNTZY|quasi-coherent]] sheaf.
:::

<1>3. On a noetherian scheme, [[D-QNTZY|coherence]] is equivalent to the existence of such presentations with $I$ and $J$ finite.

::: {.proof}
Suppose first that $\mcf$ is [[D-QNTZY|coherent]].
For each point choose an affine neighborhood $U=\Spec A$ with $\mcf|_U\cong\widetilde M$, where $M$ is finitely generated and $A$ is noetherian [@Har10a, Proposition II.5.4].
Choose a surjection $A^n\to M$ with $n$ finite.
Its kernel is finitely generated because it is a submodule of the noetherian module $A^n$.
Choose finitely many generators of this kernel to obtain
$$
A^m\longrightarrow A^n\longrightarrow M\longrightarrow0
$$
with $m,n$ finite.
The construction of step <1>1 gives the required finite-rank sheaf presentation.

Conversely, shrink a given finite-rank presentation to an affine neighborhood $U=\Spec A$.
Step <1>2 identifies $\mcf|_U$ with $\widetilde M$ for the cokernel $M$ of a map $A^m\to A^n$ with $m,n$ finite.
In particular, $M$ is finitely generated.
Over the noetherian ring $A$, every kernel of a map $A^r\to M$ with $r$ finite is finitely generated, being a submodule of $A^r$.
Thus $M$ is a [[D-QNTZY|coherent module]], and the affine local descriptions make $\mcf$ [[D-QNTZY|coherent]].
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 prove the characterization of [[D-QNTZY|quasi-coherence]], and step <1>3 proves the noetherian finite-rank characterization.
:::
:::
