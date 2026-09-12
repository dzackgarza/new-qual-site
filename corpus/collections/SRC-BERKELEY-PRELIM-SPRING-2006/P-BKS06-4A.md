---
schema: qual/card@1
id: P-BKS06-4A
kind: problem
title: UC Berkeley Spring 2006 prelim 4A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $D = \{ z \in \mathbb { C } : | z | < 1 \}$ . Find all holomorphic functions $f \colon D  \mathbb { C }$ such that $f ( { \frac { 1 } { n } } + i e ^ { - n } )$ is real for all integers $n \geq 2$
:::

::: {.solution}
We show that the only such functions are the real constant functions. Let

$$
f ( z ) = \sum a _ { n } z ^ { n }
$$

be the Taylor series for $f$ around 0. We first prove by contradiction that $a _ { k }$ are real. Suppose that k is the smallest index so that Im $. a _ { k } \neq 0$ . Then we must have

$$
\mathrm { I m } a _ { k } = \operatorname* { l i m } _ { x \to 0 , x \in \mathbb { R } } x ^ { - k } \mathrm { I m } f ( x )
$$

On the other hand, because there is a bound on $f ^ { \prime } ( z )$ in a closed disk containing all the numbers $\textstyle { \frac { 1 } { n } } + i e ^ { - n }$

$$
\mathrm { I m } f \bigl ( { \frac { 1 } { n } } \bigr ) = \mathrm { I m } f \bigl ( { \frac { 1 } { n } } + i e ^ { - n } \bigr ) + O \bigl ( e ^ { - n } \bigr ) = O \bigl ( e ^ { - n } \bigr )
$$

as $n \to \infty$ . Hence

$$
\operatorname { I m } a _ { k } = \operatorname* { l i m } _ { n \to \infty } n ^ { k } \mathrm { I m } f ( { \frac { 1 } { n } } ) = 0 ,
$$

which is a contradiction. As a consequence, $f ( { \frac { 1 } { n } } )$ must be real.

By bounding $f ^ { \prime \prime } ( z )$ on a closed disk, we may write

$$
f ( \frac { 1 } { n } + i e ^ { - n } ) = f ( \frac { 1 } { n } ) + i e ^ { - n } f ^ { \prime } ( \frac { 1 } { n } ) + O ( e ^ { - 2 n } )
$$

Taking imaginary parts we get

$$
\operatorname { R e } f ^ { \prime } ( { \frac { 1 } { n } } ) = O ( e ^ { - n } )
$$

Arguing as above, the Taylor series at 0 for $f ^ { \prime } ( z )$ has purely imaginary coefficients. We conclude that all ${ a } _ { k } { } ^ {  ' } \mathrm { s }$ must vanish with the exception of $a _ { 0 }$
:::
