---
schema: qual/card@1
id: PR-COHLES
kind: proposition
title: The long exact sequence, and the ideal sequence as a computational device
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Long Exact Sequences
  - Ideal Sheaves
relations:
- kind: uses
  target: D-COHDER
- kind: uses
  target: T-IJW1K
review: draft
prompts:
- What is the long exact sequence in sheaf cohomology?
- How do you compute the cohomology of a hypersurface in $\PP^n$?
- Prove the long exact sequence in cohomology for a short exact sequence of complexes.
---

::: {.proposition}
A short exact sequence $0 \to \mcf' \to \mcf \to \mcf'' \to 0$ of sheaves of abelian groups gives a long exact sequence
\[
0 \to H^0(\mcf') \to H^0(\mcf) \to H^0(\mcf'') \mapsvia{\delta} H^1(\mcf') \to \cdots ,
\]
natural in morphisms of short exact sequences.
:::

::: {.lemma title="Long exact sequence of a short exact sequence of complexes"}
Let $0 \to C'^\bullet \xrightarrow{u} C^\bullet \xrightarrow{v} C''^\bullet \to 0$ be a short exact sequence of complexes in an abelian category.
Then there are connecting morphisms $\delta^i \colon h^i(C''^\bullet) \to h^{i+1}(C'^\bullet)$, natural in the sequence, making
$$\cdots \to h^i(C'^\bullet) \to h^i(C^\bullet) \to h^i(C''^\bullet) \xrightarrow{\delta^i} h^{i+1}(C'^\bullet) \to \cdots$$
exact.
:::

<1>1. For every $i$ the rows of
$$\begin{aligned} & \operatorname{coker}(d'^{i-1}) \to \operatorname{coker}(d^{i-1}) \to \operatorname{coker}(d''^{i-1}) \to 0 \\ 0 \to\ & \ker(d'^{i+1}) \to \ker(d^{i+1}) \to \ker(d''^{i+1}) \end{aligned}$$
are exact, with vertical maps induced by the differentials $d^i$.

::: {.proof}
Apply the snake lemma to the map of short exact sequences $0 \to C'^{i-1} \to C^{i-1} \to C''^{i-1} \to 0$ and $0 \to C'^{i} \to C^{i} \to C''^{i} \to 0$ along the differentials: the kernels give exactness of $0 \to \ker d'^{i-1} \to \ker d^{i-1} \to \ker d''^{i-1}$ and the cokernels exactness of $\operatorname{coker} d'^{i-1} \to \operatorname{coker} d^{i-1} \to \operatorname{coker} d''^{i-1} \to 0$; shifting the index gives the bottom row.
:::

<1>2. The kernels of the vertical maps $\operatorname{coker}(d^{i-1}) \to \ker(d^{i+1})$ are the $h^i$, and their cokernels are the $h^{i+1}$.

::: {.proof}
The map $C^i / \operatorname{im} d^{i-1} \to \ker d^{i+1}$ induced by $d^i$ has kernel $\ker d^i / \operatorname{im} d^{i-1} = h^i(C^\bullet)$ and cokernel $\ker d^{i+1} / \operatorname{im} d^i = h^{i+1}(C^\bullet)$, and likewise for $C'^\bullet$ and $C''^\bullet$.
:::

<1>3. Q.E.D.

::: {.proof}
The snake lemma applied to the diagram of step <1>1 gives the exact sequence $h^i(C'^\bullet) \to h^i(C^\bullet) \to h^i(C''^\bullet) \xrightarrow{\delta^i} h^{i+1}(C'^\bullet) \to h^{i+1}(C^\bullet) \to h^{i+1}(C''^\bullet)$ by step <1>2, and these segments overlap to the long exact sequence.
:::

::: {.remark}
For derived-functor cohomology, the proposition follows by applying the lemma to $0 \to \Gamma(X, I'^\bullet) \to \Gamma(X, I^\bullet) \to \Gamma(X, I''^\bullet) \to 0$ for compatible injective resolutions, which remains exact because $I'^\bullet$ is injective in each degree.
For Čech cohomology of quasicoherent sheaves on a quasicompact separated scheme with a finite affine cover $\mathfrak{U}$, the sequence $0 \to C^\bullet(\mathfrak{U}, \mcf') \to C^\bullet(\mathfrak{U}, \mcf) \to C^\bullet(\mathfrak{U}, \mcf'') \to 0$ is exact because every finite intersection of the cover is affine and sections of quasicoherent sheaves over affines form exact sequences, and the lemma applies directly.
:::

::: {.remark title="What the connecting map is"}
$\delta$ sends a global section of $\mcf''$ to the obstruction to lifting it: lift locally on a cover, take the differences of the lifts on overlaps, and read the result as a class in $H^1(\mcf')$.
So $H^1(\mcf') = 0$ is precisely the statement that every global section of the quotient lifts.
:::

::: {.remark title="How every computation actually goes"}
For $Y \subseteq \PP^n$ closed with ideal sheaf $\mci_Y$, twist the ideal sequence:
\[
0 \to \mci_Y(d) \to \OO_{\PP^n}(d) \to \OO_Y(d) \to 0 .
\]
Known cohomology of the middle term plus known cohomology of the left term determines the right, which is the unknown.
For a smooth hypersurface of degree $e$, $\mci_Y = \OO(-e)$ and everything is a binomial coefficient; this is how one gets $h^0(\OO_Y(d))$, the Hilbert polynomial of $Y$, and the genus of a plane curve as $\binom{e-1}{2}$.

The other constant use is the skyscraper sequence $0 \to \OO(D-p) \to \OO(D) \to k(p) \to 0$ on a curve, which is how $\ell(D)$ moves by at most one when a point is added, and hence how Riemann--Roch is proved by induction.
:::
