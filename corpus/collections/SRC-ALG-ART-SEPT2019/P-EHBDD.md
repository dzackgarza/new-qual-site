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

(a) What does it mean to say that $R$ is *semisimple*? State the Artin-Wedderburn Theorem.

(b) If $V$ is a completely reducible $R$-module of finite length, show that the algebra $\operatorname{End}_R(V)$ is semisimple.
Deduce for a semisimple ring $R$ that $eRe$ is semisimple too.

(c) Assuming that $R$ is left Artinian, show that $J(eRe) = eJ(R)e$, where $J$ denotes Jacobson radical.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
(a) $R$ is semisimple if ${}_RR$ is a completely reducible module. The Artin–Wedderburn theorem: $R$ is semisimple if and only if $R \cong M_{n_1}(D_1) \times \cdots \times M_{n_r}(D_r)$ for some $r\ge 0$, $n_1,\dots,n_r \ge 1$ and division algebras $D_1,\dots,D_r$.

::: pf-proof
These are the definition and the theorem.
:::

:::

::: {.pf-step #s2}
(b) If $V$ is completely reducible of finite length, then $\operatorname{End}_R(V)$ is semisimple.

::: pf-proof
Write $V \cong L_1^{n_1} \oplus \cdots \oplus L_r^{n_r}$ with $L_1,\dots,L_r$ pairwise non-isomorphic irreducibles. Let $D_i = \operatorname{End}_R(L_i)$, a division algebra by Schur's lemma. As $\operatorname{Hom}_R(L_i,L_j)=0$ for $i\ne j$,
$$
\operatorname{End}_R(V) \cong \operatorname{End}_R(L_1^{n_1}) \times \cdots \times \operatorname{End}_R(L_r^{n_r}) \cong M_{n_1}(D_1)\times\cdots\times M_{n_r}(D_r),
$$
which is semisimple by step [](#s1){.pf-ref}.
:::

:::

::: {.pf-step #s3}
(b) If $R$ is semisimple, then $eRe$ is semisimple.

::: pf-proof
One has $eRe \cong \operatorname{End}_R(Re)^{op}$. As $R$ is semisimple, $Re \le {}_RR$ is completely reducible of finite length, so $\operatorname{End}_R(Re)$ is semisimple by step [](#s2){.pf-ref}. A ring $S$ is semisimple if and only if $S^{op}$ is, by step [](#s1){.pf-ref}, since $M_n(D)^{op}\cong M_n(D^{op})$.
:::

:::

::: {.pf-step #s4}
(c) If $R$ is left Artinian, then so is $eRe$.

::: pf-proof
Let $J_1 \supseteq J_2 \supseteq \cdots$ be a chain of left ideals of $eRe$. Then $RJ_1 \supseteq RJ_2 \supseteq \cdots$ is a chain of left ideals of $R$, so $RJ_n = RJ_{n+1} = \cdots$ for some $n$. Every $j\in J_m$ satisfies $j=ej$, so $eRJ_m = eReJ_m = J_m$. Multiplying by $e$ gives $J_n = J_{n+1} = \cdots$.
:::

:::

::: {.pf-step #s5}
(c) $J(eRe)=eJ(R)e$.

::: pf-proof
In a left Artinian ring $S$, $J(S)$ is the unique nilpotent two-sided ideal $I$ such that $S/I$ is semisimple: a nilpotent ideal lies in $J(S)$, and $J(S)$ lies in every ideal with semisimple quotient. By step [](#s4){.pf-ref} this applies to $S=eRe$.

As $J(R)$ is a nilpotent two-sided ideal of $R$, $eJ(R)e$ is a nilpotent two-sided ideal of $eRe$. The kernel of $eRe\to R/J(R)$ is $eRe\cap J(R)=eJ(R)e$, so $eRe / eJ(R)e \cong \bar e (R/J(R)) \bar e$, where $\bar e = e + J(R)$. This ring is semisimple by step [](#s3){.pf-ref} because $R/J(R)$ is semisimple. Hence $J(eRe)=eJ(R)e$.
:::

:::

::: pf-qed
Step [](#s1){.pf-ref} answers (a), steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove (b), and step [](#s5){.pf-ref} proves (c).
:::

:::

:::
