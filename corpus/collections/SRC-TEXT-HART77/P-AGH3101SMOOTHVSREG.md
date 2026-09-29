---
schema: qual/card@1
id: P-AGH3101SMOOTHVSREG
kind: problem
title: Smooth is not regular over a nonperfect field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Regular Local Rings
  - Nonperfect Fields
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.1 and the smooth-versus-geometrically-regular criterion.
    The proof identifies the coordinate ring with a localization of
    k_0[x,y], which proves regularity without a closed-point Jacobian shortcut,
    and then exhibits a nonregular point after adjoining a pth root of t.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Over a nonperfect field, smooth and regular are not equivalent.
For example, let $k_0$ be a field of characteristic $p > 0$, let $k = k_0(t)$, and let $X \subseteq \AA_k^2$ be the curve defined by $y^2 = x^p - t$.

Show that every local ring of $X$ is a regular local ring, but that $X$ is not smooth over $k$.
:::

::: {.solution}
Let
$$
A=k[x,y]/(y^2-x^p+t),
\qquad
X=\Spec A.
$$

::: pf

::: {.pf-step #s1}

The element
$$
u=x^p-y^2\in k_0[x,y]
$$
is transcendental over $k_0$.

::: pf-proof

The polynomial ring $k_0[x,y]$ is a domain and $u$ is nonconstant.
If a nonzero polynomial
$$
F(T)=c_mT^m+\cdots+c_0\in k_0[T]
$$
satisfied $F(u)=0$, then regarding $F(x^p-y^2)$ as a polynomial in $x$, its
highest $x$-degree term would be
$$
c_mx^{pm},
$$
which cannot cancel with any lower power of $u$.
Thus $F(u)\ne0$.

:::

:::

::: {.pf-step #s2}

The coordinate ring $A$ is a localization of the polynomial ring $k_0[x,y]$.

::: pf-proof

Write
$$
S=k_0[t]\setminus\{0\}.
$$
Since $k=k_0(t)=S^{-1}k_0[t]$, we have
$$
\begin{aligned}
A
&=k_0(t)[x,y]/(y^2-x^p+t)\\
&\cong
S^{-1}\!\left(k_0[t,x,y]/(t-(x^p-y^2))\right).
\end{aligned}
$$
Eliminating $t$ identifies the ring inside parentheses with $k_0[x,y]$, and
under this identification an element $q(t)\in S$ becomes
$$
q(x^p-y^2).
$$
Step [](#s1){.pf-ref} shows that none of these elements is zero. Hence
$$
\boxed{
A\cong
\bigl\{q(x^p-y^2):0\ne q\in k_0[t]\bigr\}^{-1}k_0[x,y].
}
$$

:::

:::

::: {.pf-step #s3}

Every local ring of $X$ is regular.

::: pf-proof

The polynomial ring $k_0[x,y]$ is regular. Every localization of a regular
ring is regular, and step [](#s2){.pf-ref} expresses $A$ as such a localization.
Therefore $A$ is a regular ring.

For every point $P\in X$, the local ring
$$
\OO_{X,P}=A_{\mathfrak p}
$$
is a further localization of $A$, hence is a regular local ring.

:::

:::

::: {.pf-step #s4}

After a purely inseparable field extension, $X$ acquires a nonregular point.

::: pf-proof

Let
$$
k'=k(\alpha),
\qquad
\alpha^p=t.
$$
Then
$$
X_{k'}
=\Spec k'[x,y]/(y^2-x^p+\alpha^p).
$$
Put $v=x-\alpha$. In characteristic $p$,
$$
x^p-\alpha^p=(x-\alpha)^p=v^p,
$$
so
$$
X_{k'}\cong\Spec k'[v,y]/(y^2-v^p).
$$

Consider the point $P=(v,y)=(0,0)$. Its local ring is
$$
B=\bigl(k'[v,y]/(y^2-v^p)\bigr)_{(v,y)}.
$$
This is a hypersurface local ring of dimension one. The defining equation
$y^2-v^p$ lies in $(v,y)^2$, so it imposes no linear relation in the cotangent
space. Hence
$$
\dim_{k'}\mathfrak m_B/\mathfrak m_B^2=2.
$$
A noetherian local ring is regular exactly when its embedding dimension equals
its Krull dimension. Here
$$
2\ne1,
$$
so $B$ is not regular.

This argument includes $p=2$: then $y^2-v^2=(y-v)^2$, making the failure of
geometric regularity especially visible through nonreducedness.

:::

:::

::: {.pf-step #s5}

The curve $X$ is not smooth over $k$.

::: pf-proof

Smoothness is preserved by arbitrary base change. If
$$
X\longrightarrow\Spec k
$$
were smooth, then
$$
X_{k'}\longrightarrow\Spec k'
$$
would be smooth as well. A scheme smooth over a field is regular
[[T-MORSMREG|by the smoothness--regularity theorem]].
But step [](#s4){.pf-ref} exhibits a nonregular local ring on $X_{k'}$.
This contradiction proves that $X$ is not smooth over $k$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove that every local ring of $X$ is regular, while steps
[](#s4){.pf-ref} and [](#s5){.pf-ref} prove that $X$ fails to be smooth over the imperfect field $k$.

:::

:::

:::
