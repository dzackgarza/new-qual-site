---
schema: qual/card@1
id: P-JHUSP01RAC
kind: problem
title: "3.) Recall that is lower semicontinuous if lim in for every"
classification:
  areas:
  - real-analysis
  topics:
  - real-analysis-topics
solved: false
relations: []
---

3.) Recall that $f : [ 0 , 1 ] \to \mathbb { R }$ is lower semicontinuous if lim in $\operatorname { f } _ { x \to x _ { 0 } } f ( x ) \geq f ( x _ { 0 } )$ for every $x _ { 0 } \in [ 0 , 1 ]$ . Prove that if $f$ is a nonnegative lower semicontinuous function then one always has $\begin{array} { r } { S _ { + } ( f , P ) \to \int _ { 0 } ^ { 1 } } \end{array}$ f(x)dx as $| P | \to 0$ if $S _ { + } ( f , P )$ is the lower Riemann sum associated with a partition $\dot { P }$ of $[ 0 , 1 ]$ and $| P |$ is the smallest interval of the partition. Here $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x$ is the Lebesgue integral of $f .$ .

Here, if $0 = t _ { 0 } < t _ { 1 } < \cdots < t _ { n } = 1$ , is the partition $P ,$ then

$$
S _ { + } ( f , P ) = \sum _ { j = 1 } ^ { n } \operatorname* { i n f } _ { x \in [ t _ { j - 1 } , t _ { j } ) } f ( x ) ( t _ { j } - t _ { j - 1 } ) .
$$

Hint: To prove $\begin{array} { r } { S _ { + } ( f , P )  \int _ { 0 } ^ { 1 } f ( x ) d x } \end{array}$ as $| P | \to 0 ,$ , it suffices to show that $S _ { + } ( f , P _ { n } ) $ $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x { \mathrm { ~ i f ~ } } P _ { n }$ is a nested sequence of partitions whose lengths goes to zero.
