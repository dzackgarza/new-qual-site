---
schema: qual/card@1
id: P-EHBDD
kind: problem
title: Semisimplicity and the Jacobson radical of the corner ring $eRe$
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Jacobson Radical
  - Rings
relations: []
review: draft
---

::: {.problem}
In this question, $R$ is a ring and $e \in R$ is an idempotent, so that $eRe$ is another ring with identity element $e$.

a. What does it mean to say that $R$ is *semisimple*? State the Artin-Wedderburn Theorem.
b. If $V$ is a completely reducible $R$-module of finite length, show that the algebra $\operatorname{End}_R(V)$ is semisimple.
Deduce for a semisimple ring $R$ that $eRe$ is semisimple too.
c. Assuming that $R$ is left Artinian, show that $J(eRe) = eJ(R)e$, where $J$ denotes Jacobson radical.
:::

::: {.solution}
**(a)** $R$ is semisimple if ${}_RR$ is a completely reducible module.

Artin–Wedderburn: $R$ is semisimple $\iff$ $R \cong M_{n_1}(D_1) \times \cdots \times M_{n_r}(D_r)$ for $r\ge 0$, $n_1,\dots,n_r \ge 1$, division algebras $D_1,\dots,D_r$.
(Could write $\oplus$ instead of $\times$, okay too.)

**(b)** Write $V \cong L_1^{n_1} \oplus \cdots \oplus L_r^{n_r}$ with $L_1,\dots,L_r$ pairwise non-isomorphic irreducibles.
Let $D_i = \operatorname{End}_R(L_i)$ — a division algebra by Schur's Lemma.
As $\operatorname{Hom}_R(L_i,L_j)=0$ for $i\ne j$, $$\operatorname{End}_R(V) \cong \operatorname{End}_R(L_1^{n_1}) \oplus \cdots \oplus \operatorname{End}_R(L_r^{n_r}) \cong M_{n_1}(D_1)\oplus\cdots\oplus M_{n_r}(D_r)$$ which is semisimple.

For $eRe$: note $eRe \cong \operatorname{End}_R(Re)^{op}$.
As $R$ is semisimple, $Re \le {}_RR$ is completely reducible of finite length, so $\operatorname{End}_R(Re)^{op}$ is semisimple by the previous part.
You can remove the op — $R$ is semisimple $\iff R^{op}$ is semisimple.

**(c)** In an Artinian ring, $J(R)$ is the nilpotent 2-sided ideal such that $R/J(R)$ is semisimple (characterization).

To use this for the question, need to check that $R$ Artinian $\Rightarrow eRe$ Artinian.
Let $J_1 \supset J_2 \supset \cdots$ be a chain of (left) ideals in $eRe$.
Then $RJ_1 \supset RJ_2 \supset \cdots$ is one in $R$, so stabilizes: $RJ_n = RJ_{n+1} = \cdots$.
Now multiply by $e$: $eRJ_n = eRJ_{n+1} = \cdots$.
But $eRJ_n = eReJ_n = J_n$, so this does the job: $J_n = J_{n+1} = \cdots$.

As $J(R)$ is a nilpotent 2-sided ideal of $R$, $eJ(R)e$ is so in $eRe$.
Remains to show $eRe / eJ(R)e$ is semisimple.
This is $\bar e (R/J(R)) \bar e$ where $\bar e = e + J(R) \in R/J(R)$, which is semisimple.
This is indeed semisimple by (b).
:::
