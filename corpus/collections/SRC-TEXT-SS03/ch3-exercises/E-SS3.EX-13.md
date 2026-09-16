---
schema: qual/card@1
id: E-SS3.EX-13
kind: problem
title: "A mild pole bound forces a removable singularity"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
13. Suppose $f ( z )$ is holomorphic in a punctured disc $D _ { r } ( z _ { 0 } ) - \{ z _ { 0 } \}$ . Suppose also that

$$
| f (z) | \leq A | z - z _ {0} | ^ {- 1 + \epsilon}
$$

for some $\epsilon > 0$ , and all $z \ \mathrm { n e a r } \ z _ { 0 }$ . Show that the singularity of $f$ at $z _ { 0 }$ is removable.
:::

::: {.solution}
Translate so that $z_0=0$. Write the Laurent expansion
\[
f(z)=\sum_{n=-\infty}^{\infty}a_n z^n
\]
in a punctured disc. For $m\ge1$, Cauchy's coefficient formula on $|z|=\rho$ gives
\[
a_{-m}=\frac1{2\pi i}\int_{|z|=\rho} f(z)z^{m-1}\,dz.
\]
Using the assumed bound,
\[
|a_{-m}|\le \rho\cdot A\rho^{-1+\epsilon}\rho^{m-1}
=A\rho^{m-1+\epsilon}.
\]
Since $m-1+\epsilon>0$, letting $\rho\downarrow0$ gives $a_{-m}=0$ for every $m\ge1$. Thus the principal part vanishes, so the singularity is removable.
:::
