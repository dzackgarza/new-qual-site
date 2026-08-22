---
schema: qual/card@1
id: E-SS4.EX-8
kind: exercise
title: "SS 4.8: Compact support of a Fourier transform and coefficient growth"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
solved: false
---

::: exercise
8. Suppose $\hat { f }$ has compact support contained in $[ - M , M ]$ and let $\begin{array} { r } { f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ Show that

$$

a _ {n} = \frac {(2 \pi i) ^ {n}}{n !} \int_ {- M} ^ {M} \hat {f} (\xi) \xi^ {n} d \xi ,

$$

and as a result

$$

\limsup _ {n \to \infty} (n! | a _ {n} |) ^ {1 / n} \leq 2 \pi M.

$$

In the converse direction, let f be any power series $\textstyle f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ with lim $\begin{array} { r } { \operatorname* { s u p } _ { n \to \infty } ( n ! | a _ { n } | ) ^ { 1 / n } \leq 2 \pi M } \end{array}$ . Then, f is holomorphic in the complex plane, and for every $\epsilon > 0$ there exists $A _ { \epsilon } > 0$ such that

$$

| f (z) | \leq A _ {\epsilon} e ^ {2 \pi (M + \epsilon) | z |}.

$$
:::
