---
schema: qual/card@1
id: P-TRIV-DE37
kind: problem
title: Green function of $-\frac{d^2}{dx^2}+m^2$ on the line
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 37, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $\left( - \frac { d ^ { 2 } } { d x ^ { 2 } } + m ^ { 2 } \right) G ( x ) = \delta ( x )$
:::

::: {.solution}
Assume $m>0$ and seek the Green function on $\mathbb R$ that decays as $|x|\to\infty$.

<1>1. Away from $x=0$, every decaying solution has the form
\[
G(x)=
\begin{cases}
A e^{mx},&x<0,\\
B e^{-mx},&x>0.
\end{cases}
\]

::: {.proof}
For $x\ne0$, the equation is $-G''+m^2G=0$, or $G''=m^2G$. Its solutions are linear combinations of $e^{mx}$ and $e^{-mx}$. Decay at $-\infty$ leaves only $e^{mx}$ on the negative half-line, while decay at $+\infty$ leaves only $e^{-mx}$ on the positive half-line.
:::

<1>2. The absence of a $\delta'$ term requires $G$ to be continuous at $0$, hence
\[
A=B.
\]

::: {.proof}
If $G$ had a jump at $0$, its first distributional derivative would contain a multiple of $\delta_0$, and its second derivative would contain a multiple of $\delta_0'$. The right side contains only $\delta_0$, so the jump must vanish. Thus $G(0^-)=G(0^+)$.
:::

<1>3. Integrating across $0$ gives
\[
G'(0^+)-G'(0^-)=-1.
\]

::: {.proof}
Integrate
\[
-G''+m^2G=\delta_0
\]
from $-\epsilon$ to $\epsilon$. The $m^2G$ integral tends to zero as $\epsilon\to0^+$, while the second-derivative term gives
\[
-G'(0^+)+G'(0^-)=1.
\]
Rearranging gives the displayed jump condition.
:::

<1>4. The coefficient is
\[
A=B=\frac1{2m}.
\]

::: {.proof}
By step <1>1,
\[
G'(0^-)=mA,
\qquad
G'(0^+)=-mB.
\]
Using $A=B$ from step <1>2 in the jump condition of step <1>3 gives $-2mA=-1$.
:::

<1>5. Therefore
\[
\boxed{G(x)=\frac{e^{-m|x|}}{2m}}.
\]

::: {.proof}
Combine steps <1>1 and <1>4. The resulting function is continuous, has derivative jump $-1$, solves the homogeneous equation away from the origin, and decays at both infinities, so its image under $-d^2/dx^2+m^2$ is exactly $\delta_0$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the decaying Green function on the line.
:::
:::
