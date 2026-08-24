---
schema: qual/card@1
id: P-JHUMAY09ANF
kind: problem
title: "be the unit circle with the usual Lebesgue measure. For each let be a nonnegativ"
classification:
  areas:
  - real-analysis
  topics:
  - real-analysis-topics
relations: []
review: draft
---

6. Let $\mathbb { R } / \mathbb { Z }$ be the unit circle with the usual Lebesgue measure.
   For each $n = 1 , 2 , 3 , . . .$ let $K _ { n } : \mathbb { R } / \mathbb { Z } \to \mathbb { R } _ { + }$ be a nonnegative integrable function such that $\begin{array} { r } { \int _ { \mathbb { R } / \mathbb { Z } } K _ { n } ( t ) d t = 1 } \end{array}$ and lim $\begin{array} { r } { { \bf \delta } _ { \cdot n \longrightarrow \infty } \int _ { \varepsilon \le | t | \le 1 / 2 } K _ { n } ( t ) d t = 0 } \end{array}$ for every $0 < \varepsilon < 1 / 2$ , where we identify R $/ \mathbb { Z }$ with $( - 1 / 2 , 1 / 2 ]$ in the usual way.
   (Such a sequence of $K _ { n }$ are called approximations to the identity.)
   Let $f : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$ be continuous, and define the convolutions $f * K _ { n } : \mathbb { R } / \mathbb { Z } \to$ R by

$$
f * K _ { n } ( x ) = \int _ { \mathbb { R } / \mathbb { Z } } f ( x - t ) K _ { n } ( t ) d t .
$$

Show that $f * K _ { n }$ converges uniformly to $f$ .
