---
schema: qual/card@1
id: P-W23PS
kind: problem
title: The integral $\int_0^\infty\frac{1}{1+x^n}\,dx$ by a wedge of angle $\frac{2\pi}{n}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

:::{.problem}
Suppose $n \geq 2$. Use a wedge of angle $\frac{2 \pi}{n}$ to evaluate the integral
\[
    I=\int_{0}^{\infty} \frac{1}{1+x^{n}} d x
\]
:::

::: remark
The current Quals `.docx` writes the OMML limits as $-\infty$ to $\infty$ (Word’s default nary limits). That integral has a pole on the real axis when $n$ is odd, and the same sentence asks for a wedge of angle $2\pi/n$, which evaluates the integral from $0$ to $\infty$. The exam as transcribed in `9999_2021_Fall.md.source`, and the existing solutions, are $\int_0^\infty$.
:::

:::{.solution title="Newer, sketch"}
By the ML estimate, $\int_{C_R} f \to 0$.

The residue contribution: note the simple pole at $\omega_n \da e^{i\pi \over n}$,
\[
\Res_{z=\omega_n} f(z) = {1\over n\omega_n^{n-1}} = {\omega \over n\omega^n} = -{\omega_n \over n}
.\]

The segment contributions: $\int_{\gamma_1}f\to I$, and
\[
\int_{\gamma_2}f(z) \dz = \int_\infty^0 {1\over 1 + (\zeta_nt)^n} \zeta_n \dt = -\zeta_n I
,\]
so the contour contributions sum to $(1-\zeta_n)I$.

Solving:
\[
I 
= -{2\pi i \omega_n\over n(1-\zeta_n)} 
= -2\pi i {1\over \omega_n\inv - \omega_n} 
= -2\pi i {1\over 2i \sin\qty{\pi \over n}} 
= {\pi \over n} \csc\qty{\pi \over n}
.\]
:::

:::{.solution title="Older, detailed"}
Write $\omega_{n, k} = \exp\qty{(2k+1)i\pi \over n}$ and factor $z^n+1$ as 
\[
z^n+1  = \prod_{1\leq k \leq n}(z-\omega_{n, k}) = 
(z-e^{i\pi \over n})(z-e^{3i\pi \over n})
\cdots (z-e^{(2n-1)i\pi \over n})
.\]
Note that only the root $e^{i\pi\over n}$ lies in the $2\pi/n$ wedge, so it is the only (simple) pole of $f(z) \da {1\over 1+z^n}$ in this region.
Since the pole is simple, we can compute the residue easily.
Write $r_0 \da e^{e\pi\over n}$, then By L'Hopital,
\[
\Res_{z = r_0} {1\over 1+z^n}
&= \lim_{z\to r_0} {z-r_0 \over 1 + z^n} \\
&= \lim_{z\to r_0} {1\over nz^{n-1}} \\
&= {1\over nr_0^{n-1}} \\
&= {1\over n e^{i\pi (n-1) \over n}} \\
&= n\inv {\exp\qty{-i\pi (n-1)\over n }}
.\]

Take a contour $\Gamma$ comprised of

- $\gamma_1 = [0, R] \subseteq \RR$
- $\gamma_2 = \ts{Re^{it} \st t\in [0, 2\pi/n]}$
- $\gamma_3 = \zeta_n [0, R]$

By the residue theorem
\[
2\pi i \Res_{z=r_0} f(z) = I \da \int_\Gamma f = \qty{\int_{\gamma_1} + \int_{\gamma_2} + \int_{\gamma_3}}f
.\]


:::{.claim}
Taking orientations into account,
\[
\int_{\gamma_3} f = -\zeta_n \int_{\gamma_1} f
.\]
:::

:::{.claim}
\[
\int_{\gamma_2}f\convergesto{R\to\infty}0
.\]
:::



so in the limit we have
\[
2\pi i \Res_{z=r_0}f(z)  &= \qty{1 - \zeta_n}\int_{\gamma_1}f \\
\implies \int_{\gamma_1} f 
&= {2\pi i \Res_{z=r_0}f(z) \over 1 - \zeta_n}\\
&= {2\pi i e^{-\pi (n-1) \over n} \over n\qty{1-e^{2\pi i \over n}}} \\
&= {2\pi i \over n}
\left[
e^{i\pi} e^{-i\pi \over n}\qty{1 - e^{2\pi i \over n}}
\right]\inv \\
&= {2\pi i \over n}
\left[
-1\qty{e^{-i\pi \over n} - e^{\pi i \over n}}
\right]\inv\\
&= {2\pi i \over n}
\left[
2i \sin\qty{\pi\over n}
\right]\inv \\
&= {\pi \over n\sin\qty{\pi \over n}}
.\]

:::{.proof}
Parameterize the curves:

- $\gamma_1 \da \ts{t \st t\in [0, R]}, \dz = \dt$
- $\gamma_3 \da \ts{t\zeta_n \st t\in [0, R]}, \dz = \zeta_n \dt$

Then, a direct check:
\[
\int_{\gamma_3}f(z) \dz 
&= \int_0^R {1\over 1 + (\zeta_n t)^n}\zeta_n \dt \\
&= \zeta_n\int_0^R {1\over 1 + t^n}\dt \\
&= \zeta_n \int_{\gamma_1}f(z) \dz
.\]


:::

:::{.proof}
Parameterize $\gamma_2 = \ts{Re^{it} \st t\in [0, 2\pi/n]}$ and apply the ML estimate:
\[
{1\over 1 + (Re^{it})^n} \leq {1\over R^n - 1} \implies \int_{\gamma_2}f \leq {1\over R^n - 1} \qty{{2\pi R \over n}} = \bigo(R^{n-1})\convergesto{R\to\infty}0
.\]

:::

:::

