---
schema: qual/card@1
id: FE-SRFFERMATQUARTIC
kind: example
title: The Fermat quartic is a K3 surface containing $48$ lines
classification:
  areas:
  - algebraic-geometry
  topics:
  - K3 Surfaces
  - Adjunction
  - Lines on Surfaces
relations:
- kind: uses
  target: T-SRFADJ
- kind: related-to
  target: T-SRFKOD
review: draft
prompts:
- What is the Fermat quartic?
---

::: {.example title="Fermat quartic"}
The \dfn{Fermat quartic} is $X = V(x^4 + y^4 + z^4 + w^4) \subseteq \PP^3_\CC$.

1. $X$ is smooth: the partial derivatives $4x^3, 4y^3, 4z^3, 4w^3$ vanish simultaneously only at the origin.

2. $X$ is a K3 surface. By adjunction $\omega_X \cong \omega_{\PP^3} \otimes \OO_{\PP^3}(4) \otimes \OO_X = \OO_X(4 - 4) = \OO_X$ [@Har77, Proposition II.8.20], and the sequence $0 \to \OO_{\PP^3}(-4) \to \OO_{\PP^3} \to \OO_X \to 0$ gives $H^1(X, \OO_X) = 0$ because $H^1(\OO_{\PP^3}) = H^2(\OO_{\PP^3}(-4)) = 0$ [@Har77, Theorem III.5.1].

3. Its invariants are $\chi(\OO_X) = h^0 - h^1 + h^2 = 1 - 0 + 1 = 2$, with $h^2 = h^0(\omega_X) = 1$ by Serre duality [@Har77, Corollary III.7.7]; Noether's formula $12\chi(\OO_X) = K_X^2 + e(X)$ [@Har77, Example A.4.1.2] with $K_X^2 = 0$ gives the topological Euler characteristic $24$, and then $b_2 = 24 - 2 = 22$ and $h^{1,1} = b_2 - 2h^{2,0} = 20$.

4. $X$ contains exactly $48$ lines. If $\zeta^4 = \eta^4 = -1$, the line $\{x = \zeta y,\ z = \eta w\}$ lies on $X$, since $x^4 + y^4 = (\zeta^4 + 1) y^4 = 0$ and likewise for $z, w$. There are $16$ such lines for each of the $3$ ways to split the coordinates into two pairs, and the remark below shows there are no others. Each line $L$ has $L^2 = -2$ by adjunction: $2g - 2 = L^2 + L \cdot K_X$ with $g = 0$ and $K_X \sim 0$ [@Har77, Proposition V.1.5].

5. The $48$ lines span a sublattice of rank $20$ in $\operatorname{NS}(X)$. Since the class of a divisor lies in $H^{1,1}(X)$, of dimension $20$ by item 3, this exhausts $\operatorname{NS}(X) \otimes \QQ$: $X$ has Picard number $20$, the maximum for a complex K3 surface.
:::

::: {.remark title="No other lines"}
Of the four restrictions $\ell_i = \restrictionof{x_i}{L}$ at least two are linearly independent, since otherwise $L$ would be a point. The quartic is invariant under permuting coordinates, and a permutation carries the three splittings of item 4 to one another, so assume $\ell_0, \ell_1$ independent and use them as coordinates $s, t$ on $L$. Then $\ell_2 = as + bt$ and $\ell_3 = cs + dt$, and $L \subseteq X$ says that
$$
s^4 + t^4 + (as + bt)^4 + (cs + dt)^4 \equiv 0,
$$
that is,
$$
1 + a^4 + c^4 = a^3b + c^3d = a^2b^2 + c^2d^2 = ab^3 + cd^3 = 1 + b^4 + d^4 = 0.
$$
By the third equation either $b = 0$, or $a = 0$, or $ab \neq 0$. If $b = 0$ the third gives $cd = 0$, and $d = 0$ makes the fifth read $1 = 0$, so $c = 0$ and then $a^4 = d^4 = -1$. If $b \neq 0$ and $a = 0$ the third gives $cd = 0$, and $c = 0$ makes the first read $1 = 0$, so $d = 0$ and then $b^4 = c^4 = -1$. If $ab \neq 0$ the third gives $cd \neq 0$, and the second times $b^2$ and the fourth times $a^2$ then give $(cb)^2 = (da)^2$, so $cb = \pm da$: writing $a = \pm\mu d$ and $c = \mu b$, the second equation gives $d^2 = \mp b^2$, so that $a^2b^2 + c^2d^2 = 2\mu^2b^2d^2 = \mp 2\mu^2b^4 \neq 0$, contradicting the third. The solutions are therefore $(a, 0, 0, d)$ and $(0, b, c, 0)$, with the two nonzero entries fourth roots of $-1$: sixteen lines each, the families $\{z = ax,\ w = dy\}$ and $\{z = by,\ w = cx\}$, and together with the family displayed in item 4 these are the $48$.
:::
