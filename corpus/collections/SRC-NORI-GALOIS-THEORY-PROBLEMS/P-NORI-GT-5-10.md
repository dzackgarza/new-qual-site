---
schema: qual/card@1
id: P-NORI-GT-5-10
kind: problem
title: Abelian normal closure of $K(a^{1/p})$ is a Kummer extension by an element of $F$
classification:
  areas: [algebra]
  topics:
  - Kummer Theory
  - Abelian Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.10 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the setup of Problems 5.8 and 5.9, on which this problem depends, from p. 5 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $K/F$ be a finite Galois extension with Galois group $G$.
Assume that $K$ contains a primitive $p$-th root of unity.
Let $a \in K^\times$, and let $L$ be the field obtained from $K$ by adjoining $p$-th roots of $\sigma(a)$ for all $\sigma \in G$.
Assume that (i) $\operatorname{Gal}(L/F)$ is Abelian, and (ii) $F$ contains a primitive $p$-th root of unity.

Assume furthermore that $p$ does not divide the order of $\operatorname{Gal}(K/F)$.
Show that there is some $b \in F$ such that $L = K(b^{1/p})$.
:::

::: {.solution}

Let
$$
m=\abs{G}=[K:F].
$$
By hypothesis, $p\nmid m$.

::: pf

::: {.pf-step #s1-1}

One has
$$
L=K(a^{1/p}).
$$


::: pf-proof

By Problem 5.9, for every $\sigma\in G$ there exists $c_\sigma\in K^\times$ such that
$$
\sigma(a)=a c_\sigma^p.
$$
Choose $\alpha$ with $\alpha^p=a$. Since $K$ contains all $p$-th roots of unity, every $p$-th root of $\sigma(a)$ has the form
$$
\zeta^j c_\sigma\alpha
$$
for some $p$-th root of unity $\zeta^j\in K$. Hence every $p$-th root adjoined in the definition of $L$ already lies in $K(\alpha)$, so
$$
L\subseteq K(\alpha).
$$
For the identity element of $G$, the field $L$ contains a $p$-th root of $a$, so $K(\alpha)\subseteq L$. Therefore
$$
L=K(\alpha)=K(a^{1/p}).
$$

:::

:::

::: {.pf-step #s1-2}

Define
$$
b=N_{K/F}(a)=\prod_{\sigma\in G}\sigma(a).
$$
Then $b\in F^\times$ and there exists $c\in K^\times$ such that
$$
b=a^m c^p.
$$


::: pf-proof

The norm $b=N_{K/F}(a)$ belongs to $F^\times$. By Problem 5.9, write
$$
\sigma(a)=a c_\sigma^p
$$
for each $\sigma\in G$. Multiplying over all $\sigma$ gives
$$
b
=\prod_{\sigma\in G}\sigma(a)
=\prod_{\sigma\in G}a c_\sigma^p
=a^m\left(\prod_{\sigma\in G}c_\sigma\right)^p.
$$
Taking
$$
c=\prod_{\sigma\in G}c_\sigma\in K^\times
$$
gives the claim.

:::

:::

::: {.pf-step #s1-3}

One has
$$
K(b^{1/p})\subseteq K(a^{1/p}).
$$


::: pf-proof

Let $\alpha^p=a$. By step [](#s1-2){.pf-ref},
$$
b=a^m c^p=(c\alpha^m)^p.
$$
Thus $c\alpha^m$ is a $p$-th root of $b$ lying in $K(\alpha)$. Since $K$ contains all $p$-th roots of unity, adjoining any chosen $p$-th root of $b$ gives the same field. Hence
$$
K(b^{1/p})\subseteq K(\alpha)=K(a^{1/p}).
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
K(a^{1/p})\subseteq K(b^{1/p}).
$$


::: pf-proof

Since $p\nmid m$, choose integers $r,s$ such that
$$
rm+sp=1.
$$
Let $\beta=c\alpha^m$, so by step [](#s1-3){.pf-ref} one has $\beta^p=b$ and $\beta\in K(b^{1/p})$. Then
$$
\frac{\beta^r a^s}{c^r}
=\frac{(c\alpha^m)^r(\alpha^p)^s}{c^r}
=\alpha^{rm+ps}
=\alpha.
$$
Here $a,c\in K$, so the left-hand side belongs to $K(\beta)=K(b^{1/p})$. Therefore
$$
\alpha\in K(b^{1/p}),
$$
and hence $K(a^{1/p})\subseteq K(b^{1/p})$.

:::

:::

::: {.pf-step #s1-5}

There exists $b\in F^\times$ such that
$$
\boxed{L=K(b^{1/p})}.
$$


::: pf-proof

Take $b=N_{K/F}(a)$ from step [](#s1-2){.pf-ref}. By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref},
$$
K(a^{1/p})=K(b^{1/p}).
$$
Combining this with step [](#s1-1){.pf-ref} gives
$$
L=K(b^{1/p}).
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required statement.

:::

:::

:::
