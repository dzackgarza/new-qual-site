---
schema: qual/card@1
id: PR-QDRB4
kind: proposition
title: Galois subextensions of a Galois tower
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
---

::: {.proposition}
Let $L/k$ be a finite [[D-5JYEI|Galois extension]] and let $F$ be an intermediate field, $k\subseteq F\subseteq L$.
Then:

(a) $L/F$ is Galois.

(b) $F/k$ is Galois if and only if $\Gal(L/F) \normal \Gal(L/k)$.

(c) In that case restriction $\sigma\mapsto\sigma|_F$ induces an isomorphism
$$
\Gal(F/k) \cong \Gal(L/k)/\Gal(L/F).
$$

\begin{tikzcd}
	{L} \\
	\\
	{F} \\
	\\
	{k}
	\arrow["{\text{Galois}}", from=1-1, to=5-1, curve={height=-18pt}, no head]
	\arrow["{\text{Galois}}", from=5-1, to=3-1, curve={height=-12pt}, squiggly, no head]
	\arrow["{\text{Galois}}"', from=1-1, to=3-1, curve={height=12pt}, dashed, no head]
\end{tikzcd}
:::

::: {.proof}
(a) $L$ is the splitting field over $k$ of a separable polynomial $f\in k[x]$, and $L$ is also generated over $F$ by the roots of $f\in F[x]$, so $L$ is the splitting field of $f$ over $F$ and $L/F$ is Galois.

(b) and (c). Fix an algebraic closure $\bar k$ containing $L$.
Every $k$-embedding $F\to\bar k$ extends to a $k$-embedding $L\to\bar k$, which has image $L$ by [[PR-OZYUC]] because $L/k$ is normal; so the $k$-embeddings $F\to\bar k$ are exactly the restrictions $\sigma|_F$ with $\sigma\in\Gal(L/k)$.
For $\sigma\in\Gal(L/k)$ we have $\Gal(L/\sigma(F))=\sigma\Gal(L/F)\sigma^{-1}$, and by the Galois correspondence $\sigma(F)=F$ if and only if $\sigma\Gal(L/F)\sigma^{-1}=\Gal(L/F)$.
Hence $\Gal(L/F)\normal\Gal(L/k)$ if and only if $\sigma(F)=F$ for every $\sigma\in\Gal(L/k)$, if and only if every $k$-embedding $F\to\bar k$ has image $F$, which by [[PR-OZYUC]] means $F/k$ is normal.
Since $F/k$ is separable as a subextension of the separable extension $L/k$, this is equivalent to $F/k$ being Galois.
In that case restriction is a homomorphism $\Gal(L/k)\to\Gal(F/k)$; it is surjective because every $k$-automorphism of $F$ extends to $L$, and its kernel is $\Gal(L/F)$, which gives (c).
:::
