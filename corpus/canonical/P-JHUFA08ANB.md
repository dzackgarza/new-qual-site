---
schema: qual/card@1
id: P-JHUFA08ANB
kind: problem
title: "2) (10 points) Let and be σ-finite measure spaces and let be a measurable function with respect to the product σ-algebra"
classification:
  areas:
  - real-analysis
  topics:
  - real-analysis-topics
relations: []
review: draft
---

2) (10 points) Let $( X , { \mathcal { M } } , \mu )$ and $( Y , \mathcal { N } , \nu )$ be σ-finite measure spaces and let $K ( x , y )$ be a measurable function with respect to the product σ-algebra $\mathcal { M } \times \mathcal { N }$ . Assume that there is a constant $0 < A <$ ∞ so that for all $x \in X$

$$
\int _ { Y } | K ( x , y ) | d \nu ( y ) \leq A ,
$$

and for all $y \in Y$

$$
\int _ { X } | K ( x , y ) | d \mu ( x ) \leq A .
$$

Let $1 \leq p \leq \infty$ and for $f \in L ^ { p } ( X , \mathcal { M } , \mu )$ define

$$
T f ( y ) = \int _ { X } f ( x ) K ( x , y ) d \mu ( x ) .
$$

Prove that

$$
\| T F \| _ { L ^ { p } ( \nu ) } \leq A \| f \| _ { L ^ { p } ( \mu ) } .
$$
