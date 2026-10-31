---
schema: qual/card@1
id: P-TRIV-DE37
kind: problem
title: Green function of $-\frac{d^2}{dx^2}+m^2$ on the line
classification:
  areas: [prelim]
  topics:
  - Green's Functions
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 37, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $\left( -\frac{d^2}{dx^2} + m^2 \right) G(x) = \delta(x)$.
:::

::: {.solution}

Assume $m>0$ and seek the Green function on $\RR$ that decays as $\abs{x}\to\infty$.

::: pf

::: {.pf-step #s1-1}

Away from $x=0$, every decaying solution has the form
$$
G(x)=
\begin{cases}
A e^{mx},&x<0,\\
B e^{-mx},&x>0.
\end{cases}
$$


::: pf-proof

For $x\ne0$, the equation is $-G''+m^2G=0$, or $G''=m^2G$. Its solutions are linear combinations of $e^{mx}$ and $e^{-mx}$. Decay at $-\infty$ leaves only $e^{mx}$ on the negative half-line, while decay at $+\infty$ leaves only $e^{-mx}$ on the positive half-line.

:::

:::

::: {.pf-step #s1-2}

The absence of a $\delta'$ term requires $G$ to be continuous at $0$, hence
$$
A=B.
$$


::: pf-proof

If $G$ had a jump at $0$, its first distributional derivative would contain a multiple of $\delta_0$, and its second derivative would contain a multiple of $\delta_0'$. The right side contains only $\delta_0$, so the jump must vanish. Thus $G(0^-)=G(0^+)$.

:::

:::

::: {.pf-step #s1-3}

Integrating across $0$ gives
$$
G'(0^+)-G'(0^-)=-1.
$$


::: pf-proof

Integrate
$$
-G''+m^2G=\delta_0
$$
from $-\epsilon$ to $\epsilon$. The $m^2G$ integral tends to zero as $\epsilon\to0^+$, while the second-derivative term gives
$$
-G'(0^+)+G'(0^-)=1.
$$
Rearranging gives the displayed jump condition.

:::

:::

::: {.pf-step #s1-4}

The coefficient is
$$
A=B=\frac1{2m}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
G'(0^-)=mA,
\qquad
G'(0^+)=-mB.
$$
Using $A=B$ from step [](#s1-2){.pf-ref} in the jump condition of step [](#s1-3){.pf-ref} gives $-2mA=-1$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{G(x)=\frac{e^{-m\abs{x}}}{2m}}.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-4){.pf-ref}. The resulting function is continuous, has derivative jump $-1$, solves the homogeneous equation away from the origin, and decays at both infinities, so its image under $-d^2/dx^2+m^2$ is exactly $\delta_0$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the decaying Green function on the line.

:::

:::

:::
