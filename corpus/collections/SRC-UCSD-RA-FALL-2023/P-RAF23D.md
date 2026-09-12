---
schema: qual/card@1
id: P-RAF23D
kind: problem
title: "Sinc function, Shannon sampling, and bandlimited functions"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2023 real-analysis qualifying exam, with the convention \hat f(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\operatorname{sinc} x = \frac{\sin \pi x}{\pi x}$ (with $\operatorname{sinc} 0 = 1$). Prove:

(i) If $a > 0$, $\hat{\chi}_{[-a,a]} = \check{\chi}_{[-a,a]} = 2a\operatorname{sinc}(2ax)$.

(ii) Let $\mathcal{H}_a = \{f \in L^2 : \hat{f}(\xi) = 0 \text{ if } |\xi| > a\}$.
Then $\mathcal{H}_a$ is a Hilbert space and $\{\sqrt{2a}\operatorname{sinc}(2ax - k) : k \in \mathbb{Z}\}$ is an orthonormal basis.

(iii) If $f \in \mathcal{H}_a$, then $f \in C_0$ (continuous vanishing at infinity) and $f = \sum_{-\infty}^{\infty} f\!\left(\frac{k}{2a}\right)\operatorname{sinc}(2ax - k)$ in $L^2$.
:::

::: solution
<1>1. Compute the Fourier transform of the interval indicator.
::: proof
For $x\ne0$,
\[
\widehat{\chi_{[-a,a]}}(x)
=\int_{-a}^a e^{-2\pi ixt}\,dt
=\frac{e^{-2\pi iax}-e^{2\pi iax}}{-2\pi ix}
=\frac{\sin(2\pi ax)}{\pi x}
=2a\operatorname{sinc}(2ax).
\]
At $x=0$ both sides equal $2a$, so the identity holds everywhere. Since $\chi_{[-a,a]}$ is even, the inverse transform gives the same function:
\[
\boxed{
\widehat{\chi_{[-a,a]}}
=\check{\chi}_{[-a,a]}
=2a\operatorname{sinc}(2ax).}
\]
:::

<1>2. Identify $\mathcal H_a$ with $L^2([-a,a])$.
::: proof
By Plancherel, the Fourier transform is unitary on $L^2(\mathbb R)$. Therefore
\[
\mathcal H_a
=\{f\in L^2:\operatorname{supp}\widehat f\subset[-a,a]\}
\]
is the inverse image of the closed subspace $L^2([-a,a])$, hence is itself a closed subspace of $L^2$. Thus $\mathcal H_a$ is a Hilbert space.

For $k\in\mathbb Z$, put
\[
\phi_k(x):=\sqrt{2a}\operatorname{sinc}(2ax-k)
=\sqrt{2a}\operatorname{sinc}\!\left(2a\left(x-\frac{k}{2a}\right)\right).
\]
From Step 1 and the translation rule,
\[
\widehat{\phi_k}(\xi)
=\frac1{\sqrt{2a}}
e^{-2\pi i k\xi/(2a)}\chi_{[-a,a]}(\xi).
\]
The functions
\[
\frac1{\sqrt{2a}}e^{-2\pi i k\xi/(2a)},
\qquad k\in\mathbb Z,
\]
form the standard orthonormal basis of $L^2([-a,a])$. Since the Fourier transform is unitary,
\[
\boxed{\{\phi_k:k\in\mathbb Z\}\text{ is an orthonormal basis of }\mathcal H_a.}
\]
:::

<1>3. Show that every bandlimited $f$ is continuous and vanishes at infinity.
::: proof
If $f\in\mathcal H_a$, then $\widehat f\in L^2([-a,a])$. Since the interval has finite measure, Cauchy--Schwarz gives
\[
\|\widehat f\|_1
\le (2a)^{1/2}\|\widehat f\|_2<\infty.
\]
Therefore Fourier inversion gives
\[
f(x)=\int_{-a}^a\widehat f(\xi)e^{2\pi ix\xi}\,d\xi
\]
for a continuous representative of $f$. By the Riemann--Lebesgue lemma this representative tends to $0$ as $|x|\to\infty$. Hence
\[
f\in C_0(\mathbb R).
\]
:::

<1>4. Compute the orthonormal-basis coefficients.
::: proof
By Plancherel,
\[
\begin{aligned}
\langle f,\phi_k\rangle
&=\langle\widehat f,\widehat{\phi_k}\rangle\\
&=\frac1{\sqrt{2a}}
\int_{-a}^a\widehat f(\xi)e^{2\pi i k\xi/(2a)}\,d\xi\\
&=\frac1{\sqrt{2a}}f\!\left(\frac{k}{2a}\right).
\end{aligned}
\]
Expanding $f$ in the orthonormal basis $(\phi_k)$ therefore gives, in $L^2$,
\[
\begin{aligned}
f(x)
&=\sum_{k\in\mathbb Z}
\langle f,\phi_k\rangle\phi_k(x)\\
&=\sum_{k\in\mathbb Z}
f\!\left(\frac{k}{2a}\right)
\operatorname{sinc}(2ax-k).
\end{aligned}
\]
Thus
\[
\boxed{
f=\sum_{k\in\mathbb Z}
f\!\left(\frac{k}{2a}\right)
\operatorname{sinc}(2ax-k)
\quad\text{in }L^2.}
\]
:::
:::
