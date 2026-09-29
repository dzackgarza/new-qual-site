---
schema: qual/card@1
id: P-BKF14-6A
kind: problem
title: Order of $\operatorname{Sp}_4(\mathbb F_3)$ and the number of symplectic forms on $\mathbb F_3^4$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: counting
    ordered symplectic bases gives the stabilizer order, and orbit-stabilizer
    under GL_4(F_3) gives the number of forms.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked every fiber cardinality in the symplectic-basis count, the
    nondegeneracy of the orthogonal complement, and the final quotient
    51840 and 468.
---

::: {.problem}
Find the order of the group of linear transformations preserving a non-degenerate skewsymmetric bilinear form on a 4-dimensional vector space over the field with 3 elements, and find the number of such forms.
:::

::: {.solution}
Let $V=\FF_3^4$ and fix a nondegenerate skew-symmetric bilinear form
$\omega$ on $V$. Since the characteristic is not $2$, $\omega$ is
alternating.

::: pf

::: {.pf-step #s1}

The number of choices for the first vector $e_1$ of a symplectic
basis is
$$
3^4-1=80.
$$

::: pf-proof

The vector $e_1$ may be any nonzero vector of the $4$-dimensional
space $V$, which has $3^4$ elements.

:::

:::

::: {.pf-step #s2}

Once $e_1$ is chosen, the number of vectors $f_1$ satisfying
$$
\omega(e_1,f_1)=1
$$
is
$$
3^3=27.
$$

::: pf-proof

Nondegeneracy implies that the linear functional
$$
V\longrightarrow\FF_3,
\qquad
v\longmapsto\omega(e_1,v)
$$
is nonzero. It is therefore surjective, and its kernel has dimension
$3$. Every fiber has $3^3$ elements.

:::

:::

::: {.pf-step #s3}

Put $U_1=\operatorname{span}\{e_1,f_1\}$. Then $U_1$ is
nondegenerate and
$$
W\coloneqq U_1^\perp
$$
is a $2$-dimensional nondegenerate symplectic subspace.

::: pf-proof

In the basis $(e_1,f_1)$, the restriction of $\omega$ to $U_1$ has
matrix
$$
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
$$
which is nonsingular. Thus $U_1\cap U_1^\perp=0$. Nondegeneracy of
$\omega$ on $V$ then gives
$$
V=U_1\oplus U_1^\perp
$$
and $\dim W=2$. If a vector of $W$ is orthogonal to all of $W$, it is
also orthogonal to $U_1$, hence to all of $V$; nondegeneracy of
$\omega$ forces it to be zero. Thus $\omega|_W$ is nondegenerate.

:::

:::

::: {.pf-step #s4}

The number of choices for $e_2\in W\setminus\{0\}$ is
$$
3^2-1=8,
$$
and for each such $e_2$ the number of $f_2\in W$ satisfying
$$
\omega(e_2,f_2)=1
$$
is
$$
3.
$$

::: pf-proof

The first count is the number of nonzero vectors in the
$2$-dimensional space $W$. For the second, nondegeneracy of
$\omega|_W$ makes $w\mapsto\omega(e_2,w)$ a nonzero linear functional
on $W$. Its fibers therefore have cardinality $3^{2-1}=3$.

:::

:::

::: {.pf-step #s5}

The order of the group preserving $\omega$ is
$$
\boxed{
|\operatorname{Sp}_4(\FF_3)|
=(3^4-1)3^3(3^2-1)3
=51\,840.
}
$$

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} count exactly the ordered symplectic bases
$(e_1,f_1,e_2,f_2)$ of $(V,\omega)$. Given one fixed symplectic basis,
each $\omega$-preserving automorphism is uniquely determined by its
image basis, and every symplectic basis occurs in this way. Hence the
symplectic group acts simply transitively on the set of ordered
symplectic bases, so its order is
$$
(3^4-1)\cdot3^3\cdot(3^2-1)\cdot3
=
80\cdot27\cdot8\cdot3
=
51\,840.
$$

:::

:::

::: {.pf-step #s6}

The group $\operatorname{GL}_4(\FF_3)$ acts transitively on the
set of nondegenerate skew-symmetric bilinear forms on $V$, and the
stabilizer of $\omega$ is $\operatorname{Sp}_4(\FF_3)$.

::: pf-proof

Every nondegenerate alternating form admits a symplectic basis by the
construction in steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}. Sending a symplectic basis for one
form to a symplectic basis for another gives an element of
$\operatorname{GL}_4(\FF_3)$ carrying one form to the other. Thus the
action is transitive. By definition, the stabilizer of $\omega$ is the
group of linear automorphisms preserving $\omega$.

:::

:::

::: {.pf-step #s7}

The number of nondegenerate skew-symmetric bilinear forms on $V$
is
$$
\boxed{468}.
$$

::: pf-proof

The order of the general linear group is
$$
|\operatorname{GL}_4(\FF_3)|
=(3^4-1)(3^4-3)(3^4-3^2)(3^4-3^3).
$$
By orbit-stabilizer and steps [](#s5){.pf-ref} and [](#s6){.pf-ref}, the number of forms is
$$
\begin{aligned}
\frac{|\operatorname{GL}_4(\FF_3)|}
{|\operatorname{Sp}_4(\FF_3)|}
&=
\frac{
(3^4-1)(3^4-3)(3^4-3^2)(3^4-3^3)
}{
(3^4-1)3^3(3^2-1)3
}\\
&=
(3^3-1)3^2(3-1)\\
&=
26\cdot9\cdot2\\
&=
468.
\end{aligned}
$$

:::

:::

::: pf-qed

Steps [](#s5){.pf-ref} and [](#s7){.pf-ref} give the two requested numbers.

:::

:::

:::
