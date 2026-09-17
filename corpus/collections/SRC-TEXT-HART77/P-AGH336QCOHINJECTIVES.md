---
schema: qual/card@1
id: P-AGH336QCOHINJECTIVES
kind: problem
title: Injective quasi-coherent sheaves and cohomology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Quasicoherent Sheaves
  - Injective Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts and the hint with the retained Hartshorne Chapter III section 3 transcription. Read the quasi-coherent open-pushforward prerequisite. The proof verifies injectivity of the affine-cover construction by adjunction and proves flasqueness of arbitrary quasi-coherent injectives by splitting their embeddings into that construction.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme.

(a) Show that the sheaf $\mcg$ constructed in the proof of (3.6) is an injective object in the category $\QCoh(X)$ of quasi-coherent sheaves on $X$.
Thus $\QCoh(X)$ has enough injectives.

(b) Show that any injective object of $\QCoh(X)$ is flasque.

(c) Conclude that one can compute cohomology as the derived functors of $\Gamma(X,\wait)$, considered as a functor from $\QCoh(X)$ to $\Ab$.
:::

::: {.hint}
For (b), the method of proof of (2.4) will not work, because $\mco_U$ is not quasi-coherent on $X$ in general.
Instead, use (II, Ex. 5.15) to show that if $\mci \in \QCoh(X)$ is injective, and if $U \subseteq X$ is an open subset, then $\ro{\mci}{U}$ is an injective object of $\QCoh(U)$.
Then cover $X$ with open affines.
:::

::: {.solution}
The category $\QCoh(X)$ is a full abelian subcategory of $\OO_X$-modules, with kernels and cokernels computed as sheaves [@Har10a, Proposition II.5.7].
Choose a finite affine open cover $X=\bigcup_{a=1}^r U_a$, where $U_a=\Spec A_a$, and let $j_a:U_a\hookrightarrow X$ be the inclusions.
For a quasi-coherent $F$, write $F|_{U_a}=\widetilde{M_a}$ and choose an embedding $M_a\hookrightarrow J_a$ into an injective $A_a$-module.
The sheaf used in the affine-cover construction of [@Har10a, Corollary III.3.6] is
$$
G=\bigoplus_{a=1}^r j_{a*}\widetilde{J_a}.
$$

<1>1. Each $j_{a*}\widetilde{J_a}$ is a quasi-coherent sheaf injective in $\QCoh(X)$.

::: {.proof}
An open immersion into a noetherian scheme is quasi-compact and separated.
Its direct image preserves quasi-coherence [@Har10a, Proposition II.5.8(c)], as used in [[P-AGH2515EXTCOH]].
Thus $j_{a*}\widetilde{J_a}$ is quasi-coherent.
The affine equivalence $\operatorname{Mod}(A_a)\simeq\QCoh(U_a)$ is exact, so the module injectivity of $J_a$ makes $\widetilde{J_a}$ injective in $\QCoh(U_a)$.

For $E\in\QCoh(X)$, restriction and direct image give the adjunction
$$
\Hom_X(E,j_{a*}\widetilde{J_a})
\cong\Hom_{U_a}(E|_{U_a},\widetilde{J_a}).
$$
Given a monomorphism $E\hookrightarrow E'$ in $\QCoh(X)$, restriction is exact and gives a monomorphism on $U_a$.
A morphism from $E|_{U_a}$ to $\widetilde{J_a}$ therefore extends to $E'|_{U_a}$ by injectivity on that affine open.
Adjunction turns this extension into an extension from $E'$ to $j_{a*}\widetilde{J_a}$.
This is injectivity in $\QCoh(X)$.
:::

<1>2. The sheaf $G$ is injective in $\QCoh(X)$, and the construction gives a monomorphism $F\hookrightarrow G$.

::: {.proof}
A finite direct sum is also a finite product.
To extend a map into $G$ across a monomorphism, extend each of its finitely many components using step <1>1 and assemble them.
Hence $G$ is injective.

The local embeddings $F|_{U_a}\hookrightarrow\widetilde{J_a}$ induce maps $F\to j_{a*}\widetilde{J_a}$ by adjunction.
Combining them gives a morphism $F\to G$.
At any point $x\in X$, choose $a$ with $x\in U_a$.
The $a$th component on that stalk is the injective map $F_x\to(\widetilde{J_a})_x$, because restriction of $j_{a*}$ back to $U_a$ is the identity.
Thus the combined map is injective at every stalk and is a monomorphism.
Every quasi-coherent sheaf therefore embeds into an injective object of $\QCoh(X)$, proving (a).
:::

<1>3. The sheaf $G$ is flasque, and every injective object of $\QCoh(X)$ is flasque.

::: {.proof}
Since $A_a$ is noetherian and $J_a$ is an injective module, $\widetilde{J_a}$ is flasque on $U_a$ [@Har10a, Proposition III.3.4].
For open sets $W\subseteq V\subseteq X$, the restriction map of its direct image is
$$
\widetilde{J_a}(V\cap U_a)\longrightarrow\widetilde{J_a}(W\cap U_a),
$$
which is surjective by flasqueness on $U_a$.
Thus each summand of $G$ is flasque, and so is the finite direct sum.

Now let $I$ be injective in $\QCoh(X)$.
Step <1>2, applied to $F=I$, gives a monomorphism $e:I\hookrightarrow G$ with $G$ flasque and quasi-coherent.
Injectivity of $I$ extends $\id_I$ along $e$ to a morphism $p:G\to I$ satisfying $pe=\id_I$.
For any $W\subseteq V$ and $s\in I(W)$, extend $e(s)$ to $t\in G(V)$ by flasqueness, then apply $p$.
The section $p(t)$ restricts to $pe(s)=s$.
Hence every restriction map on $I$ is surjective, proving (b).
:::

<1>4. For every $F\in\QCoh(X)$ and $i\ge0$, the derived functor computed in $\QCoh(X)$ agrees naturally with sheaf cohomology:
$$
R^i\bigl(\Gamma(X,-)|_{\QCoh(X)}\bigr)(F)\cong H^i(X,F).
$$

::: {.proof}
By step <1>2, choose an injective resolution $F\to I^\bullet$ in $\QCoh(X)$.
The exact inclusion of $\QCoh(X)$ into all module sheaves makes this an exact resolution of the underlying abelian sheaf.
Step <1>3 makes its terms flasque.
They are consequently acyclic for ordinary global sections, so this same resolution computes ordinary sheaf cohomology [@Har10a, Proposition III.2.5 and Remark III.2.5.1].
On the other hand, its global-section complex defines the derived functor in $\QCoh(X)$.
The two computations are the identical complex $\Gamma(X,I^\bullet)$, giving the asserted isomorphism in all degrees.
Comparison of resolutions gives naturality in $F$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove (a), step <1>3 proves (b), and step <1>4 proves (c).
:::
:::
