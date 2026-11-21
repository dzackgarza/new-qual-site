---
schema: qual/card@1
id: P-APAS24E
kind: problem
title: Schur's lemma for complex representations of finite groups
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 5 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p.
    5 of the paper's own numbered pages, is the statement the card answers, and the head of the solution
    names it; the file retained at assets/attachments/SP24_math_202_exam.pdf puts a cover page before
    those pages, so paper p. 5 is its page 6. Checked: the statement against the paper's text layer at
    the page named; the statement and both parts of Schur's lemma for complex finite-dimensional
    representations; `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering and the
    QED. Not checked: no retained solution set exists for this paper to compare the argument with, and
    no other card of the collection in this pass.
---

::: {.problem}
Give a complete statement and proof of Schur's Lemma, in the category of complex finite-dimensional representations of finite groups.
:::

::: {.solution}

The problem is Problem 5 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p. 5 of the paper's numbered pages — the retained file `assets/attachments/SP24_math_202_exam.pdf` puts a cover page before them.

The argument is the card's own; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

**Schur's Lemma.** Let $V$ and $W$ be finite-dimensional irreducible complex representations of a finite group $G$, and let $\Hom_{G}(V,W)$ denote the $G$-equivariant linear maps.

(a) Every $T\in\Hom_{G}(V,W)$ is either $0$ or an isomorphism.

(b) Every $T\in\Hom_{G}(V,V)$ is multiplication by a scalar.

::: pf

::: {.pf-step #part-a}
(a) Every $T\in\Hom_{G}(V,W)$ is $0$ or an isomorphism.

::: pf-proof

::: {.pf-step #stable}
$\ker T$ is a $G$-stable subspace of $V$, and $\operatorname{im}T$ is a $G$-stable subspace of $W$.

::: pf-proof
For $v\in\ker T$ and $g\in G$, equivariance gives $T(g\cdot v)=g\cdot T(v)=0$, so $g\cdot v\in\ker T$; for $w=T(v)\in\operatorname{im}T$, one has $g\cdot w=g\cdot T(v)=T(g\cdot v)\in\operatorname{im}T$.
:::

:::

::: {.pf-qed}
$V$ is irreducible, so the $G$-stable subspace $\ker T$ is $0$ or $V$; $W$ is irreducible, so the $G$-stable subspace $\operatorname{im}T$ is $0$ or $W$. If $T\ne0$ then $\operatorname{im}T\ne0$, hence $\operatorname{im}T=W$, and $\ker T\ne V$, hence $\ker T=0$; so $T$ is bijective, that is an isomorphism. If $T=0$ the first alternative holds.
:::

:::

:::

::: {.pf-step #part-b}
(b) Every $T\in\Hom_{G}(V,V)$ satisfies $T=\lambda I$ for some $\lambda\in\CC$.

::: pf-proof
Since $V$ is a finite-dimensional complex vector space and $T$ is a complex-linear endomorphism, $T$ has an eigenvalue $\lambda\in\CC$ (the characteristic polynomial has a root over $\CC$). The map $T-\lambda I$ is $G$-equivariant, being a $\CC$-linear combination of equivariant maps, and it has nonzero kernel, since an eigenvector lies in it. By step [](#part-a){.pf-ref} applied with $W=V$, an equivariant endomorphism that is not an isomorphism must be $0$; so $T-\lambda I=0$ and $T=\lambda I$. Hence
$$
\boxed{\Endo_{G}(V)=\CC I.}
$$
:::

:::

:::
:::
