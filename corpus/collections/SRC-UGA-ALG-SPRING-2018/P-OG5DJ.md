---
schema: qual/card@1
id: P-OG5DJ
kind: problem
title: Splitting field, Galois group, and intermediate fields of $x^4-4x^2+2$ over
  $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $f(x) = x^4 - 4x^2 + 2 \in \QQ[x]$.

a.
Find the splitting field $K$ of $f$, and compute $[K: \QQ]$.

b.
Find the Galois group $G$ of $f$, both as an explicit group of automorphisms, and as a familiar abstract group to which it is isomorphic.

c.
Exhibit explicitly the correspondence between subgroups of $G$ and intermediate fields between $\QQ$ and $K$.
:::

::: {.solution}

Write $\alpha=\sqrt{2+\sqrt2}$ and $\beta=\sqrt{2-\sqrt2}$, both positive reals.

::: pf

::: {.pf-step #roots}

The roots of $f$ are $\pm\alpha,\pm\beta$, $f$ is irreducible, and $\alpha\beta=\sqrt2$.

::: pf-proof

As a quadratic in $x^2$, $f$ has roots $x^2=2\pm\sqrt2$, which gives the four roots. Eisenstein's criterion at $p=2$ shows that $f$ is irreducible over $\QQ$. Finally $(\alpha\beta)^2=(2+\sqrt2)(2-\sqrt2)=2$ and $\alpha\beta>0$.

:::

:::

::: {.pf-step #field}

$K=\QQ(\alpha)$ and $[K:\QQ]=4$.

::: pf-proof

$\sqrt2=\alpha^2-2\in\QQ(\alpha)$, so $\beta=\sqrt2/\alpha\in\QQ(\alpha)$. Hence all four roots lie in $\QQ(\alpha)$, and $K=\QQ(\alpha)$. By Step [](#roots){.pf-ref}, $f$ is the minimal polynomial of $\alpha$, so $[K:\QQ]=\deg f=4$.

:::

:::

::: {.pf-step #group}

$G=\Gal(K/\QQ)=\langle\sigma\rangle\cong\ZZ/4\ZZ$, where $\sigma(\alpha)=\beta$. Explicitly, $\sigma$ acts on the roots as the $4$-cycle $\alpha\mapsto\beta\mapsto-\alpha\mapsto-\beta\mapsto\alpha$.

::: pf-proof

$K/\QQ$ is a splitting field in characteristic $0$, so it is Galois and $\cardinality{G}=4$ by Step [](#field){.pf-ref}. Since $G$ acts transitively on the roots of the irreducible $f$, there is $\sigma\in G$ with $\sigma(\alpha)=\beta$. Then $\sigma(\sqrt2)=\sigma(\alpha)^2-2=\beta^2-2=-\sqrt2$, so
$$
\sigma(\beta)=\frac{\sigma(\sqrt2)}{\sigma(\alpha)}=\frac{-\sqrt2}{\beta}=-\alpha .
$$
Hence $\sigma^2(\alpha)=-\alpha\neq\alpha$, so $\sigma$ has order $4$ and generates $G$. Since $\sigma$ is additive, $\sigma(-\alpha)=-\beta$ and $\sigma(-\beta)=\alpha$.

:::

:::

::: {.pf-step #corr}

The subgroups of $G$ and the intermediate fields correspond as
$$
\{1\}\leftrightarrow K,\qquad \langle\sigma^2\rangle\leftrightarrow\QQ(\sqrt2),\qquad G\leftrightarrow\QQ .
$$

::: pf-proof

A cyclic group of order $4$ has exactly the three subgroups $\{1\}\subset\langle\sigma^2\rangle\subset G$. The fundamental theorem of Galois theory gives exactly three intermediate fields, with $[K^{\langle\sigma^2\rangle}:\QQ]=[G:\langle\sigma^2\rangle]=2$. By Step [](#group){.pf-ref}, $\sigma^2(\alpha)=-\alpha$, so $\sigma^2(\sqrt2)=(-\alpha)^2-2=\sqrt2$. Thus $\QQ(\sqrt2)\subseteq K^{\langle\sigma^2\rangle}$, and both fields have degree $2$ over $\QQ$, so they are equal.

:::

:::

::: pf-qed

Steps [](#roots){.pf-ref} and [](#field){.pf-ref} prove part (a), Step [](#group){.pf-ref} proves part (b), and Step [](#corr){.pf-ref} proves part (c).

:::

:::

:::
