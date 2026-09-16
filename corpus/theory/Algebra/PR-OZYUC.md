---
schema: qual/card@1
id: PR-OZYUC
kind: proposition
title: Characterization of normal algebraic extensions
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Galois Theory
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field, let $L/k$ be an algebraic extension, and let $\bar{k}$ be an algebraic closure of $k$ containing $L$.
Then $L/k$ is [[D-LZTAK|normal]] if and only if every $k$-embedding $\sigma\colon L\to \bar{k}$ satisfies $\sigma(L) = L$.
In that case every $k$-embedding $\sigma\colon L\to\bar k$ restricts to a $k$-automorphism of $L$:

\begin{tikzcd}
	&& {\bar{k}} \\
	\\
	L && {\sigma(L) = L} \\
	\\
	k && k
	\arrow[hook, from=5-1, to=3-1]
	\arrow[Rightarrow, no head, from=5-1, to=5-3]
	\arrow[hook, from=5-3, to=3-3]
	\arrow[hook, from=3-3, to=1-3]
	\arrow["\sigma", hook, from=3-1, to=1-3]
	\arrow["\sigma", hook, two heads, from=3-1, to=3-3]
\end{tikzcd}
:::

::: {.proof}
Suppose $L/k$ is normal and let $\sigma\colon L\to\bar k$ be a $k$-embedding.
For $\alpha\in L$ with minimal polynomial $m_\alpha\in k[x]$, $\sigma(\alpha)$ is a root of $m_\alpha$, and all roots of $m_\alpha$ lie in $L$, so $\sigma(L)\subseteq L$.
Moreover $\sigma$ injects the finite set of roots of $m_\alpha$ in $L$ into itself, hence permutes it, so $\alpha$ lies in $\sigma(L)$; thus $\sigma(L)=L$.

Conversely, suppose every $k$-embedding $L\to\bar k$ has image $L$.
Let $f\in k[x]$ be irreducible with a root $\alpha\in L$, and let $\beta\in\bar k$ be any root of $f$.
There is a $k$-embedding $k(\alpha)\to\bar k$ with $\alpha\mapsto\beta$, and since $L/k(\alpha)$ is algebraic and $\bar k$ is algebraically closed, it extends to a $k$-embedding $\sigma\colon L\to\bar k$.
Then $\beta=\sigma(\alpha)\in\sigma(L)=L$, so $f$ splits in $L$ and $L/k$ is normal.
:::
