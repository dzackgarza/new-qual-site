---
schema: qual/card@1
id: P-AGH2612DEGSHEAF
kind: problem
title: Degree of a coherent sheaf on a complete nonsingular curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coherent Sheaves
  - Degree
  - Torsion Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three degree requirements with the retained Hartshorne II.6.12 transcription. Made the algebraically closed field convention explicit, constructed degree from the determinant homomorphism proved in II.6.11, and proved uniqueness on the entire coherent-sheaf Grothendieck group.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a complete nonsingular curve over an algebraically closed field $k$.
Show that there is a unique way to define the degree of any coherent sheaf on $X$, $\deg \mcf \in \ZZ$, such that

(a) if $D$ is a divisor, then $\deg \mcl(D) = \deg D$;

(b) if $\mcf$ is a torsion sheaf, meaning a sheaf whose stalk at the generic point is zero, then $\deg \mcf = \sum_{P \in X} \length(\mcf_P)$;

(c) if $0 \to \mcf' \to \mcf \to \mcf'' \to 0$ is exact, then $\deg \mcf = \deg \mcf' + \deg \mcf''$.
:::

::: {.solution}
Write $\gamma(\mathcal F)$ for the class of a coherent sheaf in the group $K(X)$ of [[P-AGH2610KGROUP]].
For a divisor $D$, put $\OO_X(D)=\mathcal L(D)$ and $\psi(D)=\sum_P n_P\gamma(k(P))$ when $D=\sum_P n_PP$.
The [[P-AGH2611KCURVE|determinant homomorphism]] is denoted by $\det:K(X)\to\Pic(X)$.

<1>1. The degree of divisors induces a homomorphism $d:\Pic(X)\to\ZZ$ with $d([\OO_X(D)])=\deg D$.

::: {.proof}
Every principal divisor on the complete nonsingular curve has degree zero [@Har10a, Proposition II.6.10].
Thus the additive map $D=\sum_P n_PP\mapsto\sum_P n_P$ descends to $\Cl(X)$.
The [[D-5PQ5W|Cartier and Weil comparison]] identifies $\Cl(X)$ with $\Pic(X)$ by $[D]\mapsto[\OO_X(D)]$ [@Har10a, Corollary II.6.16].
Transporting degree through this isomorphism gives $d$.
In particular, $d([\OO_X])=0$.
:::

<1>2. Define the degree of a coherent sheaf by
$$
\boxed{\deg\mathcal F\coloneqq d\bigl(\det(\gamma(\mathcal F))\bigr).}
$$
This satisfies (a) and (c).

::: {.proof}
For an invertible sheaf $\OO_X(D)$, its determinant class is $[\OO_X(D)]$, so step <1>1 gives condition (a).
For a short exact sequence of coherent sheaves, the defining relation in $K(X)$ is
$$
\gamma(\mathcal F)=\gamma(\mathcal F')+\gamma(\mathcal F'').
$$
Both determinant and $d$ are homomorphisms, by [[P-AGH2611KCURVE]], step <1>5, and step <1>1 of this proof.
Their composite is additive, proving (c).
:::

<1>3. The degree in step <1>2 satisfies the torsion formula (b).

::: {.proof}
A coherent torsion sheaf $\mathcal T$ has finite support and finite-length stalks at its supporting closed points.
Its class is
$$
\gamma(\mathcal T)=\sum_P\ell_P\gamma(k(P)),
\qquad\ell_P=\operatorname{length}_{\OO_{X,P}}(\mathcal T_P),
$$
by [[P-AGH2611KCURVE]], step <1>1.
The same card's step <1>5 gives $\det(\gamma(k(P)))=[\OO_X(P)]$.
Every closed point has degree one because $k$ is algebraically closed.
Applying $d\circ\det$ therefore gives $\deg\mathcal T=\sum_P\ell_P$, as required.
:::

<1>4. Any degree assignment satisfying (a) and (c) equals the assignment in step <1>2; in particular, all three requirements determine it uniquely.

::: {.proof}
Let $\delta$ be such an assignment.
Condition (c) applied to the zero sequence gives $\delta(0)=0$; applied to a sheaf isomorphism regarded as a short exact sequence, it gives invariance under isomorphism.
It therefore induces a homomorphism $\bar\delta:K(X)\to\ZZ$.
Condition (a) gives $\bar\delta(\gamma(\OO_X))=0$.
For every divisor $D$, [[P-AGH2611KCURVE]], step <1>2, gives
$$
\psi(D)=\gamma(\OO_X(D))-\gamma(\OO_X),
\qquad \bar\delta(\psi(D))=\deg D.
$$
The isomorphism in step <1>7 of that card says that every element of $K(X)$ is of the form $\psi(D)+n\gamma(\OO_X)$.
Thus $\bar\delta$ is determined on a generating set and agrees there with $d\circ\det$.
The homomorphisms, and hence the degree assignments, coincide.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 construct a degree satisfying all three requirements, and step <1>4 proves uniqueness.
:::
:::
