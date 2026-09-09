---
schema: qual/card@1
id: P-RASP23G
kind: problem
title: "Riesz fractional integration formula via Fourier transform"
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
  date: 2026-09-09
  note: Checked against Problem 7 and the Fourier-transform convention on the cover page of the official UCSD Spring 2023 real-analysis qualifying exam. The source says only "compact support function"; the card makes the standard test-function regularity phi in C_c^infty explicit so both displayed integrals are ordinary absolutely convergent Lebesgue integrals.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\Gamma(z)$ be the gamma function defined by $\Gamma(z) = \int_0^\infty e^{-t} t^{z-1}\,dt$ for $z$ with $\operatorname{Re}(z) > 0$.
For $\phi\in C_c^\infty(\mathbb R^n)$, prove that for any $0 < \alpha < n$,
$$
\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}} \int_{\mathbb{R}^n} |x|^{\alpha-n} \hat{\phi}(x)\,dx = \frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}} \int_{\mathbb{R}^n} |\xi|^{-\alpha} \phi(\xi)\,d\xi.
$$

Hint: Use the Fourier transform of the Gaussian, the identity $\int \hat{f} g = \int f \hat{g}$ for $L^1$ functions and the change of variables for the integral in the definition of $\Gamma$.
:::


::: solution
Use the Fourier-transform convention from the exam,
\[
\widehat h(\xi)=\int_{\mathbb R^n}e^{-2\pi i\langle\xi,y\rangle}h(y)\,dy.
\]
Set
\[
s:=\frac{n-\alpha}{2}>0.
\]
For $x\ne0$, the Gamma-function identity with the substitution $t=\pi\lambda|x|^2$ gives
\[
\int_0^\infty e^{-\pi\lambda|x|^2}\lambda^{s-1}\,d\lambda
=\frac{\Gamma(s)}{\pi^s}|x|^{-2s}
=\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}}|x|^{\alpha-n}.
\]
Therefore the left-hand side equals
\[
\int_{\mathbb R^n}\widehat\phi(x)
\left(\int_0^\infty e^{-\pi\lambda|x|^2}\lambda^{s-1}\,d\lambda\right)dx.
\]
Because $\phi\in C_c^\infty$, its Fourier transform is rapidly decreasing; since $0<\alpha<n$, the weight $|x|^{\alpha-n}$ is locally integrable. Thus the relevant integrals are absolutely convergent, and Fubini applies:
\[
\begin{aligned}
&\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}}
\int_{\mathbb R^n}|x|^{\alpha-n}\widehat\phi(x)\,dx\\
&\qquad=
\int_0^\infty \lambda^{s-1}
\left(\int_{\mathbb R^n}\widehat\phi(x)e^{-\pi\lambda|x|^2}\,dx\right)d\lambda.
\end{aligned}
\]

Let
\[
g_\lambda(x)=e^{-\pi\lambda|x|^2}.
\]
The Gaussian transform formula on the exam cover page is
\[
\widehat g_\lambda(\xi)
=\lambda^{-n/2}e^{-\pi|\xi|^2/\lambda}.
\]
Using
\[
\int \widehat\phi\,g_\lambda
=\int \phi\,\widehat g_\lambda,
\]
we obtain
\[
\begin{aligned}
\text{LHS}
&=\int_0^\infty\lambda^{s-1-n/2}
\left(\int_{\mathbb R^n}
\phi(\xi)e^{-\pi|\xi|^2/\lambda}\,d\xi\right)d\lambda\\
&=\int_{\mathbb R^n}\phi(\xi)
\left(\int_0^\infty
\lambda^{-\alpha/2-1}e^{-\pi|\xi|^2/\lambda}\,d\lambda\right)d\xi.
\end{aligned}
\]
Again Fubini is justified by absolute convergence; on the right this reduces to local integrability of $|\xi|^{-\alpha}$ and compact support of $\phi$.

For $\xi\ne0$, substitute
\[
t=\frac{\pi|\xi|^2}{\lambda}.
\]
Then
\[
\begin{aligned}
\int_0^\infty
\lambda^{-\alpha/2-1}e^{-\pi|\xi|^2/\lambda}\,d\lambda
&=(\pi|\xi|^2)^{-\alpha/2}
\int_0^\infty e^{-t}t^{\alpha/2-1}\,dt\\
&=\frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}}|\xi|^{-\alpha}.
\end{aligned}
\]
Substitution into the preceding expression gives
\[
\boxed{
\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}}
\int_{\mathbb R^n}|x|^{\alpha-n}\widehat\phi(x)\,dx
=
\frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}}
\int_{\mathbb R^n}|\xi|^{-\alpha}\phi(\xi)\,d\xi.
}
\]
:::
