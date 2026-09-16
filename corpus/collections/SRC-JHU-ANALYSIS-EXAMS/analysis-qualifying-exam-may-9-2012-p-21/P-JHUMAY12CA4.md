---
schema: qual/card@1
id: P-JHUMAY12CA4
kind: problem
title: Half-plane preservation and two interpolation values force a translation
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the closed half-plane and both interpolation values with May 2012 problem 4 in the retained source. Corrected the title: the conclusion is a translation, and the fixed points belong to f minus one."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified preservation of the open half-plane, the explicit disk map and inverse, its two distinct fixed points and the final identity-theorem extension."
---

::: {.problem}
Let $U = \{z \in \mathbb{C} \mid \operatorname{Im}(z) \leq \frac{\pi}{2}\}$ and $f$ be an entire function satisfying $f(U) \subset U$, $f(-1) = 0$, $f(0) = 1$.
Prove that $f(z) = z + 1$.
:::

::: {.solution}
Set $g(z)=f(z)-1$ and $H=\{z:\operatorname{Im}z<\pi/2\}$.
Then $g(-1)=-1$ and $g(0)=0$.

<1>1. The restriction $g:H\to H$ is a holomorphic self-map.

::: {.proof}
Subtracting the real number one leaves imaginary parts
unchanged, so $g(U)\subset U$. Both $-1$ and zero belong
to $H$, and their distinct images show that $g$ is
nonconstant there. By the open mapping theorem, $g(H)$
is open in $\mathbb C$ [@SS03]. It is contained in the
closed half-plane $U$, so it cannot contain a point of
the boundary line: any neighborhood of such a point
meets $\mathbb C\setminus U$. Hence $g(H)\subset H$.
:::

<1>2. A disk normalization makes $g$ the identity on $H$.

::: {.proof}
Define
$$
\psi(z)=\frac{z}{z-i\pi},\qquad
\psi^{-1}(w)=\frac{i\pi w}{w-1}.
$$
The pole $i\pi$ is outside $H$. Direct calculation gives
$$
1-|\psi(z)|^2
=\frac{\pi^2-2\pi\operatorname{Im}z}{|z-i\pi|^2}>0
\quad(z\in H),
$$
and
$$
\frac\pi2-\operatorname{Im}\frac{i\pi w}{w-1}
=\frac{\pi(1-|w|^2)}{2|1-w|^2}>0
\quad(|w|<1).
$$
Substitution verifies the inverse formulas. Thus $\psi$
is a biholomorphism from $H$ to the unit disk $D$.

The holomorphic disk self-map
$G=\psi\circ g\circ\psi^{-1}$ fixes zero and
$\beta=\psi(-1)=1/(1+i\pi)\ne0$. Schwarz's lemma gives
$|G(w)|\leq|w|$ [@SS03]. The quotient $G(w)/w$ extends
holomorphically through zero, has modulus at most one,
and equals one at $\beta$. The maximum modulus principle
therefore makes that quotient identically one [@SS03].
It follows that $G(w)=w$ on $D$ and $g(z)=z$ on $H$.
:::

<1>3. The equality holds on the entire plane.

::: {.proof}
The entire function $f(z)-z-1$ vanishes on the nonempty
open set $H$. The identity theorem on the connected
plane makes it identically zero [@SS03]. Hence
$f(z)=z+1$ for every $z\in\mathbb C$.
This translation indeed preserves $U$ and has the two
prescribed interpolation values.
:::
:::
