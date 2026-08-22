---
schema: qual/card@1
id: E-SS4.EX-5
kind: exercise
title: "More generally, let  be a rational function with (degree  (degreeP )+2 and $Q"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
solved: false
---

::: exercise
5. More generally, let $R ( x ) = P ( x ) / Q ( x )$ be a rational function with (degree $Q ) \geq$ (degreeP )+2 and $Q ( x ) \neq 0$ on the real axis.

(a) Prove that if $\alpha _ { 1 } , \ldots , \alpha _ { k }$ are the roots of R in the upper half-plane, then there exists polynomials $P _ { j } ( \boldsymbol { \xi } )$ of degree less than the multiplicity of $\alpha _ { j }$ so that

$$

\int_ {- \infty} ^ {\infty} R (x) e ^ {- 2 \pi i x \xi} d x = \sum_ {j = 1} ^ {k} P _ {j} (\xi) e ^ {- 2 \pi i \alpha_ {j} \xi}, \quad \text {when} \xi <   0.

$$

(b) In particular, if $Q ( z )$ has no zeros in the upper half-plane, then $\begin{array} { r } { \int _ { - \infty } ^ { \infty } R ( x ) e ^ { - 2 \pi i x \xi } \dot { d x } = 0 } \end{array}$ for $\xi < 0 .$

(c) Show that similar results hold in the case $\xi > 0$

(d) Show that

$$

\int_ {- \infty} ^ {\infty} R (x) e ^ {- 2 \pi i x \xi} d x = O (e ^ {- a | \xi |}), \quad \xi \in \mathbb {R}

$$

as $| \xi | \to \infty$ for some $a > 0$ . Determine the best possible $a \mathrm { { s } }$ in terms of the roots of R.

[Hint: For part $\mathrm { ( a ) }$ , use residues. The powers of $\xi$ appear when one diferentiates the function $f ( z ) = R ( z ) e ^ { - 2 \pi i z \xi }$ (as in the formula of Theorem 1.4 in the previous chapter). For part (c) argue in the lower half-plane.]
:::
