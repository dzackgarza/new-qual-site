---
schema: qual/card@1
id: P-PRACT20-W6-05
kind: problem
title: "Week 6: Miscellaneous Topics, problem 5"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that $f : ( 0 , 1 ) \to \mathbb { R }$ is uniformly continuous.
Let $\{ x _ { n } \}$ be a sequence in $( 0 , 1 )$ such that $x _ { n } \to 0$ . Show that the sequence $\{ f ( x _ { n } ) \}$ converges.
[Note: generalizing this fact, one can show that if $U \subset \mathbb { R } ^ { n }$ is open, then $f : U \to \mathbb { R }$ is uniformly continuous iff f can be continuously extended to the closure ${ \overline { { U } } } . ]$
:::

::: {.solution}
Define the sequence $y _ { n } = f ( x _ { n } )$ . Let $\varepsilon > 0$ . Since f is uniformly continuous, there is $\delta > 0$ such that $| x - y | < \delta \implies | f ( x ) - f ( y ) | < \varepsilon$ for all $x , y \in [ 0 , 1 ]$ (that is, δ is independent of $x , y )$ . Since $x _ { n } \to 0$ , in particular $x _ { n }$ is a Cauchy sequence so there is $N \in  { \mathbb { N } }$ such that $| x _ { n } - x _ { m } | < \delta$ whenever $n , m \geq N$ . But then

$$
| y _ { n } - y _ { m } | = | f ( x _ { n } ) - f ( x _ { m } ) | < \varepsilon
$$

when $n , m \geq N$ This shows that $y _ { n }$ is a Cauchy sequence and thus converges to some limit $f _ { 0 } \in \mathbb { R }$ . [This concludes the proof, but performing the same construction for $z _ { n } = f _ { n } ( w _ { n } )$ where $w _ { n }$ is an arbitrary sequence in $( 0 , 1 )$ tending to 1, we find that $z _ { n }  f _ { 1 } \in \mathbb { R }$ Then defining $F ( 0 ) = f _ { 0 } , F ( 1 ) = f _ { 1 }$ , and $F ( x ) = f ( x )$ , for $x \in ( 0 , 1 )$ , we see that F is a continuous extension of f to [0, 1] which gives an idea of how prove the final note in the problem statement.]
:::
