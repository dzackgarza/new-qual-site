---
schema: qual/card@1
id: P-AGH332COMPONENTAFFINE
kind: problem
title: Affineness is detected on irreducible components
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Affine Schemes
  - Serre Criterion
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the complete statement with the retained Hartshorne Chapter III section 3 transcription. The proof inducts on the finite component set and uses the product-zero relation between the two reduced-union ideals to filter an arbitrary coherent sheaf into sheaves on affine closed subschemes.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a reduced noetherian scheme.
Show that $X$ is affine if and only if each irreducible component is affine.
:::

::: {.solution}
Every irreducible component is given its reduced induced closed-subscheme structure.
The noetherian scheme has finitely many irreducible components.
We use [[T-5IOUR|Serre's affineness criterion]] and [[T-COHAFF|vanishing of higher quasi-coherent cohomology on affine schemes]] [@Har10a, Theorems III.3.5 and III.3.7].

::: pf

::: {.pf-step #s1}

If $X$ is affine, each irreducible component is affine.

::: pf-proof

For $X=\Spec A$, an irreducible component has reduced coordinate ring $A/\mathfrak p$, where $\mathfrak p$ is a minimal prime of $A$.
It is the affine closed subscheme $\Spec(A/\mathfrak p)$.

:::

:::

::: {.pf-step #s2}

Suppose $X=Y\cup Z$ is a union of two reduced closed subschemes and $X$ is reduced.
If $Y$ and $Z$ are affine, then $H^1(X,F)=0$ for every coherent sheaf $F$ on $X$.

::: pf-proof

Let $I$ and $J$ be the coherent ideal sheaves defining $Y$ and $Z$.
Their intersection is zero.
Indeed, on any affine open $\Spec A\subseteq X$, the ring $A$ is reduced, the ideals defining $Y$ and $Z$ are radical, and their zero sets cover $\Spec A$.
The intersection of those ideals is radical with zero set all of $\Spec A$, hence is the nilradical $0$.
In particular $IJ=0$ as ideal sheaves.

For a coherent $F$, use the exact sequence
$$
0\longrightarrow IF\longrightarrow F\longrightarrow F/IF\longrightarrow0.
$$
The quotient $F/IF$ is annihilated by $I$, so it is the direct image of a coherent sheaf on $Y$.
The subsheaf $IF$ is annihilated by $J$, since $J(IF)=(JI)F=0$, so it is the direct image of a coherent sheaf on $Z$.
These assertions follow locally from the correspondence between modules annihilated by an ideal and modules over the quotient ring; all these sheaves are coherent because $X$ is noetherian.

Cohomology of a sheaf on a closed subspace agrees with cohomology of its direct image [@Har10a, Lemma III.2.10].
Affineness of $Y$ and $Z$ therefore gives
$$
H^1(X,IF)=0,\qquad H^1(X,F/IF)=0.
$$
The long exact sequence of the displayed short exact sequence forces $H^1(X,F)=0$.

:::

:::

::: {.pf-step #s3}

If every irreducible component is affine, then $X$ is affine.

::: pf-proof

Induct on the number $r$ of irreducible components.
For $r=0$, the scheme is empty and is $\Spec(0)$.
For $r=1$, reducedness identifies $X$ with its sole reduced component, which is affine by hypothesis.

For $r>1$, take $Y$ to be one component and let $Z$ be the union of the other $r-1$ components, with its reduced induced structure.
The scheme $Z$ is reduced and noetherian, and its irreducible components, with their reduced structures, are precisely the remaining components of $X$.
They are affine by hypothesis, so induction gives affineness of $Z$.
The chosen $Y$ is affine as well.
Step [](#s2){.pf-ref} gives $H^1(X,F)=0$ for every coherent $F$, in particular for every coherent ideal sheaf.
Serre's criterion therefore makes $X$ affine.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the forward implication and step [](#s3){.pf-ref} proves the converse.

:::

:::

:::
