---
schema: qual/card@1
id: D-COHFLQ
kind: definition
title: Flasque sheaves and acyclicity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Flasque Sheaves
  - Acyclic Resolutions
relations:
- kind: uses
  target: D-COHDER
review: draft
---

::: {.definition}
$\mcf$ is \dfn{flasque}, or \dfn{flabby}, if every restriction $\mcf(U) \to \mcf(V)$, for $V \subseteq U$, is surjective.
:::

::: {.proposition}
Injective implies flasque, flasque implies $\globsec{X;-}\dash$acyclic, and for a short exact sequence with flasque left term the sequence of global sections stays exact.
:::

::: {.proof}
**(1) An injective sheaf is flasque.**
Let $(X,\OO_X)$ be a ringed space and $\mci$ an injective $\OO_X$-module; a sheaf of abelian groups on $X$ is the case $\OO_X=\ZZ$.
For open $U\subseteq X$ let $\OO_U \coloneqq j_!(\restrictionof{\OO_X}{U})$ be the extension by zero of the restricted structure sheaf [@Har77, Exercise II.1.19].
A homomorphism $\OO_U\to\mci$ is determined by its value on the unit section, so evaluation of that section is a bijection
$$
\Hom_{\OO_X}(\OO_U,\mci)\cong \Gamma(U,\mci)=\mci(U).
$$
For $V\subseteq U$ the extension by zero of the identity of $\OO_V$ is a monomorphism $\OO_V\injects\OO_U$. Injectivity of $\mci$ makes the induced map
$$
\Hom_{\OO_X}(\OO_U,\mci)\surjects\Hom_{\OO_X}(\OO_V,\mci)
$$
surjective, and under the two identifications this map is the restriction $\mci(U)\to\mci(V)$. Every restriction of $\mci$ is therefore surjective, that is, $\mci$ is flasque [@Har77, Lemma III.2.4].

**(2) A flasque sheaf is acyclic for the global-section functor.**
Let $\mcf$ be flasque. Embed $\mcf$ in an injective $\mci$, which exists because sheaves of abelian groups on $X$ have enough injectives [@Har77, Corollary III.2.3], and let $\mcg\coloneqq\mci/\mcf$, so that
$$
0\to\mcf\to\mci\to\mcg\to0
$$
is exact. By (1) $\mci$ is flasque, and $\mcf$ is flasque by hypothesis, so $\mcg$ is flasque [@Har77, Exercise II.1.16(c)].

Flasqueness of $\mcf$ makes the sequence of global sections exact [@Har77, Exercise II.1.16(b)], so that $\Gamma(X,\mci)\surjects\Gamma(X,\mcg)$. An injective object is acyclic [@Har77, Theorem III.1.1A(e)], so $H^i(X,\mci)=0$ for every $i>0$; the long exact sequence of the short exact sequence [@Har77, Theorem III.1.1A(c)] is therefore
$$
\Gamma(X,\mci)\surjects\Gamma(X,\mcg)\to H^1(X,\mcf)\to H^1(X,\mci)=0
$$
in low degree and
$$
H^{i-1}(X,\mci)=0\to H^{i-1}(X,\mcg)\to H^i(X,\mcf)\to H^i(X,\mci)=0
$$
for $i\geq2$, where the outer terms vanish because $\mci$ is injective. The first sequence gives $H^1(X,\mcf)=0$; the second gives $H^i(X,\mcf)\cong H^{i-1}(X,\mcg)$ for $i\geq2$. Since $\mcg$ is flasque, induction on $i$ gives $H^i(X,\mcf)=0$ for every $i>0$, that is, $\mcf$ is $\globsec{X;-}$-acyclic ([[D-DEFACYC]]); consequently a flasque resolution computes $H^i(X,\mcf)$ [@Har77, Proposition III.1.2A].

**(3) The sections of a short exact sequence with flasque left term stay exact.**
Let $0\to\mcf'\to\mcf\to\mcf''\to0$ be exact with $\mcf'$ flasque and let $U\subseteq X$ be open. The global-section functor is left exact, so
$$
0\to\mcf'(U)\to\mcf(U)\to\mcf''(U)
$$
is exact; the content of the clause is that the last map is onto [@Har77, Exercise II.1.16(b)], and its proof is the maximal-extension argument written on [[P-AGH2116FLASQUE]]: a section of $\mcf''$ over $U$ lifts on a neighbourhood of each point because $\mcf\to\mcf''$ is onto on stalks, two lifts over opens meeting $U$ differ there by a section of $\mcf'$, flasqueness of $\mcf'$ extends that difference from the overlap to the larger open, and subtracting it makes the two lifts agree on the overlap, so they glue over a strictly larger open. Zorn's lemma gives a lift over $U$.
:::

::: {.remark}
Every sheaf $\mcf$ embeds in the flasque sheaf $\prod_x j^x_* \mcf_x$ of discontinuous sections [@Har77, Exercise II.1.16(e)], so every sheaf has a resolution by $\globsec{X;-}$-acyclic sheaves by (2), and that resolution computes the cohomology of $\mcf$ [@Har77, Remark III.2.5.1].
:::

::: {.example title="Flasque sheaves"}
The following sheaves are flasque:

- the sheaf $\prod_x j^x_* \mcf_x$ of discontinuous sections of any sheaf $\mcf$, where $j^x\colon\theset{x}\injects X$;

- every constant sheaf on an irreducible topological space [@Har77, Exercise II.1.16(a)];

- the sheaf $\tilde{I}$ on $\Spec A$ for a Noetherian ring $A$ and an injective $A\dash$module $I$ [@Har77, Proposition III.3.4]; Hartshorne uses this to prove that $H^i(\Spec A,\tilde M)=0$ for $i>0$ [@Har77, Theorem III.3.5].
:::
