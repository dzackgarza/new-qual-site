---
schema: qual/card@1
id: E-SS4.EX-7
kind: exercise
title: "The Poisson summation formula applied to specific examples often provides intere"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
---

::: exercise
7. The Poisson summation formula applied to specific examples often provides interesting identities.

(a) Let $\tau$ be fixed with $\operatorname { I m } ( \tau ) > 0$ . Apply the Poisson summation formula to

$$
f (z) = (\tau + z) ^ {- k},
$$

where k is an integer $\geq 2 .$ , to obtain

$$
\sum_ {n = - \infty} ^ {\infty} \frac {1}{(\tau + n) ^ {k}} = \frac {(- 2 \pi i) ^ {k}}{(k - 1) !} \sum_ {m = 1} ^ {\infty} m ^ {k - 1} e ^ {2 \pi i m \tau}.
$$

(b) Set $k = 2$ in the above formula to show that if $\operatorname { I m } ( \tau ) > 0$ , then

$$
\sum_ {n = - \infty} ^ {\infty} \frac {1}{(\tau + n) ^ {2}} = \frac {\pi^ {2}}{\sin^ {2} (\pi \tau)}.
$$

(c) Can one conclude that the above formula holds true whenever $\tau$ is any complex number that is not an integer?

[Hint: For (a), use residues to prove that $\hat { f } ( \xi ) = 0 , \mathrm { i f } \ \xi < 0$ , and

$$
\hat {f} (\xi) = \frac {(- 2 \pi i) ^ {k}}{(k - 1) !} \xi^ {k - 1} e ^ {2 \pi i \xi \tau}, \quad \text { when } \xi > 0. ]
$$
:::
