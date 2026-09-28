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
Call $(X, \OO_X)\in \Sch$ **reduced** iff $\OO_X(U)$ has no nilpotents for every open $U$, and for $A\in \Ring$ define $A^{\red}\da A/\sqrt{0}$ to be $A$ modulo its ideal of nilpotents.

a. Show that $X$ is reduced iff for every $p\in X$, the local ring $\OO_{X, p}$ has no nilpotents.

b. Let $\OO_X^{\red}$ be the sheafification of $U \mapsto \OO_X(U)^{\red}$.
Show that $X_{\red}\da (X, \OO_X^{\red})$ is a scheme, and that there is a morphism of schemes $X_{\red}\xrightarrow{\red} X$ inducing a homeomorphism $\abs{X_{\red}}\to \abs{X}$ on underlying topological spaces.

c. Let $X \xrightarrow{f} Y\in \Sch$ with $X$ reduced.
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

- $R_{\red}\da R/\sqrt{0_{R}}$ is a quotient, and localization commutes with quotients.

- Maps $R\to S$ with $S$ reduced factor through $R_{\red}$.

- Sheafification has the same stalks, and an isomorphism on stalks is an isomorphism of sheaves.

- Pushforwards of reduced sheaves are reduced.
:::

::: {.solution}
**Part (a).**

$\implies$: suppose $X$ is reduced and $\OO_{X, p}$ has a nonzero nilpotent germ $s_p$ with $s_p^n = 0$.
Represent $s_p$ by $s\in\OO_X(U)$ for an open $U\ni p$; since $s^n$ has zero germ at $p$, shrinking $U$ gives $s^n = 0 \in \OO_X(U)$, while $s\neq 0$ because its germ is nonzero. So $s$ is a nonzero nilpotent in $\OO_X(U)$, a contradiction.

$\impliedby$: suppose every $\OO_{X,p}$ is reduced, and let $s\in \OO_X(U)$ with $s^n=0$. For each $p\in U$ the germ $s_p$ satisfies $s_p^n = 0$ in $\OO_{X,p}$, so $s_p=0$. A section whose germs all vanish is zero by the sheaf axiom, so $s = 0$.

**Part (b).** Let $P$ be the presheaf $U\mapsto\OO_X(U)^\red$, so $\OO_X^\red$ is its sheafification, and let $\rho\colon\OO_X\to\OO_X^\red$ be the quotient maps followed by sheafification. Stalks commute with quotients by the nilradical, so $P_p=\OO_{X,p}^\red=(\OO_X^\red)_p$.

Let $U=\Spec A$ be an affine open of $X$ and $j\colon\Spec A^\red\to\Spec A$ the morphism induced by $A\to A^\red$. Every prime contains $\sqrt0$, so $j$ is a homeomorphism; identify the two spaces. For an open $V\subseteq U$, the map $\OO_U(V)\to\OO_{\Spec A^\red}(V)$ lands in a reduced ring, so it factors through $P(V)$; this is a map of presheaves $\ro{P}{U}\to\OO_{\Spec A^\red}$. On the stalk at $\mfp$ it is $(A_\mfp)^\red\to(A^\red)_{\mfp}$, an isomorphism because localization commutes with quotients and $\sqrt{0_{A_\mfp}}=(\sqrt{0_A})_\mfp$. The induced map $\ro{\OO_X^\red}{U}\to\OO_{\Spec A^\red}$ is therefore an isomorphism of sheaves. So $X_\red$ is covered by open sets isomorphic to affine schemes, and it is a scheme.

Let $\red\colon X_\red\to X$ be the identity on spaces with $\red^\#\da\rho$. Over each affine $U=\Spec A$ it is $j$, a morphism of schemes, so $\red$ is a morphism of schemes, and its underlying map is the identity, a homeomorphism.

**Part (c).** Let $f\colon X\to Y$ with $X$ reduced, and let $g$ have the same underlying map as $f$, which is possible since $\red$ is the identity on spaces.

For an open $V\subseteq Y$, $f^\#_V\colon\OO_Y(V)\to\OO_X(f^{-1}V)$ lands in a reduced ring, so it kills the nilpotents and factors through $\OO_Y(V)^\red$. These factorizations form a map of presheaves from $U\mapsto\OO_Y(U)^\red$ to the sheaf $f_*\OO_X$, which by the universal property of sheafification factors uniquely through $\OO_Y^\red$; call the result $g^\#$. Then $\red\circ g=f$. On the stalk at $x\in X$, $g^\#_x\colon\OO_{Y,f(x)}^\red\to\OO_{X,x}$ is induced by the local map $f^\#_x$, and the maximal ideal of $\OO_{Y,f(x)}^\red$ is the image of that of $\OO_{Y,f(x)}$, so $g^\#_x$ is local and $g$ is a morphism of schemes.

For uniqueness, a morphism $g'$ with $\red\circ g'=f$ has underlying map $f$, and on stalks $g'^\#_x\circ\rho_{f(x)}=f^\#_x$. Each $\rho_{f(x)}$ is surjective, so the stalk maps of $g'^\#$ agree with those of $g^\#$, and $g'=g$.
:::
