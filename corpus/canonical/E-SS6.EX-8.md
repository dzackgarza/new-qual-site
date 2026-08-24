---
schema: qual/card@1
id: E-SS6.EX-8
kind: exercise
title: "The Bessel functions arise in the study of spherical symmetries and the Fourier "
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
---

::: exercise
8. The Bessel functions arise in the study of spherical symmetries and the Fourier transform. See Chapter 6 in Book I. Prove that the following power series identity holds for Bessel functions of real order $\nu > - 1 / 2$

$$

J _ {\nu} (x) = \frac {(x / 2) ^ {\nu}}{\Gamma (\nu + 1 / 2) \sqrt {\pi}} \int_ {- 1} ^ {1} e ^ {i x t} (1 - t ^ {2}) ^ {\nu - (1 / 2)} d t = \left(\frac {x}{2}\right) ^ {\nu} \sum_ {m = 0} ^ {\infty} \frac {(- 1) ^ {m} \left(\frac {x ^ {2}}{4}\right) ^ {m}}{m ! \Gamma (\nu + m + 1)}

$$

whenever $x > 0$ . In particular, the Bessel function $J _ { \nu }$ satisfies the ordinary diferential equation

$$

\frac {d ^ {2} J _ {\nu}}{d x ^ {2}} + \frac {1}{x} \frac {d J _ {\nu}}{d x} + \left(1 - \frac {\nu^ {2}}{x ^ {2}}\right) J _ {\nu} = 0.

$$

[Hint: Expand the exponential $e ^ { i x t }$ in a power series, and express the remaining integrals in terms of the gamma function, using Exercise 7.]
:::
