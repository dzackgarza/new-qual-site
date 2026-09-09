---
schema: qual/card@1
id: P-3RGXW
kind: problem
title: Isomorphism classes of subgroups of $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Subgroups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Describe the isomorphism classes of subgroups of the additive group of rational numbers $(\mathbb{Q}, +)$ (rank 1 torsion-free abelian groups).
(1) How many isomorphism classes are there (what is the exact cardinality)?
(2) Are the subrings $\mathbb{Z}[1/p \mid p \in S]$ associated to different sets of primes $S \subseteq \mathbb{P}$ distinct and non-isomorphic?
(3) Do these exhaust all subgroups of $\mathbb{Q}$? (Explain Baer's classification via height vectors and types).
:::

::: solution
Let $G\le\QQ$ be nonzero and fix $0\ne x\in G$. For each prime $p$, define
\[
h_p(x)=\sup\{m\ge0:x\in p^mG\}\in\NN\cup\{\infty\}.
\]
The sequence $(h_p(x))_p$ is called a characteristic of $G$.

<1>1. Changing the nonzero element changes its characteristic only at finitely many primes, and never changes which coordinates are infinite.
::: proof
If $0\ne y\in G$, then $y=(a/b)x$ for nonzero integers $a,b$. Hence for every prime $p$,
\[
h_p(y)=h_p(x)+v_p(b)-v_p(a)
\]
whenever the height is finite, with truncation at $0$ as appropriate. Only primes dividing $ab$ can change, and an infinite height remains infinite. Thus the equivalence class of the characteristic is independent of the chosen nonzero element.
:::

Two characteristics $(a_p)$ and $(b_p)$ are called equivalent when they agree at all but finitely many primes and
\[
a_p=\infty\iff b_p=\infty
\]
for every $p$. Their equivalence class is the type of $G$.

<1>2. Two nonzero subgroups of $\QQ$ are isomorphic if and only if they have the same type.
::: proof
This is Baer's classification of rank-one torsion-free abelian groups. In the special case of subgroups of $\QQ$, any homomorphism between two nonzero such groups is multiplication by a rational number: after choosing $0\ne x$ in the source, the image of every $y\in G$ is forced by the rational relation between $x$ and $y$. Multiplication by a rational changes only finitely many finite $p$-heights, exactly as in <1>1. Conversely, equivalent height data differ by such a finite rational rescaling, which gives an isomorphism.
:::

<1>3. There are exactly $2^{\aleph_0}$ isomorphism classes.
::: proof
There are at most $2^{\aleph_0}$ subgroups because $\QQ$ is countable.

For each set of primes $S$, let
\[
G_S=\ZZ[1/p:p\in S].
\]
For $1\in G_S$,
\[
h_p(1)=\begin{cases}
\infty,&p\in S,\\
0,&p\notin S.
\end{cases}
\]
Thus $G_S\cong G_T$ implies $S=T$. Since the set of primes is countable, there are $2^{\aleph_0}$ choices of $S$. Hence the number of isomorphism classes is exactly $2^{\aleph_0}$.
:::

<1>4. The groups $G_S$ do not exhaust all subgroups of $\QQ$.
::: proof
Choose finite numbers $e_p\ge0$, not all zero, varying over infinitely many primes, and set
\[
G=\left\langle p^{-j}:p\text{ prime},\ 0\le j\le e_p\right\rangle\le\QQ.
\]
Then $h_p(1)=e_p$. Such a type can have infinitely many positive finite coordinates, whereas every $G_S$ has only heights $0$ or $\infty$. Hence it is not of localization type.
:::

Therefore Baer's types classify all nonzero subgroups of $\QQ$, and there are exactly continuum many isomorphism classes.
:::
