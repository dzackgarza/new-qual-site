---
schema: qual/card@1
id: P-BKF04-1B
kind: problem
title: $A_n\cap S_m=A_m$ for the standard inclusion, but not for every embedding $S_m\hookrightarrow S_n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $S _ { n }$ be the group of permutations of $\{ 1 , \ldots , n \}$ , and let $A _ { n }$ be the alternating subgroup. Suppose $m \leq n$

(a) Identify $S _ { m }$ with the subgroup of $S _ { n }$ consisting of elements that fix $m + 1 , \ldots , n$ Prove that $A _ { n } \cap S _ { m } = A _ { m }$

(b) Is it true in general that if $f \colon S _ { m } \to S _ { n }$ is an injective homomorphism, then $A _ { n } \bigcap { f ( S _ { m } ) } = f ( A _ { m } ) ?$ Give a proof or a counterexample.
:::

::: {.solution}
(a) By definition $A_n$ is the kernel of the unique homomorphism $\operatorname{sgn}_n\colon S_n\to\{\pm1\}$ mapping each transposition to $-1$. Restricting $\operatorname{sgn}_n$ to $S_m$ gives a homomorphism mapping each transposition in $S_m$ to $-1$, so this restriction equals $\operatorname{sgn}_m$. Thus $A_m=\ker(\operatorname{sgn}_m)=\ker(\operatorname{sgn}_n)\cap S_m=A_n\cap S_m$.

(b) It is false. Take $m\geq2$ and $n=2m$. The group $S_m\times S_m$ acts on $\{1,\ldots,2m\}$, the first factor permuting $\{1,\ldots,m\}$ and the second permuting $\{m+1,\ldots,2m\}$. This action gives an injective homomorphism $\iota\colon S_m\times S_m\to S_{2m}$. Define $f\colon S_m\to S_{2m}$ by $f(\sigma)=\iota(\sigma,\sigma)$. Then $f$ maps each transposition in $S_m$ to a product of two disjoint transpositions, an element of $A_{2m}$, and the transpositions generate $S_m$, so $f(S_m)\subseteq A_{2m}$. Hence $A_{2m}\cap f(S_m)=f(S_m)$, and this is strictly larger than $f(A_m)$, since $f$ is injective and $A_m\ne S_m$.
:::
