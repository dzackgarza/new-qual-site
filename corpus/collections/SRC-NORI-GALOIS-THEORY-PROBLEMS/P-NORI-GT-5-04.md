---
schema: qual/card@1
id: P-NORI-GT-5-04
kind: problem
title: 'Natural irrationalities: $\operatorname{Gal}(EK/E)\cong\operatorname{Gal}(K/K\cap E)$'
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.4 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the hypothesis of part (3) of Problem 5.3, on which this problem depends, from p. 4 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Given $F \subset E \subset E'$ and $F \subset K \subset E'$, where $F, E, K$ are subfields of $E'$.
It is not assumed that $E$ is an algebraic extension of $F$.
Assume that $K$ is a finite Galois extension of $F$, so that $EK$ is a finite Galois extension of $E$ (Problem 5.3).
Show that $\sigma \mapsto \sigma\restrict_K$ gives an isomorphism $\operatorname{Gal}(EK/E) \to \operatorname{Gal}(K/K \cap E)$.

*Warning* If your proof never relies on the Fundamental Thm of Galois theory, it is likely to be wrong.
So, state precisely where you appeal to this thm.
:::

::: {.solution}

Define
$$
\rho:\operatorname{Gal}(EK/E)\to\operatorname{Gal}(K/K\cap E),
\qquad
\rho(\sigma)=\sigma\restrict_K.
$$

::: pf

::: {.pf-step #s1-1}

For every $\sigma\in\operatorname{Gal}(EK/E)$, one has
$$
\sigma(K)=K.
$$


::: pf-proof

Since $\sigma$ fixes $E$ pointwise and $F\subseteq E$, the restriction of $\sigma$ to $K$ is an $F$-embedding
$$
K\hookrightarrow E'.
$$
The extension $K/F$ is normal. Therefore every $F$-embedding of $K$ into an extension field has image $K$. Hence $\sigma(K)=K$.

:::

:::

::: {.pf-step #s1-2}

The map $\rho$ is well defined and is a group homomorphism.


::: pf-proof

By step [](#s1-1){.pf-ref}, $\sigma\restrict_K$ is an automorphism of $K$. It fixes $F$ because $F\subseteq E$, and it fixes every element of
$$
K\cap E
$$
pointwise because $\sigma$ fixes all of $E$. Thus
$$
\sigma\restrict_K\in\operatorname{Gal}(K/K\cap E).
$$
Restriction clearly respects composition, so $\rho$ is a homomorphism.

:::

:::

::: {.pf-step #s1-3}

The homomorphism $\rho$ is injective.


::: pf-proof

Suppose
$$
\rho(\sigma)=\operatorname{id}_K.
$$
By definition, $\sigma$ also fixes $E$ pointwise. Since the compositum $EK$ is generated as a field by $E$ and $K$, an automorphism fixing both subfields pointwise fixes all of $EK$. Hence
$$
\sigma=\operatorname{id}_{EK}.
$$
Thus $\ker\rho$ is trivial.

:::

:::

::: {.pf-step #s1-4}

Let
$$
J=\rho(\operatorname{Gal}(EK/E))\subseteq\operatorname{Gal}(K/F).
$$
Then
$$
K\cap E\subseteq K^J.
$$


::: pf-proof

Every element of $J$ is the restriction of an automorphism of $EK$ fixing $E$ pointwise. Hence every element of $K\cap E$ is fixed by every element of $J$.

:::

:::

::: {.pf-step #s1-5}

Conversely,
$$
K^J\subseteq K\cap E.
$$


::: pf-proof

Let $x\in K^J$. Then $x\in K$, and every element of $J$ fixes $x$. By definition of $J$, this means every
$$
\sigma\in\operatorname{Gal}(EK/E)
$$
fixes $x$.

Here is the first explicit use of the Fundamental Theorem of Galois Theory: because $EK/E$ is finite Galois by Problem 5.3,
$$
(EK)^{\operatorname{Gal}(EK/E)}=E.
$$
Thus $x\in E$. Since already $x\in K$, one has
$$
x\in K\cap E.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{K^J=K\cap E}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

One has
$$
J=\operatorname{Gal}(K/K\cap E).
$$


::: pf-proof

Here is the second explicit use of the Fundamental Theorem of Galois Theory: since $K/F$ is finite Galois, the correspondence
$$
H\longmapsto K^H
$$
is a bijection from subgroups of $\operatorname{Gal}(K/F)$ to intermediate fields between $F$ and $K$, with inverse
$$
M\longmapsto\operatorname{Gal}(K/M).
$$
By step [](#s1-6){.pf-ref}, the subgroup $J$ has fixed field $K\cap E$. Therefore the unique subgroup corresponding to this field is
$$
J=\operatorname{Gal}(K/K\cap E).
$$

:::

:::

::: {.pf-step #s1-8}

Hence $\rho$ is surjective.


::: pf-proof

Its image is $J$, and step [](#s1-7){.pf-ref} identifies this image with the entire target group.

:::

:::

::: {.pf-step #s1-9}

Therefore restriction gives an isomorphism
$$
\boxed{
\operatorname{Gal}(EK/E)
\xrightarrow{\ \sim\ }
\operatorname{Gal}(K/K\cap E),
\qquad
\sigma\longmapsto\sigma\restrict_K.
}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives a homomorphism, step [](#s1-3){.pf-ref} gives injectivity, and step [](#s1-8){.pf-ref} gives surjectivity.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required natural-irrationalities isomorphism, and steps [](#s1-5){.pf-ref} and [](#s1-7){.pf-ref} explicitly identify the two uses of the Fundamental Theorem of Galois Theory requested by the warning in the source.

:::

:::

:::
