---
schema: qual/card@1
id: P-AGXHWREDUCED
kind: problem
title: Reducedness on stalks and the universal property of the reduction of a scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Reduced Schemes
  - Nilpotents
  - Sheafification
relations: []
review: draft
---

::: {.problem}
Call $(X, \OO_X)\in \Sch$ **reduced** iff $\OO_X(U)$ has no nilpotents for every open $U$, and for $A\in \Ring$ define $A^{\red}\definedas A/\sqrt{0}$ to be $A$ modulo its ideal of nilpotents.

(a) Show that $X$ is reduced iff for every $p\in X$, the local ring $\OO_{X, p}$ has no nilpotents.

(b) Let $\OO_X^{\red}$ be the sheafification of $U \mapsto \OO_X(U)^{\red}$.
Show that $X_{\red}\definedas (X, \OO_X^{\red})$ is a scheme, and that there is a morphism of schemes $X_{\red}\xrightarrow{\red} X$ inducing a homeomorphism $\abs{X_{\red}}\to \abs{X}$ on underlying topological spaces.

(c) Let $X \xrightarrow{f} Y\in \Sch$ with $X$ reduced.
Show that there is a unique morphism $X \xrightarrow{g} Y_{\red}$ such that $f$ is the composition

\begin{tikzcd}
	X && Y \\
	\\
	&& {Y_{\red}}
	\arrow["f", from=1-1, to=1-3]
	\arrow["{\exists ! g}"', from=1-1, to=3-3]
	\arrow["\red"', from=3-3, to=1-3]
\end{tikzcd}
:::

::: {.hint}
(a) A section that is zero in every stalk is zero, by the sheaf axiom.

(b)

- Cover by affines.

- $\sqrt{0_{R}} \leq \mfp$ for every $\mfp\in \Spec R$.

- $R_{\red}\definedas R/\sqrt{0_{R}}$ is a quotient, and localization commutes with quotients.

- Maps $R\to S$ with $S$ reduced factor through $R_{\red}$.

- Sheafification has the same stalks, and an isomorphism on stalks is an isomorphism of sheaves.

- Pushforwards of reduced sheaves are reduced.
:::

::: {.solution}
Write $P$ for the presheaf $U \mapsto \OO_X(U)^\red$, so that $\OO_X^\red$ is its sheafification, and write $\rho\colon \OO_X \to \OO_X^\red$ for the quotient maps followed by sheafification.

::: pf

::: pf-step
(a) $X$ is reduced if and only if every local ring $\OO_{X,p}$ has no nonzero nilpotents.

::: pf-proof

::: pf-step
If $X$ is reduced, then every $\OO_{X,p}$ has no nonzero nilpotents.

::: pf-proof
Suppose $s_p \in \OO_{X,p}$ is nonzero with $s_p^n = 0$.
Represent $s_p$ by $s \in \OO_X(U)$ for an open $U \ni p$.
The germ of $s^n$ at $p$ is $0$, so after shrinking $U$ we have $s^n = 0$ in $\OO_X(U)$.
The germ of $s$ is nonzero, so $s \neq 0$.
Then $s$ is a nonzero nilpotent in $\OO_X(U)$, which contradicts reducedness.
:::

:::

::: pf-step
If every $\OO_{X,p}$ has no nonzero nilpotents, then $X$ is reduced.

::: pf-proof
Let $s \in \OO_X(U)$ with $s^n = 0$.
For each $p \in U$, the germ satisfies $s_p^n = 0$, so $s_p = 0$.
A section whose germs all vanish is zero by the identity axiom, so $s = 0$.
:::

:::

:::

:::

::: pf-step
(b) $X_\red$ is a scheme, and there is a morphism $\red\colon X_\red \to X$ whose underlying map is a homeomorphism.

::: pf-proof

::: {.pf-step #stalks}
For every $p \in X$, $(\OO_X^\red)_p = P_p = \OO_{X,p}^\red$.

::: pf-proof
Sheafification preserves stalks.
Stalks are filtered colimits, which commute with quotients by the nilradical: an element of the colimit is nilpotent exactly when some representative is nilpotent.
:::

:::

::: {.pf-step #affine}
For an affine open $U = \Spec A$ of $X$, there is an isomorphism of locally ringed spaces $(U, \restrictionof{\OO_X^\red}{U}) \cong \Spec A^\red$.

::: pf-proof
Let $j\colon \Spec A^\red \to \Spec A$ be induced by $A \to A^\red$.
Every prime contains $\sqrt{0}$, so $j$ is a homeomorphism; identify the two spaces.
For an open $V \subseteq U$, the map $\OO_U(V) \to \OO_{\Spec A^\red}(V)$ lands in a reduced ring, so it factors through $P(V)$.
This gives a map of presheaves $\restrictionof{P}{U} \to \OO_{\Spec A^\red}$, and so a map of sheaves $\restrictionof{\OO_X^\red}{U} \to \OO_{\Spec A^\red}$.
By step [](#stalks){.pf-ref}, its stalk at $\mfp$ is $(A_\mfp)^\red \to (A^\red)_\mfp$.
This is an isomorphism, because localization is exact and $\sqrt{0_{A_\mfp}} = (\sqrt{0_A})_\mfp$.
A map of sheaves that is an isomorphism on stalks is an isomorphism.
:::

:::

::: pf-step
$X_\red$ is a scheme.

::: pf-proof
By step [](#affine){.pf-ref}, the affine opens of $X$ give an open cover of $X_\red$ by affine schemes.
:::

:::

::: pf-step
The pair $\red = (\id_{\abs X}, \rho)$ is a morphism of schemes $X_\red \to X$ whose underlying map is a homeomorphism.

::: pf-proof
Over each affine open $U = \Spec A$, the pair $\red$ is the morphism $j$ of step [](#affine){.pf-ref}, so its stalk maps are local and $\red$ is a morphism of schemes.
Its underlying map is the identity.
:::

:::

:::

:::

::: pf-step
(c) If $X$ is reduced, every morphism $f\colon X \to Y$ factors as $f = \red \circ g$ for a unique $g\colon X \to Y_\red$.

::: pf-proof

::: {.pf-step #exist}
There is a morphism $g\colon X \to Y_\red$ with $\red \circ g = f$.

::: pf-proof
Let $g$ have the same underlying map as $f$; this is required, because $\red$ is the identity on spaces.
For an open $V \subseteq Y$, the map $f^\#_V\colon \OO_Y(V) \to \OO_X(f^{-1}V)$ lands in a reduced ring, so it factors through $\OO_Y(V)^\red$.
These factorizations form a map from the presheaf $V \mapsto \OO_Y(V)^\red$ to the sheaf $f_*\OO_X$.
By the universal property of sheafification, it factors uniquely through $\OO_Y^\red$; call the result $g^\#$.
Then $g^\# \circ \rho = f^\#$, so $\red \circ g = f$.
At $x \in X$, the map $g^\#_x\colon \OO_{Y,f(x)}^\red \to \OO_{X,x}$ is induced by the local map $f^\#_x$.
The maximal ideal of $\OO_{Y,f(x)}^\red$ is the image of the maximal ideal of $\OO_{Y,f(x)}$, so $g^\#_x$ is local and $g$ is a morphism of schemes.
:::

:::

::: pf-step
The morphism $g$ is unique.

::: pf-proof
Let $g'\colon X \to Y_\red$ satisfy $\red \circ g' = f$.
Then $g'$ has underlying map $f$, and on stalks $g'^\#_x \circ \rho_{f(x)} = f^\#_x = g^\#_x \circ \rho_{f(x)}$.
Each $\rho_{f(x)}$ is surjective, so $g'^\#_x = g^\#_x$ for all $x$.
Maps of sheaves that agree on all stalks are equal, so $g' = g$.
:::

:::

:::

:::

:::
:::
