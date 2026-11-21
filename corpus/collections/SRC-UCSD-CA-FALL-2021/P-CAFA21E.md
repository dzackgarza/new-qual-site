---
schema: qual/card@1
id: P-CAFA21E
kind: problem
title: "Biholomorphism to a strip and unbounded harmonic function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $G = \{ z = x+iy : x > 0,\, y > 0,\, xy < 1 \}$.

(i) Construct a biholomorphism between $G$ and the strip $S = \{ z = x+iy : 0 < y < 1 \}$.

(ii) Construct an unbounded continuous function $u : \overline{G} \to \RR$, harmonic in $G$, and such that $u$ vanishes on $\partial G$.
:::

::: {.solution}

No retained solution set covers this exercise: both constructions are the card's own, with surjectivity of $\Phi$, the harmonicity of $U$ and the vanishing on $\partial G$ as separate steps.

Let $G=\theset{x+iy\mid x>0,\ y>0,\ xy<1}$ and $S=\theset{w\mid 0<\operatorname{Im}w<1}$.

::: pf

::: {.pf-step #onto}
$\Phi(z)=z^{2}/2$ maps $G$ bijectively onto $S$.

::: pf-proof
For $z=x+iy$ one has $z^{2}/2=\frac{x^{2}-y^{2}}{2}+ixy$, so $\operatorname{Im}\Phi(z)=xy$, and $x>0$, $y>0$, $xy<1$ say exactly $\operatorname{Im}\Phi(z)\in(0,1)$. Conversely, if $w\in S$ then $w$ lies in the open upper half-plane, so its two square roots are $\pm z$ with $z$ in the open first quadrant; for that $z$ one has $x>0$, $y>0$ and $xy=\operatorname{Im}w\in(0,1)$, so $z\in G$ and $\Phi(z)=w$.
:::

:::

::: {.pf-step #biholo}
$\Phi$ is biholomorphic from $G$ onto $S$.

::: pf-proof
$\Phi$ is holomorphic with $\Phi'(z)=z\ne0$ on $G$, so it is a local biholomorphism, and it is a bijection by step [](#onto){.pf-ref}; a bijective local biholomorphism is a biholomorphism onto its image.
:::

:::

::: {.pf-step #harmonic}
(ii) $U(w)=e^{\pi\operatorname{Re}w}\sin(\pi\operatorname{Im}w)$ is harmonic on $S$, continuous on $\overline S$ and vanishes on $\partial S$.

::: pf-proof
$U=\operatorname{Im}\big(e^{\pi w}\big)$ is the imaginary part of a holomorphic function, hence harmonic. On $\operatorname{Im}w=0$ we have $\sin(0)=0$, and on $\operatorname{Im}w=1$ we have $\sin\pi=0$, so $U$ vanishes on both boundary lines.
:::

:::

::: {.pf-step #vanishes}
$u(z)=U\big(\Phi(z)\big)=e^{\pi\operatorname{Re}(z^{2}/2)}\sin\big(\pi xy\big)$ is harmonic on $G$, continuous on $\overline G$ and vanishes on $\partial G$.

::: pf-proof
$u$ is the composite of the holomorphic $\Phi$ with the harmonic $U$, hence harmonic on $G$; it is continuous on $\overline G$ because $\Phi$ and $U$ are continuous. The boundary $\partial G$ is the union of the positive imaginary axis ($x=0$), the positive real axis ($y=0$) and the hyperbola $xy=1$ with $x,y\ge0$. On the two axes $xy=0$, so $\sin(\pi xy)=0$; on the hyperbola $xy=1$, so $\sin\pi=0$. Hence $u=0$ on $\partial G$.
:::

:::

::: {.pf-step #unbounded}
$u$ is unbounded on $\overline G$.

::: pf-proof
Take $xy=\tfrac12$ and $\frac{x^{2}-y^{2}}{2}\to+\infty$, that is $x\to\infty$ and $y=\frac{1}{2x}\to0$: these points lie in $G$. There $\sin(\pi xy)=\sin\frac{\pi}{2}=1$ and $e^{\pi\operatorname{Re}(z^{2}/2)}=e^{\pi(x^{2}-y^{2})/2}\to\infty$, so $u\to\infty$ along them.
:::

:::

::: {.pf-qed}
Part (i) is steps [](#onto){.pf-ref} and [](#biholo){.pf-ref}; part (ii) is steps [](#harmonic){.pf-ref}, [](#vanishes){.pf-ref} and [](#unbounded){.pf-ref}: $u$ is continuous on $\overline G$, harmonic in $G$, zero on $\partial G$ and unbounded.
:::

:::

:::
