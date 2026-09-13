---
schema: qual/card@1
id: T-DEFNAKA
kind: theorem
title: Nakayama's lemma, in its several forms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Nakayama's Lemma
  - Local Rings
relations:
- kind: uses
  target: D-DEFNOETH
review: draft
prompts:
- State Nakayama's lemma.
- Over a local ring, how do you produce a minimal generating set of a finitely generated module?
- Where does finite generation get used, and what goes wrong without it?
---

::: {.theorem title="Nakayama's lemma"}
Let $A$ be a ring, $I$ an ideal, and $M$ an $A$-module.

(i) If $M$ is finitely generated and $M = IM$, there exists $a \equiv 1 \pmod I$ with $aM = 0$.

(ii) If in addition $I \subseteq \Jac A$, then $M = 0$.

(iii) If $I \subseteq \Jac A$, $M$ is finitely generated and $N \subseteq M$ is a submodule such that $N/IN \to M/IM$ is surjective, then $M = N$.

(iv) If $(A,\mm)$ is local, $M$ is finitely generated, and $f_1,\ldots,f_n \in M$ have images generating $M/\mm M$ as an $A/\mm$-vector space, then the $f_i$ generate $M$ as an $A$-module.
:::

::: {.remark}
Part (i) is the determinant trick: writing $m_i = \sum_j a_{ij}m_j$ with $a_{ij}\in I$ says $\id - (a_{ij})$ kills $M$, and multiplying by the adjugate shows $\det(\id - (a_{ij}))$ does too, an element congruent to $1$ modulo $I$.
Part (ii) follows because such an $a$ lies in no maximal ideal, hence is a unit.
Part (iii) applies (ii) to the cokernel $L$ of $N \injects M$, using right exactness of $\wait\tensor A/I$ to get $L = IL$.
Part (iv) is (iii) with $N = \generators{f_1,\ldots,f_n}$ and $I = \mm$.

Form (iv) is the one used constantly: over a local ring a minimal generating set of $M$ is exactly a basis of the vector space $M/\mm M$, so the minimal number of generators is $\dim_{A/\mm}M/\mm M$.
That is the statement behind the definition of a regular local ring, behind the fact that a finitely generated module over a local ring with constant fibre rank is free, and behind the local triviality of coherent sheaves.

Finite generation is not decoration.
$M = \QQ$ over $A = \ZZ_{(p)}$ satisfies $M = \mm M$ and is nonzero.
:::
