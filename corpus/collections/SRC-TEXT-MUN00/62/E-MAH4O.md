---
schema: qual/card@1
id: E-MAH4O
kind: problem
title: The inclusion of a curve in the punctured plane is trivial off its interior
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 4, printed p. 384. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. Both directions are the book's own two lemmas, one
    each way round: if 0 lies in the unbounded component then the inclusion is nullhomotopic by Lemma 61.2, the
    nulhomotopy lemma (printed p. 377), whose statement at the top of p. 378 is exactly "A compact, g: A -> R^2 -
    0, 0 in the unbounded component of R^2 - g(A) implies g nullhomotopic"; and if 0 lies in a bounded
    component then the inclusion is not nullhomotopic by the contrapositive of Lemma 62.2, the Borsuk lemma
    (printed p. 382). The card's earlier version proved the first direction through a polygonal ray and invoked
    a straightening of the ray by a homeomorphism of the plane, which the book does not prove; that borrowed step
    is gone. The definition of "separates" is the one on printed p. 378.
---

::: {.exercise}

Let $C$ be a simple closed curve in $\RR^2 - 0$; let $j: C \to \RR^2 - 0$ be the inclusion mapping.
Show that $j_*$ is trivial if $0$ lies in the unbounded component of $\RR^2 - C$, and is nontrivial otherwise.
(In fact, $j_*$ is an isomorphism in the latter case, as we shall prove in §65.)
:::

::: {.solution}

$C$ is the image of $S^1$ under an imbedding, hence compact. As in Lemma 61.2 (printed p. 377), identify $\RR^2\cup\theset{\infty}$ with $S^2$ and take the two punctures to be $0$ and $\infty$; the components of $\RR^2-C$ are the components of $S^2-C$ other than the one containing $\infty$ (Lemma 61.1, printed p. 377).

::: pf

::: pf-step

If $0$ lies in the unbounded component of $\RR^2-C$, then $j$ is nullhomotopic and $j_*$ is trivial.

::: pf-proof

Apply Lemma 61.2 (nulhomotopy lemma, printed pp. 377--378) with $A=C$ and $g=j$. Its hypothesis is that $0$ and $\infty$ lie in the same component of $S^2-C$, which is exactly the hypothesis that $0$ lies in the unbounded component of $\RR^2-C$; its conclusion is that $j:C\to\RR^2-\theset{0}$ is nullhomotopic. A map inducing a homomorphism of fundamental groups is trivial when it is nullhomotopic, so $j_*$ is trivial.

:::

:::

::: pf-step

If $0$ lies in a bounded component of $\RR^2-C$, then $j$ is not nullhomotopic and $j_*$ is nontrivial.

::: pf-proof

Then $0$ and $\infty$ lie in different components of $S^2-C$. The map $j:C\to S^2-\theset{0,\infty}$ is continuous and injective, and $C$ is compact. If $j$ were nullhomotopic, Lemma 62.2 (the Borsuk lemma, printed p. 382) would put $0$ and $\infty$ in the same component of $S^2-j(C)=S^2-C$, contrary to the choice of the component. So $j$ is not nullhomotopic. A homeomorphism $\gamma:S^1\to C$ exists, and $j_*$ sends the class of $\gamma$ to the class of the loop $j\circ\gamma$, which is the class represented by $j$; since $j$ is not nullhomotopic, that class is not the identity.

:::

:::

::: pf-qed

Steps 1 and 2 are the two assertions.

:::

:::
:::
