---
schema: qual/card@1
id: D-SCHIMG
kind: definition
title: The scheme-theoretic image of a morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subschemes
  - Morphisms Of Schemes
  - Ideal Sheaves
relations:
- kind: uses
  target: D-SCHSUB
- kind: uses
  target: D-SCHRED
review: draft
prompts:
- What is the scheme-theoretic image of a morphism?
- Which topological properties can the set-theoretic image of a morphism fail to have?
- What is the scheme-theoretic closure of a locally closed subscheme?
---

::: {.definition}
For $f: X \to Y$, the image of $f$ \dfn{lies in} a closed subscheme $Z \subseteq Y$ with ideal sheaf $\mci_Z$ if the composite $\mci_Z \to \OO_Y \to f_* \OO_X$ is zero, equivalently if $f$ factors through $Z$.
The \dfn{scheme-theoretic image} of $f$ is the smallest closed subscheme of $Y$ in which the image of $f$ lies, the intersection of all such $Z$.
When $\mci \coloneqq \ker(\OO_Y \to f_* \OO_X)$ is quasicoherent — for instance when $f$ is quasicompact and quasiseparated — this ideal sheaf defines it.
:::

::: {.definition title="Constructible set"}
In a Noetherian topological space $X$, the \dfn{constructible} subsets form the smallest family of subsets containing every open set and closed under finite intersections and complements.
A subset of $X$ is constructible if and only if it is a finite disjoint union of locally closed subsets.
[@Har77, Exercise II.3.18]
:::

::: {.definition title="Scheme-theoretic closure"}
The \dfn{scheme-theoretic closure} of a locally closed immersion $i \colon X \to Y$ is the scheme-theoretic image of $i$.
:::

::: {.proposition}
If $X$ is reduced, the scheme-theoretic image is $\closure{f(X)}$ with its reduced induced structure.
For $f: \Spec B \to \Spec A$ induced by $\varphi: A \to B$, the image is $\Spec(A/\ker \varphi)$.
:::

::: {.remark}
The set-theoretic image of a morphism need not be closed, open, or locally closed: $\AA^2 \to \AA^2$, $(x,y) \mapsto (x, xy)$, has image the plane minus the $y$-axis, together with the origin.
By Chevalley's theorem, the image of a constructible set under a finite-type morphism of Noetherian schemes is constructible.

The scheme-theoretic image of the morphism $\Spec k[\varepsilon]/\varepsilon^2 \to \AA^1$ given by $t\mapsto\varepsilon$ is the double point $V(t^2)$, because the kernel of $k[t] \to k[\varepsilon]/\varepsilon^2$ is $(t^2)$.
The closure of its set-theoretic image, with the reduced induced structure, is the reduced point $V(t)$.
The implication of the proposition is one-way: the morphism $\Spec k[\varepsilon]/\varepsilon^2 \to \Spec k$ has scheme-theoretic image $\Spec k$, which is reduced although the source is not, so a nonreduced source need not produce a nonreduced image.

A global example exists on every elliptic curve $E$ over a field $k$ of characteristic $2$: $\alpha_2\coloneqq\ker(F_{E/k}\colon E\to E^{(2)})$ is a closed subgroup scheme of $E$, isomorphic as a scheme to $\Spec k[\varepsilon]/(\varepsilon^2)$ and supported at the single reduced point $O$.
Indeed, in the chart at $O$ of a Weierstrass equation, put $u=x/y$ and $v=1/y$; the equation becomes
$$v(1+a_1u+a_3v-a_2u^2-a_4uv-a_6v^2)=u^3 .$$
The parenthesis is a unit, so $\widehat{\OO}_{E,O}=k[[u]]$ with $v\in u^3k[[u]]$; relative Frobenius pulls back the corresponding coordinate on $E^{(2)}$ to $u^2$, so the kernel has ideal $(u^2)$.
For the explicit supersingular curve $y^2+y=x^3$ over $\FF_2$, the displayed equation is $v(1+v)=u^3$.
The class of $u$ is thus a nonzero global nilpotent on $\alpha_2$, while its reduction is $\Spec k$.
After every field extension $K/k$, $(\alpha_2)_K=\Spec K[\varepsilon]/(\varepsilon^2)$ still has a nonzero global nilpotent and one reduced support point; taking $D=\Spec k[\delta]/(\delta^2)$ gives $\alpha_2\times_kD=\Spec k[\delta,\varepsilon]/(\delta^2,\varepsilon^2)$ inside $E\times_kD$, again with nonzero global nilpotents and reduction $\Spec k$.

Multiplicity in a fibre is a separate assertion from multiplicity in the image, and it is not decided by reducedness of the source either.
For $\Spec k[s,t]/(s-t^2) \to \Spec k[s]$ over an algebraically closed field $k$ with $\operatorname{char}k\neq2$, the fibre over $s=a\neq0$ is two reduced points with residue field $k$, while the fibre over $s=0$ is the nonreduced one-point scheme $\Spec k[\varepsilon]/\varepsilon^2$ [@Har77, Exercise II.3.10, whose two-point assertion needs $\operatorname{char}k\neq2$].
If $\operatorname{char}k=2$, algebraic closedness makes $a=r^2$ for a unique $r\in k$, and the fibre over $s=a$ is $\Spec k[t]/((t-r)^2)$ instead: it has one reduced support point and the nonzero nilpotent $t-r$.
In every characteristic, every closed fibre has length $2$, the degree of the finite flat morphism, so constant fibre length does not force the fibres to be reduced.
:::
