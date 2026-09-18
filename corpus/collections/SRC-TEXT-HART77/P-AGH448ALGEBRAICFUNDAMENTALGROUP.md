---
schema: qual/card@1
id: P-AGH448ALGEBRAICFUNDAMENTALGROUP
kind: problem
title: The algebraic fundamental group of an elliptic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Riemann-Hurwitz
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.8 together with III.10.3, IV.4.7, and the preceding
    Frobenius/Hasse-invariant discussion. Cross-checked the prime-to-p and
    p-primary torsion structure against standard elliptic-curve references and
    the general curve fundamental-group statement in SGA 1, Expose X, 2.6.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
For any curve $X$, the **algebraic fundamental group** $\pi_1(X)$ is defined as $\cocolim \operatorname{Gal}(K'/K)$, where $K$ is the function field of $X$, and $K'$ runs over all Galois extensions of $K$ such that the corresponding curve $X'$ is étale over $X$ (III, Ex. 10.3).

Thus, for example, $\pi_1(\PP^1)=1$. (See 2.5.3)

Show that for an elliptic curve $X$,
$$
\pi_1(X) =
\begin{cases}
\Prod_{\ell \text{ prime}} \ZZ_\ell \times \ZZ_\ell & \characteristic k = 0,
\\ \\
\Prod_{\ell\neq p} \ZZ_\ell \times \ZZ_\ell & \characteristic k = p \text{ and } \Hasse X = 0,
\\ \\
\ZZ_p \times \Prod_{\ell\neq p} \ZZ_\ell \times \ZZ_\ell & \characteristic k = p \text{ and } \Hasse X \neq 0
\end{cases}
,$$
where $\ZZ_\ell=\varprojlim \ZZ/\ell^n$ is the $\ell$-adic integers.

Hints: Any Galois étale cover $X'$ of an elliptic curve is again an elliptic curve. If the degree of $X'$ over $X$ is relatively prime to $p$, then $X'$ can be dominated by the cover $n_X: X \to X$ for some integer $n$ with $(n, p)=1$. The Galois group of the covering $n_X$ is $\ZZ/n \times \ZZ/n$. Étale covers of degree divisible by $p$ can occur only if the Hasse invariant of $X$ is not zero.

Note: More generally, Grothendieck has shown (SGA 1, X, 2.6) that the algebraic fundamental group of any curve of genus $g$ is isomorphic to a quotient of the completion, with respect to subgroups of finite index, of the ordinary topological fundamental group of a compact Riemann surface of genus $g$, i.e., a group with $2g$ generators $a_1, \ldots, a_g, b_1, \ldots, b_g$ and the relation $\qty(a_1 b_1 a_1^{-1} b_1^{-1}) \cdots \qty(a_g b_g a_g^{-1} b_g^{-1})=1$.
:::

::: {.solution}
Fix the origin $O\in X(k)$. We compute the inverse limit over connected
finite Galois etale covers of $X$.

<1>1. Every connected finite etale cover
$$
\phi:Y\longrightarrow X
$$
is a genus-one curve; after choosing $O_Y\in\phi^{-1}(O)$, it is an elliptic
curve and $\phi:(Y,O_Y)\to(X,O)$ is an etale isogeny.

::: {.proof}
Let $d=\deg\phi$. Since $\phi$ is etale, Riemann--Hurwitz gives
$$
2g(Y)-2=d\bigl(2g(X)-2\bigr)=0.
$$
Thus $g(Y)=1$. The point $O_Y$ makes $Y$ an elliptic curve, and a morphism
of elliptic curves that sends the origin to the origin is a group
homomorphism. Hence $\phi$ is an isogeny. Because $\phi$ is etale, it is
separable and
$$
\#\ker\phi(k)=d.
$$
Translations by the points of $\ker\phi(k)$ are exactly the deck
transformations, so
$$
\Gal(Y/X)\cong\ker\phi(k).
$$
:::

<1>2. If $\phi:Y\to X$ is an etale isogeny of degree $d$, then the dual
isogeny satisfies
$$
\phi\circ\hat\phi=[d]_X.
$$
In particular, whenever $[d]_X$ is etale, the cover $[d]_X:X\to X$
dominates $\phi$.

::: {.proof}
This is [[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(c)]]. The displayed
factorization is a morphism of covers
$$
\begin{aligned}
X&\xrightarrow{\hat\phi}Y\xrightarrow{\phi}X,\\
X&\xrightarrow{[d]_X}X.
\end{aligned}
$$
Thus $[d]_X$ dominates $\phi$ whenever it belongs to the etale covering
system.
:::

<1>3. If $m$ is prime to $p=\characteristic k$ (with no restriction when
$\characteristic k=0$), then
$$
[m]_X:X\longrightarrow X
$$
is an etale Galois cover with
$$
\boxed{\Gal([m]_X)\cong(\ZZ/m\ZZ)^2.}
$$

::: {.proof}
The multiplication map has degree $m^2$. When $m$ is invertible in $k$, it
is separable, hence etale on the elliptic curve. Its kernel is the full
$m$-torsion group
$$
X[m](k)\cong(\ZZ/m\ZZ)^2.
$$
By step <1>1, this kernel is the deck-transformation group.
:::

<1>4. Suppose $\characteristic k=p>0$ and the Hasse invariant of $X$ is
zero. Then every finite etale cover of $X$ has degree prime to $p$.

::: {.proof}
Suppose that an etale isogeny $\phi:Y\to X$ has degree
$$
d=p^r m,
\qquad
(m,p)=1.
$$
By step <1>2,
$$
\phi\circ\hat\phi=[d]_X.
$$
Since $\phi$ is separable, the inseparable degree of the left side is the
inseparable degree of $\hat\phi$.

When the Hasse invariant is zero, $X$ is supersingular and $[p]_X$ is
purely inseparable of degree $p^2$. Hence the inseparable degree of
$[d]_X$ is $p^{2r}$. It follows that the inseparable degree of
$\hat\phi$ is $p^{2r}$. But
$$
\deg\hat\phi=\deg\phi=p^r m
$$
by [[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(f)]], whose $p$-adic valuation
is only $r$. Therefore $r=0$.
:::

<1>5. In the Hasse-zero case, the covers $[m]_X$ with $(m,p)=1$ are
cofinal, and therefore
$$
\boxed{
\pi_1(X)
\cong
\prod_{\ell\ne p}(\ZZ_\ell\times\ZZ_\ell).
}
$$

::: {.proof}
By step <1>4 every connected finite etale Galois cover has degree $d$ prime
to $p$. Step <1>2 says that it is dominated by $[d]_X$, and step <1>3
computes the Galois group of this standard cover. Hence the standard covers
form a cofinal system. Taking the inverse limit over integers prime to $p$
gives
$$
\varprojlim_{(m,p)=1}(\ZZ/m\ZZ)^2
\cong
\prod_{\ell\ne p}\ZZ_\ell^2.
$$
:::

<1>6. Suppose $\characteristic k=p>0$ and the Hasse invariant of $X$ is
nonzero. For $r\ge0$ let
$$
F_X^{(r)}:X\longrightarrow X^{(p^r)}
$$
be the $r$-fold relative Frobenius and let
$$
V_X^{(r)}:X^{(p^r)}\longrightarrow X
$$
be the corresponding Verschiebung, so that
$$
[p^r]_X=V_X^{(r)}\circ F_X^{(r)}.
$$
For $(m,p)=1$, put
$$
\psi_{r,m}=[m]_X\circ V_X^{(r)}:X^{(p^r)}\longrightarrow X.
$$
Then $\psi_{r,m}$ is etale Galois and
$$
\boxed{
\Gal(\psi_{r,m})
\cong
\ZZ/p^r\ZZ\times(\ZZ/m\ZZ)^2.
}
$$

::: {.proof}
Nonzero Hasse invariant is the ordinary case. Thus $F_X^{(r)}$ has degree
$p^r$ and is purely inseparable, while $V_X^{(r)}$ is separable of degree
$p^r$. Hence $V_X^{(r)}$ is etale. Step <1>3 shows that $[m]_X$ is also
etale, so $\psi_{r,m}$ is etale.

The kernel of $V_X^{(r)}$ has $k$-points
$$
\ker V_X^{(r)}(k)\cong\ZZ/p^r\ZZ.
$$
Also
$$
X^{(p^r)}[m](k)\cong(\ZZ/m\ZZ)^2
$$
lies in $\ker\psi_{r,m}$. These subgroups have coprime orders and their
product has order $p^r m^2=\deg\psi_{r,m}$, so they give the entire kernel.
Step <1>1 identifies this kernel with the Galois group.
:::

<1>7. The covers $\psi_{r,m}$ of step <1>6 are cofinal among connected
finite etale Galois covers of $X$.

::: {.proof}
Let $\phi:Y\to X$ be an etale isogeny and write
$$
\deg\phi=p^r m,
\qquad
(m,p)=1.
$$
By step <1>2,
$$
\phi\circ\hat\phi=[p^r m]_X.
$$
In the ordinary case the inseparable degree of $[p^r m]_X$ is $p^r$.
Since $\phi$ is separable, the inseparable degree of $\hat\phi$ is also
$p^r$. The separable--inseparable factorization of a morphism of smooth
curves therefore has the form
$$
\hat\phi=u\circ F_X^{(r)}
$$
for a separable isogeny $u:X^{(p^r)}\to Y$ of degree $m$.

Using $[p^r]_X=V_X^{(r)}F_X^{(r)}$, we get
$$
\phi\circ u\circ F_X^{(r)}
=
[m]_X\circ V_X^{(r)}\circ F_X^{(r)}.
$$
The relative Frobenius of the smooth curve is finite faithfully flat, hence
is an epimorphism for morphisms of schemes. Cancellation therefore gives
$$
\phi\circ u
=
[m]_X\circ V_X^{(r)}
=
\psi_{r,m}.
$$
Thus $\psi_{r,m}$ dominates $\phi$.
:::

<1>8. In the ordinary positive-characteristic case,
$$
\boxed{
\pi_1(X)
\cong
\ZZ_p\times\prod_{\ell\ne p}(\ZZ_\ell\times\ZZ_\ell).
}
$$

::: {.proof}
By step <1>7 it suffices to take the inverse limit of the Galois groups in
step <1>6. Hence
$$
\begin{aligned}
\pi_1(X)
&\cong
\varprojlim_{r,(m,p)=1}
\left(\ZZ/p^r\ZZ\times(\ZZ/m\ZZ)^2\right)\\
&\cong
\ZZ_p\times\prod_{\ell\ne p}(\ZZ_\ell\times\ZZ_\ell).
\end{aligned}
$$
:::

<1>9. If $\characteristic k=0$, then
$$
\boxed{
\pi_1(X)
\cong
\prod_{\ell\text{ prime}}(\ZZ_\ell\times\ZZ_\ell).
}
$$

::: {.proof}
Every multiplication map $[m]_X$ is etale in characteristic zero. For a
connected finite etale Galois cover $\phi$ of degree $d$, step <1>2 shows
that $[d]_X$ dominates $\phi$. Thus the multiplication maps are cofinal.
By step <1>3,
$$
\begin{aligned}
\pi_1(X)
&\cong
\varprojlim_m(\ZZ/m\ZZ)^2\\
&\cong
\prod_{\ell\text{ prime}}(\ZZ_\ell\times\ZZ_\ell).
\end{aligned}
$$
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 gives the characteristic-zero formula, step <1>5 gives the
Hasse-zero formula in characteristic $p$, and step <1>8 gives the nonzero
Hasse-invariant formula in characteristic $p$.
:::
:::
