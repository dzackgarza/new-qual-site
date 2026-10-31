---
schema: qual/card@1
id: P-NORI-GT-7-01
kind: problem
title: Eigenspaces of a character of a Galois group are one-dimensional
classification:
  areas: [algebra]
  topics:
  - Characters of Galois Groups
  - Linear Independence of Characters
  - Kummer Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 7.1 of the retained Nori Galois Theory Problems PDF.
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-09-28
  note: The extraction left a NUL byte for the superscript chi of V; restored from the space V^chi the statement defines.
---

::: {.problem}
Let $G = \Gal(K/F)$. Assume that the order of $\mu_{n}(F)$ is $n$.

Let $\chi \colon G \to \mu_{n}(F)$ be a homomorphism. Show that $V^{\chi} = \{a \in K \st \sigma(a) = \chi(\sigma) \cdot a \ \forall \sigma \in G\}$ is a one-dimensional $F$-vector space of $K$.

Hint: Let $b \in K$. Let $a \in K$ denote the sum of $\chi(\sigma)^{-1}\sigma(b)$, taken over all $\sigma \in G$. Show that $a$ belongs to $V^{\chi}$.

Use Dedekind's "linear independence of characters" to show that there is some $b \in K$ such that the above $a$ is nonzero.
:::

::: {.solution}

For $b\in K$, define
$$
P_\chi(b)=\sum_{\sigma\in G}\chi(\sigma)^{-1}\sigma(b).
$$

::: pf

::: {.pf-step #s1-1}

For every $b\in K$, one has
$$
P_\chi(b)\in V^\chi.
$$


::: pf-proof

Let $\tau\in G$. Then
$$
\begin{aligned}
\tau(P_\chi(b))
&=\sum_{\sigma\in G}\chi(\sigma)^{-1}\tau\sigma(b).
\end{aligned}
$$
Reindex by $\rho=\tau\sigma$, so $\sigma=\tau^{-1}\rho$. Since $\chi$ is a homomorphism,
$$
\chi(\tau^{-1}\rho)^{-1}
=\chi(\tau)\chi(\rho)^{-1}.
$$
Hence
$$
\begin{aligned}
\tau(P_\chi(b))
&=\sum_{\rho\in G}\chi(\tau^{-1}\rho)^{-1}\rho(b)\\
&=\chi(\tau)\sum_{\rho\in G}\chi(\rho)^{-1}\rho(b)\\
&=\chi(\tau)P_\chi(b).
\end{aligned}
$$
Thus $P_\chi(b)$ satisfies the defining condition for $V^\chi$.

:::

:::

::: {.pf-step #s1-2}

The $F$-linear map
$$
P_\chi:K\longrightarrow K
$$
is not the zero map.


::: pf-proof

The elements of $G$ are distinct field homomorphisms $K\to K$. Dedekind's linear independence of characters says that distinct field homomorphisms are linearly independent over the target field. Therefore a relation
$$
\sum_{\sigma\in G}c_\sigma\sigma=0
$$
with coefficients $c_\sigma\in K$ forces every $c_\sigma=0$.

In the definition of $P_\chi$, the coefficient of $\sigma$ is
$$
\chi(\sigma)^{-1}\in F^\times\subseteq K^\times,
$$
which is nonzero for every $\sigma$. Hence the displayed linear combination of automorphisms cannot be the zero map.

:::

:::

::: {.pf-step #s1-3}

The space $V^\chi$ contains a nonzero element.


::: pf-proof

By step [](#s1-2){.pf-ref}, there exists $b\in K$ with
$$
P_\chi(b)\neq0.
$$
By step [](#s1-1){.pf-ref}, this element lies in $V^\chi$.

:::

:::

::: {.pf-step #s1-4}

Any two nonzero elements of $V^\chi$ differ by multiplication by an element of $F^\times$.


::: pf-proof

Let $a,c\in V^\chi$ be nonzero. For every $\sigma\in G$,
$$
\sigma\left(\frac ca\right)
=\frac{\sigma(c)}{\sigma(a)}
=\frac{\chi(\sigma)c}{\chi(\sigma)a}
=\frac ca.
$$
Thus $c/a$ is fixed by every element of $G$. Since $K/F$ is Galois,
$$
K^G=F.
$$
Therefore $c/a\in F^\times$.

:::

:::

::: {.pf-step #s1-5}

The $F$-vector space $V^\chi$ is one-dimensional.


::: pf-proof

By step [](#s1-3){.pf-ref}, choose a nonzero $a\in V^\chi$. Step [](#s1-4){.pf-ref} shows that every nonzero $c\in V^\chi$ has the form
$$
c=\lambda a
$$
for some $\lambda\in F^\times$. The zero element is also in $Fa$. Hence
$$
V^\chi=Fa,
$$
so
$$
\boxed{\dim_F V^\chi=1}.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required statement.

:::

:::

:::
