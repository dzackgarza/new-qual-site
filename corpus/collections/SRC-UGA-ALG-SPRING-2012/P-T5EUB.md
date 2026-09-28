---
schema: qual/card@1
id: P-T5EUB
kind: problem
title: A normal $p$-subgroup lies in every Sylow $p$-subgroup, and $G$ has a nontrivial
  abelian normal subgroup of order divisible by $p$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and $p$ a prime number such that there is a normal subgroup $H\normal G$ with $\abs{H} = p^i > 1$.

a.
Show that $H$ is a subgroup of any Sylow $p\dash$subgroup of $G$.

b.
Show that $G$ contains a nonzero abelian normal subgroup of order divisible by $p$.
:::

::: {.concept}
\envlist

- $p$ groups have nontrivial centers.

- Definition of maximality and $p\dash$groups

- Sylows are conjugate

- $Z(G) \ch G$ always.

- Transitivity of characteristic: $A \ch B$ and $B\normal C$ implies $A \normal C$.
:::

::: {.strategy}
Just use maximality for (a). For (b), centers are always abelian, so $Z(H)$ is good to consider, just need to ensure it's normal in $G$.
Use transitivity of characteristic.
:::

::: {.solution}
\envlist

::: {.proof title="of a"}
\envlist

- By definition, $S\in \Syl_p(G) \iff S$ is a *maximal* $p\dash$subgroup: $S<G$ is a $p\dash$group, so $\size S = p^k$ for some $k$, $S$ is a proper subgroup, and $S$ is maximal in the sense that there are no proper $p\dash$subgroups $S'$ with $S \subseteq S' \subseteq G$.

- Since $\size H = p^i$, $H$ is a $p\dash$subgroup of $G$.

- If $H$ is maximal, then by definition $H\in \Syl_p(G)$

- Otherwise, if $H$ is not maximal, there exists an $H' \supseteq H$ with $H'\leq G$ a $p\dash$subgroup properly containing $H$.

  - In this apply the same argument to $H'$: this yields a proper superset containment at every stage, and since $G$ is finite, there is no infinite ascending chain of proper supersets.

  - So this terminates in some maximal $p\dash$subgroup $S$, i.e. a Sylow $p\dash$subgroup.

- So $H \subseteq S$ for some $S\in \Syl_p(G)$.

- All Sylows are conjugate, so for any $S' \in \Syl_p(G)$ we can write $S' = gS\inverseof{g}$ for some $g$.

- Then using that $H$ is normal, $H \subseteq S \implies H = gH\inverseof{g} \subseteq gS\inverseof{g} \da S'$.
  So $H$ is contained in every Sylow $p\dash$subgroup.

:::

::: {.proof title="of b"}
\envlist

- Claim: $Z(H) \leq H$ works.

  - It is nontrivial since $H$ is a $p\dash$group and $p\dash$groups have nontrivial centers

  - It is abelian since $Z(Z(H)) = Z(H)$.

  - $\size Z(H) = p^\ell$ for some $\ell \leq i$ by Lagrange

- It thus remains to show that $Z(H) \normal G$.

- Use that $Z(H) \ch H$ and use transitivity of characteristic to conclude $Z(H) \normal H$.

- That $Z(H) \ch H$: let $\psi \in \Aut(H)$ and $x=\psi(y)\in \psi(Z(H))$ so $y\in Z(H)$, then for arbitrary $h\in H$,
 \[
 \psi(y)h 
 &= \psi(y) (\psi \circ \inverseof{\psi})(h) \\
 &= \psi( y \cdot \inverseof{\psi}(h) ) \\
 &= \psi( \inverseof{\psi}(h) \cdot y ) && \text{since } \inverseof{\psi}(h)\in H, \, y\in Z(H) \\
 &= h\psi(y)
 .\]

- That $A \ch B \normal C \implies A\normal C$:

  - $A\ch B$ iff $A$ is fixed by every $\psi\in \Aut(B)$., WTS $cA\inverseof{c} = A$ for all $c\in C$.

  - Since $B\normal C$, the automorphism $\psi(\wait) \da c(\wait)\inverseof{c}$ descends to an element of $\Aut(B)$.

  - Then $\psi(A) = A$ since $A\ch B$, so $cA\inverseof{c} = A$ and $A\normal C$.
:::

:::
