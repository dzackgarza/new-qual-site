---
schema: qual/card@1
id: P-ALGS14E
kind: problem
title: Abelian groups injective as $\mathbb{Z}$-modules iff divisible
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Prove that an abelian group $A$ is injective as a $\mathbb{Z}$-module if and only if it is divisible.
:::

::: {.solution}
<1>1. Suppose first that $A$ is injective.
Let $a\in A$ and let $n\ge1$.
Define a homomorphism
\[
f:n\mathbb Z\longrightarrow A,
\qquad f(n)=a.
\]
By injectivity, $f$ extends along $n\mathbb Z\hookrightarrow\mathbb Z$ to a homomorphism $F:\mathbb Z\to A$.
If $b=F(1)$, then
\[
a=f(n)=F(n)=nb.
\]
Thus $A$ is divisible.
::: {.proof}
This is exactly the extension property defining injective $\mathbb Z$-modules.
:::

<1>2. Conversely, assume that $A$ is divisible.
Let $B\subseteq C$ be abelian groups and let $f:B\to A$ be a homomorphism.
We prove that $f$ extends to $C$.
Consider pairs $(D,g)$ with
\[
B\subseteq D\subseteq C,
\qquad g:D\to A,
\qquad g|_B=f,
\]
ordered by extension.
Every chain has an upper bound obtained by taking the union of the domains and the compatible maps, so by Zorn's lemma there is a maximal pair $(D,g)$.
::: {.proof}
For a chain, the maps agree on overlaps because the pairs are ordered by extension; hence their union is a well-defined homomorphism.
:::

<1>3. Suppose $D\ne C$ and choose $c\in C\setminus D$.
Set
\[
I=\{n\in\mathbb Z:nc\in D\}.
\]
Then $I$ is an ideal of $\mathbb Z$, so $I=m\mathbb Z$ for some $m\ge0$.
::: {.proof}
$I$ is closed under addition and multiplication by arbitrary integers.
:::

<1>4. If $m=0$, define
\[
\widetilde g(d+kc)=g(d)
\qquad(d\in D,\ k\in\mathbb Z).
\]
This is well defined and extends $g$ to the strictly larger subgroup $D+\mathbb Zc$, contradicting maximality.
::: {.proof}
If $d+kc=d'+k'c$, then $(k-k')c=d'-d\in D$, so $k-k'\in I=0$; hence $k=k'$ and then $d=d'$.
:::

<1>5. Now suppose $m>0$.
Since $mc\in D$ and $A$ is divisible, choose $a\in A$ such that
\[
ma=g(mc).
\]
Define
\[
\widetilde g(d+kc)=g(d)+ka.
\]
Then $\widetilde g:D+\mathbb Zc\to A$ is a well-defined homomorphism extending $g$.
::: {.proof}
If $d+kc=d'+k'c$, then $(k-k')c=d'-d\in D$, so $m\mid(k-k')$ because $I=m\mathbb Z$.
Write $k-k'=qm$.
Then
\[
g(d'-d)=g((k-k')c)=qg(mc)=qma=(k-k')a,
\]
which gives $g(d)+ka=g(d')+k'a$.
Additivity is immediate from the formula.
:::

<1>6. Since $c\notin D$, the subgroup $D+\mathbb Zc$ strictly contains $D$, contradicting maximality in both cases.
Therefore $D=C$, so $f$ extends to $C$.
Hence $A$ is injective.
::: {.proof}
<1>2--<1>5 prove the extension property for every inclusion $B\subseteq C$.
:::
:::
