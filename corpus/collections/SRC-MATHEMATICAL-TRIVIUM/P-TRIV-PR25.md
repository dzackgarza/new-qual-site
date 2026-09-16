---
schema: qual/card@1
id: P-TRIV-PR25
kind: problem
title: Monte Carlo integration and its sample size
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
”Monte-Carlo method” Consider the function $f ( x _ { 1 } , . . . , x _ { n } )$ defined in $V =$ $\{ - 1 \leqslant x _ { i } \leqslant 1 , \ i = 1 , . . . , n \}$ 1and bounded from below and above, $| f ( x _ { 1 } , . . . , x _ { n } ) | \leqslant$ C. Define a random variable $\eta = f ( \xi _ { 1 } , . . . , \xi _ { n } )$ , where $\xi _ { i }$ 1are distributed uniformly between 1 and 1.

(a) Show that $\mathbf { E } \eta = I$ , where $I = \int _ { V } f ( x _ { 1 } , . . . , x _ { n } ) d ^ { n } x$ . Hence the random variables can be used to compute the high-dimensional integrals with a given precision.

(b) Consider the series of N random variables $\eta _ { i } = f ( \xi _ { i 1 } , . . . \xi _ { i n } ) , i = 1 , . . . , N$ where all $\xi _ { i j }$ are distributed uniformly in $[ - 1 , 1 ]$ 1. Then the quantity $\tilde { I } =$ $\frac { 1 } { N } ( \eta _ { 1 } + . . . + \eta _ { N } )$ for large N approaches I with high enough probability.
Estimate how large N should be to ensure that

$$
P ( | \tilde { I } - I | < \Delta ) \geqslant 1 - \alpha ,\tag{53}
$$

where $\Delta$ and α are given small numbers.
:::
