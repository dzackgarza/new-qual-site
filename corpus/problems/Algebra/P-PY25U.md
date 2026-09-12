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
<1>1. Suppose every nonconstant polynomial in $F[x]$ splits over $C$.
::: {.proof}
First, $C$ is algebraically closed. Indeed, let $\beta$ be algebraic over $C$. Since $C/F$ is algebraic, $\beta$ is algebraic over $F$. Let $m_{\beta,F}(x)\in F[x]$ be its minimal polynomial. By hypothesis this polynomial splits over $C$. The minimal polynomial of $\beta$ over $C$ divides $m_{\beta,F}$ in $C[x]$, so it must be linear. Hence $\beta\in C$.

Now let $E/F$ be algebraic. Consider pairs $(K,\sigma)$ where
\[
F\subseteq K\subseteq E
\]
and $\sigma:K\hookrightarrow C$ is an $F$-embedding, ordered by extension. Every chain has an upper bound obtained by taking the union of the domains and embeddings, so Zorn's lemma gives a maximal pair $(K,\sigma)$.

If $K\ne E$, choose $\alpha\in E\setminus K$. Let $m_{\alpha,K}(x)$ be its minimal polynomial. Applying $\sigma$ to the coefficients gives a polynomial over $\sigma(K)\subseteq C$. Since $C$ is algebraically closed, it has a root $c\in C$. Sending $\alpha\mapsto c$ extends $\sigma$ to an embedding $K(\alpha)\hookrightarrow C$, contradicting maximality. Hence $K=E$.
:::

<1>2. Suppose every algebraic extension of $F$ embeds in $C$.
::: {.proof}
Let $f\in F[x]$ be nonconstant and let $E/F$ be a splitting field of $f$. Then $E/F$ is finite algebraic, so there is an $F$-embedding
\[
\sigma:E\hookrightarrow C.
\]
All roots of $f$ lie in $E$, and their images under $\sigma$ are again roots of $f$ because $\sigma$ fixes $F$. Therefore every root of $f$ lies in $C$ up to this embedded copy of $E$, and $f$ splits into linear factors over $C$.
:::
:::
