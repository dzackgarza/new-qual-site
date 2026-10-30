---
schema: qual/card@1
id: P-UCLARA15F-10
kind: problem
title: Residue computation of $\int_0^\infty e^{\cos x}\sin(\sin x)\,\frac{dx}{x}$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 10 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Use the Residue Theorem to prove that
$$
\int_0^\infty e^{\cos x} \sin(\sin x)\,\frac{dx}{x} = \frac{\pi}{2}(e - 1).
$$
Use a large semicircle as part of the contour.
:::

::: {.solution}

Let $F(z) \coloneqq \frac{e^{e^{iz}}-1}{z}$, holomorphic on $\CC\setminus\theset{0}$. For $0<\varepsilon<R$, let $\Gamma_{R,\varepsilon}$ be the closed contour that runs along $[-R,-\varepsilon]$, along the upper semicircle $C_\varepsilon$ of radius $\varepsilon$ about $0$ from $-\varepsilon$ to $\varepsilon$, along $[\varepsilon,R]$, and along the upper semicircle $C_R$ of radius $R$ from $R$ to $-R$.

::: pf

::: {.pf-step #cauchy}

$\int_{\Gamma_{R,\varepsilon}}F(z)\,dz=0$.

::: pf-proof

$F$ is holomorphic on a neighbourhood of the closed region that $\Gamma_{R,\varepsilon}$ bounds, since that region omits the half-disc of radius $\varepsilon$ about the only singularity $0$. Apply Cauchy's theorem.

:::

:::

::: {.pf-step #large-arc}

$\int_{C_R}F(z)\,dz\to0$ as $R\to\infty$.

::: pf-proof

For $z=Re^{i\theta}$ with $0\le\theta\le\pi$, $\abs{e^{iz}}=e^{-R\sin\theta}\le1$. For $\abs{w}\le1$, $e^w-1=w\int_0^1e^{tw}\,dt$ gives $\abs{e^w-1}\le e\abs{w}$. With $w=e^{iz}$, $\abs{F(z)}\le\frac eR e^{-R\sin\theta}$, so
$$
\abs{\int_{C_R}F(z)\,dz}\le e\int_0^\pi e^{-R\sin\theta}\,d\theta = 2e\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta\le 2e\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta\le\frac{\pi e}{R},
$$
using $\sin\theta\ge 2\theta/\pi$ on $[0,\pi/2]$, which holds because $\sin$ is concave there.

:::

:::

::: {.pf-step #small-arc}

$\int_{C_\varepsilon}F(z)\,dz\to-i\pi(e-1)$ as $\varepsilon\to0$.

::: pf-proof

The numerator $e^{e^{iz}}-1$ is entire with value $e-1$ at $0$, so $F(z)=\frac{e-1}{z}+G(z)$ with $G$ bounded near $0$. The term $G$ contributes $O(\varepsilon)$, and $\int_{C_\varepsilon}\frac{dz}{z}=\int_\pi^0 i\,d\theta=-i\pi$.

:::

:::

::: {.pf-step #segments}

$\int_{-R}^{-\varepsilon}F(x)\,dx+\int_{\varepsilon}^{R}F(x)\,dx=2i\int_{\varepsilon}^{R}e^{\cos x}\sin(\sin x)\frac{dx}{x}$.

::: pf-proof

For real $x$, $e^{e^{ix}}=e^{\cos x}\left(\cos(\sin x)+i\sin(\sin x)\right)$ and $e^{e^{-ix}}=\overline{e^{e^{ix}}}$, so $F(-x)=-\overline{F(x)}$ and $F(x)+F(-x)=2i\operatorname{Im}F(x)=2ie^{\cos x}\sin(\sin x)/x$. Substitute $x=-t$ in the first integral.

:::

:::

::: pf-step

$\displaystyle\int_0^\infty e^{\cos x}\sin(\sin x)\,\frac{dx}{x}=\boxed{\frac{\pi}{2}(e-1)}$.

::: pf-proof

The integrand extends continuously to $x=0$ with value $e$, since $\frac{\sin(\sin x)}{x}=\frac{\sin(\sin x)}{\sin x}\cdot\frac{\sin x}{x}\to1$. By steps [](#cauchy){.pf-ref}, [](#small-arc){.pf-ref} and [](#segments){.pf-ref}, letting $\varepsilon\to0$ gives $2i\int_0^R e^{\cos x}\sin(\sin x)\frac{dx}{x}=i\pi(e-1)-\int_{C_R}F(z)\,dz$. By step [](#large-arc){.pf-ref}, the right side tends to $i\pi(e-1)$ as $R\to\infty$, so the improper integral converges to $\frac{\pi}{2}(e-1)$.

:::

:::

:::

:::
