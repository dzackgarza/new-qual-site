---
schema: qual/card@1
id: P-Q4P4R
kind: problem
title: Galois groups over $\mathbb{Q}$ of $x^4+4$ and $x^3+x^2-2x-1$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared both polynomials and the root-transformation hint with page 6 of the original scan, Fields 3."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: "Expanded the polynomial identity behind the hint and checked the distinct roots and the generator's three-cycle action."
---

::: {.problem}
Find the Galois groups, over $\mathbb{Q}$, of the following polynomials.

a. $x^4 + 4$.

b. $x^3 + x^2 - 2x - 1$.
Hint: show that if $r$ is a root, then $r^2 - 2$ also is a root.
:::

::: {.solution}
<1>1. The Galois group of $x^4+4$ over $\mathbf Q$ is $C_2$.

::: {.proof}
The factorization
$$
x^4+4=(x^2-2x+2)(x^2+2x+2)
$$
gives roots $1+i$, $1-i$, $-1+i$, and $-1-i$.
They all lie in $\mathbf Q(i)$, and a field containing the roots contains
$i=(1+i)-1$. Hence the splitting field is exactly $\mathbf Q(i)$.
The polynomial $x^2+1$ has no rational root, so this field has degree
$2$ over $\mathbf Q$. Its automorphisms are the identity and complex
conjugation, giving $C_2$.
:::

<1>2. The Galois group of $h(x)=x^3+x^2-2x-1$ over $\mathbf Q$ is
$C_3$, acting cyclically on its roots.

::: {.proof}
<2>1. The only possible rational roots are $\pm1$, but
$h(1)=-1$ and $h(-1)=1$. A reducible cubic has a linear factor, so
$h$ is irreducible. If $\alpha$ is any root, then
$[\mathbf Q(\alpha):\mathbf Q]=3$.

<2>2. Direct multiplication gives
$$
\begin{aligned}
h(x^2-2)&=x^6-5x^4+6x^2-1\\
&=h(x)(x^3-x^2-2x+1).
\end{aligned}
$$
Thus $\beta=\alpha^2-2$ is another root in $\mathbf Q(\alpha)$.
It is distinct from $\alpha$: otherwise $\alpha$ would satisfy
$x^2-x-2=0$, contrary to its degree $3$. Dividing $h$ by
$(x-\alpha)(x-\beta)$ over $\mathbf Q(\alpha)$ gives a linear factor.
Its root is
$$
\gamma=-1-\alpha-\beta=1-\alpha-\alpha^2,
$$
by the coefficient of $x^2$ in $h$. All three roots are distinct,
since an irreducible polynomial over a characteristic-zero field is
separable. Therefore the splitting field is exactly
$L=\mathbf Q(\alpha)$, of degree $3$ over $\mathbf Q$.

<2>3. A splitting field in characteristic zero is Galois and its
automorphism group has order equal to its degree [@DF04]. Hence
$\operatorname{Gal}(L/\mathbf Q)$ has order $3$ and is cyclic.
More explicitly, the isomorphism
$\mathbf Q(\alpha)\to\mathbf Q(\beta)$ determined by
$\alpha\mapsto\beta$ is an automorphism of $L$, since
$\mathbf Q(\beta)\subseteq L$ also has degree $3$ over $\mathbf Q$.
The relation $h(\alpha)=0$ gives
$\alpha^4=3\alpha^2-\alpha-1$, and consequently
$$
\beta^2-2=\alpha^4-4\alpha^2+2
=1-\alpha-\alpha^2=\gamma.
$$
Thus this automorphism sends $\alpha$ to $\beta$ and $\beta$ to
$\gamma$; being a permutation of the three roots, it sends $\gamma$
back to $\alpha$. It is the required generator of $C_3$.
:::
:::
