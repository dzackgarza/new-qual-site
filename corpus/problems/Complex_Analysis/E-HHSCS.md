---
schema: qual/card@1
id: E-HHSCS
kind: problem
title: The integral of $\log x/(1+x^a)$ over $[0,\infty)$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

:::{.exercise}
\[
I\da \int_0^\infty {\log(x) \over 1+x^a}\dx 
&= - \qty{\pi \over a}^2\cos\qty{\pi\over a}\csc^2\qty{\pi \over a} \\
&= - {\pi^2\over a^2} {\cos\qty{\pi\over a} \over \sin^2\qty{\pi\over a}}
.\]

:::

:::{.solution}
For the usual reasons, integrals along semicircles of radius $R$ and $\eps$ go to zero, so noting the poles at $\omega_a \da e^{i\pi\over a}$, take an indented sector:^[Sector monodromy.]

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-22_05-25-35.png)

Set $\zeta_a \da e^{2\pi i \over a}$.
Contributions from the contours: let $\gamma_1$ be the contour along $\RR$ and $\gamma_2$ along $\zeta_a \RR$, oriented so the overall contour is counterclockwise.
Then $\int_{\gamma_1}f(z)\dz \to I$ for $f(z) \da {\log(z) \over 1+z^a}$, so compute the monodromy term: parameterize $\gamma_2 \da \ts{\zeta_a t \st t\in [\eps, R]}$, so
\[
\int_{\gamma_2}f(z) \dz 
&=\int_R^\eps f(\zeta_a t) \zeta_a \dt \\
&= -\zeta_a \int_\eps^R {\log(\zeta_a t) \over (\zeta_a t)^a + 1}\dt \\
&= -\zeta_a \int_{\eps}^R {\log(z) + {2\pi i \over a} \over  t^a+1}\dt \\
&\to -\zeta_a I - \zeta_a {2\pi i \over a} \int_0^\infty {1\over t^a + 1 }\dt \\
&\da -\zeta_a I - {2\pi i\over a}\zeta_a I'
.\]

:::{.claim}
\[
I' = {\pi\over a}\csc\qty{\pi\over a}
.\]
:::

:::{.proof}
Computing the auxiliary integral $I'$:
the integrand has the same pole at $\omega_a$, so apply the same technique.
Write $g(z) \da {1\over z^a+1}$.

The contributions from the contours:
\[
\qty{ \int_{\gamma_1} + \int_{\gamma_2}} g(z) \to (1-e^{2\pi i })I' = -2i\sin\qty{\pi\over a}e^{i\pi\over a}
,\]
using the exponential balancing trick.

Computing the residue:
\[
\Res_{z=e^{i\pi\over a}}g(z) 
&= {1\over az^{a-1}}\evalfrom_{z=e^{i\pi\over a}} = {1\over ae^{i\pi\qty{a-1\over a}}} = {1\over a e^{i\pi} e^{-i\pi\over a}} \\
\implies 2\pi i \Res_{z=e^{i\pi\over a}}g(z) 
&= -{2\pi i \over a}e^{i \pi \over a}
.\]

Combining and solving:
\[
I' = { - {2\pi i\over a} e^{i\pi \over a} \over -2i\sin\qty{\pi\over a}e^{i\pi\over a}} = {\pi \over a}\csc\qty{\pi \over a}
.\]
:::

Given this, the RHS of the residue theorem limits to
\[
(1-\zeta_a) I - {2\pi i\over a}\zeta_a \qty{ {\pi \over a}\csc\qty{\pi\over a} }
= (1-\zeta_a) I - {2\pi^2\over a^2}i\zeta_a \csc\qty{\pi\over a}
.\]

For the LHS, we compute the residue at $\omega_a$:
\[
\Res_{z=\omega_a} f(z) 
&= \lim_{z\to \omega_a} {(z-\omega_a) \log(z) \over z^a + 1} \\
&\eqLH \lim_{z\to \omega_k} {\log(z) \over az^{a-1}}\\
&= {\log\qty{e^{i\pi \over a}} \over ae^{i\pi \qty{a-1\over a}} } \\
&= -{i\pi /a \over ae^{- i\pi \over a} } \\
&= -{i\pi \over a^2} e^{i\pi\over a}
,\]
so
\[
2\pi i \Res_{z=\omega_a} f(z) = -2\pi i \qty{i\pi\over a^2}e^{i\pi \over a} 
= {2\pi^2\over a^2}e^{i\pi\over a}
.\]

After some truly arduous arithmetic, this assembles to:
\[
{2\pi^2\over a^2}e^{i\pi\over a}
&= (1-\zeta_a) I - {2\pi^2\over a^2}i\zeta_a \csc\qty{\pi\over a} \\ \\
\implies
{2\pi^2\over a^2}e^{i\pi\over a}
&= (1-e^{2\pi i\over a}) I - {2\pi^2\over a^2}ie^{2\pi i \over a} \csc\qty{\pi\over a} \\ \\
\implies
{2\pi^2\over a^2}
&= (e^{-{i\pi\over a}}-e^{\pi i\over a}) I - {2\pi^2\over a^2}ie^{\pi i \over a} \csc\qty{\pi\over a} \\ \\
&= -2i\sin\qty{\pi\over a}I  - {2\pi^2\over a^2}ie^{\pi i \over a} \csc\qty{\pi\over a} \\ \\
\implies
I 
&= { {2\pi^2\over a^2} + {2\pi^2\over a^2}ie^{\pi i \over a} \csc\qty{\pi\over a}  \over -2i\sin\qty{\pi \over a} } \\\\
&= {2\pi^2\over a^2} \qty{ 1 + ie^{\pi i \over a} \csc\qty{\pi\over a}  \over -2i\sin\qty{\pi \over a} } \\ \\
&= -{\pi^2\over a^2}\csc\qty{\pi\over a} \cdot (-i)\qty{1 + ie^{i\pi\over a}\csc\qty{\pi\over a}} \\ \\
&= -{\pi^2\over a^2}\csc\qty{\pi\over a} \qty{ -i + \qty{\cos\qty{\pi\over a} +i\sin\qty{\pi\over a}}\csc\qty{\pi\over a}} \\ \\
&= -{\pi^2\over a^2}\csc\qty{\pi\over a} \qty{-i + \cot\qty{\pi\over a} + i } \\ \\
&= -{\pi^2\over a^2}\csc\qty{\pi\over a} \cot\qty{\pi\over a} \\
&= -{\pi^2\over a^2}\cos\qty{\pi\over a} \csc^2\qty{\pi\over a} \\
.\]

:::

