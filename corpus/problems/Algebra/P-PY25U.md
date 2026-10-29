---
schema: qual/card@1
id: P-PY25U
kind: problem
title: An algebraic extension $C/F$ splits every polynomial over $F$ if and only if
  every algebraic extension of $F$ embeds in $C$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Zorn's Lemma
  - Splitting Fields
relations: []
review: draft
---

::: {.problem}
Let $C/F$ be an algebraic field extension. Prove that the following are equivalent:

1. Every nonconstant polynomial in $F[x]$ splits into linear factors over $C$.
2. Every algebraic extension $E/F$ admits an $F$-embedding $E\hookrightarrow C$.
:::

::: {.solution}

::: pf

::: pf-step
Condition 1 implies condition 2.

::: pf-proof

::: {.pf-step #closed}
Under condition 1, $C$ is algebraically closed.

::: pf-proof
Let $\beta$ be algebraic over $C$. Since $C/F$ is algebraic, $\beta$ is algebraic over $F$; let $m_{\beta,F}\in F[x]$ be its minimal polynomial. By condition 1, $m_{\beta,F}$ is a product of linear factors in $C[x]$. The minimal polynomial of $\beta$ over $C$ is an irreducible factor of $m_{\beta,F}$ in $C[x]$, so it is linear, and $\beta\in C$.
:::

:::

::: {.pf-step #maximal}
For an algebraic extension $E/F$, there is a maximal pair $(K,\sigma)$ with $F\subseteq K\subseteq E$ and $\sigma:K\hookrightarrow C$ an $F$-embedding, ordered by extension.

::: pf-proof
The set of pairs is nonempty, since it contains $(F,\mathrm{incl})$. A chain has the upper bound whose domain is the union of the domains and whose embedding is the union of the embeddings. Zorn's lemma gives a maximal pair.
:::

:::

::: pf-step
The maximal pair has $K=E$.

::: pf-proof
Suppose $\alpha\in E\setminus K$, with minimal polynomial $m_{\alpha,K}\in K[x]$. Applying $\sigma$ to its coefficients gives a nonconstant polynomial $m^\sigma\in C[x]$, which has a root $c\in C$ by step [](#closed){.pf-ref}. Then $K(\alpha)\cong K[x]/(m_{\alpha,K})\to C$, $\alpha\mapsto c$, extends $\sigma$, which contradicts the maximality in step [](#maximal){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Condition 2 implies condition 1.

::: pf-proof
Let $f\in F[x]$ be nonconstant, and let $E/F$ be a splitting field of $f$, so $f=a\prod_{i=1}^n(x-\alpha_i)$ in $E[x]$. Since $E/F$ is algebraic, condition 2 gives an $F$-embedding $\sigma:E\hookrightarrow C$. Applying $\sigma$ to the coefficients, which fixes $f$, gives $f=a\prod_{i=1}^n(x-\sigma(\alpha_i))$ in $C[x]$.
:::

:::

:::

:::
