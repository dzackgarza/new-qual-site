---
schema: qual/card@1
id: E-SS6.EX-10
kind: exercise
title: "SS 6.10: Mellin transforms of cosine and sine"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
---

::: exercise
10. An integral of the form

$$

F (z) = \int_ {0} ^ {\infty} f (t) t ^ {z - 1} d t

$$

is called a Mellin transform, and we shall write $\mathcal { M } ( f ) ( z ) = F ( z )$ . For example, the gamma function is the Mellin transform of the function $e ^ { - t }$

(a) Prove that

$$

\mathcal {M} (\cos) (z) = \int_ {0} ^ {\infty} \cos (t) t ^ {z - 1} d t = \Gamma (z) \cos \left(\pi \frac {z}{2}\right) \quad \mathrm{for} 0 <   \mathrm{Re} (z) <   1,

$$

and

$$

\mathcal {M} (\sin) (z) = \int_ {0} ^ {\infty} \sin (t) t ^ {z - 1} d t = \Gamma (z) \sin \left(\pi \frac {z}{2}\right) \quad \mathrm{for} 0 <   \mathrm{Re} (z) <   1.

$$

(b) Show that the second of the above identities is valid in the larger strip $- 1 < \operatorname { R e } ( z ) < 1$ , and that as a consequence, one has

$$

\int_ {0} ^ {\infty} \frac {\sin x}{x} d x = \frac {\pi}{2} \quad \mathrm{and} \quad \int_ {0} ^ {\infty} \frac {\sin x}{x ^ {3 / 2}} d x = \sqrt {2 \pi}.

$$

This generalizes the calculation in Exercise 2 of Chapter 2.

[Hint: For the first part, consider the integral of the function $f ( w ) = e ^ { - w } w ^ { z - 1 }$ around the contour illustrated in Figure 1. Use analytic continuation to prove the second part.]

Figure 1. The contour in Exercise 10
:::
