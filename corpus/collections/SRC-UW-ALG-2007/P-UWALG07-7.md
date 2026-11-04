---
schema: qual/card@1
id: P-UWALG07-7
kind: problem
title: Symplectic bases and the dimension of isotropic subspaces
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Bilinear Forms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2007`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) induction on $\dim V$: a hyperbolic plane $\langle e_1,f_1\rangle$ is nondegenerate, so
    $V=\langle e_1,f_1\rangle\oplus\langle e_1,f_1\rangle^\perp$ with the restriction to the
    complement again nondegenerate; characteristic $\ne2$ is what makes $\omega(v,v)=0$.
    (b) an isotropic $W$ satisfies $W\subseteq W^\perp$, so $\dim W\le\dim W^\perp=\dim V-\dim W$.
    Nothing is left in outline.
---
---

::: {.problem}
Let $V$ be a vector space over a field $k$ that is not of characteristic two.
Let $\omega:V\times V\to k$ be a non-degenerate skew-symmetric bilinear form, i.e., $\omega(x,y)=-\omega(y,x)$ for all $x,y\in V$, and if $x\neq0$ there is a $y$ such that $\omega(x,y)\neq0$.

(a) Show that there exists a basis $e_1,\ldots,e_n,f_1,\ldots,f_n$ of $V$ such that $\omega(e_i,e_j)=\omega(f_i,f_j)=0$ and $\omega(e_i,f_j)=\delta_{ij}$ for all $i,j$.
(In particular $\dim V=2n$ is even.)

(b) We say a subspace $W\subset V$ is *isotropic* if $\omega(w_1,w_2)=0$ for all $w_1,w_2\in W$.
Show that the dimension of an isotropic subspace is at most $\frac12\dim V$.
:::

::: {.solution}

Let $\omega$ be a nondegenerate skew-symmetric form on a $k$-vector space $V$ with $\operatorname{char}k\ne2$.

::: pf

::: {.pf-step #s1}

$\omega(v,v)=0$ for all $v$, and for a subspace $W$, $\dim W+\dim W^\perp=\dim V$ where $W^\perp=\{v:\omega(w,v)=0\ \forall w\in W\}$.

::: pf-proof

$\omega(v,v)=-\omega(v,v)$ gives $2\omega(v,v)=0$, and $2\ne0$ in $k$, so $\omega(v,v)=0$.

For the dimension formula: the map $\Phi:V\to W^*$, $\Phi(v)=\omega(\cdot,v)|_W$, is linear with kernel $W^\perp$. It is onto because $\omega$ is nondegenerate and every functional on $W$ extends to $V$ (extend by zero on a complement). Rank–nullity gives $\dim V=\dim W^\perp+\dim W^*=\dim W^\perp+\dim W$.

:::

:::

::: {.pf-step #s2}

Part (a): there is a basis $e_1,\dots,e_n,f_1,\dots,f_n$ with $\omega(e_i,e_j)=\omega(f_i,f_j)=0$ and $\omega(e_i,f_j)=\delta_{ij}$; in particular $\dim V=2n$.

::: pf-proof

Induct on $\dim V$. For $V=0$ there is nothing to prove.

Let $V\ne0$. Choose $e_1\ne0$; by nondegeneracy there is $g$ with $\omega(e_1,g)=c\ne0$, and replacing $g$ by $g/c$ gives $f_1$ with $\omega(e_1,f_1)=1$. Then $\omega(f_1,e_1)=-1$.

Let $H=\langle e_1,f_1\rangle$, a $2$-dimensional subspace on which $\omega$ restricts to the form with matrix $\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$, which is nondegenerate. Put $H^\perp=\{v:\omega(h,v)=0\ \forall h\in H\}$.

*Claim: $V=H\oplus H^\perp$.* For $v\in V$ the restriction $\omega(\cdot,v)|_H\in H^*$ is realized by a unique $h\in H$, by nondegeneracy of $\omega|_H$; then $v-h\in H^\perp$. So $V=H+H^\perp$. If $v\in H\cap H^\perp$ then $\omega(v,h)=0$ for all $h\in H$, so $v=0$ by nondegeneracy on $H$. Hence the sum is direct.

*Claim: $\omega|_{H^\perp}$ is nondegenerate.* If $u\in H^\perp$ satisfies $\omega(u,H^\perp)=0$, then also $\omega(u,H)=0$ because $H\perp H^\perp$ in either argument, so $\omega(u,V)=0$ and hence $u=0$.

By step [](#s1){.pf-ref}, $\dim H^\perp=\dim V-2<\dim V$, so the induction hypothesis applies to $H^\perp$: it has a symplectic basis $e_2,\dots,e_n,f_2,\dots,f_n$. Together with $e_1,f_1$ these form a basis of $V$ with the required properties, since $H\perp H^\perp$.

Finally $\dim V=2n$ is even.

:::

:::

::: {.pf-step #s3}

Part (b): an isotropic subspace $W$ satisfies $\dim W\le\tfrac12\dim V$.

::: pf-proof

$W$ is isotropic, meaning $\omega(w_1,w_2)=0$ for all $w_1,w_2\in W$; equivalently $\omega(w,v)=0$ for all $w\in W$, so $v\in W$ implies $v\in W^\perp$. Hence $W\subseteq W^\perp$.

Subspaces of a finite dimensional space satisfy $\dim$ is monotone under inclusion, so
$$
\dim W\le\dim W^\perp=\dim V-\dim W
$$
by step [](#s1){.pf-ref}, that is $2\dim W\le\dim V$, which is the assertion.

Equality is attained: the span of $e_1,\dots,e_n$ in a symplectic basis of step [](#s2){.pf-ref} is isotropic of dimension $n=\tfrac12\dim V$, and it equals its own orthogonal complement there.

:::

:::

:::

:::
