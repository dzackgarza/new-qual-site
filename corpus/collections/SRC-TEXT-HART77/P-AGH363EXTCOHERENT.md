---
schema: qual/card@1
id: P-AGH363EXTCOHERENT
kind: problem
title: Coherence and quasi-coherence of sheaf Ext
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Sheaves
  - Coherent Sheaves
  - Quasicoherent Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both finiteness assertions with the retained Hartshorne III.6.3 transcription and Propositions III.6.2 and III.6.5. The proof computes on an affine finite-free resolution and distinguishes finite generation of the Ext modules from their associated sheaves being quasi-coherent.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, and let $\mcf, \mcg \in \Mod(X)$.

(a) If $\mcf, \mcg$ are both coherent, then $\mathcal{E}xt^i(\mcf, \mcg)$ is coherent, for all $i \geq 0$.

(b) If $\mcf$ is coherent and $\mcg$ is quasi-coherent, then $\mathcal{E}xt^i(\mcf, \mcg)$ is quasi-coherent, for all $i \geq 0$.
:::

::: {.solution}
Sheaf Ext restricts to open subsets:
$$
\mathcal{E}xt_X^i(\mcf,\mcg)|_U
\cong\mathcal{E}xt_U^i(\mcf|_U,\mcg|_U)
$$
[@Har10a, Proposition III.6.2].
Both [[D-QNTZY|coherence and quasi-coherence]] are local properties.
It therefore suffices to work on an arbitrary affine open $U=\Spec A\subseteq X$, where $A$ is noetherian.
Write $\mcf|_U=\widetilde M$ and $\mcg|_U=\widetilde N$; the module $M$ is finite, and $N$ is finite in (a) and arbitrary in (b).

<1>1. The module $M$ has a resolution by finite free $A$-modules
$$
\cdots\longrightarrow P_2\longrightarrow P_1\longrightarrow P_0
\longrightarrow M\longrightarrow0.
$$

::: {.proof}
Choose a finite generating set for $M$ to obtain $P_0\twoheadrightarrow M$.
Its kernel is finitely generated because $A$ is noetherian and $P_0$ is finite.
Choose a finite free module surjecting onto that kernel and repeat.
This gives an exact resolution, although it need not terminate.
The associated-sheaf functor is exact on $\Spec A$, so sheafification gives a resolution of $\widetilde M$ by finite-rank free sheaves.
:::

<1>2. On $U$ there is an isomorphism
$$
\mathcal{E}xt_U^i(\widetilde M,\widetilde N)
\cong\widetilde{\Ext_A^i(M,N)}
\qquad(i\ge0).
$$

::: {.proof}
The locally free resolution formula [@Har10a, Proposition III.6.5] computes the left side as the $i$th cohomology sheaf of
$$
\sheafhom_U(\widetilde P_\bullet,\widetilde N).
$$
For each finite free $P_j$, the natural map
$$
\widetilde{\Hom_A(P_j,N)}
\longrightarrow\sheafhom_U(\widetilde P_j,\widetilde N)
$$
is an isomorphism: a basis identifies both sides with a finite direct sum of copies of $\widetilde N$.
These natural maps commute with precomposition by the resolution differentials, hence identify the full complexes.
Exactness of sheafification identifies kernels, images and their quotients, so the cohomology sheaf is the associated sheaf of
$$
H^i(\Hom_A(P_\bullet,N))=\Ext_A^i(M,N).
$$
This proves the assertion, including $i=0$.
For a fixed degree only the neighboring finite free terms enter its kernel and image; an infinite resolution causes no infinite-product issue.
:::

<1>3. The sheaf in step <1>2 is coherent in (a) and quasi-coherent in (b).

::: {.proof}
In (a), each $\Hom_A(P_j,N)$ is a finite direct sum of the finite module $N$.
Its submodules and quotients are finite over the noetherian ring $A$.
Therefore the cohomology modules $\Ext_A^i(M,N)$ are finite, and their associated sheaves are coherent [@Har10a, Proposition II.5.4].

In (b), the Ext modules need not be finite, but the associated sheaf of every $A$-module is quasi-coherent.
Thus step <1>2 gives quasi-coherence with no finiteness requirement on $N$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove both assertions on each affine open, and locality of sheaf Ext and of the two finiteness properties gives (a) and (b) on $X$.
:::
:::
