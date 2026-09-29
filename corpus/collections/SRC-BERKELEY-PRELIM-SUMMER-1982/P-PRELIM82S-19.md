---
schema: qual/card@1
id: P-PRELIM82S-19
kind: problem
title: A fixed-point-free prime-order rational representation has dimension divisible by $p-1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Since M has no nonzero fixed vector, M-I is invertible. Factoring
    M^p-I=(M-I)(I+M+...+M^{p-1}) therefore gives Phi_p(M)=0. The prime
    cyclotomic polynomial Phi_p is irreducible over Q by Eisenstein after
    the shift x↦x+1. Hence V is naturally a vector space over
    Q[x]/(Phi_p), a field of Q-dimension p-1, so dim_Q V is a multiple of
    p-1.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over $\mathbb Q$, and let $M\in\operatorname{Aut}(V)$ fix no nonzero vector.
Suppose
\[
M^p=I
\]
for a prime $p$.
Show that
\[
p-1\mid\dim_{\mathbb Q}V.
\]
:::

::: {.solution}
If $V=0$, then
$$
\dim_{\QQ}V=0
$$
is divisible by $p-1$. Assume henceforth that $V\neq0$.

::: pf

::: {.pf-step #s1}

The linear map
$$
M-I:V\longrightarrow V
$$
is invertible.

::: pf-proof

Its kernel is
$$
\ker(M-I)
=
\{v\in V:Mv=v\}.
$$
By hypothesis, $M$ fixes no nonzero vector, so this kernel is $\{0\}$.
Thus $M-I$ is injective. Since $V$ is finite-dimensional, every injective
endomorphism of $V$ is surjective and hence invertible.

:::

:::

::: {.pf-step #s2}

Let
$$
\Phi_p(x)
=
1+x+\cdots+x^{p-1}.
$$
Then
$$
\boxed{
\Phi_p(M)=0.
}
$$

::: pf-proof

The polynomial identity
$$
x^p-1
=
(x-1)\Phi_p(x)
$$
gives
$$
M^p-I
=
(M-I)\Phi_p(M).
$$
By hypothesis, $M^p=I$, so
$$
(M-I)\Phi_p(M)=0.
$$
Step [](#s1){.pf-ref} says that $M-I$ is invertible. Multiplying by its inverse gives
$$
\Phi_p(M)=0.
$$

:::

:::

::: {.pf-step #s3}

The polynomial $\Phi_p(x)$ is irreducible over $\QQ$.

::: pf-proof

The substitution
$$
x\longmapsto x+1
$$
is an automorphism of $\QQ[x]$, so it preserves irreducibility. Using
$$
\Phi_p(x)
=
\frac{x^p-1}{x-1},
$$
one obtains
$$
\begin{aligned}
\Phi_p(x+1)
&=
\frac{(x+1)^p-1}{x}\\
&=
\sum_{k=1}^{p}
\binom pk x^{k-1}.
\end{aligned}
$$
Its leading coefficient is $1$. Since $p$ is prime,
$$
p\mid\binom pk
$$
for every $1\leq k\leq p-1$. Its constant term is
$$
\binom p1=p,
$$
which is not divisible by $p^2$. Eisenstein's criterion with the prime
$p$ therefore shows that $\Phi_p(x+1)$ is irreducible over $\QQ$.
Consequently $\Phi_p(x)$ is irreducible over $\QQ$.

:::

:::

::: pf-step

The quotient
$$
K
=
\QQ[x]/(\Phi_p(x))
$$
is a field satisfying
$$
\boxed{
[K:\QQ]=p-1.
}
$$

::: pf-proof

By step [](#s3){.pf-ref}, the polynomial $\Phi_p$ is irreducible over the field
$\QQ$, so its principal ideal is maximal and the quotient is a field.
Moreover,
$$
\deg\Phi_p=p-1.
$$
The residue classes of
$$
1,x,\ldots,x^{p-2}
$$
form a $\QQ$-basis of the quotient, so its degree over $\QQ$ is $p-1$.

:::

:::

::: pf-step

The vector space $V$ has a natural structure of vector space over
$K$.

::: pf-proof

For a residue class
$$
[q(x)]\in K
$$
and $v\in V$, define
$$
[q(x)]\cdot v
=
q(M)v.
$$
This is well defined: if
$$
q(x)-r(x)
\in
(\Phi_p(x)),
$$
then
$$
q(x)-r(x)
=
s(x)\Phi_p(x)
$$
for some $s(x)\in\QQ[x]$, and step [](#s2){.pf-ref} gives
$$
\bigl(q(M)-r(M)\bigr)v
=
s(M)\Phi_p(M)v
=
0.
$$
The field and vector-space axioms follow from the corresponding polynomial
identities under evaluation at $M$.

:::

:::

::: {.pf-step #s6}

The dimension of $V$ over $\QQ$ satisfies
$$
\dim_{\QQ}V
=
(p-1)\dim_KV.
$$

::: pf-proof

Let
$$
m=\dim_KV.
$$
This dimension is finite because $V$ is already finite-dimensional over
$\QQ$. Choose a $K$-basis
$$
v_1,\ldots,v_m
$$
of $V$ and a $\QQ$-basis
$$
e_1,\ldots,e_{p-1}
$$
of $K$. Then the
$$
m(p-1)
$$
vectors
$$
e_i v_j
\qquad
1\leq i\leq p-1,\quad
1\leq j\leq m
$$
form a $\QQ$-basis of $V$. Hence
$$
\dim_{\QQ}V
=
m(p-1).
$$

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{
p-1\mid\dim_{\QQ}V.
}
$$

::: pf-proof

Step [](#s6){.pf-ref} expresses $\dim_{\QQ}V$ as an integer multiple of $p-1$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required divisibility statement.

:::

:::

:::
