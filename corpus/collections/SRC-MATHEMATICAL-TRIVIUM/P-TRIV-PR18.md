---
schema: qual/card@1
id: P-TRIV-PR18
kind: problem
title: 'Mathematical Trivium — Probability problem 18'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Consider the series ω of n experiments whose results are given by independent variables $\xi _ { i } , i = 1 , . . . , n$ , taking the values 1 (success) with the probability $p ,$ and 0 (fail) with the probability $q = 1 - p$ . Compose the sum $S _ { n } ( \omega ) = \xi _ { 1 } + . . . + \xi _ { n }$ . It is clear that for any typical series ω and for large n, $S _ { n } ( \omega ) / n$ must be close enough to p. But what is the total amount of the typical series and how it behaves as n grows?
Denote by $C ( n , \epsilon )$ all typical series, or, more precisely,

$$
C ( n , \epsilon ) = \left\{ \omega | \mathbf { \epsilon } \left| \frac { S _ { n } ( \omega ) } { n } - p \right| \leqslant \epsilon \right\} ,\tag{47}
$$

with some small $\epsilon .$

(a) Show that if $\omega \in C ( n , \epsilon )$ , then the probability $p ( \omega )$ of such series to realize is enclosed withing the region

$$
e ^ { - n ( H + \tilde { \epsilon } ) } \leqslant p ( \omega ) \leqslant e ^ { - n ( H - \tilde { \epsilon } ) } ,\tag{48}
$$

where

$$
\tilde { \epsilon } = \operatorname * { m a x } \left\{ \epsilon , \epsilon \left( - 2 \log ( p q ) \right) \right\} ,\tag{49}
$$

and the quantity

$$
H = - p \log p - q \log q\tag{50}
$$

is called entropy.

(b) Show that the total amount of the typical series lies in the region

$$
e ^ { n ( H - \tilde { \epsilon } ) } \leqslant N ( C ( n , \epsilon ) ) \leqslant e ^ { n ( H + \tilde { \epsilon } ) } .\tag{51}
$$

Hence the number of the typical series is exponentially large, while the probability of each of them is exponentially small.
:::
