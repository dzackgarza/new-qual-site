---
schema: qual/card@1
id: P-5RAUN
kind: problem
title: A finite simple group has no 2-dimensional irreducible complex representation
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Representation Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 7 of the Algebra Preliminary Examination 2017 (University of
    Washington), printed p. 1 of the single-page paper retained at
    assets/attachments/UW-Algebra-Qual-2017.pdf, is the statement the card answers; the paragraph
    at the head of the solution already recorded that the paper prints no solutions, and now names
    the problem and the page. Checked: the statement and its printed hint about the determinant
    against the paper's text layer at the page named; the solution read for the faithful
    representation with determinant one, the divisibility of the character degree by the group
    order, and the element of order 2 acting as minus the identity; `qualc.authoring check` on the
    card, and `tmp/lam.sh` for the numbering and the QED. Not checked: no retained solution set
    exists for this paper to compare the argument with, the mathematics of the card is not
    re-proved in this pass, and no other card of the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. The character-degree divisibility is lifted out of the middle of the
    argument into its own step, proved once for an arbitrary irreducible character of degree d
    and then applied with d = 2; the diagonalizability of rho(t) is justified by the separable
    minimal polynomial X^2 - 1; and the exclusion of a trivial representation of dimension 2 is
    stated as reducibility. Not claimed: a retained solution set; the provenance names the
    question paper, which states its own rules and carries no solutions. The statement and the
    conclusion are unchanged.
---

::: {.problem}
Show that a finite simple group cannot have a 2-dimensional irreducible representation over $\CC$.
(Hint: the determinant might prove useful.)
:::


::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/UW-Algebra-Qual-2017.pdf`, the question paper of the Algebra Preliminary Examination 2017 (University of Washington) (it opens "Do as many of the eight problems as you can", and this is Problem 7), and it contains no solutions. The argument below is the card's own; it is the card's previous prose with the character-degree divisibility made a separate step and its conclusion used in the place it is needed.

Throughout $G$ is a finite simple group, $\rho:G\to\GL(V)$ is an irreducible complex representation with $\dim_\CC V=2$, and $\cardinality{\cdot}$ denotes order.

::: pf

::: {.pf-step #faithful}
$\rho$ is faithful.

::: pf-proof
$\ker\rho$ is normal in $G$. Since $G$ is simple, $\ker\rho$ is $1$ or $G$; if it were $G$ then $\rho$ would be trivial, and a trivial representation of dimension $2$ is a direct sum of two trivial $1$-dimensional representations, hence reducible, contrary to hypothesis. So $\ker\rho=1$.

:::

:::

::: {.pf-step #det-trivial}
$\det\rho(g)=1$ for every $g\in G$.

::: pf-proof
$\det\rho:G\to\CC^\times$ is a homomorphism, so its kernel $K$ is normal. If $K=1$ then $\det\rho$ is injective and $G$ is isomorphic to a subgroup of the abelian group $\CC^\times$, hence abelian; a finite simple abelian group is cyclic of prime order, and every irreducible complex representation of an abelian group is $1$-dimensional (simultaneous eigenvectors of the commuting operators $\rho(g)$), contradicting $\dim V=2$. Simplicity of $G$ then forces $K=G$, which is the assertion.

:::

:::

::: {.pf-step #divisibility}
If $\chi$ is the character of an irreducible complex representation of a finite group $G$ of degree $d=\chi(1)$, then $d$ divides $\cardinality{G}$.

::: pf-proof
Let $C$ range over the conjugacy classes of $G$ with representatives $c$, and let $z_C=\sum_{g\in C}g\in Z(\ZZ[G])$ be the class sums, which form a $\ZZ$-basis of $Z(\ZZ[G])$. On the irreducible module, $z_C$ acts as a scalar $\omega_C$, and comparing traces on that module gives $\omega_C\chi(1)=\chi(z_C)=\cardinality{C}\chi(c)$, so $\omega_C=\cardinality{C}\chi(c)/d$. Multiplication by $z_C$ is an endomorphism of the finitely generated free abelian group $Z(\ZZ[G])$, so its matrix has integer entries and its eigenvalues — among them $\omega_C$ — are algebraic integers by Cayley–Hamilton. Character values are algebraic integers, being sums of roots of unity. Column orthogonality gives
$$
\cardinality{G}=\sum_{g\in G}\chi(g)\overline{\chi(g)}=\sum_C\cardinality{C}\chi(c)\chi(c^{-1}),
$$
so dividing by $d$,
$$
\frac{\cardinality{G}}{d}=\sum_C\frac{\cardinality{C}\chi(c)}{d}\chi(c^{-1})=\sum_C\omega_C\chi(c^{-1}),
$$
a sum of algebraic integers, hence an algebraic integer. It is rational, and a rational algebraic integer is an integer; so $d\mid\cardinality{G}$.

:::

:::

::: {.pf-step #even-order}
$2\mid\cardinality{G}$, and $G$ has an element $t$ of order $2$.

::: pf-proof
Apply step [](#divisibility){.pf-ref} to the degree $d=2$ of $\rho$. Cauchy's theorem then provides an element of order $2$, the prime $2$ dividing $\cardinality{G}$.

:::

:::

::: {.pf-step #minus-identity}
$\rho(t)=-I$.

::: pf-proof
$\rho(t)^2=\rho(t^2)=I$, so the minimal polynomial of $\rho(t)$ divides $X^2-1$, which has distinct roots; hence $\rho(t)$ is diagonalizable with eigenvalues in $\theset{1,-1}$. Its determinant is $1$ by step [](#det-trivial){.pf-ref}, so the two eigenvalues are both $1$ or both $-1$, that is $\rho(t)=I$ or $\rho(t)=-I$. Faithfulness of $\rho$ and $t\ne1$ exclude $\rho(t)=I$.

:::

:::

::: {.pf-step #central}
$t\in Z(G)$, so $G$ is abelian, a contradiction.

::: pf-proof
$\rho(t)=-I$ commutes with $\rho(g)$ for every $g\in G$, and $\rho$ is faithful and a homomorphism, so $t$ commutes with every $g\in G$ and $t\in Z(G)\setminus\theset1$. Then $Z(G)$ is a nontrivial normal subgroup, and simplicity forces $Z(G)=G$, so $G$ is abelian. But then $\rho$ is $1$-dimensional, as in step [](#det-trivial){.pf-ref}, contradicting $\dim V=2$.

:::

:::

::: {.pf-step #conclusion}
A finite simple group has no $2$-dimensional irreducible complex representation.

::: pf-proof
The assumption of such a representation produced the contradiction of step [](#central){.pf-ref}; the argument used only simplicity, finiteness and $\dim V=2$.

:::

:::

:::
:::
