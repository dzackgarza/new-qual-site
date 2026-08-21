---
schema: qual/card@1
id: P-P7IWV
kind: problem
title: One root of $z^4+2z^3-2z+10$ in each open quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Prove that $f(z) = z^4 + 2z^3 -2z + 10$ has exactly one root in each open
quadrant.
:::

:::{.solution}
Take a large semicircle 

- $\gamma_1 = [0, R]$
- $\gamma_2 = \ts{Re^{it} \st t\in [0, \pi/2]}$
- $\gamma_3 = i[0, R]$

- $\Delta\Arg(f, \gamma_1) = 0$:
  The only way $f\circ \gamma_1$ can change argument is by changing sign, since it's real valued.
  Use that $f(0) = 10, f(1) = 11$ and $f'(t) = 4t^3+6t-2 > 0$ so $f$ is increasing on $[1, \infty)$.
  Then by Rouché, on $\abs{z} = 1$ we have $\abs{z^4+2z^3-2}\leq 5 < 10 = \abs{10}$, so $f$ has no zeros on $\abs{z} \leq 1$.

- $\Delta\Arg(f, \gamma_2) = 2\pi$: parameterize $\gamma_2(t) = Re^{it}$, then $f(\gamma(t)) \sim R^4e^{it}$ for large $R$, which changes argument by $2\pi$ for $t$ in $[0, \pi/2]$.

- $\Delta\Arg(f, \gamma_3) = 0$: check $f(it) = t^4 + 10 + i(-2t^3-2t)$ and we let $t$ range through $[0, R]$.
For $t>0$, the real part is strictly positive, so this can not wind about the origin.

By the argument principle, $\size Z_f = {1\over 2\pi} \Delta\Arg(f, \Gamma) = 1$. 
:::

:::{.solution title="older"}
It suffices to show there's only one root in the open quadrant $Q_1$, since they come in conjugate pairs.
Assume that there are no roots on $\RR$ or $i\RR$.
Since polynomials are entire, the argument principle can be used to count zeros:
\[
Z_f = {1\over 2\pi i}\int_\gamma \logd f(z)\dz = \Delta_\gamma \Arg(f)
.\]
To take the curve $\gamma$ comprised of

- $\gamma_1 = [0, R]$,
- $\gamma_2 = Re^{it}$ for $t\in [0, \pi/2]$
- $\gamma_3 = i[0, R]$.

Then

- $\Delta_{\gamma_1}\Arg(f) = 0$, since $f(\RR_{\geq 0}) \subseteq \RR_{\geq 0}$.
- $\Delta_{\gamma_2}\Arg(f) = 4\cdot {\pi\over 2} = 2\pi$ since $f\sim z^4$ for large $R$.
- $\Delta_{\gamma_3}\Arg(f)$: consider
\[
f(it) = t^4 - it^3 -2it + 10 = t^4\qty{1 - it\inv -2it^{-2} +10t^{-4}} \\
\implies \Arg(f(it)) \sim \Arg(t^4) =0
.\]

So $\Delta_\gamma \Arg(f) = 1$, meaning there is one zero enclosed by $\gamma$ for $R$ large enough.
As $R\to \infty$, this covers $Q_1$.
:::

