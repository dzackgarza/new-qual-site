---
schema: qual/card@1
id: PR-VGA2L
kind: proposition
title: Curves of genus $0$
slogan: 'A genus-zero curve with a rational point is $\PP^1$; without one, the anticanonical system presents it as a smooth conic.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Rational Curves
  - Conics
relations:
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- What can you say about curves of genus $0$?
- Is every genus-zero curve isomorphic to $\PP^1$?
---

::: {.proposition}
Let $C$ be a smooth projective geometrically integral curve of genus $0$ over a field $k$.

- If $C$ has a $k$-rational point, then $C \cong \PP^1_k$.

- The anticanonical line bundle $\omega_C^{-1}$ has degree $2$ and
$$
h^0(C,\omega_C^{-1})=3.
$$
Its complete linear system defines a closed immersion
$$
C\hookrightarrow\PP^2_k
$$
whose image is a smooth plane conic.

- If $k$ is algebraically closed or finite, then $C(k)\ne\varnothing$, so $C\cong\PP^1_k$.
:::

::: {.proof}
Suppose first that $p\in C(k)$. Riemann--Roch gives
$$
h^0(C,\OO_C(p))=2,
$$
because $\deg(K_C-p)=-3$. After base change to $\bar k$, for every $q\in C(\bar k)$, Riemann--Roch applied to the degree-zero divisor $p-q$ gives
$$
h^0\bigl(C_{\bar k},\OO(p-q)\bigr)=1.
$$
Since $h^0(\OO(p-q))=h^0(\OO(p))-1$ for every $q$, the complete linear system $\abs p$ has no base point and defines a nonconstant morphism to $\PP^1_{\bar k}$. Its degree is $\deg p=1$, so it is an isomorphism. Hence the morphism
$$
C\longrightarrow\PP^1_k
$$
defined by $\abs p$ becomes an isomorphism after the faithfully flat extension $k\subseteq\bar k$, and is therefore itself an isomorphism.

For the anticanonical system, Riemann--Roch gives
$$
h^0(C,\omega_C^{-1})
=\deg(\omega_C^{-1})+1
=3,
$$
since $\deg\omega_C^{-1}=2$ and $H^0(C,\omega_C^{\otimes2})=0$. After base change to $\bar k$, the line bundle becomes $\OO_{\PP^1}(2)$, whose complete linear system is the quadratic Veronese embedding into $\PP^2_{\bar k}$. Closed immersion descends under faithfully flat base change, so the anticanonical morphism embeds $C$ in $\PP^2_k$. Its image has degree $2$, hence is a smooth conic.

If $k$ is algebraically closed, $C$ has a $k$-point. If $k=\FF_q$, the anticanonical conic is defined by one homogeneous quadratic equation in three variables. Chevalley--Warning gives a nonzero solution over $\FF_q$, hence a $k$-rational point on $C$.
:::

::: {.example}
The smooth conic
$$
x^2+y^2+z^2=0
$$
over $\RR$ has no real point, so it is a genus-zero curve that is not isomorphic to $\PP^1_\RR$.
:::
