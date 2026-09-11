---
schema: qual/card@1
id: P-BKF04-1B
kind: problem
title: UC Berkeley Fall 2004 prelim 1B
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
(a) By definition $A _ { n }$ is the kernel of the unique homomorphism $\operatorname { s g n } _ { n } \colon S _ { n }  \{ \pm 1 \}$ mapping each transposition $\mathrm { t o } - 1$ . Restricting $\operatorname { s g n } _ { n }$ to $S _ { m }$ gives a homomorphism mapping each tranposition in $S _ { m }$ to −1, so this restriction must equal $\mathrm { s g n } _ { m }$ . Thus $A _ { m } = \ker ( \mathrm { s g n } _ { m } ) =$ ker $( \mathrm { s g n } _ { n } ) \cap S _ { m } = A _ { n } \cap S _ { m }$ •

(b) It is false. Take $m \ \geq \ 2$ and $n \ = \ 2 m$ There is an obvious action of $S _ { m } \times S _ { m }$ on $\{ 1 , \ldots , 2 m \}$ in which the first $S _ { m }$ permutes $\{ 1 , \ldots , m \}$ and the second $S _ { m }$ permutes $\{ n + 1 , \ldots , 2 m \}$ . Thus we get an injective homomorphism $\iota \colon S _ { m } \times S _ { m } \to S _ { 2 m }$ Define $f \colon S _ { m } \to S _ { 2 m }$ by $f ( { \boldsymbol { \sigma } } ) = \iota ( { \boldsymbol { \sigma } } , { \boldsymbol { \sigma } } )$ . Then f maps each transposition in $S _ { m }$ to an element of $A _ { 2 m }$ , and the transpositions generate $S _ { m } ,$ so $f ( S _ { m } ) \subseteq A _ { 2 m }$ . Hence $A _ { 2 m } \cap f ( S _ { m } ) = f ( S _ { m } )$ , and this is strictly larger than $f ( A _ { m } )$ , since f is injective.
:::
