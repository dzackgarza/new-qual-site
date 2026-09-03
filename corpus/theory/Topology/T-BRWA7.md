---
schema: qual/card@1
id: T-BRWA7
kind: theorem
title: The five lemma
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.theorem}
Suppose the rows in the commutative diagram
\[
\begin{tikzcd}
A \ar[r,"f"] \ar[d,"\alpha"'] &
B \ar[r,"g"] \ar[d,"\beta"'] &
C \ar[r,"h"] \ar[d,"\gamma"'] &
D \ar[r,"i"] \ar[d,"\delta"'] &
E \ar[d,"\varepsilon"'] \\
A' \ar[r,"f'"'] & B' \ar[r,"g'"'] & C' \ar[r,"h'"'] & D' \ar[r,"i'"'] & E'
\end{tikzcd}
\]
are exact.
If $\alpha$ is surjective, $\beta$ and $\delta$ are isomorphisms, and $\varepsilon$ is injective, then $\gamma$ is an isomorphism.

<!--![5 lemma.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/5_lemma.svg/388px-5_lemma.svg.png)-->
:::

::: {.proof}
For injectivity, let $c\in C$ satisfy $\gamma(c)=0$.
Then
\[
\delta(h(c))=h'(\gamma(c))=0.
\]
Since $\delta$ is injective, $h(c)=0$.
Exactness of the top row gives $c=g(b)$ for some $b\in B$.
Now
\[
0=\gamma(g(b))=g'(\beta(b)),
\]
so exactness of the bottom row gives $a'\in A'$ with $\beta(b)=f'(a')$.
Choose $a\in A$ with $\alpha(a)=a'$ using surjectivity of $\alpha$.
Commutativity gives
\[
\beta(b)=f'(\alpha(a))=\beta(f(a)).
\]
Since $\beta$ is injective, $b=f(a)$, hence $c=g(f(a))=0$.
Thus $\gamma$ is injective.

For surjectivity, let $c'\in C'$.
Since $\delta$ is surjective, choose $d\in D$ with $\delta(d)=h'(c')$.
Then
\[
\varepsilon(i(d))=i'(\delta(d))=i'(h'(c'))=0.
\]
Since $\varepsilon$ is injective, $i(d)=0$.
Exactness of the top row gives $c\in C$ with $h(c)=d$.
Hence
\[
h'(c'-\gamma(c))=h'(c')-\delta(h(c))=0.
\]
By exactness of the bottom row, $c'-\gamma(c)=g'(b')$ for some $b'\in B'$.
Choose $b\in B$ with $\beta(b)=b'$ using surjectivity of $\beta$.
Then
\[
c'=\gamma(c)+g'(\beta(b))=\gamma(c)+\gamma(g(b))=\gamma(c+g(b)).
\]
Thus $\gamma$ is surjective, so it is an isomorphism.
:::
