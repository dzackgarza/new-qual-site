---
schema: qual/card@1
id: P-NORI-GT-5-08
kind: problem
title: Normal closure of a Kummer extension $K(a^{1/p})$ over $F$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.8 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $K / F$ be a finite Galois extension with Galois group G. Assume that K contains a primitive p-th root of unity.
Let $a \ \in \ K ^ { \times }$ Prove that every normal extension of F that contains $K ( a ^ { 1 / p } )$ necessarily contains the field L obtained from K by adjoining p-th roots of $\sigma ( a )$ for all $\sigma \in G )$
:::

::: {.solution}

Choose $b$ with $b^p=a$, so that $K(a^{1/p})=K(b)$. Let $M/F$ be a normal extension containing $K(b)$.

::: pf

::: {.pf-step #s1-1}

For every $\sigma\in G$, there is an $F$-embedding
$$
\widetilde\sigma:M\longrightarrow \overline F
$$
whose restriction to $K$ is $\sigma$.


::: pf-proof

The inclusion $K\subseteq M$ and the automorphism $\sigma:K\to K\subseteq\overline F$ give an $F$-embedding of the intermediate field $K$ into an algebraic closure of $F$. Since $M/F$ is algebraic, the extension theorem for embeddings extends this map to an $F$-embedding
$$
\widetilde\sigma:M\to\overline F.
$$

:::

:::

::: {.pf-step #s1-2}

For every $\sigma\in G$, the image of $M$ under $\widetilde\sigma$ is $M$.


::: pf-proof

The extension $M/F$ is normal. Therefore every $F$-embedding of $M$ into an algebraic closure has image $M$. Applying this to the embedding from step [](#s1-1){.pf-ref} gives
$$
\widetilde\sigma(M)=M.
$$

:::

:::

::: {.pf-step #s1-3}

For every $\sigma\in G$, the field $M$ contains a $p$-th root of $\sigma(a)$.


::: pf-proof

Since $b\in M$, step [](#s1-2){.pf-ref} gives
$$
\widetilde\sigma(b)\in M.
$$
Moreover,
$$
\widetilde\sigma(b)^p
=\widetilde\sigma(b^p)
=\widetilde\sigma(a)
=\sigma(a),
$$
because $a\in K$ and $\widetilde\sigma\restrict_K=\sigma$. Hence $\widetilde\sigma(b)$ is a $p$-th root of $\sigma(a)$ lying in $M$.

:::

:::

::: {.pf-step #s1-4}

The field $M$ contains the field $L$ obtained from $K$ by adjoining $p$-th roots of all $\sigma(a)$ with $\sigma\in G$.


::: pf-proof

By hypothesis, $K\subseteq M$. By step [](#s1-3){.pf-ref}, for every $\sigma\in G$ the field $M$ contains a $p$-th root of $\sigma(a)$. Therefore $M$ contains the field generated over $K$ by these roots, namely $L$.

Because $K$ contains a primitive $p$-th root of unity, adjoining one $p$-th root of a given $\sigma(a)$ adjoins all of its $p$-th roots, so the field $L$ is independent of the choices of roots.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required containment $L\subseteq M$ for every normal extension $M/F$ containing $K(a^{1/p})$.

:::

:::

:::
