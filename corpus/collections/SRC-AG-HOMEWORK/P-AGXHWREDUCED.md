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
:::
