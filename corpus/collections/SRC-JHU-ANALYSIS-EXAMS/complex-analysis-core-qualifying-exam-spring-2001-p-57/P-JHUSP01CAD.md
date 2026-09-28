---
schema: qual/card@1
id: P-JHUSP01CAD
kind: problem
title: A positive harmonic function on the punctured plane is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared positivity, harmonicity and the punctured-plane domain with both recorded appearances, including Spring 2001 question 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Lifted by the exponential map to a positive entire harmonic function, constructed a global conjugate on the plane, and applied Liouville to its bounded exponential."
---

::: {.problem}
Question 4. Let $u ( z ) > 0$ be a positive harmonic function in the punctured plane $0 < | z |$ Show that u must be constant.
:::

::: {.solution}
<1>1. Lifting by the exponential map gives a positive harmonic function on the whole plane.
::: {.proof}
Define
$$
v(w)=u(e^w),\qquad w\in\mathbb C.
$$
Since the exponential map is holomorphic and never vanishes, $v$ is defined on
all of $\mathbb C$. Composition of a harmonic function with a holomorphic map is
harmonic; explicitly, writing $w=s+it$ and using the chain rule gives
$$
\Delta v(w)=|e^w|^2(\Delta u)(e^w)=0.
$$
Moreover $v(w)>0$ everywhere because $u>0$ on the punctured plane.
:::

<1>2. Every positive harmonic function on the plane is constant.
::: {.proof}
Because $\mathbb C$ is simply connected, the harmonic function $v$ has a global
harmonic conjugate, so there is an entire function $H$ with
$\operatorname{Re}H=v$. Then
$$
E(w)=e^{-H(w)}
$$
is entire and
$$
|E(w)|=e^{-v(w)}<1.
$$
Liouville's theorem makes $E$ constant. Since an exponential never vanishes,
$0=E'=-H'e^{-H}$ implies $H'=0$, hence $H$ and therefore $v$ are constant.
:::

<1>3. Constancy descends to the punctured plane.
::: {.proof}
The exponential map is onto $\mathbb C\setminus\{0\}$. For any $z\ne0$, choose
$w$ with $e^w=z$. If $v\equiv c$, then
$$
u(z)=u(e^w)=v(w)=c.
$$
Thus $u$ is constant on the punctured plane.
:::
:::
