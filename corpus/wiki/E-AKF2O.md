---
schema: qual/card@1
id: E-AKF2O
kind: exercise
title: "$1/(1+x^2)^{n+1}$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="$1/(1+x^2)^{n+1}$ "}

\[
I \da \int_{-\infty}^{\infty} \frac{d x}{\left(1+x^{2}\right)^{n+1}}=\frac{(2 n) !}{4^{n}(n !)^{2}} \pi .
\]

Note that this solution can be written many ways:
\[
I = {2n \choose n} {\pi \over 4^n}
= {\falling{2n}{n} \over n!} {\pi \over 4^n}
= {(2n)(2n-1)\cdots(n+1)\over n!} {\pi \over 4^n}
.\]

:::

:::{.solution}
The integrand is $f\in \bigo\qty{1\over z^{2n+2}} \subseteq \bigo\qty{1\over z^{1+\eps}}$, so a semicircular contour will work:

![Semicircular contour](../../assets/30_Complex_Analysis/040_Residues/figures/2021-12-23_18-05-57.png)

Thus
\[
I 
&= 2\pi i \sum_{z_k \in \HH} \Res_{z=z_k} {1\over (1+z^2)^{n+1}} \\
&= 2\pi i \Res_{z=i} {1\over (z+i)^{n+1}(z-i)^{n+1} } \\
&= 2\pi i \lim_{z\to i}{1\over n!}\qty{\dd{}{z}}^n (z+i)^{-(n+1)} \\
&= 2\pi i \lim_{z\to i}{1\over n!}\qty{\dd{}{z}}^{n-1} -(n+1)(z+i)^{-(n+2)} \\
&= 2\pi i \lim_{z\to i}{1\over n!}\qty{\dd{}{z}}^{n-2} -(n+1) \cdot -(n+2) (z+i)^{-(n+3)} \\
&= \qquad \vdots \\
&= 2\pi i \lim_{z\to i}{1\over n!}\qty{\dd{}{z}}^{n-k} (-1)^k (n+1)(n+2)\cdots(n+k) (z+i)^{-(n+k-1)} \\
&= \qquad \vdots \\
&= 2\pi i \lim_{z\to i} {1 \over n!}(-1)^n (n+1)(n+2)\cdots(2n)(z+i)^{-(2n-1)} \\
&= { \falling{2n}{n} \over n!} 2\pi i (-1)^n (2i)^{-(2n-1)} \\
&= { \falling{2n}{n} \over n!} 2\pi i (-1)^n {1\over 2^{2n+1} i^{2n+1}} \\
&= { \falling{2n}{n} \over n!} \pi (-1)^n {1\over 4^n i^{2n}} \\
&= { \falling{2n}{n} \over n!} \pi (-1)^n {1\over 4^n (-1)^n } \\
&= { \falling{2n}{n} \over n!} {\pi \over 4^n } 
.\]
:::

