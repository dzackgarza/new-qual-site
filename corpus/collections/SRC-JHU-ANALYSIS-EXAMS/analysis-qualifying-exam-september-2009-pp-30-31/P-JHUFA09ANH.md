---
schema: qual/card@1
id: P-JHUFA09ANH
kind: problem
title: "Harmonic conjugate on the punctured disk up to a logarithmic term"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Isolated Singularities
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the punctured-disk domain and the real logarithmic correction with September 2009 problem 8 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Constructed a conjugate after lifting to the left half-plane, proved that the period is purely imaginary and constant, and descended the corrected periodic function using local logarithm branches."
---

::: {.problem}
8. Let h be a harmonic function on the punctured disk

$$
U : = \left\{ z \in \mathbb { C } : 0 < | z | < 1 \right\} .
$$

Show that there exists a constant $c \in \mathbb { R }$ and a holomorphic function f on U such that $\mathrm { R e } f ( z ) = h ( z ) + c \log | z |$ for all $z \in U$
:::

::: solution
Let $L=\{w\in\mathbb C:\operatorname{Re}w<0\}$.
The exponential maps $L$ onto $U$, and two points of
$L$ have the same exponential exactly when their difference
is $2\pi i k$ for an integer $k$.

<1>1. The lifted harmonic function is the real part of a holomorphic function on $L$.

::: proof
Define $\widetilde h(w)=h(e^w)$. Composition with the
holomorphic map $w\mapsto e^w$ preserves harmonicity:
the chain rule gives
$$
\Delta\widetilde h(w)=|e^w|^2(\Delta h)(e^w)=0.
$$
On the simply connected half-plane $L$, the harmonic
function $\widetilde h$ has a holomorphic conjugate,
so there is a holomorphic $H$ with
$\operatorname{Re}H=\widetilde h$ [@SS03]. Explicitly,
the Cauchy–Riemann equations show that
$\widetilde h_s-i\widetilde h_t$ is holomorphic for
$w=s+it$. Its primitive on $L$, after addition of a
real constant, has real part $\widetilde h$. This proves
the required global existence on the half-plane rather
than assuming a conjugate on the punctured disk.
:::

<1>2. A real linear term removes the period of this conjugate.

::: proof
The function $A(w)=H(w+2\pi i)-H(w)$ is holomorphic on $L$.
Since $e^{w+2\pi i}=e^w$, it has real part zero. The
Cauchy–Riemann equations then force its imaginary part
to have both partial derivatives zero. Connectedness of
$L$ implies $A(w)=i\beta$ for a fixed $\beta\in\mathbb R$.
Set $c=-\beta/(2\pi)$ and $G(w)=H(w)+cw$. Then
$$
G(w+2\pi i)-G(w)=i\beta+2\pi ic=0.
$$
Iteration in both directions makes $G$ invariant under
every translation by $2\pi ik$, $k\in\mathbb Z$.
:::

<1>3. The periodic holomorphic function descends to the desired function on $U$.

::: proof
For $z\in U$, choose any $w\in L$ with $e^w=z$ and
define $f(z)=G(w)$. Any two choices differ by $2\pi ik$,
so step <1>2 makes this definition independent of the choice.
Near each $z\ne0$ there is a holomorphic logarithm branch
$\ell$, obtained for example from the local inverse
function theorem applied to the exponential [@SS03].
Its real part is $\log|z|<0$, so it takes its values in
$L$. Locally $f=G\circ\ell$, which proves holomorphy of
$f$ throughout $U$.
For any such $w$,
$$
\operatorname{Re}f(z)
=\operatorname{Re}H(w)+c\operatorname{Re}w
=h(z)+c\log|z|.
$$
The constant $c$ is real by construction. This establishes
the required representation without any boundedness
assumption near the puncture.
:::
:::
