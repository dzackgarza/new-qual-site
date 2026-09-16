---
schema: qual/card@1
id: P-MMAQ-HYVMMQ7TJW
kind: problem
title: Factorial splitting-field degree forces irreducibility and minimal root fields
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared all three claims with Fields 3 on PDF page 2; renamed the intermediate field E to avoid reusing the fixed splitting field L, and replaced the truncated title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the full symmetric root action, irreducibility via conjugates, the third-root transposition using n>=3, and the maximal point-stabilizer argument under Galois correspondence."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Fields and Galois Theory (3) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAF3, whose solution repeats this symmetric-group argument."
---

::: {.problem}
Fix a field $F$, a separable polynomial $f\in F[x]$ of degree $n \geq 3$, and a splitting field $L$ for $f$.
Prove that if $[L:F] = n!$ then:

1. $f$ is irreducible.

2. For each root $r$ of $f$, $r$ is the unique root of $f$ in $F(r)$.

3. For every root $r$ of $f$, there is no field $E$ with $F \subsetneq E \subsetneq F(r)$.
:::

::: {.solution}
Let $X$ be the set of the $n$ distinct roots of $f$ in $L$,
and put $G=\operatorname{Gal}(L/F)$.

<1>1. The action of $G$ on $X$ identifies it with
the full symmetric group $\operatorname{Sym}(X)$.

::: {.proof}
The extension is Galois because it is the splitting
field of a separable polynomial [@DF04]. Its automorphisms
permute the roots. If an automorphism fixes every root,
it fixes the field they generate over $F$, namely $L$,
so it is the identity. The action is therefore faithful.
Since $|G|=[L:F]=n!=|\operatorname{Sym}(X)|$, its image
is the whole symmetric group.
:::

<1>2. The polynomial $f$ is irreducible over $F$.

::: {.proof}
Choose $r\in X$ and let $m_r$ be its monic minimal
polynomial over $F$. This polynomial divides $f$.
For every $\sigma\in G$, applying $\sigma$ to
$m_r(r)=0$ gives $m_r(\sigma(r))=0$. Step <1>1 says
that these images include all $n$ roots. The root bound
gives $\deg m_r\geq n$, while $m_r\mid f$ gives
$\deg m_r\leq n$. Thus $f$ is a nonzero constant
multiple of the irreducible polynomial $m_r$.
:::

<1>3. For each root $r$, no other root belongs to $F(r)$.

::: {.proof}
The subgroup $H=\operatorname{Gal}(L/F(r))$ consists
exactly of the permutations fixing $r$. Suppose
$s\in X\setminus\{r\}$. Since $n\geq3$, there is
$t\in X\setminus\{r,s\}$. Step <1>1 supplies the
automorphism acting as the transposition $(s\ t)$.
It fixes $r$ and hence fixes $F(r)$ pointwise, but
does not fix $s$. Consequently $s\notin F(r)$.
:::

<1>4. The root field $F(r)$ has no strict intermediate
field over $F$.

::: {.proof}
The point stabilizer $H$ is a maximal proper subgroup
of $G$. Indeed, if $H\subsetneq J\leq G$, choose
$g\in J$ moving $r$. Since $H$ permutes the remaining
roots arbitrarily, the $J$-orbit of $r$ is all of $X$.
Its stabilizer in $J$ is precisely $H$. Thus
$|J|=n|H|=n!$, and $J=G$ by orbit-stabilizer.

For $F\subseteq E\subseteq F(r)$, Galois correspondence
gives $H\subseteq\operatorname{Gal}(L/E)\subseteq G$
[@DF04]. The subgroup must be $H$ or $G$, so its
fixed field $E$ must be $F(r)$ or $F$. These are
exactly the two allowed endpoints.
:::
:::
