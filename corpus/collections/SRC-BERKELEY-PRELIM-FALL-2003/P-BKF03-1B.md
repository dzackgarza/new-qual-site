---
schema: qual/card@1
id: P-BKF03-1B
kind: problem
title: Berkeley Fall 2003 prelim problem 1B
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the sector-contour residue computation, ray rotation factor, arc decay, and final evenness factor.
---

::: {.problem}
Evaluate $\int _ { - \infty } ^ { \infty } { \frac { x ^ { 2 } } { x ^ { n } + 1 } } d x$ , where $n \geq 4$ is an even integer.
:::
\n\n::: {.solution}\nBecause $n$ is even, the integrand is even. Thus it suffices to compute\n\[\nI:=\int_0^\infty \frac{x^2}{1+x^n}\,dx,\n\]\nand then double the result.\n\nLet\n\[\nF(z)=\frac{z^2}{1+z^n},\n\qquad\n\rho=e^{\pi i/n},\n\qquad\n\omega=e^{2\pi i/n}=\rho^2.\n\]\n\n<1>1. In the sector $0<\arg z<2\pi/n$, the function $F$ has exactly one pole, at $z=\rho$, and\n\[\n\operatorname{Res}_{z=\rho}F(z)=-\frac{\rho^3}{n}.\n\]\n::: {.proof}\nThe poles satisfy $z^n=-1$, so they are\n\[\ne^{(2k+1)\pi i/n}.\n\]\nExactly one has argument strictly between $0$ and $2\pi/n$, namely $\rho=e^{\pi i/n}$. It is simple because $(1+z^n)'=nz^{n-1}$ does not vanish there. Therefore\n\[\n\operatorname{Res}_{z=\rho}F(z)\n=\frac{\rho^2}{n\rho^{n-1}}\n=\frac{\rho^{3-n}}n.\n\]\nSince $\rho^n=-1$, one has $\rho^{3-n}=-\rho^3$, giving the formula.\n:::\n\n<1>2. The integral over the circular arc of radius $R$ in this sector tends to $0$ as $R\to\infty$.\n::: {.proof}\nOn the arc, $|z|=R$. For $R$ large,\n\[\n|1+z^n|\ge R^n-1,\n\]\nso\n\[\n|F(z)|\le \frac{R^2}{R^n-1}=O(R^{2-n}).\n\]\nThe arc length is $2\pi R/n$, hence its integral is $O(R^{3-n})$. Since $n\ge4$, this tends to $0$.\n:::\n\n<1>3. The two radial sides of the sector contribute $(1-\rho^6)I$ in the limit.\n::: {.proof}\nThe lower radial side contributes\n\[\n\int_0^R \frac{x^2}{1+x^n}\,dx.\n\]\nOn the upper radial side, traversed back toward the origin, set $z=\omega t$ with $t$ decreasing from $R$ to $0$. Since $\omega^n=e^{2\pi i}=1$,\n\[\nF(\omega t)\,\omega\,dt\n=\frac{\omega^3t^2}{1+t^n}\,dt\n=\rho^6\frac{t^2}{1+t^n}\,dt.\n\]\nTherefore the upper side contributes\n\[\n-\rho^6\int_0^R\frac{t^2}{1+t^n}\,dt.\n\]\nLetting $R\to\infty$ gives $(1-\rho^6)I$.\n:::\n\n<1>4. The residue theorem gives\n\[\nI=\frac{\pi}{n\sin(3\pi/n)}.\n\]\n::: {.proof}\nBy <1>1--<1>3, the residue theorem yields\n\[\n(1-\rho^6)I\n=2\pi i\left(-\frac{\rho^3}{n}\right)\n=-\frac{2\pi i}{n}\rho^3.\n\]\nNow\n\[\n\rho^3-\rho^{-3}=2i\sin\frac{3\pi}{n},\n\]\nso, after multiplying by $\rho^3$,\n\[\n\rho^6-1=2i\rho^3\sin\frac{3\pi}{n}.\n\]\nHence\n\[\n1-\rho^6=-2i\rho^3\sin\frac{3\pi}{n}.\n\]\nSubstituting into the contour identity and cancelling the nonzero factor $-2i\rho^3$ gives\n\[\nI=\frac{\pi}{n\sin(3\pi/n)}.\n\]\n:::\n\n<1>5. Therefore\n\[\n\boxed{\int_{-\infty}^{\infty}\frac{x^2}{x^n+1}\,dx\n=\frac{2\pi}{n\sin(3\pi/n)}}.\n\]\n::: {.proof}\nSince $n$ is even, $x^n$ and $x^2$ are both even functions, so the integrand is even. Thus the integral over the whole real line is $2I$, and <1>4 gives the displayed value.\n:::\n:::\n