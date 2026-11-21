---
schema: qual/card@1
id: P-CAF13G
kind: problem
title: "A holomorphic function on the upper half-plane vanishing on a boundary interval is zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The prose said "the sequential hypothesis says precisely that f extends continuously to the interval (0,1)" without the passage from sequences to a limit; the card now derives it from the sequential criterion for limits in the metric space C_+, which is exactly what the hypothesis gives. The Schwarz reflection step states the version used and, more importantly, says why the two formulas agree on the interval (both give 0), which is what makes the extension well defined; and the identity theorem is applied twice with the connectedness of the disc and of C_+ named. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Suppose $f \in \operatorname{Hol}(\CC_+)$ has the property that, for any sequence $z_n$ in $\CC_+$ that converges to a point in $(0, 1)$, $f(z_n) \to 0$.
Prove that $f \equiv 0$ on $\CC_+$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $\CC_+=\{z:\operatorname{Im}z>0\}$ and $I=(0,1)$.

::: pf

::: {.pf-step #limit}
$f$ extends to a function continuous on $\CC_+\cup I$ by $f(x)=0$ for $x\in I$.

::: pf-proof
Fix $x\in I$. By hypothesis, for every sequence $z_n\in\CC_+$ with $z_n\to x$ we have $f(z_n)\to0$. Since $\CC_+$ is a metric space, the sequential criterion for limits gives $\lim_{z\to x,\,z\in\CC_+}f(z)=0$; so setting $f(x)=0$ on $I$ makes $f$ continuous at each point of $I$, and it was already continuous on $\CC_+$.
:::

:::

::: {.pf-step #reflection}
For each $x_0\in I$ there are $\varepsilon>0$ and $F$ holomorphic on the disc $D(x_0,\varepsilon)$ with $F=f$ on $D(x_0,\varepsilon)\cap\CC_+$.

::: pf-proof
The boundary values are real, indeed identically $0$ on $I$ by step [](#limit){.pf-ref}, and $f$ is continuous on $\CC_+\cup I$. The Schwarz reflection principle (in the form: a function holomorphic on $\CC_+$ and continuous and real-valued on an open interval $I\subseteq\RR$ extends holomorphically across $I$) then gives, for a disc $D=D(x_0,\varepsilon)$ with $D\cap\RR\subseteq I$, the holomorphic extension
$$
F(z)=\begin{cases}f(z),&\operatorname{Im}z>0,\\[2pt] \overline{f(\overline z)},&\operatorname{Im}z<0,\end{cases}
$$
on $D$. The two formulas agree on $D\cap\RR$ because there $f=0=\overline{f}$, which is what makes $F$ well defined and holomorphic across the interval.
:::

:::

::: {.pf-step #vanishes}
$F\equiv0$ on $D(x_0,\varepsilon)$, hence $f\equiv0$ on $D(x_0,\varepsilon)\cap\CC_+$.

::: pf-proof
$F$ vanishes on the interval $D(x_0,\varepsilon)\cap\RR$, which is infinite and has accumulation points in the disc; being holomorphic on the connected disc, $F$ vanishes identically there by the identity theorem. In particular $f=F=0$ on the nonempty open set $D(x_0,\varepsilon)\cap\CC_+$.
:::

:::

::: {.pf-step #conclusion}
$f\equiv0$ on $\CC_+$.

::: pf-proof
$\CC_+$ is connected, $f$ is holomorphic on it, and by step [](#vanishes){.pf-ref} it vanishes on the nonempty open subset $D(x_0,\varepsilon)\cap\CC_+\subseteq\CC_+$. The identity theorem then gives $f\equiv0$ on $\CC_+$.
:::

:::

:::
:::
